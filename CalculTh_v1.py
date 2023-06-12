import numpy as np
import matplotlib.pyplot as plt
import InertieThBat.Composant

from InertieThBat.Composant import Composant

"""Seconde version à deux milieux, résolution explicite"""

class CalculTh :

    """
    Description :
    
    Réalise un calcul thermique pour un mur 1D en fonction du temps
    Méthdode de résolution de l'équation de la chaleur : Explicite
    Résolution pour un mur composé de plusieurs matériaux homogènes

    ----------------------------------------------------------------

    Méthodes :

    __init__()
    """

    def __init__(self, composant, delta_t, dx = 0.001, dt = 18.0) :
        
        """
        Initialisation des paramètres :
        """

        # Epaisseur totale du mur
        self.ep_comp = composant.ep_comp()

        # Vecteur des coefficients de diffusion
        
        
        # Duree de la simulation thermique
        self.delta_t = delta_t

        # Precision spatiale simulation
        self.dx = dx

        # Precision temporelle simulation
        self.dt = dt

        
        
""" 1/ Discretisation """

# En m
ep = 0.20
# En secondes
d = 3600

# Nombre d'iterations d'espace
space_steps = 200
# Nombre d'iterations de temps
time_steps = 200

# Largeur de la maille d'espace en m
dx = ep/space_steps
# Largeur de la maille de temps en s
dt = d/time_steps


""" 2/ Caracteristiques materiau """

## Materiau 1

# En W.m-1.K-1
_lambda_1 = 0.038
# En kg.m-3
rho_1 = 1650
# En J.kg-1.K-1
cp_1 = 1030

# Diffusivite en m2.s-1
k_1 = _lambda_1/(rho_1*cp_1)

## Materiau 2

# En W.m-1.K-1
_lambda_2 = 1.5
# En kg.m-3
rho_2 = 2400
# En J.kg-1.K-1
cp_2 = 880

# Diffusivite en m2.s-1
k_2 = _lambda_2/(rho_2*cp_2)

## Interface

# Capacité calorifique volumique moyenne
cv_m = (cp_1*rho_1 + cp_2*rho_2)/2


""" 3/ Coefficient caracteristique de diffusion """

## Materiau 1
r_1 = k_1*(dt/(dx**2))

## Materiau 2
r_2 = k_2*(dt/(dx**2))


""" 4/ Conditions aux limites """

# Remarque : Simulation de conditions aux limites pour un cas hors equilibre + conditions au limites stationnaires

# Temperature exterieure notee u pour ne pas confondre avec le temps
u_ext = 38
# Temperature interieure
u_int = 25

# Vecteur de taille 1 contenant u_ext, utile pour la construction du vecteur des conditions aux limites
U_ext = np.array([u_ext])
# Idem qu'au dessus, avec u_int
U_int = np.array([u_int])

# Vecteur des conditions aux limites (stationnaire, ne change pas dans le temps)
U_cl = np.concatenate((U_ext, np.zeros(space_steps - 3), U_int))


""" 5/ Conditions initiales """

# Remarque : Les conditions initiales sont celles d'un état hors équilibre. L'ensemble du materiau est a u_int, sauf le premier point a u_ext

U_ci = np.linspace(u_int, u_int, space_steps - 1)


""" 6/ Matrice tridiagonale de diffusion """

# Liste pour la creation des diagonales hautes et basses
ext_diag = [r for i in range(space_steps - 2)]

# Liste pour la creation de la diagonale centrale
center_diag = [(1 - 2*r) for i in range(space_steps - 1)]

# Creation de la matrice tridiagonale
M_diff = np.diag(ext_diag, -1) + np.diag(center_diag, 0) + np.diag(ext_diag, 1)


""" 7/ Calcul de diffusion de la chaleur au travers du materiau """

# Initialiser le vecteur de calcul egal au vecteur des conditions initiales
U_i = U_ci
# Initialiser la matrice resultat egale au vecteur des conditions initiales
res = U_ci

for i in range(time_steps) :
    
    # Calcul de la ligne avec la ligne precedente
    U_ip1 = np.matmul(M_diff, U_i) + U_cl*r
    # Ajout de la ligne calculee a la matrice resultat
    res = np.vstack((res, U_ip1))
    # Initialisation du vecteur de calcul egal a la ligne calculee precedemment
    U_i = U_ip1

""" 8/ Affichage des résultats """

# Creer une nouvelle figure
plt.figure()
# Creer une carte de chaleur
plt.imshow(res, cmap = 'magma')
# Afficher le plot
plt.show()

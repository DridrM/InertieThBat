import InertieThBat.MateriauTh as mth
import InertieThBat.ComposantTh as cth

# Creation de deux objets 'Materiau' m1 et m2
m1 = mth.Materiau(2500, 800, 0.145)
m2 = mth.Materiau(1650, 900, 0.036)

# Creation d'un objet 'Composant' c1 a partir de m1 et m2
c1 = cth.Composant(m1, m2)

# Definition epaisseurs m1 et m2
c1.ep_materiaux(0.20, 0.10)

# Calcul epaisseur composant c1
c1.ep_comp()

# Test si m1 et m2 sont du type 'Materiau'
c1.test((m1, m2))

# Test si m1 et 2 sont du type 'Materiau'
c1.test((m1, 2))

# Resistance thermique composant c1
c1.rth_comp()

# Composant c2 avec une entree fausse de type int
c2 = cth.Composant(m1, 2)

# Definition epaisseurs
c2.ep_materiaux(0.05, 0.10)

# Test epaisseur c2, renvoie une alerte
c2.ep_comp()

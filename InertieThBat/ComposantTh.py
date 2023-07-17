from InertieThBat.MateriauTh import Materiau

class Composant :

    """
    Description :
    
    Définit une composition de mur 1D pour un calcul thermique d'inertie
    ----------------------------------------------------------------

    Méthodes :
    
    - __init__ -> Définit le tuple self.materiaux contenant les objets du type Materiaux
    - test -> Vérifie si les objets du tuple self.materiaux sont du type Materiau
    - ep_comp -> Calcule l'épaisseur de la composition comme la somme des épaisseurs des materiaux
    - rth_comp -> Calcule la résistance thermique de la composition comme la somme des résistances thermiques des materiaux
    """

    def __init__(self, *materiaux : Materiau) -> None :

        """
        Description :

        Définit :
        - le tuple materiaux contenant les objets du type Materiaux
            Placer le materiau le plus à l'extérieur en premier, et le plus à l'intérieur en dernier
        - Le tuple ep_mat vide dans un premier temps, stockant les épaisseurs des matériaux
        ----------------------------------------------------------------
        
        Arguments :

        - materiaux -> tuple
        - ep_mat -> tuple
        """
        
        self.materiaux = materiaux
        self.ep_mat = tuple()

    def test(self, values : tuple) -> bool :
        
        """
        Description :

        Retourne vrai si toutes les entrées sont du type Materiau
        Retourne faux si une seule entrée n'est pas du type Materiau
        ----------------------------------------------------------------

        Arguments :

        - *values -> InertieThBat.MateriauTh.Materiau
        """
        
        return all(isinstance(value, Materiau) for value in values)
    
    def ep_materiaux(self, *ep : float) -> None :
        
        """
        Description :
        
        Définit dans un tuple l'épaisseur des materiaux en mètres de l'extérieur vers l'intérieur
        Si il n'y a pas le même nombre d'épaisseur que de matériaux, renvoie un message d'alerte
        Si il n'y a pas d'épaisseur renseignée, renvoie un message d'alerte
        ----------------------------------------------------------------
        
        Arguments :
        
        - *ep -> float
        """

        if len(ep) != len(self.materiaux) :
            print("Renseigner le même nombre d'épaisseurs que de matériaux")
        
        else :
            self.ep_mat = ep
    
    def rth_materiaux(self) -> tuple :

        """
        Description :
        
        Définit dans un tuple les résistances thermiques des materiaux de l'extérieur vers l'intérieur
        ----------------------------------------------------------------
        
        Arguments : None
        """

        return tuple(ep/_lambda for ep, _lambda in zip(self.ep_mat, self._lambda_comp()))
    
    def ep_comp(self) -> float :

        """
        Description :

        Renvoie la somme des épaisseurs des materiaux
        ----------------------------------------------------------------
        
        Arguments : None
        """
        
        if self.test(self.materiaux) == False :
            print("Renseigner des objets de type 'Materiau'")
        
        elif len(self.ep_mat) == 0 :
            print("Renseigner le même nombre d'épaisseurs que de matériaux")

        else :
            return sum(self.ep_mat)

    def rth_comp(self) -> float :

        """
        Description :

        Renvoie la somme des  résistances thermiques des materiaux
        ----------------------------------------------------------------
        
        Arguments : None
        """
        
        if self.test(self.materiaux) == False :
            print("Renseigner des objets de type 'Materiau'")
        
        elif len(self.ep_mat) == 0 :
            print("Renseigner le même nombre d'épaisseurs que de matériaux")

        else :
            return sum(self.rth_materiaux())

    def _lambda_comp(self) -> tuple :

        """
        Description :

        Renvoie la liste des coefficients de conductivité thermique de la composition pour chaque materiau
        de l'intérieur vers l'extérieur
        ----------------------------------------------------------------

        Arguments : None
        """

        return tuple(materiau._lambda for materiau in self.materiaux)

    def rho_cp_comp(self) -> tuple :

        """
        Description :

        Renvoie la liste de rho*cp (masse volumique*capacité_calorifique) de la composition pour chaque materiau
        de l'intérieur vers l'extérieur
        ----------------------------------------------------------------

        Arguments : None
        """

        return tuple(materiau.rho*materiau.cp for materiau in self.materiaux)
from math import sqrt

class Materiau :

    """
    Description :
    
    Définit un materiau et ses propriétés thermiques :
    - Masse volumique rho
    - Capacité calorifique massique cp
    - Conductivité thermique lambda
    - Diffusivité thermique k
    - Effusivité thermique ef
    ----------------------------------------------------------------

    Méthodes :
    
    - __init__ -> Définit rho, cp, lambda
    - test -> Vérifie si les valeurs rentrées ne sont pas négatives
    - k -> Calcule la diffusivité thermique k
    - ef -> Calcule l'effusivité thermique ef
    """

    def __init__(self, rho : float, cp : float, _lambda : float) -> None :
        self.rho = rho
        self.cp = cp
        self._lambda = _lambda

    def __str__(self) -> str :
        
        """
        Description :
        
        Affiche les propriétés rho, cp, lambda, k, ef
        ----------------------------------------------------------------
        
        Arguments : None
        """
        
        return f"Masse volumique : {self.rho} kg.m-3\nCapacité calorifique massique : {self.cp} J.K-1.kg-1\nConductivité thermique : {self._lambda} W.m-1.K-1\nDiffusivité thermique : {self.k()} m².s-1\nEffusivité thermique : {self.ef()} W.K−1.m−2.s1/2"
    
    def test(self, *values : float) -> bool :
        
        """
        Description :

        Retourne faux si une seule entrée est négative
        Retourne vrai si toutes les entrées sont positives
        ----------------------------------------------------------------
        
        Arguments :
        
        - *values -> float
        """
        
        if any(value < 0 for value in values) :
            return True
        
        else :
            return False
    
    def k(self) -> float :
        
        """
        Description :
        
        Calcule le coefficient de diffusivité thermique k en m².s-1
        ----------------------------------------------------------------
        
        Arguments : None
        """
        
        if self.test(self._lambda, self.rho, self.cp) :
            print("Rentrer des valeurs positives pour lambda, rho et cp")
        
        else :
            return self._lambda/(self.rho*self.cp)
    
    def ef(self) -> float :
        
        """
        Description :
        
        Calcule le coefficient d'effusivité thermique ef en W.K−1.m−2.s1/2
        ----------------------------------------------------------------
        
        Arguments : None
        """
        
        if self.test(self._lambda, self.rho, self.cp) :
            print("Rentrer des valeurs positives pour lambda, rho et cp")
        
        else :
            return sqrt(self._lambda*self.rho*self.cp)

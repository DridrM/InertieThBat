import numpy as np

class ConditionsLimites:

    def __init__(self,
                 t_max_ext: float,
                 t_min_ext: float,
                 t_max_int: float,
                 t_min_int: float,
                 d_sim = 24, # Duree de la simulation en heures
                 dt = 60 # Duree d'un intervalle de temps en secondes
                 ) -> None:

        """
        Description :

        Définit :
        -
        -
        -
        ----------------------------------------------------------------

        Arguments :

        -
        -
        -
        """

        # Temperature minimale exterieure atteinte sur 24h
        self.t_min_ext = t_min_ext

        # Temperature maximale exterieure atteinte sur 24h
        self.t_max_ext = t_max_ext

        # Temperature minimale interieure atteinte en 24h
        self.t_min_int = t_min_int

        # Temperature maximale interieure atteinte en 24h
        self.t_max_int = t_max_int

        # Taille des vecteurs conditions aux limites
        self.delta_t = int((d_sim*60)/(dt/60))

        # Vecteur de construction des vecteurs conditions aux limites de taille delta_t
        self.x = np.linspace(0, 2*np.pi, self.delta_t)

    def vec_cl_ext(self) -> np.array:

        """
        Description :


        ----------------------------------------------------------------

        Arguments : None
        """

        return 0.5*(self.t_min_ext - self.t_max_ext)*np.cos(self.x) + 0.5*(self.t_max_ext + self.t_min_ext)

    def vec_cl_int(self) -> np.array:

        """
        Description :


        ----------------------------------------------------------------

        Arguments : None
        """

        return 0.5*(self.t_min_int - self.t_max_int)*np.cos(self.x) + 0.5*(self.t_max_int + self.t_min_int)
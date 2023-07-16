from os import chdir

chdir("C:\\Users\\Hadrien utilisateur\\Documents\\Python Projects")

from InertieThBat.Materiau import Materiau
from InertieThBat.Composant import Composant

m1 = Materiau(2500, 800, 0.145)
m2 = Materiau(1650, 900, 0.036)

c1 = Composant(m1, m2)

c1.ep_materiaux(0.20, 0.10)

c1.ep_comp()

c1.test((m1, m2))

c1.test((m1, 2))

c1.rth_comp()

c2 = Composant(m1, 2)

c2.ep_materiaux(0.05, 0.10)

c2.ep_comp()

/!\ Work in progress. 1 module is not yet finished.
/!\ All the docstring, comments and variable names are still in french

# Aim of the project
Programming language : Python
Create a basic 1D thermal calculation package to compute thermal inertia of a multilayer wall.
Training myself at package structure and linear algebra with numpy.

# Modules

## Materiau
Create a material with its physical properties :
    * Thikness
    * Volumic mass
    * Specific heat capacity
    * Thermal conductivity
    * Thermal diffusivity
    * Thermal effusivity

## Composant
Add multiple __Materiau__ objects into one __Composant__ object, acting like a 1D sliced multilayer wall.

## CalculTh_v1
Calculate and plot thermal diffusion through a wall (__Composant__ object) giving some initial and boundary conditions, with 1D numeric explicit method resolution of the heat equation.

'''
==================================================================================
Simply supported PLA beam solution (maximum values): 3 points and 4 points bending
For the 3 points bending, the point load is placed in the middle of the beam.
For the 4 points bending, the points lods are placed at the same distance from the 
supports

Author: Adel Tayeb
==================================================================================
'''

import numpy as np
import matplotlib.pyplot as plt

# Beam parameters
length = 200 # Length of the beam (mm)

width = 20 # Width of the beam (mm)

height = 10 # Height of the beam (mm)

I =  width*height**3/12 # Area moment of Inertia (mm^4)
print('the Area moment is ', I)

E = 3500 # Elastic modulus of PLA (Mpa) 

F = 100  # Point load (N)

load_type = 1 # Flag for load type: 0: 3 points bending, 1: 4 points bending

# Functions

def beam_deflection(E,I,F,L,x,load_type):
    if load_type == 0: # this is the case for 3 points bending 
        if x <= L/2:
            deflection = -F*x*(3*L**2-4*x**2)/(48*E*I)
        elif x > L/2: 
            deflection = -F*(L-x)*(3*L**2-4*(L-x)**2)/(48*E*I)
        else:
            raise RuntimeError('x should be in the interval [0, L]')
    else: # this is the case for 4 points bending
        a = float(input('Enter the distance between support and lod in (mm)'))
        # TO DO: define a condition on the value of a
        if x <= a:
            deflection = -F*x*(3*a*L**2-3*a**2-x**2)/(E*I)
        elif x > a and x <= (L-a):
            deflection = -F*a*(3*x*L**2-3*x**2-a**2)/(E*I)
        elif x > (L-a) and x <= L:
            deflection = -F*(L-x)*(3*a*L**2-3*a**2-(L-x)**2)/(E*I)
        else:
            raise RuntimeError('x should be in the interval [0, L]')
    return deflection


# Testing
x = 10
print('the deflection @x is ', beam_deflection(E,I,F,length,x,load_type))

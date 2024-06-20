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

E = 3500 # Elastic modulus of PLA (Mpa) 

F = 100  # Point load (N)

load_type = 1 # Flag for load type: 0: 3 points bending, 1: 4 points bending

# a is the distance between the load and the support for the case of 4 points bending

if load_type == 1:
    a = float(input('Enter the distance between support and lod in (mm)'))
    if a > length/2:
        raise RuntimeError('a can not be bigger than L/2')
else:
    a = 0
# TO DO: define a condition on the value of a



## Functions
# Deflection

def beam_deflection(E,I,F,L,x,load_type,a):
    if load_type == 0: # this is the case for 3 points bending 
        if x <= L/2:
            deflection = -F*x*(3*L**2-4*x**2)/(48*E*I)
        elif x > L/2: 
            deflection = -F*(L-x)*(3*L**2-4*(L-x)**2)/(48*E*I)
        else:
            raise RuntimeError('x should be in the interval [0, L]')
    else: # this is the case for 4 points bending
        if x <= a:
            deflection = -F*x*(3*a*L-3*a**2-x**2)/(6*E*I)
        elif x > a and x <= (L-a):
            deflection = -F*a*(3*x*L-3*x**2-a**2)/(6*E*I)
        elif x > (L-a) and x <= L:
            deflection = -F*(L-x)*(3*a*L-3*a**2-(L-x)**2)/(6*E*I)
        else:
            raise RuntimeError('x should be in the interval [0, L]')
    return deflection

# Shear force

def shear_force(E,I,F,L,x,load_type,a):
    if load_type == 0: # this is the case for 3 points bending 
        if x <= L/2:
            force = F/2
        elif x > L/2: 
            force = -F/2
        else:
            raise RuntimeError('x should be in the interval [0, L]')
    else: # this is the case for 4 points bending
        if x <= a:
            force = F
        elif x > a and x <= (L-a):
            force = 0
        elif x > (L-a) and x <= L:
            force = -F
        else:
            raise RuntimeError('x should be in the interval [0, L]')
    return force

# Bending moment

def bending_moment(E,I,F,L,x,load_type,a): # the result is in (Nm)
    if load_type == 0: # this is the case for 3 points bending 
        if x <= L/2:
            moment = F*x/2
        elif x > L/2: 
            moment = (-F/2)*x + F*L/2
        else:
            raise RuntimeError('x should be in the interval [0, L]')
    else: # this is the case for 4 points bending
        if x <= a:
            moment = F*x
        elif x > a and x <= (L-a):
            moment = F*a
        elif x > (L-a) and x <= L:
            moment = -F*x + F*L
        else:
            raise RuntimeError('x should be in the interval [0, L]')
    return 1000*moment # just to convert to Nm


# Maximum deflection shear force and bending moment calculations
D_max = beam_deflection(E,I,F,length,length/2,load_type,a)
T_max = shear_force(E,I,F,length,0,load_type,a)
M_max = bending_moment(E,I,F,length,length/2,load_type,a)

print(f"Maximum Deflection: {abs(D_max)} mm")
print(f"Maximum Shear Force: {T_max} N")
print(f"Maximum Bending Moment: {M_max} Nm")


# Generating points for plotting
x_values = np.linspace(0, length, 100)
bd_values = [beam_deflection(E,I,F,length,x,load_type,a) for x in x_values]
sf_values = [shear_force(E,I,F,length,x,load_type,a) for x in x_values]
bm_values = [bending_moment(E,I,F,length,x,load_type,a) for x in x_values]

# Plotting Beam Deflection Diagram (BDD) Shear Force Diagram (SFD) and Bending Moment Diagram (BMD)
plt.figure(figsize=(18, 6))

# Beam Deflection Diagram
plt.subplot(1, 3, 1)
plt.plot(x_values, bd_values, label='Beam Deflection (Y)', lw=2, color='green')
plt.fill_between(x_values, 0, bd_values, color='skyblue', alpha=0.5)
plt.axhline(0, color='black', lw=1)  # Beam axis
plt.title('Beam Deflection Diagram (BDD)')
plt.xlabel('Position along the beam (mm)')
plt.ylabel('Beam Deflection (mm)')
plt.grid(True)
plt.legend()

# Shear Force Diagram
plt.subplot(1, 3, 2)
plt.plot(x_values, sf_values, label='Shear Force (Vx)', lw=2, color='blue')
plt.fill_between(x_values, 0, sf_values, color='skyblue', alpha=0.5)
plt.axhline(0, color='black', lw=1)  # Beam axis
plt.title('Shear Force Diagram (SFD)')
plt.xlabel('Position along the beam (mm)')
plt.ylabel('Shear Force (N)')
plt.grid(True)
plt.legend()

# Bending Moment Diagram
plt.subplot(1, 3, 3)
plt.plot(x_values, bm_values, color='red', label='Bending Moment (Mx)', lw=2)
plt.fill_between(x_values, 0, bm_values, color='salmon', alpha=0.5)
plt.axhline(0, color='black', lw=1)  # Beam axis
plt.title('Bending Moment Diagram (BMD)')
plt.xlabel('Position along the beam (mm)')
plt.ylabel('Bending Moment (Nm)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

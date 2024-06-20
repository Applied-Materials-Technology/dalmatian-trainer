'''
==================================================================================
Simply supported PLA beam solution: 3 points and 4 points bending

Author: Adel Tayeb
==================================================================================
'''

import numpy as np
import matplotlib.pyplot as plt

# Beam parameters
length = 10  # Length of the beam (mm)

w = 10  # Uniformly distributed load in kN/m 

# Functions
def shear_force(x):
    return w * (length / 2 - x)  # kN

def bending_moment(x):
    return (w * x / 2) * (length - x)  # kNm

# Maximum shear force calculation
V_max = w * length / 2  # The maximum shear force at the ends of the beam

# Maximum bending moment calculation
M_max = w * length ** 2 / 8  # The maximum bending moment at the midpoint of the beam

print(f"Maximum Shear Force: {V_max} kN")
print(f"Maximum Bending Moment: {M_max} kNm")

# Generating points for plotting
x_values = np.linspace(0, length, 100)
sf_values = [shear_force(x) for x in x_values]
bm_values = [bending_moment(x) for x in x_values]

# Plotting SFD
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_values, sf_values, label='Shear Force (Vx)', lw=2, color='blue')
plt.fill_between(x_values, 0, sf_values, color='skyblue', alpha=0.5)
plt.axhline(0, color='black', lw=1)  # Beam axis
plt.title('Shear Force Diagram (SFD)')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Shear Force (kN)')
plt.grid(True)
plt.legend()

# Plotting BMD
plt.subplot(1, 2, 2)
plt.plot(x_values, bm_values, color='red', label='Bending Moment (Mx)', lw=2)
plt.fill_between(x_values, 0, bm_values, color='salmon', alpha=0.5)
plt.axhline(0, color='black', lw=1)  # Beam axis
plt.title('Bending Moment Diagram (BMD)')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Bending Moment (kNm)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

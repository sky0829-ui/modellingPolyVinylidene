import numpy as np
import matplotlib.pyplot as plt

# Electric field (E) and polarization (P) data
E = np.array([-2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 
              0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
P = np.array([-29.8, -29.4, -28.5, -26.5, -22.3, -16.0, -8.5, -2.5, 5.2, 17.0, 
              25.0, 17.0, 5.2, -2.5, -8.5, -16.0, -22.3, -26.5, -28.5, -29.4, -29.8])

# Plotting the P-E loop
plt.figure(figsize=(8, 6))
plt.plot(E, P, 'o-', label='P-E Loop')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.xlabel('Electric Field (kV/mm)')
plt.ylabel('Polarization (µC/cm²)')
plt.title('Synthetic P-E Loop for BaTiO₃')
plt.grid()
plt.legend()
plt.show()

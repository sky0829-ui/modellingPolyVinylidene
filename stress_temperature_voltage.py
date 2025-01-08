import numpy as np
import matplotlib.pyplot as plt

# Constants for BaTiO3
d33 = 190e-12  # Piezoelectric coefficient (C/N)
p = 4e-6       # Pyroelectric coefficient (C/m^2·K)
epsilon_r = 1700  # Relative permittivity
epsilon_0 = 8.854e-12  # Permittivity of free space (F/m)

# Stress and Temperature ranges
stress = np.linspace(0, 1e6, 100)  # Stress in N/m^2
delta_temp = np.linspace(0, 50, 100)  # Temperature change in K

# Calculate voltage for each effect
V_piezo = (d33 * stress) / (epsilon_r * epsilon_0)
V_pyro = (p * delta_temp[:, None]) / (epsilon_r * epsilon_0)

# Combine contributions
V_total = V_piezo + V_pyro.mean(axis=0)

# Plot voltage vs stress
plt.figure(figsize=(8, 6))
plt.plot(stress / 1e6, V_piezo, label="Piezoelectric Voltage")
plt.plot(stress / 1e6, V_total, label="Total Voltage", linestyle="--")
plt.xlabel("Stress (MPa)")
plt.ylabel("Voltage Output (V)")
plt.title("Voltage Output vs Stress")
plt.legend()
plt.grid()

# Plot voltage vs temperature change
plt.figure(figsize=(8, 6))
plt.plot(delta_temp, V_pyro, label="Pyroelectric Voltage")
plt.xlabel("Temperature Change (K)")
plt.ylabel("Voltage Output (V)")
plt.title("Voltage Output vs Temperature Change")
plt.legend()
plt.grid()
plt.show()

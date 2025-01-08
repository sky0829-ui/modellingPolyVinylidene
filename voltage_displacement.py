import numpy as np
import matplotlib.pyplot as plt

# Parameters for BaTiO3
g33 = 1e-9  # Piezoelectric voltage coefficient (m/V)
beta = 1e-12  # Nonlinearity factor (m/V^3)
L = 1e-3  # Length of the sample (m)

# Voltage range
voltage = np.linspace(-100, 100, 500)  # Voltage in Volts

# Displacement calculation
displacement_linear = g33 * voltage * L
displacement_nonlinear = L * (g33 * voltage - beta * voltage**3)

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(voltage, displacement_linear * 1e6, label="Linear Model", linestyle="--")
plt.plot(voltage, displacement_nonlinear * 1e6, label="Nonlinear Model", linewidth=2)
plt.xlabel("Voltage (V)")
plt.ylabel("Displacement (µm)")
plt.title("Displacement vs Voltage for BaTiO₃")
plt.legend()
plt.grid()
plt.show()

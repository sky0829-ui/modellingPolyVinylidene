import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Experimental Data (example: synthetic data)
E_data = np.linspace(-2, 2, 100)  # Electric field (kV/mm)
P_true = 1.0 * np.tanh(E_data / 0.5) + 0.1 * E_data  # True polarization model
P_data = P_true + 0.05 * np.random.normal(size=len(E_data))  # Add noise

# Define the model function
def pe_model(E, Ps, Ec, chi):
    return Ps * np.tanh(E / Ec) + chi * E

# Initial parameter guess
initial_guess = [1.0, 0.5, 0.1]  # Ps, Ec, chi

# Fit the curve
params, covariance = curve_fit(pe_model, E_data, P_data, p0=initial_guess)

# Extract fitted parameters
Ps_fit, Ec_fit, chi_fit = params
print(f"Fitted Parameters: Ps={Ps_fit:.3f}, Ec={Ec_fit:.3f}, chi={chi_fit:.3f}")

# Plot results
plt.figure(figsize=(8, 6))
plt.scatter(E_data, P_data, label='Experimental Data', color='blue')
plt.plot(E_data, pe_model(E_data, *params), label='Fitted Model', color='red', linewidth=2)
plt.xlabel('Electric Field (E) [kV/mm]')
plt.ylabel('Polarization (P) [μC/cm²]')
plt.title('P-E Loop Fitting')
plt.legend()
plt.grid()
plt.show()

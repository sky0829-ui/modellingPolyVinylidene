import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv("Realistic_BaTiO3_PE_loop_data.csv")

# Extract Electric Field (E) and Polarization (P)
electric_field = data["Electric Field (kV/mm)"]
polarization = data["Polarization (µC/cm²)"]

# Plot the P-E loop
plt.figure(figsize=(8, 6))
plt.plot(electric_field, polarization, label="P-E Loop", color="blue", linewidth=2)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Horizontal line at P=0
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Vertical line at E=0
plt.title("P-E Loop of BaTiO3", fontsize=14)
plt.xlabel("Electric Field (kV/mm)", fontsize=12)
plt.ylabel("Polarization (µC/cm²)", fontsize=12)
plt.grid(alpha=0.5)
plt.legend()
plt.show()

# Analyze key properties
# Coercive field (E_c): E where P crosses 0
crossing_indices = np.where(np.diff(np.sign(polarization)))[0]
coercive_fields = electric_field.iloc[crossing_indices].values

# Remnant polarization (P_r): P where E=0
remnant_polarization = polarization.iloc[(np.abs(electric_field)).idxmin()]

# Display results
print("Coercive Fields (E_c):", coercive_fields, "kV/mm")
print("Remnant Polarization (P_r):", remnant_polarization, "µC/cm²")

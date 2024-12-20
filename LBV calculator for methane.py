import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # Universal gas constant in J/(mol·K)

def manton_method(P_max, dPdt_max, V):
    """
    Calculate LBV using Manton's method.
    :param P_max: Maximum explosion pressure (Pa).
    :param dPdt_max: Maximum rate of pressure rise (Pa/s).
    :param V: Volume of the combustion chamber (m^3).
    :return: Laminar Burning Velocity (LBV) in m/s.
    """
    return (3 * V * dPdt_max / (P_max ** 2)) ** (1 / 3)

def lewis_von_elbe_method(P_max, P_0, V, rho_0):
    """
    Calculate LBV using Lewis and von Elbe's method.
    :param P_max: Maximum explosion pressure (Pa).
    :param P_0: Initial pressure (Pa).
    :param V: Volume of the combustion chamber (m^3).
    :param rho_0: Initial density of the mixture (kg/m^3).
    :return: Laminar Burning Velocity (LBV) in m/s.
    """
    return (3 * V * P_max / (P_0 * rho_0)) ** (1 / 3)

def dahoe_method_2005(P_max, dPdt_max, V):
    """
    Calculate LBV using Dahoe's 2005 thin flame method.
    :param P_max: Maximum explosion pressure (Pa).
    :param dPdt_max: Maximum rate of pressure rise (Pa/s).
    :param V: Volume of the combustion chamber (m^3).
    :return: Laminar Burning Velocity (LBV) in m/s.
    """
    return (P_max * V * dPdt_max / R) ** (1 / 3)

def dahoe_method_2013(P_max, P_0, V, gamma):
    """
    Calculate LBV using Dahoe's 2013 thin flame method.
    :param P_max: Maximum explosion pressure (Pa).
    :param P_0: Initial pressure (Pa).
    :param V: Volume of the combustion chamber (m^3).
    :param gamma: Specific heat ratio.
    :return: Laminar Burning Velocity (LBV) in m/s.
    """
    return ((3 * gamma * V * (P_max - P_0)) / P_0) ** (1 / 3)

# Example Input Parameters
P_max = 1.2e5  # Pa (example value for maximum explosion pressure)
dPdt_max = 5e4  # Pa/s (example value for max rate of pressure rise)
V = 0.02  # m^3 (volume of combustion chamber)
P_0 = 1e5  # Pa (initial pressure)
rho_0 = 1.2  # kg/m^3 (initial density)
gamma = 1.4  # Specific heat ratio

# Calculations
lbv_manton = manton_method(P_max, dPdt_max, V)
lbv_lewis = lewis_von_elbe_method(P_max, P_0, V, rho_0)
lbv_dahoe_2005 = dahoe_method_2005(P_max, dPdt_max, V)
lbv_dahoe_2013 = dahoe_method_2013(P_max, P_0, V, gamma)

# Display Results
print("Laminar Burning Velocity Calculations:")
print(f"Manton's Method: {lbv_manton:.4f} m/s")
print(f"Lewis and von Elbe's Method: {lbv_lewis:.4f} m/s")
print(f"Dahoe's 2005 Method: {lbv_dahoe_2005:.4f} m/s")
print(f"Dahoe's 2013 Method: {lbv_dahoe_2013:.4f} m/s")

# Visualization
methods = ["Manton", "Lewis & von Elbe", "Dahoe 2005", "Dahoe 2013"]
values = [lbv_manton, lbv_lewis, lbv_dahoe_2005, lbv_dahoe_2013]

plt.bar(methods, values, color=['blue', 'green', 'orange', 'red'])
plt.title("Laminar Burning Velocity by Method")
plt.xlabel("Method")
plt.ylabel("LBV (m/s)")
plt.grid(axis='y')
plt.show()

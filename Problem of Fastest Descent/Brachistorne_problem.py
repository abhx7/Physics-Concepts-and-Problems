import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Boundary conditions
x1, y1 = 0, 4  # Start point
x2, y2 = 1, 0  # End point
delta_x = x2 - x1
delta_y = y1 - y2

# Define the system of equations to determine theta_end
def equations(theta_end):
    r = delta_y / (1 - np.cos(theta_end))  # Radius based on height
    return r * (theta_end - np.sin(theta_end)) - delta_x  # Horizontal distance constraint

# Solve for theta_end
theta_end = fsolve(equations, np.pi)[0]

# Compute radius
r = delta_y / (1 - np.cos(theta_end))

print(f"Radius (r): {r}")
print(f"Final Angle (theta_end): {theta_end}")

# Cycloid parameterization
theta = np.linspace(0, theta_end, 100)
x = r * (theta - np.sin(theta)) + x1  # Offset to start at x1
y = y1 - r * (1 - np.cos(theta))  # Offset to start at y1

# Visualization of the Brachistochrone Curve
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Brachistochrone Curve (Cycloid)", color='blue', linewidth=2)
plt.scatter([x1, x2], [y1, y2], color='red', zorder=5, label="Points A and B", s=100)
plt.title("Brachistochrone Problem Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.gca()#.invert_yaxis()  # Invert y-axis to reflect gravity
plt.legend()
plt.show()

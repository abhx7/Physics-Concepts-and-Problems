import numpy as np
import matplotlib.pyplot as plt

# Define constants
g = 9.81  # Acceleration due to gravity in m/s^2
A = np.array([0, 50])  # Starting point
B = np.array([60, 0])  # Ending point

# Cycloid parameters to fit the brachistochrone curve
theta_max = np.pi  # Maximum angle (adjust based on end point)
num_points = 100  # Number of points along the curve
theta = np.linspace(0, theta_max, num_points)

# Calculate the radius of the cycloid based on the desired end point
R = B[1] / (1 - np.cos(theta_max))  # Radius of the cycloid circle

# Parametric equations for the cycloid (Brachistochrone curve)
x_cycloid = A[0] + R * (theta - np.sin(theta))
y_cycloid = A[1] - R * (1 - np.cos(theta))

# Calculate time of descent along the cycloid path
ds = np.sqrt(np.diff(x_cycloid)**2 + np.diff(y_cycloid)**2)  # Path differentials
velocities = np.sqrt(2 * g * (A[1] - y_cycloid[:-1]))  # Speeds at each point
time_of_descent = np.sum(ds / velocities)  # Total time of descent

# Display time of descent
print(f"Optimized time of descent: {time_of_descent:.4f} seconds")

# Visualization
plt.figure(figsize=(10, 6))

# Plot the brachistochrone curve
plt.plot(x_cycloid, y_cycloid, 'r-', linewidth=2, label='Fastest Descent Path')

# Mark starting and ending points
plt.plot(A[0], A[1], 'bo', markersize=8, label='Start Point A')
plt.plot(B[0], B[1], 'go', markersize=8, label='End Point B')

# Add labels and formatting
plt.title('Fastest Descent Path (Brachistochrone Curve)')
plt.xlabel('x (horizontal position)')
plt.ylabel('y (vertical position)')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Annotate points
plt.text(A[0], A[1], '  A', verticalalignment='bottom', fontsize=12, fontweight='bold', color='blue')
plt.text(B[0], B[1], '  B', verticalalignment='top', fontsize=12, fontweight='bold', color='green')

plt.show()

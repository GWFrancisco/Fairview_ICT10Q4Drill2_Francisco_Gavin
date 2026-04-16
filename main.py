# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Create sample data using NumPy
x = np.array([1, 2, 3, 4, 5])
y = x * 2  # Multiply each value by 2

# Print to confirm NumPy works
print("X values:", x)
print("Y values:", y)

# Create a simple plot using Matplotlib
plt.plot(x, y)

# Add labels and title
plt.title("Test Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Show the graph
plt.show()
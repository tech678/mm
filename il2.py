import numpy as np
import matplotlib.pyplot as plt

# Define the function for the irregular lamina
def lamina_function(x):
    return np.sin(x) + 0.5 * np.sin(3*x) + 1.5

# Define the rectangle's dimensions
rectangle_width = 10  # Width of the rectangle
rectangle_height = 10  # Height of the rectangle
rectangle_area = rectangle_width * rectangle_height

# Generate random points inside the rectangle
num_points = 1000
random_x = np.random.uniform(0, rectangle_width, num_points)
random_y = np.random.uniform(0, rectangle_height, num_points)

# Count the number of points inside the object
points_inside_object = sum([1 for x, y in zip(random_x, random_y) if y < lamina_function(x)])

# Calculate the area of the object using the formula
object_area = rectangle_area * (points_inside_object / num_points)

# Print the calculated areas
print(f"Area of rectangle: {rectangle_area} cm^2")
print(f"Number of points inside object: {points_inside_object}")
print(f"Area of object: {object_area} cm^2")

# Plot the irregular lamina and the random points
x_vals = np.linspace(0, rectangle_width, 1000)
lamina_vals = lamina_function(x_vals)

plt.plot(x_vals, lamina_vals, label="Irregular Lamina: sin(x) + 0.5 * sin(3x) + 1.5")
plt.fill_between(x_vals, lamina_vals, color='lightblue', alpha=0.5)
plt.scatter(random_x, random_y, c='red', marker='.', label="Random Points")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Closed Irregular Lamina and Random Points")
plt.xlim(0, rectangle_width)
plt.ylim(0, rectangle_height)

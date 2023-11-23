# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 12
# Date: 11/20/2023
#

# comment
import numpy as np
import matplotlib.pyplot as plt

initial_point = np.array([0, 1])
matrix = np.array([[1.02, 0.095], [-0.095, 1.02]])

x_coords = []
y_coords = []

point = initial_point.copy()
for _ in range(250):
    x_coords.append(point[0])
    y_coords.append(point[1])
    point = np.dot(matrix, point)

plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, label='Points Trace')

plt.title('Pretty Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

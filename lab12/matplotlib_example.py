# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Cameron Cao
#        Manas Navale
#        Jeremiah Thomas
# Section: 577
# Assignment: Lab Topic 12
# Date: 11/20/2023
#

#comment

# As a team, we have gone through all required sections of the # tutorial, and each team member understands the material
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2.0, 2.0, 100)
f_2 = 2
f_6 = 6

y_2 = 1 / (4 * f_2) * x**2
y_6 = 1 / (4 * f_6) * x**2

plt.figure(figsize=(8, 6))
plt.plot(x, y_2, label='f = 2', linewidth=2.0, color='blue')
plt.plot(x, y_6, label='f = 6', linewidth=6.0, color='red')

plt.title('Parabolas with different focal lengths')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()

x = np.linspace(-4.0, 4.0, 25)

y = 2 * x**3 + 3 * x**2 - 11 * x - 6

plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Cubic Polynomial', color='green', marker='o')

plt.title('Plot of a Cubic Polynomial')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(x, y_sin, label='sin(x)', color='blue')
ax1.set_title('sin(x)')
ax1.legend()
ax1.grid(True)

ax2.plot(x, y_cos, label='cos(x)', color='red')
ax2.set_title('cos(x)')
ax2.legend()
ax2.grid(True)

plt.show()

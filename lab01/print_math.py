# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 1
# Date: 8/24/2023
#

from math import *

# Force
mass = 27
acceleration = 1.5
force = mass * acceleration
print("Force is", force, "N")

# Wavelength
distance = 0.025
angle = sin(radians(35)) 
wavelength = 2 * distance * angle
print("Wavelength is", wavelength, "nm")

# Radioactive decay
weight = 27
half_life = 3.8
time = 5
decay = weight * (2 ** (-time / half_life)) 
print("Radon-222 left is", decay, "g")

# Pressure
moles = 5
volume = 0.27
temp = 415
g_const = 8.314
pressure = ((moles * g_const * temp) / volume)/ 1000
print("Pressure is", pressure, "kPa")
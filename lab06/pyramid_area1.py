# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 6
# Date: 10/2/2023
#
from math import *
sideLength = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))
total = 0
bottom = ((sideLength*layers)**2)*(sqrt(3))/4

for l in range (1,layers+1):
    total += (sideLength * l * sideLength * 3) + (((sideLength*l)**2)*(sqrt(3))/4) - ((((sideLength) * (l-1))**2)*(sqrt(3))/4)

print (f'You need {total:.2f} m^2 of gold foil to cover the pyramid')
    

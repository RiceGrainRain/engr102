# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 6
# Date: 10/2/2023
#

#imports
from math import sqrt

sideLength = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))
total = 0

Sn = ((((2*(sqrt(((sideLength*3)/2)*((((sideLength*3)/2)-(sideLength))**3))) + 3*(sideLength)*sideLength) - (((sideLength)**2)*(sqrt(3))/4)) + ((2*(sqrt(((sideLength*layers*3)/2)*((((sideLength*layers*3)/2)-(sideLength*layers))**3))) + 3*(sideLength*layers)*sideLength) - ((((sideLength*layers)**2)*(sqrt(3))/4) + (((sideLength*(layers-1))**2)*(sqrt(3))/4))))/2)*layers
print(f'You need {Sn:.2f} m^2 of gold foil to cover the pyramid')


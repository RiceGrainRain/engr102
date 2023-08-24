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
#style comment
def f(x):
    return sin(x - 1)/(x - 1)

print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
guess = 2  
print("My guess for the final value is:", guess)


x_values = [1.1, 1.01, 1.001, 1.0001, 1.00001, 1.000001, 1.0000001, 1.00000001]
for x in x_values:
    result = f(x)
    print((result))


if result == guess: 
    print("my guess was correct")
else:
    print("\nMy guess was a little off")
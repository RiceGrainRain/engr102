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

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
import numpy as np


A = np.arange(12).reshape(3, 4) 
B = np.arange(8).reshape(4, 2)   
C = np.arange(6).reshape(2, 3)   

print("A =")
print(A)
print("\nB =")
print(B)
print("\nC =")
print(C)
print()

D = np.dot(np.dot(A, B), C)

print("D =")
print(D)
print()

print("D^T =")
print(D.T)
print()

E = np.sqrt(D) / 2
print("E =")
print(E)

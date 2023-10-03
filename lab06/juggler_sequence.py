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
n = abs(int(input("Enter a positive integer: ")))
originalN = n
numList = []
numList.append(n)
counter = 0
while(n!=1):
    if n%2==0:
        n = floor(sqrt(n))
        numList.append(n)
        counter += 1
    else:
        n = floor(pow(n,(3/2)))
        numList.append(n)
        counter += 1
res = str(numList)[1:-1]
print(f"The Juggler sequence starting at {originalN} is:\n{res}")
print(f"It took {counter} iterations to reach 1")
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
n = abs(int(input("Enter a value for n: ")))
sum = 0
for i in range(1,n):
    sum+=i

if n == 1:
    print("1 is a balancing number with r=0")

if sqrt(8*n*n+1) % 1 == 0:
    r = int(((-2*n-1)+sqrt(8*n*n+1))/2)
    print(f"{n} is a balancing number with r={r}")
else:
    print(f"{n} is not a balancing number")
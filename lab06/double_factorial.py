# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 6
# Date: 10/2/2023
#

def doublefactorial(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        done = False
        multiplier = n
        while(not done):
              multiplier -= 2
              if multiplier == 0:
                   return n
              else:
                   n *= multiplier
    else:
         done = False
         multiplier = n
         while(not done):
              multiplier -= 2
              if multiplier - 1 == 0:
                   return n
              else:
                   n *= multiplier


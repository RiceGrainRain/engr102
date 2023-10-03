# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 2(team)
# Date: 8/29/2023
#

from math import *

#initializing times
t = 85 - 12
time1 = 30 - 12
time2 = 37.5 - 12
time3 = 45 - 12
time4 = 52.5 - 12
time5 = 60 - 12

xi = 8
xf = -5
yi = 6
yf = 30
zi = 7
zf = 9

xspeed = (xf - xi)/t
yspeed = (yf - yi)/t
zspeed = (zf - zi)/t

xdistance = xspeed * time1 + 8
ydistance = yspeed * time1 + 6
zdistance = zspeed * time1 + 7

xdistance2 = xspeed * time2 + 8
ydistance2 = yspeed * time2 + 6
zdistance2 = zspeed * time2 + 7
xdistance3 = xspeed * time3 + 8
ydistance3 = yspeed * time3 + 6
zdistance3 = zspeed * time3 + 7
xdistance4 = xspeed * time4 + 8
ydistance4 = yspeed * time4 + 6
zdistance4 = zspeed * time4 + 7
xdistance5 = xspeed * time5 + 8
ydistance5 = yspeed * time5 + 6
zdistance5 = zspeed * time5 + 7

print("At time 30.0 seconds:")
print("x1 = " + f"{xdistance:.17}" + " m")
print("y1 = " + f"{ydistance:.17}" + " m")
print("z1 = " + f"{zdistance:.17}" + " m")
print("-----------------------")
print("At time 37.5 seconds:")
print("x2 = " + f"{xdistance2:.17}" + " m")
print("y2 = " + f"{ydistance2:.17}" + " m")
print("z2 = " + f"{zdistance2:.16}" + " m")

print("-----------------------")
print("At time 45.0 seconds:")
print("x3 = " + f"{xdistance3:.17}" + " m")
print("y3 = " + f"{ydistance3:.17}" + " m")
print("z3 = " + f"{zdistance3:.16}" + " m")

print("-----------------------")
print("At time 52.5 seconds:")
print("x4 = " + f"{xdistance4:.15}" + " m")
print("y4 = " + f"{ydistance4:.17}" + " m")
print("z4 = " + f"{zdistance4:.15}" + " m")

print("-----------------------")
print("At time 60.0 seconds:")
print("x5 = " + f"{xdistance5:.16}" + " m")
print("y5 = " + f"{ydistance5:.16}" + " m")
print("z5 = " + f"{zdistance5:.16}" + " m")

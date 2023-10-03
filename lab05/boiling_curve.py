# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 1
# Date: 9/24/2023
#
import math

#init points
x0, y0 = 1.3, 1000
x1, y1 = 5, 7000
x2, y2 = 30, 1.5e6
x3, y3 = 120, 2.5e4
x4, y4 = 1200, 1.5e6

#slop of each points
m1 = math.log(y1/y0) / math.log(x1/x0)
m2 = math.log(y2/y1) / math.log(x2/x1)
m3 = math.log(y3/y2) / math.log(x3/x2)
m4 = math.log(y4/y3) / math.log(x4/x3)

def segment_AB(x):
    return y0 * (x / x0) ** m1

def segment_BC(x):
    return y1 * (x / x1) ** m2

def segment_CD(x):
    return y2 * (x / x2) ** m3

def segment_DE(x):
    return y3 * (x / x3) ** m4

#user input
excess_temp = float(input("Enter the excess temperature: "))

#no neg temps
if excess_temp < 0:
    print("Surface heat flux is not available")
else:
   #surface heat flux
    if 1.3 <= excess_temp < 5:
        heat_flux = segment_AB(excess_temp)
    elif 5 <= excess_temp < 30:
        heat_flux = segment_BC(excess_temp)
    elif 30 <= excess_temp < 120:
        heat_flux = segment_CD(excess_temp)
    elif 120 <= excess_temp <= 1200:
        heat_flux = segment_DE(excess_temp)
    else:
        heat_flux = None

    if heat_flux is not None:
        print(f"The surface heat flux is approximately {int(heat_flux + 0.5)} W/m^2")
    else:
        print(f"Surface heat flux is not available")

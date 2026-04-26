# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 12:57:24 2023

@author: Lenovo
"""

import math
import sys
# input parameters
nglass = 1.4
nair   = 1.0 

print("Input a glass angle in degrees")
rad_glass = float(input())
theta_glass = rad_glass*(1/180)*math.pi

if theta_glass <= math.asin(-1/1.4) or theta_glass >= math.asin(1/1.4):
    print("this angle has no refraction value")
    sys.exit()
 

print("The glass angle in radians is", theta_glass)


# solve Snell's law

tmp = (nglass * math.sin(theta_glass ) ) / nair 
theta_refract = math.asin(tmp)

print("Refraction angle = " , theta_refract, " in radians" )

degree_theta_refract = theta_refract*180*(1/math.pi)

print("Refraction angle in degrees = ", degree_theta_refract)
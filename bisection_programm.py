# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:40:20 2022

@author: Lenovo
"""
import math
#The programm will calculate the root of a function given the root is between the two given points
a = float(input('a = ' ))
b = float(input('b = '))
tol = float(input('tolerance = '))
def f(x):
    return x - math.exp(1/x)
def bijection(a,b,tol):
    while abs(b-a)> 2*tol:
       c = (b+a)/2
       if f(a)*f(c) <0:
              b = c
       else:
           a = c
    return c
root = bijection(a,b,tol)
print('The root of the function for a tolerance of %.6f is %.10f and lies between points x = %.3f and x = %.3f' %(tol,root,a,b))

  
   


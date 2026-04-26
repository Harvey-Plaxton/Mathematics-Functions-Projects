# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:17:52 2023

@author: Lenovo
"""

##
##https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
##
##  Use the scipy library to solve the linear programming problem on page 15 
##  in lecture 2.
##
#If maximum is wanted do -1 x objective function
#If minimum leave as is

#  objective function
f = [-1, -1,-1,-1]
# If contraints indicate greater than; -1 x constraint variables (not -1 x result of constraint)
A = [ [1,2,-3,5]  , [5,-2,0,6] , [2,3,2,3] , [0,-1,1,2] ]
b = [4,8,3,0]
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0,None)
x3_bounds = (0, None)

# Find minimum
from scipy.optimize import linprog
res = linprog(f, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds,x2_bounds,x3_bounds),
              options={"disp": True})

# print the results out
print(res)
print(-1.0*res.fun)
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 13:31:07 2023

@author: Lenovo
"""

#
#  Analysis of the statistics of the series a_i = i**2
#


import math

# print number of terms in the series
n = 4
print("Number of terms in series = ", n)


total = 0.0 
for i in range(0,n+1) :
  total += i**2
print("Total slow method = " , total )

Sn = n * (n + 1 ) * (2*n + 1) / 6 
print("Formuale method Sn " , Sn)

var = 0.0 
for i in range(0,n+1) :
  var += (Sn - i**2)**2


std = math.sqrt(var)/n

print("Standard deviation = " , std )


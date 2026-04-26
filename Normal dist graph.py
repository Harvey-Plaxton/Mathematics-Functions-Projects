# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:22:55 2023

@author: Lenovo
"""

from random import gauss
import numpy as np
import math
import matplotlib .pyplot as plt

nsample = 10000
# generate some Gaussian values
data = []
for _ in range(nsample ):
 value = gauss (0, 1)
 data.append(value)
def normal(x,mm ,sig):
  ans = math.exp( -1.0*(x-mm)**2 / (2.0 *sig**2 )) / (sig*math.sqrt (2.0*math.pi))
  return ans
x_vec = np.linspace(-4,4,1000)
y = []
for x in x_vec :
 yl = normal(x,0 ,1)
 y.append(yl)
plt.plot(x_vec , y, "ro")
plt.show ()

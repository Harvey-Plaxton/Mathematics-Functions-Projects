# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:23:40 2023

@author: Lenovo
"""

#  Example of plotting a linear, quadratic and cubic
#  function.
#


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = x

plt.plot(x, 4*x-8, label='y=4x-8')
plt.plot(x, (4/3)*x-4, label='y=1/3(4x-12)')
plt.plot(x, 8- 4*x,label='y=8-4x')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Linear programming problem")

plt.xlim(0,10)
plt.ylim(0,10)

plt.legend()

plt.show()
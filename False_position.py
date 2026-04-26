# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:13:01 2022

@author: Lenovo
"""
import math

def f(x):
    return x - math.exp(1/x)

def False_Position(a,b,acc):
    while abs(b-a)>2*acc:
        c = b - f(b)*((b-a)/(f(b)-f(a)))
        if f(a)*f(c)<0:
            b = c
        else:
            a = c
    return c
False_Position(1,2,0.001)

# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:07:24 2022

@author: Lenovo
"""
import math
#%%
def f(x):
    return math.cos(x)
#%%
def Li(xi,xj,xk):
    coeff=1/((xi-xk)*(xi-xj))
    ai = coeff
    bi = (-xj - xk)*coeff
    ci = (-xj)*(-xk)*coeff
    return ai,bi,ci
#%%
def p2(x,x0,x1,x2,fx0,fx1,fx2):
    a0,b0,c0 = Li(x0,x1,x2)
    a1,b1,c1 = Li(x1,x0,x2)
    a2,b2,c2 = Li(x2,x0,x1)
    return (((a0*fx0)+(a1*fx1)+(a2*fx2))*x**2)+(x*((b0*fx0)+(b1*fx1)+(b2*fx2)))+(c0*fx0)+(c1*fx1)+(c2*fx2)
#%%
p2(0.43,0.3,0.4,0.5,0.95534,0.92106,0.87758)
#%%
def p2_form(x0,x1,x2,fx0,fx1,fx2):
    a0,b0,c0 = Li(x0,x1,x2)
    a1,b1,c1 = Li(x1,x0,x2)
    a2,b2,c2 = Li(x2,x0,x1)
    x_squared = (a0*fx0)+(a1*fx1)+(a2*fx2)
    x_1 = (b0*fx0)+(b1*fx1)+(b2*fx2)
    x_0 = (c0*fx0)+(c1*fx1)+(c2*fx2)
    print(f'{x_squared}x^2 + {x_1}x + {x_0}')
#%%
p2_form(0.3,0.4,0.5,0.95534,0.92106,0.87758)
p2_form(0,1,3,2,4,26)
p2_form(0,1,2,1,1,1)
p2_form(0,1,4,2,5,14)
p2_form(5,7,8,1.16,2.21,2.4)

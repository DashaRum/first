# -*- coding: utf-8 -*-
"""
C:\Documents and Settings\t08-32\.spyder2\.temp.py
"""

import math
import numpy as np
import matplotlib.pyplot as plt

class Complex:

         def __init__(self, x, y):
             self.re = x
             self.im = y
             
         def __repr__(self):
             return "Complex(%s, %s)" % (self.re, self.im)

         def __add__(self, b):
             res = Complex(self.re+b.re,self.im+b.im)
             return res
             
         def ABS(self):
             return ((self.re)**2 + (self.im)**2)**0.5

         def polar(self):
             r = self.ABS()
             phi = math.atan(self.im/self.re)*180/math.pi
             if phi>=360.0:
                 phi = phi-math.floor(phi/360.)*360
             return (r,phi)
             
         def __mul__(self, z):
             a = self.re
             b = self.im
             c = z.re
             d = z.im
             res = Complex(a*c-b*d, b*c+a*d)
             return res
             
         def quad(self):
             a = self.re
             b = self.im
             res = Complex(a**2-b**2, 2*a*b)
             return res
             
         def conj(self):
             res = Complex(self.re, -self.im)
             return res
             
         def division(self,z):
             a,b = self.re, self.im
             c,d = z.re, z.im            
             x = (a*c+b*d)/(c**2+d**2)
             y = (b*c-a*d)/(c**2+d**2)
             return Complex(x,y)

def iterate(c):
    z = c
    for k in range(1,20):
        z = z*z + c
        if z.ABS()>=2:
            return 0
    return 1


N = 1000
Mandelbrot = np.zeros(shape=(2*N,2*N))
#np.linspace(-1.0, 1.0, N):
for x in range(0,2*N):
    for y in range(0,2*N):
        c = Complex((x-1000)/(N+0.0),(y-1000)/(N+0.0))
        Mandelbrot[x,y] = iterate(c)


print Mandelbrot
plt.imshow(Mandelbrot, cmap='summer')
plt.show()

print (1+2j)*(3+6j)
print Complex(1,2)*Complex(3,6)
print Complex(2,2).ABS()





import sympy as sym
import matplotlib.pyplot as plt
import math

f = 2*(10**0)
w = 2*math.pi*f
real = (((0.9*(w**2))+0.1)/((w**4)-(2*(w**2))+1))*1000
im = (w*(((-w**2)+0.9)/((w**4)-(2*(w**2))+1)))*1000
mag = math.sqrt((real**2)+(im**2))
print(mag)
db_mag = 20*math.log10(mag)
print(db_mag)
fase = math.atan(real/im)
print(fase)

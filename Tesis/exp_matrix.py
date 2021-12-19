from scipy.linalg import expm, sinm, cosm
import numpy as np
import sympy as sym
import math

t = sym.Symbol('t')

a = np.array([[0, 1], [-2, -3]])
exp_matrix = expm(a*t)
print(exp_matrix)


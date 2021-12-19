import sympy as sym
import numpy as np
from sympy import latex
from sympy import *
from src.parameter import Parameter

z_11 = sym.Symbol('Z_11')
z_12 = sym.Symbol('Z_12')
z_21 = sym.Symbol('Z_21')
z_22 = sym.Symbol('Z_22')

k = sym.Symbol('k')
T_0 = sym.Symbol('T_0')
B = sym.Symbol('B')

#Red compuerta
Z_Lg = sym.Symbol('Z_Lg')
Z_Cpg = sym.Symbol('Z_Cpg')
Z_Rg = sym.Symbol('Z_Rg')

i = sym.Symbol('i')
w = sym.Symbol('w')

c = sym.Symbol('C_pg')
l = sym.Symbol('L_g')
r = sym.Symbol('R_g')

Z_Lg = 1j*w*l
Z_Cpg = 1/(1j*w*c)
Z_Rg = r

z_11 = Z_Lg + Z_Cpg
z_12 = Z_Cpg
z_21 = Z_Cpg
z_22 = Z_Rg+Z_Cpg

# z_11 = Z_Cpg
# z_12 = Z_Cpg
# z_21 = Z_Cpg
# z_22 = Z_Rg+Z_Cpg

Zg = np.array([[z_11, z_12], [z_21, z_22]])
print(Zg[0][0], '  |  ', Zg[0][1])
print(Zg[1][0], '  |  ', Zg[1][1])
Zg_l = Matrix(Zg.tolist())
print('ZG:\n', latex(Zg_l))

print()
A, B, C, D = Parameter.z_to_abcd(Zg[0][0], Zg[0][1], Zg[1][0], Zg[1][1])
A = sym.simplify(A)
B = sym.simplify(B)
C = sym.simplify(C)
D = sym.simplify(D)
print(A, '  |  ', B)
print(C, '  |  ', D)
ABCD_l = Matrix([[A, B], [C, D]])
print('ABCD:\n', latex(ABCD_l))
print()
A_g = np.array([[A, B], [C, D]])

C_zg = np.array([[0, 0], [0, Z_Rg]])

P_za = np.array([[1, -A], [0, -C]])
P_za_l = Matrix(P_za.tolist())
print('P_za:\n', latex(P_za_l))
P_za_t = P_za.transpose()
P_za_t_l = Matrix(P_za_t.tolist())
print('P_za_t:\n', latex(P_za_t_l))

print()
C_ag = (P_za*C_zg)*P_za_t
C_ag = np.matmul(np.matmul(P_za, C_zg), P_za_t)
print(C_ag)

C_ag_l = Matrix(C_ag.tolist())
print('ZG:\n', latex(C_ag_l))
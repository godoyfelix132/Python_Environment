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
Z_Ls = sym.Symbol('Z_Ls')
Z_Rs = sym.Symbol('Z_Rs')

i = sym.Symbol('i')
w = sym.Symbol('w')

l = sym.Symbol('L_s')
r = sym.Symbol('R_s')

Z_Ls = 1j*w*l
Z_Rs = r

z_11 = Z_Rs + Z_Ls
z_12 = Z_Rs + Z_Ls
z_21 = Z_Rs + Z_Ls
z_22 = Z_Rs + Z_Ls


# z_11 = Z_Cpg
# z_12 = Z_Cpg
# z_21 = Z_Cpg
# z_22 = Z_Rg+Z_Cpg

Zs = np.array([[z_11, z_12], [z_21, z_22]])

print(Zs[0][0], '  |  ', Zs[0][1])
print(Zs[1][0], '  |  ', Zs[1][1])
Zs_l = Matrix(Zs.tolist())
print('ZG:\n', latex(Zs_l))

print()
A, B, C, D = Parameter.z_to_abcd(Zs[0][0], Zs[0][1], Zs[1][0], Zs[1][1])
A = sym.simplify(A)
B = sym.simplify(B)
C = sym.simplify(C)
D = sym.simplify(D)
print(A, '  |  ', B)
print(C, '  |  ', D)
ABCD_l = Matrix([[A, B], [C, D]])
print('ABCD:\n', latex(ABCD_l))
print()
A_s = np.array([[A, B], [C, D]])

C_zs = np.array([[Z_Rs, Z_Rs], [Z_Rs, Z_Rs]])

P_za = np.array([[1, -A], [0, -C]])
P_za_l = Matrix(P_za.tolist())
print('P_za:\n', latex(P_za_l))
P_za_t = P_za.transpose()
P_za_t_l = Matrix(P_za_t.tolist())
print('P_za_t:\n', latex(P_za_t_l))

print()
C_as = (P_za*C_zs)*P_za_t
C_as = np.matmul(np.matmul(P_za, C_zs), P_za_t)
print(C_as)

C_as_l = Matrix(C_as.tolist())
print('C_ag:\n', latex(C_as_l))
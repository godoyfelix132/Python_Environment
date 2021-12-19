import sympy as sym
from sympy import latex
import numpy as np
import matplotlib.pyplot as plt
import math


def get_parallel(r1, r2):
    rp = 1/((1/r1)+(1/r2))
    gp = 1/rp
    return gp


s = sym.Symbol('s')
m = 10**-3
u = 10**-6
Cgdp1 = 8*(10**-14)
Cgdn3 = 7*(10**-13)
Cgsp2 = 1.5*(10**-15)
CL_v = 1*(10**-12)
f = 1*(10**6)
w = 2*3.1416*f
s_v = complex(0, w)


gmp1 = 2.5372*m
gmp2 = gmp1
gmn3 = 524.0185*u
gdsp1 = 25.2992*u
gdsp2 = gdsp1
gdsn3 = 9.219*u


d1 = sym.Symbol('g_dsp1')
# r1 = sym.Symbol('r_p1')
m2 = sym.Symbol('g_mp2')
d2 = sym.Symbol('g_dsp2')
m3 = sym.Symbol('g_mn3')
d3 = sym.Symbol('g_dsn3')
vx = sym.Symbol('V_x')
vi = sym.Symbol('V_in')
vo = sym.Symbol('V_out')
Cb1 = sym.Symbol('C_gdp1')
Cb3 = sym.Symbol('C_gdn3')
Ca2 = sym.Symbol('C_gsp2')
CL = sym.Symbol('C_L')

# d1 = sym.Symbol('d1')
# m2 = sym.Symbol('m2')
# d2 = sym.Symbol('d2')
# m3 = sym.Symbol('m3')
# d3 = sym.Symbol('d3')
# vx = sym.Symbol('vx')
# vi = sym.Symbol('vi')
# vo = sym.Symbol('Vo')
# Cb1 = sym.Symbol('Cb1')
# Cb3 = sym.Symbol('Cb3')
# Ca2 = sym.Symbol('Ca2')
# CL = sym.Symbol('CL')

# Cb1 = sym.Symbol('x')
# Cb3 = sym.Symbol('y')
# Ca2 = sym.Symbol('z')
# CL = sym.Symbol('l')

# eq_1 = sym.Eq((vx * d1) + (d2 * (vx - vo)), m2 * (vo - vx))
# eq_2 = sym.Eq((m2*(vo-vx)) + (m3*vi) + (d2*(vo-vx)) + (d3*vo), 0)
#
# solve_x_1 = sym.solve(eq_1, vx)
# solve_x_2 = sym.solve(eq_2, vx)
#
# eq_match = sym.Eq(solve_x_1[0], solve_x_2[0])
# eq = sym.solve(eq_match, vo)
# eq = sym.Eq(eq[0], 0)
# eq = eq.subs(vi, 1)
#
# print('eq 1:', latex(eq_1))
# print('eq 2:', latex(eq_2))
# print('Solve x in 1:', solve_x_1[0])
# print('Solve x in 2:', solve_x_2[0])
# print('Match:', eq_match)
# print('Final:', eq.args)
# eq = eq.args[0]
# # eq = eq.subs(m2, gmp2).subs(m3, gmn3).subs(d1, gdsp1).subs(d2, gdsp2).subs(d3, gdsn3)
# print('test 1', eq)

####################################cap
print()

#Paralelo arriba
r1 = 1/d1
r2 = 1/(s*Cb1)
P1 = get_parallel(r1, r2)
print('Parallet under', latex(P1))

P1_pos = P1*(m2 + (s*Cb3))
print('P1_pos', latex(P1_pos))

P1_neg = P1*(-m3 + (s*Cb3))
print('P1_neg', latex(P1_neg))

#Paralelo abajo
r1 = 1/d3
r2 = 1/(s*CL)
P2 = get_parallel(r1, r2)
print('Parallel below:', latex(P2))

P2_pos = P2*(m2 + (s*Ca2))
print('P2_pos', latex(P2_pos))

print('P1_pos + P2_pos:', P1_pos+P2_pos)
print('P1P2:', P1*P2)
factor = sym.factor((P1_pos)+(P2_pos)+(P1*P2), (d1 + (s*Cb1))*(d3 + (s*CL)))
factor = sym.factor(factor, s)
print('factor:', latex(factor))
# P1 = sym.Symbol('P_1')
# P2 = sym.Symbol('P_2')
# P1 = sym.Symbol('P1')
# P2 = sym.Symbol('P2')

#nodal ecuations
# node_vx = sym.Eq((d2*(vx - vo)) + (P1*vx) + (s*Ca2*(vx - vo)), (m2*(vo - vx)))
# node_vo = sym.Eq((d2*(vo - vx)) + (P2*vo) + (s*Cb3*(vo - vi)) + (m2*(vo - vx)) + (m3*vi), 0)
node_vx = sym.Eq((s*Ca2*(-vo+vx)) + (vx * P1) + (d2 * (vx - vo)), m2 * (vo - vx))
node_vo = sym.Eq((s*Cb3*(-vi+vo)) + (P2*vo) + (m3*vi) + (d2*(vo-vx)) + (m2*(vo-vx)), 0)

#simplicated ecuation
# node_vx = sym.Eq((P1*vx) + (s*Ca2*(vx - vo)), (m2*(vo - vx)))
# node_vo = sym.Eq((P2*vo) + (s*Cb3*(vo - vi)) + (m2*(vo - vx)) + (m3*vi), 0)

print('node_vx_cap', latex(node_vx))
print('node_vo_cap', latex(node_vo))

solve_x_1 = sym.solve(node_vx, vx)
solve_x_2 = sym.solve(node_vo, vx)

eq_match = sym.Eq(solve_x_1[0] - solve_x_2[0],0)
eq = sym.solve(eq_match, vo)
eq = sym.Eq(eq[0], 0)
eq = eq.subs(vi, 1)

eq = eq.args[0]
eq = eq.subs(m2, gmp2).subs(m3, gmn3).subs(d1, gdsp1).subs(d2, gdsp2).subs(d3, gdsn3).subs(Cb1, Cgdp1).subs(Cb3, Cgdn3).subs(Ca2, Cgsp2).subs(CL, CL_v).subs(s, s_v)
print('Test 2', latex(eq))

print()
#factor P1 y P2
# eq = sym.factor(eq)

# eq = sym.factor(eq, s)
eq_o = sym.factor(eq, P1)
# eq = sym.factor(eq, P2)
# eq = sym.factor(eq, P1*P2)


print('eq 1:', latex(node_vx))
print('eq 2:', latex(node_vo))
print('Solve x in 1:', solve_x_1[0])
print('Solve x in 2:', solve_x_2[0])
print('Match:', eq_match)
print('Final:', latex(eq))

#Simplify eq after all

num = (P1*((s*Cb3) - m3) + (s*Cb3*m2)-(m3*m2))
den = (P1*P2) + (P1*((s*Cb3)+m2)) + (P2*((s*Ca2)+m2)) + (s*Cb3*m2)
eq = sym.Eq(num/den, 0)
# eq = sym.simplify(eq)
print('Final 3:', latex(eq))

eq_c = eq.args[0]
eq_c = eq_c.subs(m2, gmp2).subs(m3, gmn3).subs(d1, gdsp1).subs(d2, gdsp2).subs(d3, gdsn3).subs(Cb1, Cgdp1).subs(Cb3, Cgdn3).subs(Ca2, Cgsp2).subs(CL, CL_v).subs(s, s_v)
print('Test 3', abs(eq_c))



#Agrupation s
eq = sym.factor(eq, s)
print('s agrupation:', latex(eq))

#Eliminacion de las u
Cb1 = sym.Symbol('C_gdp1')
Cb3 = sym.Symbol('C_gdn3')
Ca2 = sym.Symbol('C_gsp2')
CL = sym.Symbol('C_L')

num = ((s*Cb3) - m3)*((s*Cb1) + m2)
U_0 = m2*(d3 + d1)
U_1 = s*((m2*(Cb3 + Cb1)) + (CL*m2))
U_2 = (s**2)*(CL*(Cb1+Ca2))+(Cb3*Cb1)

eq = num/(U_0 + U_1 + U_2)
# num = sym.Eq(num, 0)
# eq_temp = sym.expand(num.args[0])
# print('Temporal', latex(eq_temp))

eq = sym.Eq(eq, 0)
print('Final Final', latex(eq))





#test
# Cb1 = sym.Symbol('C_gdp1')
# Cb3 = sym.Symbol('C_gdn3')
# Ca2 = sym.Symbol('C_gsp2')
# CL = sym.Symbol('C_L')

f_top = int(1*(10**9))
step = int(0.01*(10**9))
eq = eq.args[0]
eq = eq.subs(m2, gmp2).subs(m3, gmn3).subs(d1, gdsp1).subs(d2, gdsp2).subs(d3, gdsn3).subs(Cb1, Cgdp1).subs(Cb3, Cgdn3).subs(Ca2, Cgsp2).subs(CL, CL_v)
print('Check:', abs(eq.subs(s, s_v)))

x_list = []
y_list = []
fre = 1
for i in range(9):
    fre = fre * 10
    w = 2 * 3.1416 * fre
    s_v = complex(0, w)
    eq_t = eq.subs(s, s_v)
    eq_t = abs(eq_t)
    x_list.append(fre)
    y_list.append(eq_t)


# axes = plt.gca()
# axes.set_ylim([16, 0])
plt.ylim(0, 16)
plt.plot(x_list, y_list)
plt.xscale('log')
# plt.semilogx(x_list, y_list)
plt.show()


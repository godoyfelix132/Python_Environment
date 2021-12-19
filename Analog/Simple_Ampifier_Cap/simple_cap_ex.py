import sympy as sym
from sympy import latex

m = 10**-3
u = 10**-6
gmp1 = 2.5372*m # m1
gmp2 = gmp1 # m2
gmn3 = 524.0185*u # m3
gdsp1 = 25.2992*u # d1
gdsp2 = gdsp1 # d2
gdsn3 = 9.219*u # d3

Cgdp1 = 8*(10**-14) # Cb1
Cgdn3 = 7*(10**-13) # Cb3
Cgsp2 = 1.5*(10**-15) # Ca2
CL_v = 1*(10**-12) # CL
# f = 1*(10**3)
f = 1
w = 2*3.1416*f
s_v = complex(0, w)

vx = sym.Symbol('V_x')
vi = sym.Symbol('V_in')
vo = sym.Symbol('V_out')

def get_parallel(r1, r2):
    rp = 1/((1/r1)+(1/r2))
    return rp

def check_1(d1, d2, d3, m2, m3, s, Cb1, Ca2, Cb3, CL):
    # r = -m3*(d1 + d2 + m2)/(d1*d2 + d1*d3 + d1*m2 + d2*d3 + d3*m2)
    r1 = 1 / d1
    r2 = 1 / (s * Cb1)
    P1 = get_parallel(r1, r2)
    r1 = 1 / d3
    r2 = 1 / (s * CL)
    P2 = get_parallel(r1, r2)

    x = (s*(Cb1/d1))
    x2 = (1/(1 + x))
    x3 = (1/d1)
    P1 = x3 * x2

    y = (s*(CL /d3))
    y2 = (1/(1 + y))
    P2 = (1/d3)*y2
    node_vx = sym.Eq((s * Ca2 * (-vo + vx)) + (vx * P1) + (d2 * (vx - vo)), m2 * (vo - vx))
    # node_vx = sym.Eq(                         (vx * d1) + (d2 * (vx - vo)), m2 * (vo - vx))

    # node_vx = sym.Eq((s * Ca2 * (-vo + vx)) + (vx * 1 ) + (d2 * (vx - vo)), m2 * (vo - vx))
    # node_vx = sym.Eq(                           (vx * 1 ) + (d2 * (vx - vo)), m2 * (vo - vx))




    node_vo = sym.Eq((s * Cb3 * (-vi + vo)) + (P2 * vo) + (m3 * vi) + (d2 * (vo - vx)) + (m2 * (vo - vx)), 0)
    # node_vo = sym.Eq(                         (d3 * vo) + (m3 * vi) + (d2 * (vo - vx)) + (m2 * (vo - vx)), 0)

    # node_vo = sym.Eq((s * Cb3 * (-vi + vo)) + (1  * vo) + (m3 * vi) + (d2 * (vo - vx)) + (m2 * (vo - vx)), 0)
    # node_vo = sym.Eq(                           (1  * vo) + (m3 * vi) + (d2 * (vo - vx)) + (m2 * (vo - vx)), 0)

    return node_vx, node_vo


v1, v2 = check_1(gdsp1, gdsp2, gdsn3, gmp2, gmn3, s_v, Cgdp1, Cgsp2, Cgdn3, CL_v)
v1 = sym.solve(v1, vx)
v2 = sym.solve(v2, vx)
eq_match = sym.Eq(v2[0] - v1[0], 0)
eq = sym.solve(eq_match, vo)
print(v1)
print(v2)
print(eq)
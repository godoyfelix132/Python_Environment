import sympy as sym
from sympy import latex

gp = 0.0025372
gn = 0.0005240177
cn = 7e-13
cp = 80.2388e-15

s = sym.Symbol('s')
CL = sym.Symbol('C_L')
C1 = sym.Symbol('C_gdp1')
C3 = sym.Symbol('C_gdn3')
C2 = sym.Symbol('C_gsp2')
gd1 = sym.Symbol('g_dsp1')
gd3 = sym.Symbol('g_dsn3')
gm2 = sym.Symbol('g_mp2')
gm3 = sym.Symbol('g_mn3')
V2 = sym.Symbol('V_2')
I2 = sym.Symbol('I_2')
Vx = sym.Symbol('V_x')
Vo = sym.Symbol('V_o')
Vi = sym.Symbol('V_i')

eq_vx = sym.Eq((s*C2*(-Vo+Vx))+(((s*C1)+gd1)*Vx), gm2*(Vo-Vx))
EVx = sym.solve(eq_vx, Vx)
print(latex(EVx))
EVx = sym.Eq((Vo*((s*C2)+gm2))/(C1+gm2),0)
print(latex(EVx))

EI0 = sym.Eq(-(gm2*Vo)+(Vi*((s*C3) - gm3)), 0)
print(latex(EI0))

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

#eq2 = eq2.subs(C1, Cgdp1).subs(C2, Cgsp2).subs(gm2, gmp2).subs(CL, CL_v).subs(gd3, gdsn3)

import sympy as sym
from sympy import latex

gp = 0.0025372
gn = 0.0005240177
cn = 7e-13
cp = 80.2388e-15

s = sym.Symbol('s')
CL = sym.Symbol('CL')
C1 = sym.Symbol('Cgdp1')
C2 = sym.Symbol('Cgsp2')
gd1 = sym.Symbol('gdsp1')
gd3 = sym.Symbol('gdsn3')
gm2 = sym.Symbol('gmp2')
gm3 = sym.Symbol('gmn3')
V2 = sym.Symbol('V2')
I2 = sym.Symbol('I2')
Vx = sym.Symbol('Vx')


eq_vx = sym.Eq((s*C2*(-V2+Vx))+(((s*C1)+gd1)*Vx), gm2*(V2-Vx))
print(latex(eq_vx))
a = sym.solve(eq_vx, Vx)
print(latex(a))
eq1 = sym.Eq(I2, (V2*((s*CL)+gd3)) + (s*C2*(V2-Vx)) + (gm2*(V2-Vx)))
lat = sym.factor(eq1, Vx)
print('ctr', latex(lat))
eq1 = eq1.subs(Vx, a[0])
lat = sym.factor(eq1, V2)
print('ctr2', latex(lat))
eq1 = sym.solve(eq1, V2)
eq1 = sym.Eq(eq1[0], 0)
eq1 = eq1.subs(I2,1)
lat = sym.factor(eq1, s)
print(latex(eq1.simplify()))
print('ctr3', latex(lat))
eq2 = sym.Eq((s*(C1) + gm2)/(((s**2)*(CL*C1))+(s*gm2*(CL+C1))+(gm2*gd3)),0)

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

eq2 = eq2.subs(C1, Cgdp1).subs(C2, Cgsp2).subs(gm2, gmp2).subs(CL, CL_v).subs(gd3, gdsn3)
print(latex(eq2))

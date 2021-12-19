# Calculate symbolic equations of an cascode amplifier
import sympy as sym


gm1 = sym.Symbol('g_mp1')
gd1 = sym.Symbol('g_dsp1')
gm2 = sym.Symbol('g_mp2')
gd2 = sym.Symbol('g_dsp2')
gm3 = sym.Symbol('g_mn3')
gd3 = sym.Symbol('g_dsn3')
vg2 = sym.Symbol('V_gp2')
vg3 = sym.Symbol('V_gn3')
vx = sym.Symbol('V_x')
vin = sym.Symbol('V_in')
vout = sym.Symbol('V_out')

eq_1 = sym.Eq((gm1*vin)+(gd1*vx)+(gd2*(vx-vout)), gm2*(vg2-vx))
eq_2 = sym.Eq((gm2*(vg2-vx))+(gd2*(vout-vx))+(gd3*vout)+(gm3*vg3), 0)

eq_des_1 = sym.solve(eq_1, vx)
eq_des_2 = sym.solve(eq_2, vx)
eq_igu = sym.Eq(eq_des_1[0], eq_des_2[0])

eq_igu_0x = eq_igu.subs(vg2, 0)
eq_igu_1x = eq_igu.subs(vg2, vout)

eq_igu_00 = eq_igu_0x.subs(vg3, 0)
eq_igu_01 = eq_igu_0x.subs(vg3, vout)
eq_igu_10 = eq_igu_1x.subs(vg3, 0)
eq_igu_11 = eq_igu_1x.subs(vg3, vout)

eq_par_00 = sym.solve(eq_igu_00, vout)
eq_par_01 = sym.solve(eq_igu_01, vout)
eq_par_10 = sym.solve(eq_igu_10, vout)
eq_par_11 = sym.solve(eq_igu_11, vout)

print('00 = ', eq_par_00[0])
print('01 = ', eq_par_01[0])
print('10 = ', eq_par_10[0])
print('11 = ', eq_par_11[0])
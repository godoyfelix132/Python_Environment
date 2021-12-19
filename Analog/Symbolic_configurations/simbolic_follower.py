# calculate symbolic equations of source follower
import sympy as sym


gm1 = sym.Symbol('g_mp1')
gd1 = sym.Symbol('g_dsp1')
gm2 = sym.Symbol('g_mp2')
gd2 = sym.Symbol('g_dsp2')
gm3 = sym.Symbol('g_mn3')
gd3 = sym.Symbol('g_dsn3')
vg1 = sym.Symbol('V_gp1')
vg3 = sym.Symbol('V_gn3')
vx = sym.Symbol('V_x')
vin = sym.Symbol('V_in')
vo = sym.Symbol('V_o')

gm1 = sym.Symbol('a')
gd1 = sym.Symbol('b')
gm2 = sym.Symbol('c')
gd2 = sym.Symbol('d')
gm3 = sym.Symbol('e')
gd3 = sym.Symbol('f')



eq_1 = sym.Eq((gm1*vg1)+(gd1*vx)+(gd2*(vx-vo)), gm2*(vin-vx))
eq_2 = sym.Eq((gm2*(vin-vx))+(gd2*(vo-vx))+(gd3*vo)+(gm3*vg3), 0)

#substitucion
eq_1_igu_0x = eq_1.subs(vg1, 0)
eq_1_igu_1x = eq_1.subs(vg1, vx)

eq_2_igu_0x = eq_2.subs(vg1, 0)
eq_2_igu_1x = eq_2.subs(vg1, vx)

eq_1_igu_00 = eq_1_igu_0x.subs(vg3, 0)
eq_1_igu_01 = eq_1_igu_0x.subs(vg3, vo)
eq_1_igu_10 = eq_1_igu_1x.subs(vg3, 0)
eq_1_igu_11 = eq_1_igu_1x.subs(vg3, vo)

eq_2_igu_00 = eq_2_igu_0x.subs(vg3, 0)
eq_2_igu_01 = eq_2_igu_0x.subs(vg3, vo)
eq_2_igu_10 = eq_2_igu_1x.subs(vg3, 0)
eq_2_igu_11 = eq_2_igu_1x.subs(vg3, vo)


#
eq_des_1_00 = sym.solve(eq_1_igu_00, vo)
eq_des_1_01 = sym.solve(eq_1_igu_01, vo)
eq_des_1_10 = sym.solve(eq_1_igu_10, vo)
eq_des_1_11 = sym.solve(eq_1_igu_11, vo)

eq_des_2_00 = sym.solve(eq_2_igu_00, vo)
eq_des_2_01 = sym.solve(eq_2_igu_01, vo)
eq_des_2_10 = sym.solve(eq_2_igu_10, vo)
eq_des_2_11 = sym.solve(eq_2_igu_11, vo)

eq_igu_00 = sym.Eq(eq_des_1_00[0], eq_des_2_00[0])
eq_igu_01 = sym.Eq(eq_des_1_01[0], eq_des_2_01[0])
eq_igu_10 = sym.Eq(eq_des_1_10[0], eq_des_2_10[0])
eq_igu_11 = sym.Eq(eq_des_1_11[0], eq_des_2_11[0])

#final
eq_par_00 = sym.solve(eq_igu_00, vx)
eq_par_01 = sym.solve(eq_igu_01, vx)
eq_par_10 = sym.solve(eq_igu_10, vx)
eq_par_11 = sym.solve(eq_igu_11, vx)

#eq_final_00 = sym.solve(eq_par_00[0], 1/vin)
#eq_final_01 = sym.solve(eq_par_01[0], 1/vin)
#eq_final_10 = sym.solve(eq_par_10[0], 1/vin)
#eq_final_11 = sym.solve(eq_par_11[0], 1/vin)

print('00 = ', eq_par_00[0])
print('01 = ', eq_par_01[0])
print('10 = ', eq_par_10[0])
print('11 = ', eq_par_11[0])
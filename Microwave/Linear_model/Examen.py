from Microwave.Linear_model.src.touchstone import *
from Microwave.Linear_model.src.power import *
from Microwave.Linear_model.src.double_stub import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import cmath


G = 10**9

t_dir = Touchstone('files/LRM_Dir_1.s2p')
t_inv = Touchstone('files/LRM_Inv_1.s2p')
t_pol = Touchstone('files/LRM_Polar_90.s2p')

# Variable to get averages
n = 0
rs_total = 0
rs_max = 0
rs_min = 10000000
rd_total = 0
rd_max = 0
rd_min = 10000000
ld_total = 0
ld_max = 0
ld_min = 10000000

y_rs_list = []
x_rs_list = []
y_l_list = []
x_l_list = []
y_lg_list = []
x_lg_list = []

f_GHz_max = 30
f_GHz_min = 1

for r in t_dir.readings:

    w_Hz = r.w_GHz * G
    f_GHz = r.f_GHz

    re_z11 = r.re_z11
    re_z12 = r.re_z12
    re_z21 = r.re_z21
    re_z22 = r.re_z22
    im_z11 = r.im_z11
    im_z12 = r.im_z12
    im_z21 = r.im_z21
    im_z22 = r.im_z22

    # Getting rs, rd
    rs = re_z12
    rd = re_z22 - rs
    rs_total = rs_total + rs
    rd_total = rd_total + rd
    n = n+1
    if rs > rs_max:
        rs_max = rs
    if rs < rs_min:
        rs_min = rs
    if rd > rd_max:
        rd_max = rd
    if rd < rd_min:
        rd_min = rd

    # List to get (Rg, 1/(R0(C0^2))), (L, -1/C0), (Lg, -1/C0)
    if f_GHz_min < f_GHz < f_GHz_max:
        y = re_z11 - re_z12
        x = 1 / (w_Hz**2)
        y_rs_list.append(y)
        x_rs_list.append(x)

        y = w_Hz*im_z11
        x = w_Hz**2
        y_l_list.append(y)
        x_l_list.append(x)

        y = w_Hz * (im_z11 - im_z12)
        x = w_Hz ** 2
        y_lg_list.append(y)
        x_lg_list.append(x)

Rs = rs_total/n
Rd = rd_total/n

y_rs_list = np.array(y_rs_list)
x_rs_list = np.array(x_rs_list)
y_l_list = np.array(y_l_list)
x_l_list = np.array(x_l_list)
y_lg_list = np.array(y_lg_list)
x_lg_list = np.array(x_lg_list)

# Plot rs
plt.title('Rs - 1 Ghz a 30 Ghz')
plt.plot(x_rs_list, y_rs_list)
plt.xlabel('1/w2')
plt.ylabel('Re(Z11-Z12)')
# plt.show()

# Plot L
plt.title('L - 1 Ghz a 30 Ghz')
plt.plot(x_l_list, y_l_list)
plt.xlabel('w2')
plt.ylabel('wIm(Z11)')
# plt.show()

# Plot Lg
plt.title('LG - 1 Ghz a 30 Ghz')
plt.plot(x_lg_list, y_lg_list)
plt.xlabel('w2')
plt.ylabel('wIm(Z11-z12)')
# plt.show()

# RG
linear_regression = LinearRegression()
linear_regression.fit(x_rs_list.reshape(-1,1), y_rs_list)
m = linear_regression.coef_
b = linear_regression.intercept_
Rg = b
R0_C02 = 1/m

# L
linear_regression = LinearRegression()
linear_regression.fit(x_l_list.reshape(-1,1), y_l_list)
m = linear_regression.coef_
b = linear_regression.intercept_
L = m
C0_1 = -1/b

# Lg
linear_regression = LinearRegression()
linear_regression.fit(x_lg_list.reshape(-1,1), y_lg_list)
m = linear_regression.coef_
b = linear_regression.intercept_
Lg = m
C0_2 = -1/b

# Ls
Ls = L-Lg

#C0
C0 = (C0_1+C0_2) / 2
# R0
R0 = R0_C02/(C0**2)

#Ld
n = 0
for r in t_dir.readings:
    n = n + 1
    ld = (r.im_z22 / (r.w_GHz*G)) - Ls
    ld_total = ld_total + ld
    if ld > ld_max:
        ld_max = ld
    if ld < ld_min:
        ld_min = ld
Ld = ld_total/n


# Getting Cpg, Cpd, and intrinsic

f_GHz_max = 5
f_GHz_min = 1

n = 0
cpg_total = 0
cpg_max = 0
cpg_min = 10000000
cpd_total = 0
cpd_max = 0
cpd_min = 10000000

for r in t_inv.readings:
    w_Hz = r.w_GHz * G
    f_GHz = r.f_GHz

    re_y11 = r.re_y11
    re_y12 = r.re_y12
    re_y21 = r.re_y21
    re_y22 = r.re_y22
    im_y11 = r.im_y11
    im_y12 = r.im_y12
    im_y21 = r.im_y21
    im_y22 = r.im_y22

    # Getting Cpg, Cpd
    if f_GHz_min < f_GHz < f_GHz_max:
        n = n + 1
        cb = -(C0*im_y12)/((w_Hz*C0)+(2*im_y12))
        cpg = (im_y11 / w_Hz) + ((C0 ** 2) / (C0 + (2 * cb))) - C0
        cpd = (im_y22/w_Hz) + ((cb**2)/(C0+(2*cb))) - cb

        cpd_total = cpd_total + cpd
        cpg_total = cpg_total + cpg

        if cpg > cpg_max:
            cpg_max = cpg
        if cpg < cpg_min:
            cpg_min = cpg
        if cpd > cpd_max:
            cpd_max = cpd
        if cpd < cpd_min:
            cpd_min = cpd

Cpg = cpg_total/n
Cpd = cpd_total/n

# De-embeddiing
n = 0
gds_total = 0
gds_max = 0
gds_min = 10000000
cds_total = 0
cds_max = 0
cds_min = 10000000
cgd_total = 0
cgd_max = 0
cgd_min = 10000000
cgs_total = 0
cgs_max = 0
cgs_min = 10000000
ri_total = 0
ri_max = 0
ri_min = 10000000
rgd_total = 0
rgd_max = 0
rgd_min = 10000000
gm_total = 0
gm_max = 0
gm_min = 10000000
t_total = 0
t_max = 0
t_min = 10000000
for r in t_pol.readings:

    w_Hz = r.w_GHz * G
    f_GHz = r.f_GHz

    if 1 < f_GHz < 50:
        z11 = r.z11
        z12 = r.z12
        z21 = r.z21
        z22 = r.z22

        # Step 1
        z11 = z11 - complex(0, w_Hz * Lg)
        z22 = z22 - complex(0, w_Hz * Ld)

        # Step 2
        y11, y12, y21, y22 = Read.z_to_y(z11=z11, z12=z12, z21=z21, z22=z22)
        y11 = y11 - complex(0, w_Hz * Cpg)
        y22 = y22 - complex(0, w_Hz * Cpd)

        # Step 3
        z11, z12, z21, z22 = Read.y_to_z(y11=y11, y12=y12, y21=y21, y22=y22)
        z11 = z11 - complex(Rg + Rs, w_Hz * Ls)
        z12 = z12 - complex(Rs, w_Hz*Ls)
        z21 = z21 - complex(Rs, w_Hz*Ls)
        z22 = z22 - complex(Rd + Rs, w_Hz*Ls)

        # Step 4
        y11, y12, y21, y22 = Read.z_to_y(z11=z11, z12=z12, z21=z21, z22=z22)

        re_y11 = y11.real
        re_y12 = y12.real
        re_y21 = y21.real
        re_y22 = y22.real
        im_y11 = y11.imag
        im_y12 = y12.imag
        im_y21 = y21.imag
        im_y22 = y22.imag

        gds = re_y22 + re_y12
        # print(f_GHz, gds)
        cds = (im_y22 + im_y12) / w_Hz
        # print(f_GHz,cds)
        cgd = - (im_y12 / w_Hz) * (1 + ((re_y12 / im_y12) ** 2))
        # print(f_GHz,cgd)
        cgs = (((im_y11 + im_y12)**2)+((re_y11 + re_y12)**2))/(w_Hz*(im_y11 + im_y12))
        # print(f_GHz, cgs)
        ri = (re_y11 + re_y12) / (((im_y11 + im_y12) ** 2) + ((re_y11 + re_y12) ** 2))
        # print(f_GHz, ri)
        rgd = re_y12 / (-(im_y12**2)*(1 + ((re_y12/im_y12)**2)))
        # print(f_GHz, rgd)
        gm = math.sqrt((((re_y21 - re_y12) ** 2) + ((im_y21 - im_y12) ** 2)) * (1 + ((w_Hz * ri * cgs) ** 2)))
        # gm = math.sqrt((((re_y21 - re_y12) ** 2) + ((im_y21 - im_y12) ** 2)) * (1 + ((w_Hz**2) * (ri**2) * (cgs**2))))
        # print(f_GHz, gm)
        sum = y21 - y12
        x = sum.real
        y = sum.imag
        # t = -(1 / w_Hz) * math.degrees(math.atan((y + (x * w_Hz * ri * cgs)) / (x - (y * w_Hz * ri * cgs))))
        t = -(1 / w_Hz) * math.atan((y + (x * w_Hz * ri * cgs)) / (x - (y * w_Hz * ri * cgs)))
        # print(t)
        gds_total = gds_total + gds
        cds_total = cds_total + cds
        cgd_total = cgd_total + cgd
        cgs_total = cgs_total + cgs
        ri_total = ri_total + ri
        rgd_total = rgd_total + rgd
        gm_total = gm_total + gm
        t_total = t_total + t
        n = n + 1

        if gds > gds_max:
            gds_max = gds
        if gds < gds_min:
            gds_min = gds
        if cds > cds_max:
            cds_max = cds
        if cds < cds_min:
            cds_min = cds
        if cgd > cgd_max:
            cgd_max = cgd
        if cgd < cgd_min:
            cgd_min = cgd
        if cgs > cgs_max:
            cgs_max = cgs
        if cgs < cgs_min:
            cgs_min = cgs
        if ri > ri_max:
            ri_max = ri
        if ri < ri_min:
            ri_min = ri
        if rgd > rgd_max:
            rgd_max = rgd
        if rgd < rgd_min:
            rgd_min = rgd
        if gm > gm_max:
            gm_max = gm
        if gm < gm_min:
            gm_min = gm
        if t > t_max:
            t_max = t
        if t < t_min:
            t_min = t

Gds = gds_total/n
Rds = 1/Gds
Cds = cds_total/n
Cgd = cgd_total/n
Cgs = cgs_total/n
Ri = ri_total/n
Rgd = rgd_total/n
Gm = gm_total/n
T = t_total/n


print()
print(rs_min, '< Rs <', rs_max)
print(rd_min, '< Rd <', rd_max)
print(ld_min, '< ld <', ld_max)
print(cpg_min, '< Cpg <', cpg_max)
print(cpd_min, '< Cpd <', cpd_max)
print(gds_min, '< Gds <', gds_max)
print(cds_min, '< Cds <', cds_max)
print(cgd_min, '< Cgd <', cgd_max)
print(cgs_min, '< Cgs <', cgs_max)
print(ri_min, '< Ri <', ri_max)
print(rgd_min, '< Rgd <', rgd_max)
print(gm_min, '< Gm <', gm_max)
print(t_min, '< T <', t_max)

print()
print('Rs =', Rs)
print('Rd =', Rd)
print('Rg =', Rg)
print('Ls =', Ls)
print('Lg =', Lg)
print('Ld =', Ld)

print()
print('C0= ', C0)
print('R0 = ', R0)

print()
print('Cpg =', Cpg)
print('Cpd =', Cpd)

print()
print('Gds = ', Gds)
print('Rds = ', Rds)
print('Cds =', Cds)
print('Cgd =', Cgd)
print('Cgs =', Cgs)
print('Ri =', Ri)
print('Rgd =', Rgd)
print('Gm =', Gm)
print('T =', T)

# Getting S parameters of my model
# r = np.linspace(5, 10, 100)

# Ri = 2
# Cgs = 1e-12
# Cgd = 0.1e-12
# Rgd = 13
# T = 2e-12
# Gm = 0.1
# Gds = 0.005
# Cds = 0.02e-12

parameter_list = []

for f_GHz in np.linspace(0.045, 50, 401):
    f_GHz_select = f_GHz
    # print(f_GHz_select)
    f_Hz_select = f_GHz_select * G
    w_Hz_select = 2 * math.pi * f_Hz_select
    w = w_Hz_select
    den_1 = 1 + ((w*Ri*Cgs)**2)
    den_2 = 1 + ((w*Rgd*Cgd)**2)
    y11_int_real = (w**2) * ( ((Ri*(Cgs**2)) / den_1) + ((Rgd*(Cgd**2))/den_2) )
    y11_int_imag = w * ((Cgs/den_1) + (Cgd/den_2))

    y12_int_real = -(((w**2) * Rgd * (Cgd**2)) / den_2)
    y12_int_imag = -w*(Cgd/den_2)

    # y21_int_term1 = ( Gm * cmath.exp(complex(0, -w*T)) ) / complex(1, ((w*Ri*Cgs)**2))
    # y21_int_term2 = - ((w**2)*(Cgd**2)*Rgd) / den_2
    # y21_int_term3 = -complex(0, w * ((Cgd/den_2) + ((Gm * cmath.exp(complex(0, w*T))*Ri*Cgs)/(complex(1, (w*Ri*Cgs)**2)))))
    y21_int_term1 = (Gm*cmath.exp(complex(0, -w*T)))/complex(1, w*Ri*Cgs)
    y21_int_term2 = complex(0, -((w*Cgd)/(complex(1, w*Rgd*Cgd))))

    y22_int_real = Gds + (((w**2)*(Cgd**2)*Rgd)/den_2)

    y22_int_imag = w * (Cds + (Cgd/den_2))

    y11 = complex(y11_int_real, y11_int_imag)
    y12 = complex(y12_int_real, y12_int_imag)
    # y21 = y21_int_term1 + y21_int_term2 + y21_int_term3
    y21 = y21_int_term1 + y21_int_term2
    y22 = complex(y22_int_real, y22_int_imag)


    # x = 72
    # f_med = t_pol.readings[x].f_GHz
    # print(f_med)
    # print(y11)
    # print(y12)
    # print(y21)
    # print(y22)

    # Embeddiing
    z11, z12, z21, z22 = Read.y_to_z(y11=y11, y12=y12, y21=y21, y22=y22)
    z11 = z11 + complex(Rg + Rs, w*Ls)
    z12 = z12 + complex(Rs, w*Ls)
    z21 = z21 + complex(Rs, w*Ls)
    z22 = z22 + complex(Rd + Rs, w*Ls)


    y11, y12, y21, y22 = Read.z_to_y(z11=z11, z12=z12, z21=z21, z22=z22)
    y11 = y11 + complex(0, w * Cpg)
    y22 = y22 + complex(0, w * Cpd)

    z11, z12, z21, z22 = Read.y_to_z(y11=y11, y12=y12, y21=y21, y22=y22)
    z11 = z11 + complex(0, w * Lg)
    z22 = z22 + complex(0, w * Ld)

    s11, s12, s21, s22 = Read.z_to_s(z11=z11, z12=z12, z21=z21, z22=z22, z0=50)
    parameter_list.append([f_GHz_select,s11, s12, s21, s22])

Touchstone.write_touchstone(parameters_list=parameter_list,touchstone_name='My_model.s2p')

# Selecting frequency 5GHz to 10GHz
for i in parameter_list:
    if i[0] > 9:
        frequency = i[0]
        s11 = i[1]
        s12 = i[2]
        s21 = i[3]
        s22 = i[4]
        s11_polar = Read.rect_to_polar_significant(s11)
        s12_polar = Read.rect_to_polar_significant(s12)
        s21_polar = Read.rect_to_polar_significant(s21)
        s22_polar = Read.rect_to_polar_significant(s22)
        break

print()
print('Frequency', frequency)
print()
print('S11 = ', s11)
print('S12 = ', s12)
print('S21 = ', s21)
print('S22 = ', s22)
print()
print('S11 Polar = ', s11_polar)
print('S12 Polar= ', s12_polar)
print('S21 Polar= ', s21_polar)
print('S22 Polar= ', s22_polar)
print()

# Stable analisis
det = (s11 * s22) - (s12 * s21)
Cs = (s11-(det*s22.conjugate())).conjugate()/((abs(s11)**2)-(abs(det)**2))
Rs = abs((s12*s21)/((abs(s11)**2)-(abs(det)**2)))
Cl = (s22-(det*s11.conjugate())).conjugate()/((abs(s22)**2)-(abs(det)**2))
Rl = abs((s12*s21)/((abs(s22)**2)-(abs(det)**2)))

Cs_polar = Read.rect_to_polar(Cs)
Cl_polar = Read.rect_to_polar(Cl)

print()
print('Cs = ', Cs_polar)
print('Rs = ', Rs)
print('Cl = ', Cl_polar)
print('Rl = ', Rl)

k = Power.get_k(s11=s11,s12=s12,s22=s22,s21=s21)
DELTA = Power.get_delta(s11=s11,s12=s12,s21=s21,s22=s22)

print()
print('Stability')
print()
print('K = ', k)
print('Delta = ', DELTA)

#Adding resistor
Resistor_to_add = 1.75

# z11, z12, z21, z22 = Read.s_to_z(s11=s11,s12=s12,s21=s21,s22=s22,z0=50)
# z11 = z11 + Resistor_to_add
# s11, s12, s21, s22 = Read.z_to_s(z11=z11,z12=z12,z21=z21,z22=z22,z0=50)

print()
print('Frequency', frequency)
print()
print('S11 = ', s11)
print('S12 = ', s12)
print('S21 = ', s21)
print('S22 = ', s22)
print()
print('S11 Polar = ', s11_polar)
print('S12 Polar= ', s12_polar)
print('S21 Polar= ', s21_polar)
print('S22 Polar= ', s22_polar)
print()

####################
# s11 = Read.polar_to_rect(0.641, -171.3)
# s22 = Read.polar_to_rect(0.572, -95.7)
# s21 = Read.polar_to_rect(2.058, 28.5)
# s12 = Read.polar_to_rect(0.057, 16.3)
####################
U_1, U_2 = Power.get_U(s11=s11,s12=s12,s21=s21,s22=s22)
DELTA = Power.get_delta(s11=s11,s12=s12,s21=s21,s22=s22)
k = Power.get_k(s11=s11,s12=s12,s22=s22,s21=s21)
print('K After = ', k)
print('Delta After = ', abs(DELTA))


B1, C1 = Power.get_B1_C1(s11=s11,s22=s22,delta=DELTA)
B2, C2 = Power.get_B2_C2(s11=s11,s22=s22,delta=DELTA)

Gamma_SM_neg, Gamma_SM_pos = Power.get_Gamma_SM(b1=B1,c1=C1)
Gamma_LM_neg, Gamma_LM_pos = Power.get_Gamma_LM(b2=B2,c2=C2)

if abs(Gamma_SM_neg)<1:
    Gamma_SM = Gamma_SM_neg
    Gamma_S_polar = Read.rect_to_polar(Gamma_SM_neg)
else:
    Gamma_S = Gamma_SM_pos
    Gamma_S_polar = Read.rect_to_polar(Gamma_SM_pos)

if abs(Gamma_LM_neg) < 1:
    Gamma_L = Gamma_LM_neg
    Gamma_L_polar = Read.rect_to_polar(Gamma_LM_neg)
else:
    Gamma_L = Gamma_LM_pos
    Gamma_L_polar = Read.rect_to_polar(Gamma_LM_pos)

B1_polar = Read.rect_to_polar(B1)
B2_polar = Read.rect_to_polar(B2)
C1_polar = Read.rect_to_polar(C1)
C2_polar = Read.rect_to_polar(C2)

Gamma_SM_neg_polar = Read.rect_to_polar(Gamma_SM_neg)
Gamma_SM_pos_polar = Read.rect_to_polar(Gamma_SM_pos)
Gamma_LM_neg_polar = Read.rect_to_polar(Gamma_LM_neg)
Gamma_LM_pos_polar = Read.rect_to_polar(Gamma_LM_pos)

# GT_db_1 = Power.get_GT_db_1(s11=s11, s12=s12, s21=s21, s22=s22, gamma_s=Gamma_S, gamma_l=Gamma_L)
# GT_db_2 = Power.get_GT_db_2(s21=s21,s12=s12,k=k)
#
# print(Read.rect_to_polar(Gamma_SM))
# print(Read.rect_to_polar(Gamma_LM))
# Gamma_S = Power.get_Gamma_S(s11=s11, s12=s12, s21=s21, s22=s22, gamma_l=Gamma_LM)
# Gamma_L = Power.get_Gamma_L(s11=s11, s12=s12, s21=s21, s22=s22, gamma_s=Gamma_SM)
# Gamma_S_polar = Read.rect_to_polar(Gamma_S)
# Gamma_L_polar = Read.rect_to_polar(Gamma_L)
# print('s ', Read.rect_to_polar(Gamma_S))
# print(Read.rect_to_polar(Gamma_L))
#
# print(GT_db_1)
# print('Max Gain = ', 10*math.log10(GT_db_1))

print('S11 =', Read.rect_to_polar(s11))
print('S22 =', Read.rect_to_polar(s22))
print('Gamma_S =', Read.rect_to_polar(Gamma_S))
print('Gamma_l =', Read.rect_to_polar(Gamma_L))
print('Max Power Gain = ', 10*math.log10(abs(s21)/abs(s12)))
Gamma_L = Read.polar_to_rect(0.467,105.737)
Gamma_L = Gamma_L
Gamma_S = (s11+((s12*s21*Gamma_L)/(1-(s22*Gamma_L))))
print('Gamma_L',Read.rect_to_polar(Gamma_L))
print('Gamma_S', Read.rect_to_polar(Gamma_S))

# det = (s11*s22) - (s12*s21)
# go = 14 / (abs(s21)**2)
# # centro = (go*((s22-(det*s11.conjugate())).conjugate()))/(1 + (go*((abs(s22))-(abs(det)**2))))
# centro =
# print(Read.rect_to_polar(centro))
# # radio_1 = math.sqrt(    1   -    (k*go*abs(s12*s21))      +       ((go**2)*((s12*s21)**2))      )
# # radio_2 = abs(1 + (go*((abs(s22)**2)-(abs(det)**2))))
# print(radio_1/radio_2)








##################################################################
# k = Power.get_k(s11=s11,s12=s12,s22=s22,s21=s21)
# DELTA = Power.get_delta(s11=s11,s12=s12,s21=s21,s22=s22)
# U_1, U_2 = Power.get_U(s11=s11,s12=s12,s21=s21,s22=s22)
#
# Gmsg = abs(s21)/abs(s12)
# Gmsg = 10*math.log10(Gmsg)
# print(Gmsg)
# Gamma_L = Read.polar_to_rect(0.483, 98.402)
# Gamma_S = Power.get_Gamma_S(s11,s12,s21,s22,Gamma_L)
#
# Gamma_L_polar = Read.rect_to_polar_significant(Gamma_L)
# Gamma_S_polar = Read.rect_to_polar_significant(Gamma_S)
# print(Gamma_S_polar)
# print(Gamma_L_polar)

# Double Stub
Zs_norm = (1 + Gamma_S)/(1 - Gamma_S)
Zl_norm = (1 + Gamma_L)/(1 - Gamma_L)

ZA = Zs_norm
YA = 1/ZA
ZB = Zs_norm.real - 0.6j
YB = 1/ZB
ZC = 1 + 2j
YC = 1 / ZC
ZD = 1
YD = 1
cin_1 = DoubleStub.get_C_serie(z1=ZA,z2=ZB,f=frequency*G,z0=50)
lin_1 = DoubleStub.get_L_shunt(y1=YB,y2=YC,f=frequency*G,z0=50)
cin_2 = DoubleStub.get_C_serie(z1=ZC,z2=ZD,f=frequency*G,z0=50)
print('In')
print('C1 Serie', cin_1)
print('L Shunt', lin_1)
print('C2 Serie', cin_2)



ZA = Zl_norm
YA = 1/ZA
ZB = Zl_norm - -1.46j
YB = 1/ZB
ZC = 1 + 1j
YC = 1 / ZC
ZD = 1
YD = 1
cout_1 = DoubleStub.get_C_serie(z1=ZA,z2=ZB,f=frequency*G,z0=50)
lout_1 = DoubleStub.get_L_shunt(y1=YB,y2=YC,f=frequency*G,z0=50)
cout_2 = DoubleStub.get_C_serie(z1=ZC,z2=ZD,f=frequency*G,z0=50)
print('out')
print('C1 Serie', cout_1)
print('L Shunt', lout_1)
print('C2 Serie', cout_2)
#

# Gamma_S = Read.polar_to_rect(0.762, 177.3)
# Gamma_L = Read.polar_to_rect(0.718, 103.9)

# Stub
Ys_norm = ((1-Gamma_S)/(1 + Gamma_S))/50
Yl_norm = ((1-Gamma_L)/(1 + Gamma_L))/50

Zs_norm = (1 + Gamma_S)/(1 - Gamma_S)
Zl_norm = (1 + Gamma_L)/(1 - Gamma_L)
print(Zs_norm)
print(Zl_norm)

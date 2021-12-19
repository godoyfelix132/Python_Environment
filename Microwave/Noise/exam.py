from Microwave.Noise.src.function import *


def get_parameters(n):
    n = str(n)
    if n == '1':
        # Design 1
        s_11 = Function.rect(0.6, 146)
        s_12 = Function.rect(0.085, 62)
        s_21 = Function.rect(1.97, 32)
        s_22 = Function.rect(0.52, -63)
        f_min = 3
        G_opt = Function.rect(0.45, -150)
        Rn = 0.2

    if n == '3':
        # Design 3
        s_11 = Function.rect(0.55, 144)
        s_12 = Function.rect(0.135, -30)
        s_21 = Function.rect(3.1, -4)
        s_22 = Function.rect(0.33, -110)
        f_min = 1.2
        G_opt = Function.rect(0.41, -150)
        Rn = 0.22

    if n == 'e1':
        # Exam 1
        s_11 = Function.rect(0.59, -175)
        s_12 = Function.rect(0.045, 45)
        s_21 = Function.rect(3.8, 62)
        s_22 = Function.rect(0.51, -38)
        f_min = 1.6
        G_opt = Function.rect(0.2, 155)
        Rn = 0.15

    if n == 'e2':
        # Exam 2
        s_11 = Function.rect(0.6, -170)
        s_12 = Function.rect(0.05, 16)
        s_21 = Function.rect(2, 30)
        s_22 = Function.rect(0.5, -95)
        f_min = 2.5
        G_opt = Function.rect(0.5, 145)
        Rn = 5

    if n == 'a':
        # Exam 2
        s_11 = Function.rect(0.7, -105)
        s_12 = Function.rect(0.11, 20)
        s_21 = Function.rect(3, 75)
        s_22 = Function.rect(0.46, -70)
        f_min = 0.8
        G_opt = Function.rect(0.7, 55)
        Rn = 0.95

    return s_11, s_12, s_21, s_22, f_min, G_opt, Rn


s_11, s_12, s_21, s_22, f_min, G_opt, Rn = get_parameters('e1')

k = Function.get_k(s11=s_11, s12=s_12, s22=s_22, s21=s_21)
DELTA = Function.get_delta(s11=s_11, s12=s_12, s21=s_21, s22=s_22)

B1, C1 = Function.get_B1_C1(s11=s_11, s22=s_22, delta=DELTA)
B2, C2 = Function.get_B2_C2(s11=s_11, s22=s_22, delta=DELTA)

Gamma_SM_neg, Gamma_SM_pos = Function.get_Gamma_SM(b1=B1, c1=C1)
if abs(Gamma_SM_neg)<1:
    Gamma_S = Gamma_SM_neg
else:
    Gamma_S = Gamma_SM_pos

Gamma_LM_neg, Gamma_LM_pos = Function.get_Gamma_LM(b2=B2, c2=C2)
if abs(Gamma_LM_neg) < 1:
    Gamma_L = Gamma_LM_neg
else:
    Gamma_L = Gamma_LM_pos

Gamma_in = Gamma_S.conjugate()

Gamma_a = Function.get_Gamma_a(Gamma_in, Gamma_S)

VSWR = Function.get_VSWR(Gamma_a)

GT_db = Function.get_GT_db(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S, gamma_l=Gamma_L)

F = Function.get_F(Function.mag(f_min), Rn, Gamma_S, G_opt)

print('K:', k)
print('Delta:', abs(DELTA))

print('-----5-----')
print('Gamma_opt', Function.polar(G_opt))
print('Gamma_S:', Function.polar(Gamma_S))
print('Gamma_L:', Function.polar(Gamma_L))
print('Gamma_in', Function.polar(Gamma_in))
print('Gamma a:', abs(Gamma_a))

print('VSWR', VSWR)
print('GA:', GT_db)

print('F', Function.db(F))

print()
print('-----0-----')
Gamma_S0 = G_opt
print('Gamma_s', Function.polar(Gamma_S0))
Gamma_L = Function.get_Gamma_l_Av(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S0)
Gamma_in = Function.get_Gamma_in(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_l=Gamma_L)
Gamma_a = Function.get_Gamma_a(Gamma_in, Gamma_S0)
VSWR = Function.get_VSWR(Gamma_a)
GA = Function.get_GT_db(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S0, gamma_l=Gamma_L)
F = Function.get_F(Function.mag(f_min), Rn, Gamma_S0, G_opt)
print('Gamma_L:', Function.polar(Gamma_L))
print('Gamma_in:', Function.polar(Gamma_in))
print('Gamma a:', Gamma_a)
print('VSWR:', VSWR)
print('GA', GA)
print('F:', Function.db(F))

print()
print('-----1-----')
Gamma_S1 = Function.rect(0.34, 170)
print('Gamma_s', Function.polar(Gamma_S1))
Gamma_L = Function.get_Gamma_l_Av(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S1)
Gamma_in = Function.get_Gamma_in(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_l=Gamma_L)
Gamma_a = Function.get_Gamma_a(Gamma_in, Gamma_S1)
VSWR = Function.get_VSWR(Gamma_a)
GA = Function.get_GT_db(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S1, gamma_l=Gamma_L)
F = Function.get_F(Function.mag(f_min), Rn, Gamma_S1, G_opt)
print('Gamma_L:', Function.polar(Gamma_L))
print('Gamma_in:', Function.polar(Gamma_in))
print('Gamma a:', Gamma_a)
print('VSWR:', VSWR)
print('GA', GA)
print('F:', Function.db(F))

print()
print('-----2-----')
Gamma_S2 = Function.rect(0.43, 175)
print('Gamma_s', Function.polar(Gamma_S2))
Gamma_L = Function.get_Gamma_l_Av(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S2)
Gamma_in = Function.get_Gamma_in(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_l=Gamma_L)
Gamma_a = Function.get_Gamma_a(Gamma_in, Gamma_S2)
VSWR = Function.get_VSWR(Gamma_a)
GA = Function.get_GT_db(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S2, gamma_l=Gamma_L)
F = Function.get_F(Function.mag(f_min), Rn, Gamma_S2, G_opt)
print('Gamma_L:', Function.polar(Gamma_L))
print('Gamma_in:', Function.polar(Gamma_in))
print('Gamma a:', Gamma_a)
print('VSWR:', VSWR)
print('GA', GA)
print('F:', Function.db(F))

print()
print('-----3-----')
Gamma_S3 = Function.rect(0.54, 178)
print('Gamma_s', Function.polar(Gamma_S3))
Gamma_L = Function.get_Gamma_l_Av(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S3)
Gamma_in = Function.get_Gamma_in(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_l=Gamma_L)
Gamma_a = Function.get_Gamma_a(Gamma_in, Gamma_S3)
VSWR = Function.get_VSWR(Gamma_a)
GA = Function.get_GT_db(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S3, gamma_l=Gamma_L)
F = Function.get_F(Function.mag(f_min), Rn, Gamma_S3, G_opt)
print('Gamma_L:', Function.polar(Gamma_L))
print('Gamma_in:', Function.polar(Gamma_in))
print('Gamma a:', Gamma_a)
print('VSWR:', VSWR)
print('GA', GA)
print('F:', Function.db(F))

print()
print('-----4-----')
Gamma_S4 = Function.rect(0.66, -179)
print('Gamma_s', Function.polar(Gamma_S4))
Gamma_L = Function.get_Gamma_l_Av(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S4)
Gamma_in = Function.get_Gamma_in(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_l=Gamma_L)
Gamma_a = Function.get_Gamma_a(Gamma_in, Gamma_S4)
VSWR = Function.get_VSWR(Gamma_a)
GA = Function.get_GT_db(s11=s_11, s12=s_12, s21=s_21, s22=s_22, gamma_s=Gamma_S4, gamma_l=Gamma_L)
F = Function.get_F(Function.mag(f_min), Rn, Gamma_S4, G_opt)
print('Gamma_L:', Function.polar(Gamma_L))
print('Gamma_in:', Function.polar(Gamma_in))
print('Gamma a:', Gamma_a)
print('VSWR:', VSWR)
print('GA',GA)
print('F:', Function.db(F))


F1 = Function.mag(1.5)
F2 = Function.mag(3)
GA1 = Function.mag(6)
F = F1 + ((F2-1)/GA1)
print()
print('F1', F1)
print('F2', F2)
print('GA1', GA1)
print('F', F)
print('F_db', Function.db(F))

a = Function.rect(3, 56)
b = Function.polar(a)
print(a, b)

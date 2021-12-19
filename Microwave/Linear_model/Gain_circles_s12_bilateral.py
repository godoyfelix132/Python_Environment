from numpy import *
import math
import cmath

def polar_to_rect(magnitude, angle):
    r = magnitude * exp(1j * deg2rad(angle))
    return r


def rect_to_polar(complex_num):
    r = (abs(complex_num), rad2deg(angle(complex_num)))
    return r


def rect_to_polar_significative(complex_num):
    r = (significative(abs(complex_num)), significative(rad2deg(angle(complex_num))))
    return r


def significative(n):
    r = "{:.3f}".format(n)
    try:
        r = float(r)
    except ValueError:
        try:
            r = complex(r)
        except ValueError:
            print('error')
    return r

def get_U(s11,s12,s21,s22):
    num = abs(s11*s22*s21*s12)
    den = (1-((abs(s11))**2))*(1-((abs(s22))**2))
    u = num/den
    return u


def get_variation_1(u):
    v1 = 1 / ((1 + u) ** 2)
    v1_db = 10*math.log10(v1)
    return v1_db

def get_variation_2(u):
    v2 = 1 / ((1-u) ** 2)
    v2_db = 10 * math.log10(v2)
    return v2_db


def get_delta(s11, s12,s21, s22):
    d = (s11*s22)-(s12*s21)
    return d


def get_B1_C1(s11,s22,delta):
    b = 1 + ((abs(s11))**2) - ((abs(s22))**2) - ((abs(delta))**2)
    c = s11-((delta)*(s22.conjugate()))
    return b,c


def get_B2_C2(s11,s22,delta):
    b = 1 + ((abs(s22))**2) - ((abs(s11))**2) - ((abs(delta))**2)
    c = s22 - ((delta) * (s11.conjugate()))
    return b,c


def get_Gamma_SM(b1, c1):
    num_pos = b1 + (cmath.sqrt(((b1)**2)-(4*(abs(c1)**2))))
    num_neg = b1 - (cmath.sqrt(((b1) ** 2) - (4 * (abs(c1) ** 2))))
    den = 2 * c1
    gsm_pos = num_pos/den
    gsm_neg = num_neg/den
    return gsm_pos,gsm_neg


def get_Gamma_LM(b2, c2):
    num_pos = b2 + (cmath.sqrt(((b2)**2)-(4*(abs(c2)**2))))
    num_neg = b2 - (cmath.sqrt(((b2) ** 2) - (4 * (abs(c2) ** 2))))
    den = 2 * c2
    gsm_pos = num_pos/den
    gsm_neg = num_neg/den
    return gsm_pos,gsm_neg

# def get_Gamma_s():
def get_GT_bilateral_db(s11,s12,s21,s22,gamma_s,gamma_l):
    num = ((abs(s21))**2)*(1-((abs(gamma_s))**2))*(1-((abs(gamma_l))**2))
    den = abs(((1-(gamma_s*s11))*(1-(gamma_l*s22)))-(gamma_s*gamma_l*s12*s21))**2
    gt = num/den
    gt_db = 10*math.log10(gt)
    return gt_db


G = 10**9

f = 6*G

s11 = polar_to_rect(0.641, -171.3)
s22 = polar_to_rect(0.572, -95.7)
s21 = polar_to_rect(2.058, 28.5)
s12 = polar_to_rect(0.057, 16.3)

# s11 = polar_to_rect(0.6, -60)
# s22 = polar_to_rect(0.5, -60)
# s21 = polar_to_rect(1.9, 81)
# s12 = polar_to_rect(0.05, 26)

# Reinhold 507
# s11 = polar_to_rect(0.3, 30)
# s22 = polar_to_rect(0.2, -15)
# s21 = polar_to_rect(2.5, -80)
# s12 = polar_to_rect(0.2, -60)

U = get_U(s11=s11,s12=s12,s21=s21,s22=s22)

variation_1 = get_variation_1(U)
variation_2 = get_variation_2(U)

DELTA = get_delta(s11=s11,s12=s12,s21=s21,s22=s22)
B1, C1 = get_B1_C1(s11=s11,s22=s22,delta=DELTA)
B2, C2 = get_B2_C2(s11=s11,s22=s22,delta=DELTA)

Gamma_SM_neg, Gamma_SM_pos = get_Gamma_SM(b1=B1,c1=C1)
Gamma_LM_neg, Gamma_LM_pos = get_Gamma_LM(b2=B2,c2=C2)

B1_polar = rect_to_polar(B1)
B2_polar = rect_to_polar(B2)
C1_polar = rect_to_polar(C1)
C2_polar = rect_to_polar(C2)

Gamma_SM_neg_polar = rect_to_polar(Gamma_SM_neg)
Gamma_SM_pos_polar = rect_to_polar(Gamma_SM_pos)
Gamma_LM_neg_polar = rect_to_polar(Gamma_LM_neg)
Gamma_LM_pos_polar = rect_to_polar(Gamma_LM_pos)


print('U', U)
print('Variacion 1', variation_1)
print('Variacion 2', variation_2)

print('B1', B1_polar)
print('B2', B2_polar)
print('C1', C1_polar)
print('C2', C2_polar)

print('Gamma SM pos', Gamma_SM_pos_polar)
print('Gamma SM neg', Gamma_SM_neg_polar)
print('Gamma LM pos', Gamma_LM_pos_polar)
print('Gamma LM neg', Gamma_LM_neg_polar)

GT_db = get_GT_bilateral_db(s11=s11,s12=s12,s21=s21,s22=s22,gamma_s=Gamma_SM_pos,gamma_l=Gamma_LM_pos)
print(GT_db)


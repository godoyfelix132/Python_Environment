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
def get_GT_db_1(s11,s12,s21,s22,gamma_s,gamma_l):
    num = ((abs(s21)) ** 2) * (1 - ((abs(gamma_s)) ** 2)) * (1 - ((abs(gamma_l)) ** 2))
    # s21_cuad = abs(s21)**2
    # abs_gs = abs(gamma_s)
    # abs_gl = abs(gamma_l)
    # num = s21_cuad * (1- abs_gs)*(1-abs_gl)
    den = abs(((1-(gamma_s*s11))*(1-(gamma_l*s22)))-(gamma_s*gamma_l*s12*s21))**2
    gt = num/den
    gt_db = 10*math.log10(gt)
    return gt_db


def get_GT_db_2(s21,s12,k):
    gt = (abs(s21)/abs(s12)) * (k-math.sqrt((k**2)-1))
    gt_db = 10*math.log10(gt)
    return gt_db

def get_Gamma_S(s11,s12,s21,s22,gamma_l):
    gs = (s11 + (s12*s21*gamma_l)/(1-(s22*gamma_l))).conjugate()
    return gs


def get_Gamma_L(s11, s12, s21, s22, gamma_s):
    gl = (s22 + (s12 * s21 * gamma_s) / (1 - (s11 * gamma_s))).conjugate()
    return gl

def get_k(s11,s12,s22,s21):
    delta = (s11 * s22) - (s12 * s21)
    num = 1 - (abs(s11)**2) - (abs(s22)**2) + (abs(delta)**2)
    den = 2*abs(s12*s21)
    k = num/den
    return k


G = 10**9
f = 9.0369*G

# Before
# s11 = (-0.6944138414888743-0.28091892663027174j)
# s12 = (0.12733452067207937+0.007483437073170172j)
# s21 = (0.4317500481705971+1.818711377278461j)
# s22 = (0.06347623613836562-0.2630231823352905j)

# After
s11 = (-0.6468826714087947-0.26496588505894525j)
s12 = (0.1236993828713861+0.006677323254050905j)
s21 = (0.4277400071187145+1.7642933197879573j)
s22 = (0.06419834022634156-0.25903569516681635j)

# s11 = polar_to_rect(0.749, -157.975)
# s22 = polar_to_rect(0.128, 3.363)
# s21 = polar_to_rect(1.869, 76.646)
# s12 = polar_to_rect(0.271, -76.646)

# s11 = polar_to_rect(0.894,-60.6)
# s21 = polar_to_rect(3.122,123.6)
# s12 = polar_to_rect(0.02,62.4)
# s22 = polar_to_rect(0.781,-27.6)

# s11 = polar_to_rect(0.641, -171.3)
# s22 = polar_to_rect(0.572, -95.7)
# s21 = polar_to_rect(2.058, 28.5)
# s12 = polar_to_rect(0.057, 16.3)

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

if abs(Gamma_SM_neg )< 1:
    Gamma_SM = Gamma_SM_neg
else:
    Gamma_SM = Gamma_SM_pos

if abs(Gamma_LM_neg) < 1:
    Gamma_LM = Gamma_LM_neg
else:
    Gamma_LM = Gamma_LM_pos

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

GT_db_1 = get_GT_db_1(s11=s11, s12=s12, s21=s21, s22=s22, gamma_s=Gamma_SM, gamma_l=Gamma_LM)
k = get_k(s11=s11,s12=s12,s22=s22,s21=s21)
GT_db_2 = get_GT_db_2(s21=s21,s12=s12,k=k)
# Gamma_S = get_Gamma_S(s11=s11, s12=s12, s21=s21, s22=s22, gamma_l=Gamma_LM)
# Gamma_L = get_Gamma_L(s11=s11, s12=s12, s21=s21, s22=s22, gamma_s=Gamma_SM)
# Gt = abs(s21)**2
# Max_gain = abs(Gamma_S)*abs(Gt)*abs(Gamma_L)
# Max_gain_db = 10*math.log10(Max_gain)
print(GT_db_1)
print(GT_db_2)
# print(rect_to_polar(Gamma_S))
# print(rect_to_polar(Gamma_L))
# print(Max_gain_db)

det = (s11 * s22) - (s12 * s21)
Cs = (s11-(det*s22.conjugate())).conjugate()/((abs(s11)**2)-(abs(det)**2))
Rs = abs((s12*s21)/((abs(s11)**2)-(abs(det)**2)))
Cl = (s22-(det*s11.conjugate())).conjugate()/((abs(s22)**2)-(abs(det)**2))
Rl = abs((s12*s21)/((abs(s22)**2)-(abs(det)**2)))

Cs_polar = rect_to_polar(Cs)
Cl_polar = rect_to_polar(Cl)

print()
print('Cs = ', Cs_polar)
print('Rs = ', Rs)
print('Cl = ', Cl_polar)
print('Rl = ', Rl)

# Pozar 579
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


def gain_center(g, sii):
    sii_conjugate = sii.conjugate()
    num = g*sii_conjugate
    den = 1-(((abs(sii))**2)*(1-g))
    c = num/den
    return c


def gain_radio(g, sii):
    num = math.sqrt(1-g)*(1-((abs(sii))**2))
    den = 1-(((abs(sii))**2)*(1-g))
    c = num/den
    return c


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


def db_to_PP(db):
    n = 10**(db/10)
    return n


def db_to_VI(db):
    n = 10**(db/20)
    return n


def get_gmax_trans_db(s21):
    db = 10*(math.log10((abs(s21))**2))
    r = (abs(s21))**2
    return r, db


def get_gmax_adap_db(sii):
    db = 10*(math.log10(1/(1-(abs(sii))**2)))
    r = 1/(1-(abs(sii))**2)
    return r, db


def get_g(G, Gmax):
    g = G/Gmax
    return g

def get_gamma(Z):
    G = (Z-Z0)/(Z+Z0)
    return G


def Z_to_Y(z):
    y = 1/z
    return y


def Y_to_Z(y):
    z=1/y
    return z


def get_C_serie(z1, z2, f, z0):
    c = 1/(2*cmath.pi*f*(abs(z2-z1))*z0)
    return c


def get_L_serie(z1, z2, f, z0):
    l = (z0*(abs(z2-z1)))/(2*cmath.pi*f)
    return l


def get_C_shunt(y1, y2, f, z0):
    c = 1/((2*cmath.pi*f)*((z0)/(abs(y2-y1))))
    return c


def get_L_shunt(y1, y2, f, z0):
    l = ((z0)/(abs(y2-y1)))/(2*cmath.pi*f)
    return l

G = 10**9
Z0 = 50
f = 4*G

s11 = polar_to_rect(0.75, -120)
s22 = polar_to_rect(0.6, -70)
s21 = polar_to_rect(2.5, 80)

G0_max, G0_max_db = get_gmax_trans_db(s21)
Gs_max, Gs_max_db = get_gmax_adap_db(s11)
Gl_max, Gl_max_db = get_gmax_adap_db(s22)

Gs_db = 2
Gl_db = 1

Gs = db_to_PP(Gs_db)
Gl = db_to_PP(1)

gs = get_g(Gs, Gs_max)
gl = get_g(Gl, Gl_max)

cs = gain_center(gs, s11)
rs = gain_radio(gs, s11)
cl = gain_center(gl, s22)
rl = gain_radio(gs, s11)

cs_polar = rect_to_polar_significative(cs)
rs_polar = rect_to_polar_significative(rs)
cl_polar = rect_to_polar_significative(cl)
rl_polar = rect_to_polar_significative(rl)

Zs_norm = 0.11 + 0.736j
Zl_norm = 0.877 + 0.46j

Zs = Zs_norm * Z0
Zl = Zl_norm * Z0

Gamma_s = significative(get_gamma(Zs))
Gamma_l = significative(get_gamma(Zl))

Gamma_s_polar = rect_to_polar_significative(Gamma_s)
Gamma_l_polar = rect_to_polar_significative(Gamma_l)

print('Gs', Gs_db)
print('gs', significative(gs))
print('Cs', cs_polar)
print('Rs', rs_polar[0])
print('Gamma S', Gamma_s)
print('Gamma S Polar', Gamma_s_polar)
print('Zs Normalizada', Zs_norm)
print('Zs Normalizada Conjugada', Zs_norm.conjugate())
ZA = Zs_norm.conjugate()
ZB = 0.11 - 1.35j
ZC = 1 + 3.8j
ZD = 1

YA = Y_to_Z(ZA)
YB = Y_to_Z(ZB)
YC = Y_to_Z(ZC)
YD = Y_to_Z(ZD)

C1_serie = get_C_serie(ZA,ZB,f,Z0)
L1_shunt = get_L_shunt(YB,YC,f,Z0)
C2_serie = get_C_serie(ZC,ZD,f,Z0)

print('C1 Serie', C1_serie)
print('L1 Shunt', L1_shunt)
print('C2 Serie', C2_serie)

print()
print('Gl', Gl_db)
print('gl', significative(gl))
print('Cl', cl_polar)
print('Rl', rl_polar[0])
print('Gamma L', Gamma_l)
print('Gamma L Polar', Gamma_l_polar)
print('Zl Normalizada', Zl_norm)
print('Zl Normalizada Conjugada', Zl_norm.conjugate())

ZA = Zl_norm.conjugate()
ZB = 0.877 - 0.99j
ZC = 0.99 + 1j
ZD = 1

YA = Y_to_Z(ZA)
YB = Y_to_Z(ZB)
YC = Y_to_Z(ZC)
YD = Y_to_Z(ZD)

C1_serie = get_C_serie(ZA,ZB,f,Z0)
L1_shunt = get_L_shunt(YB,YC,f,Z0)
C2_serie = get_C_serie(ZC,ZD,f,Z0)

print('C1 Serie', C1_serie)
print('L1 Shunt', L1_shunt)
print('C2 Serie', C2_serie)
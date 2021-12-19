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


def Z_to_Gamma(z,z0):
    g = (z-z0)/(z+z0)
    return g

def Gamma_to_Z(gamma, z0):
    z = z0 * ((1+gamma)/(1-gamma))
    return z


def Gamma_to_Z_norm(gamma):
    z = ((1+gamma)/(1-gamma))
    return z

def get_Gamma_in(s11,s12,s22,gamma_l):
    g_in = abs(s11 + ((s12*s21*gamma_l)/(1-(s22*gamma_l))))
    return g_in

def get_delta(s11, s12,s21, s22):
    d = (s11*s22)-(s12*s21)
    return d

def get_k(s11,s12,s22,s21):
    delta = (s11 * s22) - (s12 * s21)
    num = 1 - (abs(s11)**2) - (abs(s22)**2) + (abs(delta)**2)
    den = 2*abs(s12*s21)
    k = num/den
    return k

Z0 = 50

s11 = polar_to_rect(0.894,-60.6)
s21 = polar_to_rect(3.122,123.6)
s12 = polar_to_rect(0.02,62.4)
s22 = polar_to_rect(0.781,-27.6)

# s11 = polar_to_rect(0.65,-95)
# s21 = polar_to_rect(5,115)
# s12 = polar_to_rect(0.035,40)
# s22 = polar_to_rect(0.8,-35)

Gamma_in = get_Gamma_in(s11=s11,s12=s12,s22=s22,gamma_l=0)
k = get_k(s11=s11,s12=s12,s22=s22,s21=s21)
delta_polar = rect_to_polar(get_delta(s11=s11,s12=s12,s22=s22,s21=s21))

print('K', k)
print('delta polar', delta_polar)

# Debido a que zs = 50, absoluto de gamma in = absoluto de s11
# Para evitar inestabilidad gamma in = gamma out = 1

print('|Gamma in|', abs(s11))
print('|Gamma out|', abs(s22))

Zin_norm = Gamma_to_Z_norm(s11)
Zout_norm = Gamma_to_Z_norm(s22)

print('Zin real', Zin_norm.real )
print('Zout real', Zout_norm.real)

# Zin_new = complex(Zin_norm.real + (25.5/50), Zin_norm.imag)
# s11_new = Z_to_Gamma(Zin_new,Z0)
# print(abs(s11))
# print('s11_new', abs(s11_new))
# print(Zin_new.real)


print()
zout_new = complex(Zout_norm.real + (5/50),Zout_norm.imag)
s22_new = Z_to_Gamma(zout_new,Z0)
print(abs(s22))
print(abs(s22_new))

r = polar_to_rect(0.762,177.3)
print('r',r)
r = Gamma_to_Z(r,Z0)
print(1/r)
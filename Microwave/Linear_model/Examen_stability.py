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


G = 10**9
f = 9.0369*G
#
# s11 = (-0.6944138414888743-0.28091892663027174j)
# s12 = (0.12733452067207937+0.007483437073170172j)
# s21 = (0.4317500481705971+1.818711377278461j)
# s22 = (0.06347623613836562-0.2630231823352905j)


# s11 = polar_to_rect(0.894,-60.6)
# s21 = polar_to_rect(3.122,123.6)
# s12 = polar_to_rect(0.02,62.4)
# s22 = polar_to_rect(0.781,-27.6)


Gamma_in = get_Gamma_in(s11=s11,s12=s12,s22=s22,gamma_l=0)
k = get_k(s11=s11,s12=s12,s22=s22,s21=s21)
delta_polar = rect_to_polar(get_delta(s11=s11,s12=s12,s22=s22,s21=s21))

print('K', k)
print('Delta polar', delta_polar)

#El tansistor es condicionalmente estable

#new
print()
s11 = (-0.6468826714087947-0.26496588505894525j)
s12 = (0.1236993828713861+0.006677323254050905j)
s21 = (0.4277400071187145+1.7642933197879573j)
s22 = (0.06419834022634156-0.25903569516681635j)

Gamma_in = get_Gamma_in(s11=s11,s12=s12,s22=s22,gamma_l=0)
k = get_k(s11=s11,s12=s12,s22=s22,s21=s21)
delta_polar = rect_to_polar(get_delta(s11=s11,s12=s12,s22=s22,s21=s21))

print('K', k)
print('Delta polar', delta_polar)
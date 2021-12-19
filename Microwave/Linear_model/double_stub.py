import cmath

G = 10**9
ZA = 0.2-0.2j
ZB = 0.2-0.4j
ZC = 1

YA = 2.5 + 2.5j
YB = 1 + 2j
YC = 1

f = 2*G
z0 = 50

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


r = get_C_serie(ZA,ZB,f,z0)
print(r)
r = get_L_shunt(YB,YC,f,z0)
print(r)
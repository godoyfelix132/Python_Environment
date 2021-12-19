from numpy import *
import math
import cmath

class Parameter:
    @staticmethod
    def s_to_z(s11, s12, s21, s22, z0):
        d = ((1-s11)*(1-s22))-(s12*s21)
        z11 = z0 * ((((1 + s11) * (1 - s22)) + (s12 * s21)) / d)
        z22 = z0 * ((((1 - s11) * (1 + s22)) + (s12 * s21)) / d)
        z12 = z0 * ((2 * s12) / d)
        z21 = z0 * ((2 * s21) / d)
        return z11, z12, z21, z22


    @staticmethod
    def s_to_y(s11, s12, s21, s22, y0):
        d = ((1 + s11) * (1 + s22)) - (s12 * s21)
        y11 = y0 * ((((1 - s11) * (1 + s22)) + (s12 * s21)) / d)
        y22 = y0 * ((((1 + s11) * (1 - s22)) + (s12 * s21)) / d)
        y12 = -y0 * ((2 * s12) / d)
        y21 = -y0 * ((2 * s21) / d)
        return y11, y12, y21, y22

    @staticmethod
    def s_to_abcd(s11, s12, s21, s22, z0, y0):
        a = (((1 + s11) * (1 - s22)) + (s12 * s21)) / (2 * s21)
        b = z0 * ((((1 + s11) * (1 + s22)) - (s12 * s21)) / (2 * s21))
        c = y0 * ((((1 - s11) * (1 - s22)) - (s12 * s21)) / (2 * s21))
        d = (((1 - s11) * (1 + s22)) + (s12 * s21)) / (2 * s21)
        return a,b,c,d

    @staticmethod
    def z_to_s(z11, z12, z21, z22, z0):
        d = ((z11+z0)*(z22+z0))-(z12*z21)
        s11 = (((z11 - z0)*(z22 + z0)) - (z12*z21))/d
        s22 = (((z11 + z0) * (z22 - z0)) - (z12 * z21)) / d
        s12 = (2 * z12 * z0) / d
        s21 = (2 * z21 * z0) / d
        return s11, s12, s21, s22

    @staticmethod
    def y_to_s(y11,y12,y21,y22,y0):
        d = ((y0 + y11)*(y0 + y22)) - (y12*y21)
        s11 = (((y0 - y11)*(y0 + y22)) + (y12*y21))/d
        s22 = (((y0 + y11) * (y0 - y22)) + (y12 * y21)) / d
        s12 = -((2*y12*y0)/d)
        s21 = -((2 * y21 * y0) / d)
        return s11,s12,s21,s22


    @staticmethod
    def abcd_to_s(a,b,c,d,z0):
        d0 = a + (b/z0) + (c*z0) + d
        s11 = (a + (b/z0) - (c*z0) - d)/d0
        s22 = (-a + (b / z0) - (c * z0) + d)/d0
        s12 = ((2*((a*d)-(b*c)))/d0)
        s21 = (2/d0)
        return s11,s12,s21,s22

    @staticmethod
    def z_to_y(z11,z12,z21,z22):
        d = (z11*z22)-(z12*z21)
        y11 = z22/d
        y12 = -(z12/d)
        y21 = -(z21/d)
        y22 = z11/d
        return y11,y12,y21,y22

    @staticmethod
    def z_to_abcd(z11,z12,z21,z22):
        a = z11/z21
        b = (((z11*z22)-(z12*z21))/z21)
        c = 1 / z21
        d = z22/z21
        return a,b,c,d


    @staticmethod
    def y_to_z(y11,y12,y21,y22):
        d = (y11*y22)-(y12*y21)
        z11 = y22/d
        z12 = -y12/d
        z21 = -y21/d
        z22 = y11/d
        return z11,z12,z21,z22

    @staticmethod
    def y_to_abcd(y11,y12,y21,y22):
        a = -(y22/y21)
        b = -(1/y21)
        c = -(((y11*y22)-(y12*y21))/y21)
        d = -y11/y21
        return a,b,c,d


    @staticmethod
    def abcd_to_z(a,b,c,d):
        z11 = a/c
        z12 = ((a*d)-(b*c))/c
        z21 = 1/c
        z22 = d/c
        return z11,z12,z21,z22


    @staticmethod
    def abcd_to_y(a,b,c,d):
        y11 = d/b
        y12 = ((b*c)-(a*d))/b
        y21 = -1/b
        y22 = a/b
        return y11,y12,y21,y22

if __name__ == '__main__':
    def polar_to_rect(magnitude, angle):
        r = magnitude * exp(1j * deg2rad(angle))
        return r

    Z0 = 50
    Y0 = 1/Z0
    s11 = polar_to_rect(0.894, -60.6)
    s21 = polar_to_rect(3.122, 123.6)
    s12 = polar_to_rect(0.02, 62.4)
    s22 = polar_to_rect(0.781, -27.6)

    z11,z12,z21,z22 = Parameter.s_to_z(s11=s11,s12=s12,s22=s22,s21=s21,z0=Z0)

    y11,y12,y21,y22 = Parameter.s_to_y(s11=s11,s12=s12,s22=s22,s21=s21,y0=Y0)

    a,b,c,d = Parameter.s_to_abcd(s11=s11, s12=s12, s22=s22, s21=s21, z0=Z0, y0=Y0)

    s = Parameter.z_to_s(z11,z12,z21,z22,Z0)
    # print(s)
    s = Parameter.y_to_s(y11,y12,y21,y22,Y0)
    # print(s)
    s = Parameter.abcd_to_s(a,b,c,d,Z0)
    # print(s)
    y = Parameter.z_to_y(z11,z12,z21,z22)
    # print(y)
    abcd = Parameter.z_to_abcd(z11,z12,z21,z22)
    # print(abcd)
    z = Parameter.y_to_z(y11,y12,y21,y22)
    # print(z)
    abcd = Parameter.y_to_abcd(y11,y12,y21,y22)
    # print(abcd)
    z = Parameter.abcd_to_z(a,b,c,d)
    # print(z)
    y = Parameter.abcd_to_y(a,b,c,d)
    # print(y)
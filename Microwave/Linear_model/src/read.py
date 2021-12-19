from numpy import *
import math
import cmath

class Read:
    Z0 = 50

    def __init__(self, f, re_s11, im_s11, re_s21, im_s21, re_s12, im_s12, re_s22, im_s22):
        self.f_GHz = float(f)
        self.w_GHz = 2*math.pi*self.f_GHz
        self.re_s11 = float(re_s11)
        self.im_s11 = float(im_s11)
        self.re_s21 = float(re_s21)
        self.im_s21 = float(im_s21)
        self.re_s12 = float(re_s12)
        self.im_s12 = float(im_s12)
        self.re_s22 = float(re_s22)
        self.im_s22 = float(im_s22)
        self.s11 = complex(self.re_s11, self.im_s11)
        self.s21 = complex(self.re_s21, self.im_s21)
        self.s12 = complex(self.re_s12, self.im_s12)
        self.s22 = complex(self.re_s22, self.im_s22)
        self.det_S = (self.s11*self.s22)-(self.s12*self.s21)

        self.z11, self.z12, self.z21, self.z22 = self.s_to_z(self.s11, self.s12, self.s21, self.s22, self.Z0)
        self.re_z11 = self.z11.real
        self.im_z11 = self.z11.imag
        self.re_z12 = self.z12.real
        self.im_z12 = self.z12.imag
        self.re_z21 = self.z21.real
        self.im_z21 = self.z21.imag
        self.re_z22 = self.z22.real
        self.im_z22 = self.z22.imag

        self.y11, self.y12, self.y21, self.y22 = self.z_to_y(self.z11, self.z12, self.z21, self.z22)
        self.re_y11 = self.y11.real
        self.im_y11 = self.y11.imag
        self.re_y12 = self.y12.real
        self.im_y12 = self.y12.imag
        self.re_y21 = self.y21.real
        self.im_y21 = self.y21.imag
        self.re_y22 = self.y22.real
        self.im_y22 = self.y22.imag

    @staticmethod
    def s_to_z(s11, s12, s21, s22, z0):
        d = ((1 - s11) * (1 - s22)) - (s12 * s21)
        z11 = z0 * ((((1 + s11) * (1 - s22)) + (s12 * s21)) / d)
        z22 = z0 * ((((1 - s11) * (1 + s22)) + (s12 * s21)) / d)
        z12 = z0 * ((2 * s12) / d)
        z21 = z0 * ((2 * s21) / d)
        return z11, z12, z21, z22

    @staticmethod
    def z_to_y(z11, z12, z21, z22):
        d = (z11 * z22) - (z12 * z21)
        y11 = z22 / d
        y12 = -(z12 / d)
        y21 = -(z21 / d)
        y22 = z11 / d
        return y11, y12, y21, y22

    @staticmethod
    def y_to_z(y11, y12, y21, y22):
        d = (y11 * y22) - (y12 * y21)
        z11 = y22 / d
        z12 = -y12 / d
        z21 = -y21 / d
        z22 = y11 / d
        return z11, z12, z21, z22

    @staticmethod
    def z_to_s(z11, z12, z21, z22, z0):
        d = ((z11 + z0) * (z22 + z0)) - (z12 * z21)
        s11 = (((z11 - z0) * (z22 + z0)) - (z12 * z21)) / d
        s22 = (((z11 + z0) * (z22 - z0)) - (z12 * z21)) / d
        s12 = (2 * z12 * z0) / d
        s21 = (2 * z21 * z0) / d
        return s11, s12, s21, s22

    @staticmethod
    def polar_to_rect(magnitude, angle):
        r = magnitude * exp(1j * deg2rad(angle))
        return r

    @staticmethod
    def rect_to_polar(complex_num):
        r = (abs(complex_num), rad2deg(angle(complex_num)))
        return r

    @staticmethod
    def rect_to_polar_significant(complex_num):
        r = (Read.significant(abs(complex_num)), Read.significant(rad2deg(angle(complex_num))))
        return r

    @staticmethod
    def significant(n):
        r = "{:.3f}".format(n)
        try:
            r = float(r)
        except ValueError:
            try:
                r = complex(r)
            except ValueError:
                print('error')
        return r

    def print_complex(self):
        print('Frequency:', self.frequency)
        print('S11:', self.s11)
        print('S12:', self.s12)
        print('S21:', self.s21)
        print('S22:', self.s22)

    def print_data(self):
        print('Frequency:', self.frequency)
        print('Real S11:', self.re_s11)
        print('Imag S11:', self.im_s11)
        print('Real S12:', self.re_s12)
        print('Imag S12:', self.im_s12)
        print('Real S21:', self.re_s21)
        print('Imag S21:', self.im_s21)
        print('Real S22:', self.re_s22)
        print('Imag S22:', self.im_s22)

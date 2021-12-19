import math
import cmath

class Power:

    # @staticmethod
    # def polar_to_rect(magnitude, angle):
    #     r = magnitude * exp(1j * deg2rad(angle))
    #     return r
    #
    # @staticmethod
    # def rect_to_polar(complex_num):
    #     r = (abs(complex_num), rad2deg(angle(complex_num)))
    #     return r
    #
    # @staticmethod
    # def rect_to_polar_significative(complex_num):
    #     r = (significative(abs(complex_num)), significative(rad2deg(angle(complex_num))))
    #     return r
    #
    # @staticmethod
    # def significative(n):
    #     r = "{:.3f}".format(n)
    #     try:
    #         r = float(r)
    #     except ValueError:
    #         try:
    #             r = complex(r)
    #         except ValueError:
    #             print('error')
    #     return r
    #
    @staticmethod
    def get_U(s11, s12, s21, s22):
        num = abs(s11 * s22 * s21 * s12)
        den = (1 - ((abs(s11)) ** 2)) * (1 - ((abs(s22)) ** 2))
        u = num / den
        u_1 = 1 / ((1 + u) ** 2)
        u_1_db = 10 * math.log10(u_1)
        u_2 = 1 / ((1 - u) ** 2)
        u_2_db = 10 * math.log10(u_2)
        return u_1_db, u_2_db
    #
    # @staticmethod
    # def get_variation_1(u):
    #     v1 = 1 / ((1 + u) ** 2)
    #     v1_db = 10 * math.log10(v1)
    #     return v1_db
    #
    # @staticmethod
    # def get_variation_2(u):
    #     v2 = 1 / ((1 - u) ** 2)
    #     v2_db = 10 * math.log10(v2)
    #     return v2_db
    #
    @staticmethod
    def get_delta(s11, s12, s21, s22):
        d = (s11 * s22) - (s12 * s21)
        return d
    #
    @staticmethod
    def get_B1_C1(s11, s22, delta):
        b = 1 + ((abs(s11)) ** 2) - ((abs(s22)) ** 2) - ((abs(delta)) ** 2)
        c = s11 - ((delta) * (s22.conjugate()))
        return b, c

    @staticmethod
    def get_B2_C2(s11, s22, delta):
        b = 1 + ((abs(s22)) ** 2) - ((abs(s11)) ** 2) - ((abs(delta)) ** 2)
        c = s22 - ((delta) * (s11.conjugate()))
        return b, c
    #
    @staticmethod
    def get_Gamma_SM(b1, c1):
        num_pos = b1 + (cmath.sqrt(((b1) ** 2) - (4 * (abs(c1) ** 2))))
        num_neg = b1 - (cmath.sqrt(((b1) ** 2) - (4 * (abs(c1) ** 2))))
        den = 2 * c1
        gsm_pos = num_pos / den
        gsm_neg = num_neg / den
        return gsm_pos, gsm_neg
    #
    @staticmethod
    def get_Gamma_LM(b2, c2):
        num_pos = b2 + (cmath.sqrt(((b2) ** 2) - (4 * (abs(c2) ** 2))))
        num_neg = b2 - (cmath.sqrt(((b2) ** 2) - (4 * (abs(c2) ** 2))))
        den = 2 * c2
        gsm_pos = num_pos / den
        gsm_neg = num_neg / den
        return gsm_pos, gsm_neg
    #
    @staticmethod
    def get_GT_db_1(s11, s12, s21, s22, gamma_s, gamma_l):
        num = ((abs(s21)) ** 2) * (1 - ((abs(gamma_s)) ** 2)) * (1 - ((abs(gamma_l)) ** 2))
        # s21_cuad = abs(s21)**2
        # abs_gs = abs(gamma_s)
        # abs_gl = abs(gamma_l)
        # num = s21_cuad * (1- abs_gs)*(1-abs_gl)
        den = abs(((1 - (gamma_s * s11)) * (1 - (gamma_l * s22))) - (gamma_s * gamma_l * s12 * s21)) ** 2
        gt = num / den
        gt_db = 10 * math.log10(gt)
        return gt_db

    @staticmethod
    def get_GT_db_2(s21, s12, k):
        gt = (abs(s21) / abs(s12)) * (k - math.sqrt((k ** 2) - 1))
        gt_db = 10 * math.log10(gt)
        return gt_db
    #
    @staticmethod
    def get_Gamma_S(s11, s12, s21, s22, gamma_l):
        gs = (s11 + ((s12 * s21 * gamma_l) / (1 - (s22 * gamma_l)))).conjugate()
        return gs

    @staticmethod
    def get_Gamma_L(s11, s12, s21, s22, gamma_s):
        gl = (s22 + ((s12 * s21 * gamma_s) / (1 - (s11 * gamma_s)))).conjugate()
        return gl
    #
    @staticmethod
    def get_k(s11, s12, s22, s21):
        delta = (s11 * s22) - (s12 * s21)
        num = 1 - (abs(s11) ** 2) - (abs(s22) ** 2) + (abs(delta) ** 2)
        den = 2 * abs(s12 * s21)
        k = num / den
        return k

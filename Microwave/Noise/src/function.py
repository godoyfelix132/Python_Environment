import cmath
import math


class Function:
    @staticmethod
    def get_k(s11, s12, s22, s21):
        delta = (s11 * s22) - (s12 * s21)
        num = 1 - (abs(s11) ** 2) - (abs(s22) ** 2) + (abs(delta) ** 2)
        den = 2 * abs(s12 * s21)
        k = num / den
        return k

    @staticmethod
    def get_delta(s11, s12, s21, s22):
        d = (s11 * s22) - (s12 * s21)
        return d

    @staticmethod
    def mag(_db):
        _mag = 10 ** (_db / 10)
        return _mag

    @staticmethod
    def db(_mag):
        _db = 10 * math.log10(_mag)
        return _db

    @staticmethod
    def db_20(_mag):
        _db = 20 * math.log10(_mag)
        return _db

    @staticmethod
    def deg(_rad):
        deg = _rad * (180 / math.pi)
        return deg

    @staticmethod
    def rad(_deg):
        _rad = _deg * (math.pi / 180)
        return _rad

    @staticmethod
    def polar(_complex):
        _polar = cmath.polar(_complex)
        _r = _polar[0]
        _phi = Function.deg(_polar[1])
        _polar = (_r, _phi)
        return _polar

    @staticmethod
    def rect(_r, _phi):
        _rect = cmath.rect(_r, Function.rad(_phi))
        return _rect

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

    @staticmethod
    def get_GT_db(s11, s12, s21, s22, gamma_s, gamma_l):
        num = ((abs(s21)) ** 2) * (1 - ((abs(gamma_s)) ** 2)) * (1 - ((abs(gamma_l)) ** 2))
        den = abs(((1 - (gamma_s * s11)) * (1 - (gamma_l * s22))) - (gamma_s * gamma_l * s12 * s21)) ** 2
        gt = num / den
        gt_db = 10 * math.log10(gt)
        return gt_db

    @staticmethod
    def get_VSWR(G):
        vswr = (1+abs(G))/(1-abs(G))
        return vswr

    @staticmethod
    def get_F(f_min, rn, Gamma_S, Gamma_opt):
        f = f_min + ((4*rn*(abs(Gamma_S-Gamma_opt)**2))/((1-(abs(Gamma_S)**2))*(abs(1+Gamma_opt)**2)))
        return f

    @staticmethod
    def get_Gamma_a(Gamma_in, Gamma_s):
        Gamma_a = abs((Gamma_in-Gamma_s.conjugate())/(1-(Gamma_in*Gamma_s)))
        return Gamma_a

    @staticmethod
    def get_Gamma_l_Av(s11, s12, s21, s22, gamma_s):
        G_L = (s22 + ((s12*s21*gamma_s)/(1-(s11*gamma_s)))).conjugate()
        return G_L

    @staticmethod
    def get_Gamma_in(s11, s12, s21, s22, gamma_l):
        G_in = (s11 + ((s12 * s21 * gamma_l) / (1 - (s22 * gamma_l))))
        return G_in
import cmath

class DoubleStub():
    @staticmethod
    def get_C_serie(z1, z2, f, z0):
        c = 1/(2*cmath.pi*f*(abs(z2-z1))*z0)
        return c

    @staticmethod
    def get_L_serie(z1, z2, f, z0):
        l = (z0*(abs(z2-z1)))/(2*cmath.pi*f)
        return l

    @staticmethod
    def get_C_shunt(y1, y2, f, z0):
        c = 1/((2*cmath.pi*f)*((z0)/(abs(y2-y1))))
        return c

    @staticmethod
    def get_L_shunt(y1, y2, f, z0):
        l = ((z0)/(abs(y2-y1)))/(2*cmath.pi*f)
        return l

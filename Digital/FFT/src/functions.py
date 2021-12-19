import math
from cmath import *
import numpy as np
import scipy.special

#rom()
sn = np.array([3, 5, 7, 9, 11, 13])
cn = np.array([2, 4, 6, 8, 10, 12])
cn_fact = scipy.special.factorial(cn)
#cn_fact = [2, 24, 720, 40320, 3628800]
sn_fact = scipy.special.factorial(sn)
#sn_fact = [6, 120, 5004, 362880, 39916800] 14,16 - 13, 15,17


class Function:
    @staticmethod
    def bin_digits(n, bits):
        """
        :param n: Number to convert
        :param bits: Number of bits
        :return:
        """
        s = bin(n & int("1" * bits, 2))[2:]
        return ("{0:0>%s}" % (bits)).format(s)

    @staticmethod
    def cos(x):
        if x > 1:
            x = x/(2*3.1416)
            x = x - int(x)
            x = x*(2*3.1416)
        res = 1
        for i in range(len(cn)):
            if i == 0:
                res = res - ((x ** cn[i]) / cn_fact[i])
            if i == 1:
                res = res + ((x ** cn[i]) / cn_fact[i])
            if i == 2:
                res = res - ((x ** cn[i]) / cn_fact[i])
            if i == 3:
                res = res + ((x ** cn[i]) / cn_fact[i])
            if i == 4:
                res = res - ((x ** cn[i]) / cn_fact[i])
            if i == 5:
                res = res + ((x ** cn[i]) / cn_fact[i])
            if i == 6:
                res = res - ((x ** cn[i]) / cn_fact[i])
        return res

    @staticmethod
    def sin(x):
        if x > (2 * 3.1416):
            x = x / (2 * 3.1416)
            x = x - int(x)
            x = x * (2 * 3.1416)
        res = x
        for i in range(len(sn)):
            if i == 0:
                res = res - ((x ** sn[i]) / sn_fact[i])
            if i == 1:
                res = res + ((x ** sn[i]) / sn_fact[i])
            if i == 2:
                res = res - ((x ** sn[i]) / sn_fact[i])
            if i == 3:
                res = res + ((x ** sn[i]) / sn_fact[i])
            if i == 4:
                res = res - ((x ** sn[i]) / sn_fact[i])
            if i == 5:
                res = res + ((x ** sn[i]) / sn_fact[i])
        return res


if __name__ == '__main__':

    x = 6.0625
    sin = math.sin(x)
    print(sin)
    cos = math.cos(x)
    print(cos)
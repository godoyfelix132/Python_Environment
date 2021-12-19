import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

y = sym.Symbol('y')
x = sym.Symbol('x')


# def get_rect_ind(p1, p2):
#     x1 = p1[0]
#     y1 = p1[1]
#     x2 = p2[0]
#     y2 = p2[1]
#
#     m = (y2-y1)/(x2-x1)
#     b = -(m*x1)+y1
#     return m, b


def get_rect_cap(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    m = (y2-y1)/(x2-x1)
    b = -(m*x1)+y1
    return m, b


p_1 = (6, 9e4)
p_2 = (3e6, 4.5e-1)
# p_3 = (1.5e7, 3.5)


# m2, b2 = get_rect_ind(p_2, p_3)
# l = m2/(2*np.pi)
# print('L', l)

m1, b1 = get_rect_cap(p_1, p_2)
c = 1/(2*np.pi*m1)
print('C', c)


f = np.logspace(0, 7, 1000)
w = 2*np.pi*f

# z_ind = (w*l) + b2
# y_ind = (m2 * f) + b2

# z_cap = 1/(w*c)
y_cap = (m1 * f) + b1

# plt.figure()
# plt.grid(True)
# plt.loglog(f, y_ind)
#
# plt.loglog(f, z_ind, label='Magnitud')


plt.figure()
plt.grid(True)
plt.loglog(f, y_cap)
# plt.loglog(f, z_cap, label='Magnitud')

plt.show()
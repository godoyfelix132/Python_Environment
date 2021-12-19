import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker

y = sym.Symbol('y')
x = sym.Symbol('x')

c_y_points = [9e4, 5e4, 1e4, 5e3, 1e3, 5e2, 6e1, 1.5e1, 8, 3, 2, 1.5, 6.5e-1, 5e-1]
c_x_points = [5, 1e1, 5e1, 1e2, 5e2, 1e3, 1e4, 5e4, 1e5, 5e5, 1e6, 1.5e6, 2.5e6, 3e6]

l_y_points = [5e-1, 5.5e-1, 7e-1, 1, 1.5, 2, 3, 3.5, 4]
l_x_points = [3e6, 3.5e6, 4e6, 5e6, 6e6, 8e6, 1e7, 1.3e7, 1.5e7]


add_c = 0
for i in range(len(c_y_points)):
    f = c_x_points[i]
    z = c_y_points[i]
    c = 1/(2*np.pi*f*z)
    add_c = add_c + c

add_l = 0
for i in range(len(l_y_points)):
    f = l_x_points[i]
    z = l_y_points[i]
    l = z/(2*np.pi*f)
    add_l = add_l + l

C = add_c / len(c_y_points)
print(C)

L = add_l / len(l_y_points)
print(L)

f = np.logspace(0, 8, 1000)
w = 2*np.pi*f

Zc = 1/(w*C)
Zl = w*L
Z = (1+((w**2)*C*L))/(w*C)

fig, ax = plt.subplots()
plt.ylim((1e-1, 1e6))

plt.grid(True)
plt.loglog(c_x_points+l_x_points, c_y_points+l_y_points, 'o', label='points')
plt.loglog(f, Z, label='Z')
plt.loglog(f, Zc, '--', label='1/wC')
plt.loglog(f, Zl, '--', label='wL',)


locmaj = matplotlib.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=100)
ax.xaxis.set_major_locator(locmaj)
locmin = matplotlib.ticker.LogLocator(base=10.0, subs=np.arange(2, 10) * .1, numticks=100)
ax.xaxis.set_minor_locator(locmin)
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
plt.legend()
plt.xlabel('Frecuencia (log Hz)')
plt.ylabel('Impedancia (log Z)')


all_x_points = c_x_points+l_x_points
all_y_points = c_y_points+l_y_points

f_list = []
e_list = []
for i in range(len(all_x_points)):
    f = all_x_points[i]
    w = 2 * np.pi * f
    Z = (1 + ((w ** 2) * C * L)) / (w * C)
    r = all_y_points[i]
    p = Z
    e = abs(r-p)/abs(r)*100
    e_list.append(e)
    f_list.append(f)
    print(r, p, e)

plt.figure()
plt.semilogx(f_list, e_list, label='Error Relativo')
plt.grid(True)
plt.legend()
plt.xlabel('Frecuencia (log Hz)')
plt.ylabel('Er(%)')
plt.show()

print(L*C)

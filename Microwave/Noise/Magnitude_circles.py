import cmath
import math
from Microwave.Noise.src.function import *

S_11 = Function.rect(0.552, 169)
S_12 = Function.rect(0.49, 23)
S_21 = Function.rect(1.681, 26)
S_22 = Function.rect(0.839, -67)

F_min = Function.mag(2.5)
G_opt = Function.rect(0.475, 166)
R_n = 3.5
# F_min = mag(1.2)
# G_opt = rect(0.41, -150)
# R_n = 0.22

Fi = [Function.mag(2.5), Function.mag(2.6), Function.mag(2.7), Function.mag(2.8), Function.mag(2.9), Function.mag(3)]
# Fi = [mag(2.8)]

print('F_min: ', Function.db(F_min))
print('F_i:', 2.5, '-', 3)
print('G_opt:', Function.polar(G_opt))
print('R_n:', R_n)

main_list = []
for F in Fi:
    N = ((F - F_min)/(4*R_n/50))*(abs(1 + G_opt)**2)
    C_F = G_opt/(1 + N)
    sqrt = math.sqrt((N**2) + (N*(1 - (abs(G_opt)**2))))
    r_F = (1/(1 + N)) * sqrt
    print()
    print('F:', Function.db(F))
    print('N', float('{0:.4f}'.format(N)))
    print('C_F', (float('{0:.4f}'.format(Function.polar(C_F)[0])), Function.polar(C_F)[1]))
    print('r_F', (float('{0:.4f}'.format(Function.polar(r_F)[0])), Function.polar(r_F)[1]))
    main_list.append(['viscircles([' + str(C_F.real) + ' ' + str(C_F.imag) + '],' + str(r_F) + ');'])

for c in main_list:
    print(c[0])
import matplotlib.pyplot as plt
import numpy as np
import math
m = 1e-3
u = 1e-6
n = 1e-9
Ib = 500 * m
kn = 1
Ut = 50 * m
Vb = 0.3

V2 = 0.3
V1_range = np.arange(0, 0.6, 0.01)

Vs_1_list = []
for V1 in V1_range:
    Vs_1 = (math.log((math.exp(kn*V1))+(math.exp(kn*V2))))-(kn*Vb)
    Vs_1_list.append(Vs_1)

V2_range = np.arange(0.6, 0, -0.01)
V1 = 0.3

Vs_2_list = []
for V2 in V2_range:
    Vs_2 = (math.log((math.exp(kn * V1)) + (math.exp(kn * V2)))) - (kn * Vb)
    Vs_2_list.append(Vs_2)

plt.grid(True, which="both")
plt.ylabel('I1 I2')
plt.xlabel('V1-V2')
#plt.plot(V1_range-V2_range, Vs_1_list, label='V1 = 0 -> 0.6; V2 = 0.3;')
plt.plot(V1_range-V2_range, Vs_2_list, label='V2 = 0.6 -> 0; V1 = 0.3;')
plt.show()
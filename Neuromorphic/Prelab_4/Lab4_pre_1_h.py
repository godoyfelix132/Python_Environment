import matplotlib.pyplot as plt
import numpy as np
import math
m = 1e-3
u = 1e-6
n = 1e-9
Ib = 500 * m
kn = 20
Ut = 50 * m

V1_range = np.arange(0, 0.3, 0.01)
V2_range = np.arange(0.3, 0, -0.01)
V1_V2_range = V1_range-V2_range

I1_I2_list = []
for V1_V2 in V1_V2_range:
    I1_I2 = Ib*math.tanh((kn)*((V1_V2)/(2)))
    I1_I2_list.append(I1_I2)

plt.grid(True, which="both")
plt.ylabel('I1-I2')
plt.xlabel('V1-V2')
plt.plot(V1_range-V2_range, I1_I2_list, label='I1_I2')
plt.show()
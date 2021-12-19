import matplotlib.pyplot as plt
import numpy as np
import math
m = 1e-3
u = 1e-6
n = 1e-9
Ib = 500 * m
kn = 10
Ut = 500 * m

###################################################         I1 I2
V2 = 0.3
V1_range = np.arange(0, 0.6, 0.01)

I1_list = []
for V1 in V1_range:
    I1 = Ib*((math.exp((kn*V1)/(Ut)))/((math.exp((kn*V1)/(Ut)))+(math.exp((kn*V2)/(Ut)))))
    I1_list.append(I1)

V2_range = np.arange(0.6, 0, -0.01)
V1 = 0.3

I2_list = []
for V2 in V2_range:
    I2 = Ib*((math.exp((kn*V2)/(Ut)))/((math.exp((kn*V1)/(Ut)))+(math.exp((kn*V2)/(Ut)))))
    I2_list.append(I2)

plt.grid(True, which="both")
plt.ylabel('I1 I2')
plt.xlabel('V1-V2')
plt.plot(V1_range-V2_range, I1_list, label='I1')
plt.plot(V1_range-V2_range, I2_list, label='I2')
###################################################         add
V2 = 0.3
V1_range = np.arange(0, 0.6, 0.01)

I1_list = []
for V1 in V1_range:
    I1 = Ib*((math.exp((kn*V1)/(Ut)))/((math.exp((kn*V1)/(Ut)))+(math.exp((kn*V2)/(Ut)))))
    I1_list.append(I1)

V2_range = np.arange(0.6, 0, -0.01)
V1 = 0.3

I2_list = []
for V2 in V2_range:
    I2 = Ib*((math.exp((kn*V2)/(Ut)))/((math.exp((kn*V1)/(Ut)))+(math.exp((kn*V2)/(Ut)))))
    I2_list.append(I2)

add_list = np.array(I1_list) + np.array(I2_list)
plt.plot(V1_range-V2_range, add_list, label='I1 + I2')
###################################################         I1-I2
V1_range = np.arange(0, 0.6, 0.01)
V2_range = np.arange(0.6, 0, -0.01)
V1_V2_range = V1_range-V2_range

I1_I2_list = []
for V1_V2 in V1_V2_range:
    I1_I2 = Ib*math.tanh((kn)*((V1_V2)/(2)))
    I1_I2_list.append(I1_I2)

plt.plot(V1_range-V2_range, I1_I2_list, label='I1-I2')
plt.show()
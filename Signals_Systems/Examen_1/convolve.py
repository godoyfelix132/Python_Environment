import numpy as np
import matplotlib.pyplot as plt

x_min = 0
x_max = 3
x = np.array([1,2,3,4])

y_min = 0
y_max = 3
y = np.array([4,3,2,1])

nx = np.arange(x_min, x_max+1)
ny = np.arange(y_min, y_max+1)

c_min = x_min + y_min
c_max = x_max + y_max + 1
nc = np.arange(c_min, c_max)

conv = np.convolve(x, y)
y_temp = np.flip(y)
corr = np.correlate(x, y)

print(conv)
print("c_min:", c_min, "c_max:",c_max,"\n")

print(corr)
print("c_min:", c_min, "c_max:",c_max)



# plt.stem(nx, x)
# plt.show()
#
# plt.stem(ny, y)
# plt.show()
#
# plt.stem(nc, conv)
# plt.show()
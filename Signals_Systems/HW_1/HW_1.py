import numpy as np
import matplotlib.pyplot as plt

fs = 300 #Hz

# Analog
t = np.linspace(0, 30*(10**-3), 1000)
x_t = 3 * np.sin(100*np.pi*t)

# Digital
n = np.arange(6)
nt = n*(1/fs)
x_n = 3 * np.sin((np.pi*n)/3)

# Plot
plt.plot(t, x_t)
plt.stem(nt, x_n)
plt.xlabel('t(s)')
plt.ylabel('xa(t)')
plt.show()



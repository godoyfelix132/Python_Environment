from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

m = 10**-3
u = 10**-6
gmp1 = 2.5372*m # m1
gmp2 = gmp1 # m2
gmn3 = 524.0185*u # m3
gdsp1 = 25.2992*u # d1
gdsp2 = gdsp1 # d2
gdsn3 = 9.219*u # d3

Cgdp1 = 8*(10**-14) # Cb1
Cgdn3 = 7*(10**-13) # Cb3
Cgsp2 = 1.5*(10**-15) # Ca2
CL = 1*(10**-12) # CL


def eq_1():
    num_s2 = Cgdn3*Cgdp1
    num_s = Cgdn3*gmp2
    num_0 = gmn3*gmp2
    den_s2_1 = CL*(Cgdp1 + Cgsp2)
    den_s2_2 = CL*Cgdp1
    den_s = gmp2*(CL + Cgdn3 + Cgdp1)
    den_0 = gmp2*(gdsn3+gdsp1)

#con tf
num_s2 = Cgdn3*Cgdp1
num_s = Cgdn3*gmp2
num_0 = -gmn3*gmp2
# den_s2_1 = CL*(Cgdp1 + Cgsp2)
den_s2_1 = CL*Cgdp1
# den_s = gmp2*(CL + Cgdn3 + Cgdp1)
den_s = gmp2*(CL + Cgdn3)
den_0 = gmp2*(gdsn3+gdsp1)
# den_0 = gmp2*(gdsp1)

#con IZ
num_s2 = Cgdn3*Cgdp1
num_s = Cgdn3*gmp2
num_0 = -gmn3*gmp2
# den_s2_1 = CL*(Cgdp1 + Cgsp2)
den_s2_1 = CL*Cgdp1
# den_s = gmp2*(CL + Cgdn3 + Cgdp1)
den_s = gmp2*(CL + Cgdp1)
den_0 = gmp2*(gdsn3+gdsp1)
# den_0 = gmp2*(gdsp1)

f = np.logspace(0, 9, 100)
w = 2*np.pi*f
sys = signal.TransferFunction([num_s2, num_s, num_0], [den_s2_1, den_s, den_0])
w, mag, phase = signal.bode(sys, w=w)

# f = np.logspace(0, 8, 1000000)
file = open('mag.txt', 'r')
lines = file.readlines()
file.close()
x_mag = []
y_mag = []
for l in lines:
    l_split = l.split()
    freq_t = float(l_split[0])
    mag_t = float(l_split[1])
    x_mag.append(freq_t)
    y_mag.append(mag_t)

file = open('fase.txt', 'r')
lines = file.readlines()
file.close()
x_fase = []
y_fase = []
for l in lines:
    l_split = l.split()
    freq_t = float(l_split[0])
    fase_t = float(l_split[2])
    x_fase.append(freq_t)
    y_fase.append(fase_t)



#
plt.figure()
plt.xlim((1, 10**9))
plt.title('Bode Diagram TF vs Tanner')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.semilogx(w, mag, label='TF')    # Bode magnitude plot
plt.semilogx(x_mag, y_mag, label='Tanner')
plt.legend()
plt.show()



plt.figure()
plt.xlim((1, 10**9))
plt.title('Bode Diagram TF vs Tanner')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (deg)')
plt.grid(True)
plt.semilogx(w, phase, label='TF')
plt.semilogx(x_fase, y_fase, label='Tanner')
plt.legend()
plt.show()

x_list = []
y_list_mag = []
y_list_pha = []
for i in range(len(f)):
    j, v = min(enumerate(x_mag), key=lambda x: abs(x[1]-f[i]))
    freq = f[i]
    mag_fun = mag[i]
    mag_fun = 10**(mag_fun/20)
    phase_fun = phase[i]
    mag_tan = y_mag[j]
    mag_tan = 10**(mag_tan/20)
    phase_tan = y_fase[j]

    e_rel_mag = (abs(mag_tan-mag_fun)/abs(mag_tan))*100
    e_rel_pha = (abs(phase_tan - phase_fun) / abs(phase_tan))*100

    x_list.append(freq)
    y_list_mag.append(e_rel_mag)
    y_list_pha.append(e_rel_pha)
    print(f[i], v, e_rel_mag, e_rel_pha)

plt.figure()
plt.xlim((1, 10**9))
plt.title('Error Magnitud')
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Error Relativo (%)')
plt.grid(True)
plt.semilogx(x_list, y_list_mag, label='Magnitud')
plt.legend()

plt.figure()
plt.xlim((1, 10**9))
plt.title('Error Fase')
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Error Relativo (%)')
plt.grid(True)
plt.semilogx(x_list, y_list_pha, label='Fase')
plt.legend()
plt.show()
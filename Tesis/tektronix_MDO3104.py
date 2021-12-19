import pyvisa
import numpy as np
from struct import unpack
import matplotlib.pyplot as plt
import time

rm = pyvisa.ResourceManager()
scope = rm.open_resource('TCPIP0::10.0.7.249::inst0::INSTR')

scope.write('DATA:SOU CH2') # Sets the source waveform to be transferred to Channel 1
scope.write('DATA:WIDTH 1') # Sets 1 byte per point (same as WFMOutpre:BYT_Nr).
scope.write('DATA:ENC RPB') # Sets the data format to RPBinary. (This command replaces WFMOutpre:ENCdg, WFMOutpre:BN_Fmt and WFMOutpre:BYT_Or with a single command.)
scope.write('ACQuire:MODe HIRes')# Sets high resolution in acquire waveform

ymult = float(scope.query('WFMOutpre:YMULT?'))# vertical scale multiplying factor
yzero = float(scope.query('WFMOutpre:YZERO?'))# vertical offset of the source waveform
yoff = float(scope.query('WFMOutpre:YOFF?'))# vertical position of the source waveform in digitizing levels.

xincr = float(scope.query('WFMOutpre:XINCR?'))
pts = float(scope.query('WFMOutpre:NR_pt?'))# the horizontal point spacing in units of time (seconds)



scope.write('CURVE?')
data = scope.read_raw()

headerlen = 2 + int(chr(data[1])) # Header leng
header = data[:headerlen] #value of header
data_point = data[headerlen:-1] #delete header
data_point = np.array(unpack('%sB' % len(data_point), data_point)) #array of int values

# Manual Page 127
# Volts = (ADC_wave - yoff) * ymult + yzero
y = yzero + ((data_point - yoff) * ymult)
x = np.arange(0, xincr * len(y), xincr)

file = open('data.txt', )

plt.grid(True, which="both")
plt.plot(x, y)
plt.show()

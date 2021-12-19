import pyvisa
import numpy as np
import time
import matplotlib.pyplot as plt
from datetime import datetime

rm = pyvisa.ResourceManager()

# Connection
src_vgs = rm.open_resource('GPIB0::20::INSTR')
src_vds = rm.open_resource('GPIB0::24::INSTR')

# Set configuration
src_vds.write('smua.reset()')
src_vds.write('smua.source.output = smua.OUTPUT_OFF')
src_vds.write('smua.source.func = smua.OUTPUT_DCVOLTS')

# Setting limits
src_vds.write('smua.source.limitv = 10')
src_vds.write('smua.source.limiti = 100e-3')

#######################################################################
# Setting initial values and turn on
src_vgs.write('VOLT:LEV 0V')
src_vds.write('smua.source.levelv = 0')
src_vgs.write('OUTPUT ON')
src_vds.write('smua.source.output = smua.OUTPUT_ON')

src_vgs.write('VOLT:LEV 0V')
src_vds.write('smua.source.levelv = 0')
time.sleep(0.5)
src_vds.write('print(smua.measure.i(smua.nvbuffer1))')
ids = float(src_vds.read())*1000
print('Vgs 0; Vds 0; Ids', ids)

src_vgs.write('VOLT:LEV 4V')
src_vds.write('smua.source.levelv = 0')
time.sleep(0.5)
src_vds.write('print(smua.measure.i(smua.nvbuffer1))')
ids = float(src_vds.read())*1000
print('Vgs 4; Vds 0; Ids', ids)

src_vgs.write('VOLT:LEV 0V')
src_vds.write('smua.source.levelv = 4')
time.sleep(0.5)
src_vds.write('print(smua.measure.i(smua.nvbuffer1))')
ids = float(src_vds.read())*1000
print('Vgs 0; Vds 4; Ids', ids)

src_vgs.write('VOLT:LEV 2V')
src_vds.write('smua.source.levelv = 4')
time.sleep(0.5)
src_vds.write('print(smua.measure.i(smua.nvbuffer1))')
ids = float(src_vds.read())*1000
print('Vgs 2; Vds 4; Ids', ids)


src_vgs.write('OUTPUT OFF')
src_vds.write('smua.source.output = smua.OUTPUT_OFF')

src_vds.close()
src_vgs.close()
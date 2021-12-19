import pyvisa
import numpy as np
import time
import matplotlib.pyplot as plt
from datetime import datetime

# file
title = 'IV'
now = datetime.now()
name = now.strftime("%d-%m-%Y %H-%M-%S " + 'Ids-Vds' + title + '.txt')
file = open(name, 'w')


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

# Reading
vgs_max = 8
vds_max = 8
vgs_step = 0.5
vds_step = 0.1
vgs_range = np.arange(1, vgs_max + vgs_step, vgs_step)
vds_range = np.arange(0, vds_max + vds_step, vds_step)
ids_list = []

file.write(str('Vgs range: ' + '0,' + str(vgs_max) + ',' + str(vgs_step) + '\n'))
file.write(str('Vds range: ' + '0,' + str(vds_max) + ',' + str(vds_step) + '\n'))

for vgs in vgs_range:
    src_vgs.write('VOLT:LEV ' + str(vgs) + 'V')
    temp_list = []
    time.sleep(0.5)
    file.write(str('\n' + 'Vgs: ' + str(vgs) + '\n'))
    print('Vgs ', vgs)
    for vds in vds_range:
        src_vds.write('smua.source.levelv = ' + str(vds))
        src_vds.write('print(smua.measure.i(smua.nvbuffer1))')
        ids = float(src_vds.read())*1000
        temp_list.append(ids)
        file.write(str(str(ids) + '\n'))
        print('Vds ', vds, ' Ids', ids)
    ids_list.append(temp_list)

file.close()

src_vgs.write('OUTPUT OFF')
src_vds.write('smua.source.output = smua.OUTPUT_OFF')

fig, ax = plt.subplots()
ax.grid(True, which="both")
plt.ylabel('IDS(mA)')
plt.xlabel('VDS(V)')
n = 0
for ids_values in ids_list:
    ids_values = np.array(ids_values)
    ax.plot(vds_range, ids_values, label=str('VGS ' + str(vgs_range[n]) + 'V'))
    n = n+1

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])
plt.show()

################################################################

src_vds.close()
src_vgs.close()
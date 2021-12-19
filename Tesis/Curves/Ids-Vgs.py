import pyvisa
import numpy as np
import time
import matplotlib.pyplot as plt
from datetime import datetime
import csv

# file
title = '100-24'
plt_title = '100/24'
now = datetime.now()
name = now.strftime("%d-%m-%Y %H-%M-%S " + 'Ids-Vgs ' + title)
name_file = str(name + '.txt')
file = open(name_file, 'w')


rm = pyvisa.ResourceManager()

# Connection
src_vgs = rm.open_resource('GPIB1::20::INSTR')
src_vds = rm.open_resource('GPIB1::24::INSTR')

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
vgs_step = 0.1
vds_step = 0.5
vgs_range = np.arange(0, vgs_max + vgs_step, vgs_step)
vds_range = np.arange(1, vds_max + vds_step, vds_step)
ids_list = []

file.write(str('Vgs range: ' + '0,' + str(vgs_max) + ',' + str(vgs_step) + '\n'))
file.write(str('Vds range: ' + '0,' + str(vds_max) + ',' + str(vds_step) + '\n'))

columns = [vgs_range]
for vds in vds_range:
    src_vds.write('smua.source.levelv = ' + str(vds))
    temp_list = []
    time.sleep(3)
    file.write(str('\n' + 'Vgs: ' + str(vds) + '\n'))
    for vgs in vgs_range:
        src_vgs.write('VOLT:LEV ' + str(vgs) + 'V')
        # time.sleep(0.05)
        src_vds.write('print(smua.measure.i(smua.nvbuffer1))')
        ids = float(src_vds.read()) * 1000
        temp_list.append(ids)
        file.write(str(str(ids) + '\n'))
        print('Vgs ', vgs, ' Ids', ids)
    for vgs in np.flip(vgs_range):
        src_vgs.write('VOLT:LEV ' + str(vgs) + 'V')
        # time.sleep(0.1)
    ids_list.append(temp_list)
    columns.append(temp_list)

file.close()

src_vgs.write('OUTPUT OFF')
src_vds.write('smua.source.output = smua.OUTPUT_OFF')

fig, ax = plt.subplots()
ax.grid(True, which="both")
plt.ylabel('IDS(mA)')
plt.xlabel('VGS(V)')
n = 0
for ids_values in ids_list:
    ids_values = np.array(ids_values)
    ax.plot(vgs_range, ids_values, label=str('VDS ' + str(vds_range[n]) + 'V'))
    n = n+1

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])
plt.title(plt_title)
name_plt = str(name + '.png')
plt.savefig(name_plt)

src_vds.close()
src_vgs.close()

fields = ['Vgs', 'Vd=1', 'Vd=1.5', 'Vd=2', 'Vd=2.5', 'Vd=3', 'Vd=3.5', 'Vd=4', 'Vd=4.5', 'Vd=5', 'Vd=5.5', 'Vd=6', 'Vd=6.5', 'Vd=7', 'Vd=7.5', 'Vd=8']
rows = zip(*columns)

name_csv = str(name + '.csv')

with open(name_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

# plt.show()
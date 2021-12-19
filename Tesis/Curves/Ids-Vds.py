import pyvisa
import numpy as np
import time
import matplotlib.pyplot as plt
from datetime import datetime
import csv
from tqdm import tqdm

# Transistor
state = 'U1'
w = '100'
l = '24'

# Connection
rm = pyvisa.ResourceManager()

src_vgs = rm.open_resource('GPIB1::20::INSTR')
src_vds = rm.open_resource('GPIB1::24::INSTR')

# Set configuration
src_vds.write('smua.reset()')
src_vds.write('smua.source.output = smua.OUTPUT_OFF')
src_vds.write('smua.source.func = smua.OUTPUT_DCVOLTS')

# Setting limits
src_vds.write('smua.source.limitv = 10')
src_vds.write('smua.source.limiti = 100e-3')

for i in tqdm(range(2)):
    # file
    title = state + ' ' + w + '-' + l
    plt_title = w+'/'+l
    now = datetime.now()
    name = now.strftime(title + ' Ids-Vds' + ' T' + str(i) + " %d-%m-%Y %H-%M-%S")
    name_file = str(name + '.txt')
    file = open(name_file, 'w')

    # Setting initial values and turn on
    src_vgs.write('VOLT:LEV 0V')
    src_vds.write('smua.source.levelv = 0')
    src_vgs.write('OUTPUT ON')
    src_vds.write('smua.source.output = smua.OUTPUT_ON')

    # Reading
    vgs_max = 5
    vds_max = 5
    vgs_step = 0.5
    vds_step = 0.1
    vgs_range = np.arange(1, vgs_max + vgs_step, vgs_step)
    vds_range = np.arange(0, vds_max + vds_step, vds_step)
    ids_list = []

    file.write(str('Vgs range: ' + '0,' + str(vgs_max) + ',' + str(vgs_step) + '\n'))
    file.write(str('Vds range: ' + '0,' + str(vds_max) + ',' + str(vds_step) + '\n'))

    columns = [vds_range]
    for vgs in vgs_range:
        src_vgs.write('VOLT:LEV ' + str(vgs) + 'V')
        temp_list = []
        time.sleep(0.5)
        file.write(str('\n' + 'Vgs: ' + str(vgs) + '\n'))
        # print('Vgs ', vgs)
        for vds in vds_range:
            src_vds.write('smua.source.levelv = ' + str(vds))
            src_vds.write('print(smua.measure.i(smua.nvbuffer1))')
            ids = float(src_vds.read())*1000
            temp_list.append(ids)
            file.write(str(str(ids) + '\n'))
            # print('Vds ', vds, ' Ids', ids)
        ids_list.append(temp_list)
        columns.append(temp_list)

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
    plt.title(plt_title)
    name_plt = str(name + '.png')
    plt.savefig(name_plt)



    fields = ['Vds', 'Vg=0', 'Vg=0.5', 'Vg=1', 'Vg=1.5', 'Vg=2', 'Vg=2.5', 'Vg=3', 'Vg=3.5', 'Vg=4', 'Vg=4.5', 'Vg=5', 'Vg=5.5', 'Vg=6', 'Vg=6.5', 'Vg=7', 'Vg=7.5', 'Vg=8']
    rows = zip(*columns)

    name_csv = str(name + '.csv')

    with open(name_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    # plt.show()
src_vds.close()
src_vgs.close()
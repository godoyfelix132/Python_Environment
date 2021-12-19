import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

title = '100-8'
plt_title = '100/8'
now = datetime.now()
name = now.strftime("%d-%m-%Y %H-%M-%S " + title)
name_file = str(name + '.txt')
file = open(name_file, 'w')

vgs_max = 5
vds_max = 5
vgs_step = 1
vds_step = 0.1
vgs_range = np.arange(0, vgs_max, vgs_step)
vds_range = np.arange(0, vds_max, vds_step)
ids_list = []

file.write(str('Vgs range: ' + '0,' + str(vgs_max) + ',' + str(vgs_step) + '\n'))
file.write(str('Vds range: ' + '0,' + str(vds_max) + ',' + str(vds_step) + '\n'))
for vgs in vgs_range:
    temp_list = []
    file.write(str('\n' + 'Vgs: ' + str(vgs) + '\n'))
    for vds in vds_range:
        ids = vds + vgs
        temp_list.append(ids)
        file.write(str(str(ids) + '\n'))
    ids_list.append(temp_list)
file.close()

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
plt.show()



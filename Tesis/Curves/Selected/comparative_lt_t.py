import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_id_list(temp_list):
    l_list = []
    for l in temp_list:
        r = l.split("\t")
        r = r[1].split('\n')
        l_list.append(float(r[0])*1000)
    return l_list


file=open('L 10-4.txt', 'r')
df = pd.read_csv('T 10-4.csv')
plt_title = '10-4'

text = file.readlines()

vgs1 = df['MNMOS_1:drain:I(Vg=1)[Amps]'].values.tolist()
vgs2 = df['MNMOS_1:drain:I(Vg=2)[Amps]'].values.tolist()
vgs3 = df['MNMOS_1:drain:I(Vg=3)[Amps]'].values.tolist()
vgs4 = df['MNMOS_1:drain:I(Vg=4)[Amps]'].values.tolist()
vgs5 = df['MNMOS_1:drain:I(Vg=5)[Amps]'].values.tolist()
vgs6 = df['MNMOS_1:drain:I(Vg=6)[Amps]'].values.tolist()
vgs7 = df['MNMOS_1:drain:I(Vg=7)[Amps]'].values.tolist()
vgs8 = df['MNMOS_1:drain:I(Vg=8)[Amps]'].values.tolist()

init = 2
end = 83
temp_1 = text[init:end]

init = end + 1
end = init + 81
temp_2 = text[init:end]

init = end + 1
end = init + 81
temp_3 = text[init:end]

init = end + 1
end = init + 81
temp_4 = text[init:end]

init = end + 1
end = init + 81
temp_5 = text[init:end]

init = end + 1
end = init + 81
temp_6 = text[init:end]

init = end + 1
end = init + 81
temp_7 = text[init:end]

init = end + 1
end = init + 81
temp_8 = text[init:end]

vgs1r = np.array(get_id_list(temp_1))
vgs2r = np.array(get_id_list(temp_2))
vgs3r = np.array(get_id_list(temp_3))
vgs4r = np.array(get_id_list(temp_4))
vgs5r = np.array(get_id_list(temp_5))
vgs6r = np.array(get_id_list(temp_6))
vgs7r = np.array(get_id_list(temp_7))
vgs8r = np.array(get_id_list(temp_8))

ids_list = [vgs1,vgs2,vgs3,vgs4,vgs5,vgs6,vgs7,vgs8]
ids_listr = [vgs1r,vgs2r,vgs3r,vgs4r,vgs5r,vgs6r,vgs7r,vgs8r]
vgs_range = np.arange(0, 9, 1)
vds_range = np.arange(0, 8.1, 0.1)

# fig, ax = plt.subplots()
# ax.grid(True, which="both")
# plt.ylabel('IDS(mA)')
# plt.xlabel('VDS(V)')
# n = 1
#
#
# for i in range(len(ids_list)):
#     r_list = np.array(ids_listr[i]).astype(float)
#     p_list = np.array(ids_list[i]).astype(float) * 1000
#     sub_list = r_list - p_list
#     e = np.absolute(sub_list)/np.absolute(r_list)
#     ax.plot(vds_range, e, label=str('VGS ' + str(i+1) + 'V'))
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles[::-1], labels[::-1])
# plt.title('10/4')
# plt.show()


fig, ax = plt.subplots()
ax.grid(True, which="both")
plt.ylabel('IDS(mA)')
plt.xlabel('VDS(V)')
n = 1
for ids_values in ids_list:
    ids_values = np.array(ids_values)
    ##
    ids_values = ids_values.astype(float)
    ids_values = ids_values * 1000
    ##
    ax.plot(vds_range, ids_values, linestyle = ':', label=str('VGS ' + str(vgs_range[n]) + 'V'))
    n = n+1

n = 1
for ids_values in ids_listr:
    ids_values = np.array(ids_values)
    ax.plot(vds_range, ids_values, label=str('VGS ' + str(vgs_range[n]) + 'V'))
    n = n+1

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])
plt.title(plt_title)
plt.show()
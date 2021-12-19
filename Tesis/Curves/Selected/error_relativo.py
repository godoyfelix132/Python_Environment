import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('T 10-4.csv')
dfr = pd.read_csv('N2 10-4.csv')
plt_title = '10/4'

vgs1r = dfr['Vg=1'].values.tolist()
vgs2r = dfr['Vg=2'].values.tolist()
vgs3r = dfr['Vg=3'].values.tolist()
vgs4r = dfr['Vg=4'].values.tolist()
vgs5r = dfr['Vg=5'].values.tolist()
vgs6r = dfr['Vg=6'].values.tolist()
vgs7r = dfr['Vg=7'].values.tolist()
vgs8r = dfr['Vg=8'].values.tolist()

vgs1 = df['MNMOS_1:drain:I(Vg=1)[Amps]'].values.tolist()
vgs2 = df['MNMOS_1:drain:I(Vg=2)[Amps]'].values.tolist()
vgs3 = df['MNMOS_1:drain:I(Vg=3)[Amps]'].values.tolist()
vgs4 = df['MNMOS_1:drain:I(Vg=4)[Amps]'].values.tolist()
vgs5 = df['MNMOS_1:drain:I(Vg=5)[Amps]'].values.tolist()
vgs6 = df['MNMOS_1:drain:I(Vg=6)[Amps]'].values.tolist()
vgs7 = df['MNMOS_1:drain:I(Vg=7)[Amps]'].values.tolist()
vgs8 = df['MNMOS_1:drain:I(Vg=8)[Amps]'].values.tolist()

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

# print(df.to_string())
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('N1 10-4.csv')


vgs1 = df['Vg=1'].values.tolist()
vgs2 = df['Vg=2'].values.tolist()
vgs3 = df['Vg=3'].values.tolist()
vgs4 = df['Vg=4'].values.tolist()
vgs5 = df['Vg=5'].values.tolist()
vgs6 = df['Vg=6'].values.tolist()
vgs7 = df['Vg=7'].values.tolist()
vgs8 = df['Vg=8'].values.tolist()

ids_list = [vgs1,vgs2,vgs3,vgs4,vgs5,vgs6,vgs7,vgs8]
vgs_range = np.arange(0, 9, 1)
vds_range = np.arange(0, 8.1, 0.1)

fig, ax = plt.subplots()
ax.grid(True, which="both")
plt.ylabel('IDS(mA)')
plt.xlabel('VDS(V)')
n = 1
for ids_values in ids_list:
    ids_values = np.array(ids_values)
    ax.plot(vds_range, ids_values, label=str('VGS ' + str(vgs_range[n]) + 'V'))
    n = n+1

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])
plt.title('10/4')
plt.show()

# print(df.to_string())

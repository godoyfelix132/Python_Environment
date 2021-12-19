import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('N2 50-8.csv')
plt_title = '50/8'

df.set_index('Vds', inplace=True) # Create index from Vds columns
#a = df.loc[2]['Vg=2']
#print(a)
index_range = np.arange(0, 8.5, 0.5)
ids_list = []
for i in index_range:
    try:
        ids = df.loc[i]['Vg=' + str(i)]
    except:
        a = str(int(i))
        ids = df.loc[i]['Vg=' + a]
    ids_list.append(ids)

linear_regression = LinearRegression()
linear_regression.fit(index_range.reshape(-1, 1)[10:], ids_list[10:])
m = linear_regression.coef_
b = linear_regression.intercept_
print(m,'-',b)


fig, ax = plt.subplots()
ax.grid(True, which="both")
plt.ylabel('IDS(mA)')
plt.xlabel('VDS=VGS(V)')

ax.plot(index_range, ids_list)
plt.axline((8, ids_list[-1]), slope=m, color="black", linestyle=(0, (5, 5)))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])
plt.title(plt_title)
plt.show()


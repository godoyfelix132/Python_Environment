import pandas as pd
import numpy as np

data = np.array([['', 'Col1', 'Col2'], ['Fila1', 11, 22], ['Fila', 33, 44]])
df = pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])
print('Data Frame:\n', df)
print('Row Names:', df.index)
print('Shape:', df.shape)
print('Statistic:\n', df.describe())
print('Correlation:\n', df.corr())

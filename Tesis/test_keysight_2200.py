import pyvisa
import numpy as np
import time
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager()
print(rm.list_resources())

Source1 = rm.open_resource('GPIB1::22::INSTR')
Source2 = rm.open_resource('GPIB1::25::INSTR')

Source1.write('VOLT:LEV 0V')
Source2.write('VOLT:LEV 0V')
Source1.write('OUTPUT ON')
Source2.write('OUTPUT ON')
ids_list = []
vgs_range = np.arange(2, 6, 1)
vds_range = np.arange(0, 5, 0.1)
for vgs in vgs_range:
    Source1.write('VOLT:LEV ' + str(vgs) + 'V')
    temp_list = []
    for vds in vds_range:
        time.sleep(0.5)
        Source2.write('VOLT:LEV ' + str(vds) + 'V')
        ids = Source2.query('MEAS:CURR?')
        temp_list.append(float(ids))
    ids_list.append(temp_list)
Source1.close()
Source2.close()

plt.grid(True, which="both")
for ids_values in ids_list:
    ids_values = np.array(ids_values)
    plt.plot(vds_range, ids_values)
plt.show()


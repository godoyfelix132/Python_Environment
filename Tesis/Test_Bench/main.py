from Tesis.Test_Bench.src.generator import *

visa_gen = 'TCPIP0::10.0.7.161::inst0::INSTR'
visa_scope = 'TCPIP0::10.0.7.249::inst0::INSTR'

rm = pyvisa.ResourceManager()
gen12_connection = rm.open_resource(visa_gen)

gen1 = Generator(instrument=gen12_connection, source='1')
gen1.set_function('SQU')
gen1.set_frequency('1KHz')
gen1.set_voltage('1V')
gen1.set_output('1')

gen2 = Generator(instrument=gen12_connection, source='2')
gen2.set_function('SQU')
gen2.set_frequency('1KHz')
gen2.set_voltage('1V')
gen2.set_output('1')
gen2.set_phase('90')
gen2.sync()

gen12_connection.close()
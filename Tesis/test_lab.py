import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())

Gen = rm.open_resource('TCPIP0::10.0.7.161::inst0::INSTR')
Gen.write('SOUR1:FUNC SIN')
Scope = rm.open_resource('TCPIP0::10.0.7.249::inst0::INSTR')
Source = rm.open_resource('GPIB0::22::INSTR')
print(Source.query('*IDN?'))
Source.write('VOLT:LEV 5V')
Source.write('OUTPUT ON')
# Source.write('OUTP:ENAB')
print(rm.list_opened_resources())

Scope.close()
Gen.close()

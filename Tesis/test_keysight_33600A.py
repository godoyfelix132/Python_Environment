import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
Gen = rm.open_resource('TCPIP0::10.0.7.161::inst0::INSTR')
Scope = rm.open_resource('TCPIP0::10.0.7.249::inst0::INSTR')
Scope.close()
Gen.write('SOUR1:FUNC SIN')
Gen.close()



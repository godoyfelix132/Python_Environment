import pyvisa
import time

class Generator:
    def __init__(self, instrument, function='SIN', frequency ='1.0E+03', voltage='100 mV', output='0', source='1', phase='0'):
        self._instrument = instrument
        self._function = function
        self._frequency = frequency
        self._voltage = voltage
        self._output = output
        self._source = source
        self._phase = phase

    def set_function(self, fun):
        '''SINusoid, SQUare, RAMP, NRAMp, TRIangle, NOISe(gaussian noise), PRBS(pseudo-random), ARBitrary(arbitrary waveform)'''
        self._function = str(fun)
        self._instrument.write('SOUR'+self._source+':FUNC ' + self._function)

    def set_frequency(self, freq):
        ''' INT FLOAT (mV=MV=millivolts MHZ=mhz=Megahertz MA=MEGA MAV=Megavolts)'''
        self._frequency = str(freq)
        self._instrument.write('SOUR'+self._source+':FREQ ' + self._frequency)

    def set_voltage(self, minimum='0V', maximum='100mV'):
        '''INT FLOAT (mV=MV=millivolts MHZ=mhz=Megahertz MA=MEGA MAV=Megavolts)'''
        s1 = 'SOUR'+self._source+':VOLT:HIGH ' + str(maximum)
        s2 = 'SOUR' + self._source + ':VOLT:LOW ' + str(minimum)
        self._instrument.write(s1)
        self._instrument.write(s2)

    def set_output(self, out):
        self._output = str(out)
        s = 'OUTPut'+self._source + ' ' + self._output
        self._instrument.write(s)

    def set_phase(self, degrees):
        self._phase = str(degrees)
        s = 'SOUR'+self._source+':PHASe +' + self._phase
        self._instrument.write(s)

    def sync(self):
        s = 'SOUR' + self._source + ':PHASe:SYNC'
        self._instrument.write(s)

    def high_z(self):
        s = 'OUTPut'+self._source+':LOAD INF'
        self._instrument.write(s)

    def send(self, code):
        self._instrument.write(code)

    def state(self):
        return self._function


if __name__ == '__main__':
    visa_gen = 'TCPIP0::10.0.7.161::inst0::INSTR'
    visa_scope = 'TCPIP0::10.0.7.249::inst0::INSTR'

    rm = pyvisa.ResourceManager()
    gen12_connection = rm.open_resource(visa_gen)

    gen1 = Generator(instrument=gen12_connection, source='1')
    gen1.set_function('SQU')
    gen1.set_frequency('2KHz')
    gen1.set_voltage(minimum='0V', maximum='3V')
    gen1.high_z() # Must be before turning on the output
    gen1.set_output('1')


    gen2 = Generator(instrument=gen12_connection, source='2')
    gen2.set_function('SQU')
    gen2.set_frequency('2KHz')
    gen2.set_voltage(minimum='0V', maximum='3V')
    gen2.set_phase('90')
    gen2.high_z() # Must be before turning on the output
    gen2.set_output('1')

    gen2.sync()

    gen12_connection.close()
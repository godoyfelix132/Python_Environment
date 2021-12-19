import pyvisa


class Scope:
    def __init__(self, instrument):
        self._instrument = instrument

    def set_function(self, fun):
        '''SINusoid, SQUare, RAMP, NRAMp, TRIangle, NOISe(gaussian noise), PRBS(pseudo-random), ARBitrary(arbitrary waveform)'''
        self._function = str(fun)
        self._instrument.write('SOUR'+self._source+':FUNC ' + self._function)


if __name__ == '__main__':
    visa_scope = 'TCPIP0::10.0.7.249::inst0::INSTR'

    rm = pyvisa.ResourceManager()
    scope1_connection = rm.open_resource(visa_scope)

    scope1 = Scope(instrument=scope1_connection)

    scope1_connection.close()
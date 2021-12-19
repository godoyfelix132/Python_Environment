import numpy as np
import matplotlib.pyplot as plt
import pyaudio


class Wave:
    @staticmethod
    def sin(_amp, _freq, _start, _stop, _rate):
        """
        :param amp: Amplitude(mag)
        :param freq: Frequency(Hz)
        :param start: Start time(seconds)
        :param stop: Stop time (seconds)
        :param rate: Sample Rate (HZ)
        :return: Sin signal (np.array)
        """
        _points = int((_rate/_freq)*(stop*_freq))
        _time = np.linspace(_start, _stop, _points)
        _w = 2 * np.pi * _freq
        _signal = _amp*np.sin(_w*_time).astype(np.float32)
        return _time, _signal

    @staticmethod
    def cut_signal(_time, _signal, _start, _stop):
        """
        :param time: Time array (seconds)
        :param signal: Signal to cut
        :param start: Start time to cut (milliseconds)
        :param stop: Stop time to cut (milliseconds)
        :return:
        """
        _time = _time*(10**3)
        _time_c = []
        _signal_c = []
        for i in range(len(_time)):
            if start <= _time[i] <= stop:
                _time_c.append(_time[i])
                _signal_c.append(_signal[i])
            elif _time[i] > stop:
                break
        return np.array(_time_c), np.array(_signal_c)

    @staticmethod
    def signal_shape(_time, _signal, _freq):
        """
        :param time: Time of the signal (seconds)
        :param signal: Signal
        :param freq: Hz
        :return: Shape
        """
        _time = _time * (10 ** 3)
        _time_c = []
        _signal_c = []
        _stop = (1/_freq) * (10 ** 3)
        for i in range(len(_time)):
            if _time[i] <= _stop:
                _time_c.append(_time[i])
                _signal_c.append(_signal[i])
            elif _time[i] > _stop:
                break
        return np.array(_time_c), np.array(_signal_c)

    @staticmethod
    def plot_wave(_time, _signal):
        plt.figure()
        plt.title('Sine wave')
        plt.xlabel('Time')
        plt.ylabel('Amplitude = sin(time)')
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        plt.plot(_time, _signal)

    @staticmethod
    def plot_waves(_time, _signals):
        """
        :param _time: Time (any)
        :param _signals: List of signals
        :return:
        """
        plt.figure()
        plt.title('Sine wave')
        plt.xlabel('Time')
        plt.ylabel('Amplitude = sin(time)')
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        for _signal in _signals:
            plt.plot(_time, _signal)

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def sin_noise(_time, _amp_n, _freq_n):
        """
        :param _time: Fundamental time (seconds)
        :param _amp_n: Amplitude of noise (mag)
        :param _freq_n: Frequency of noise (Hz)
        :return:
        """
        _w = 2 * np.pi * _freq_n
        _signal = _amp_n * np.sin(_w * _time).astype(np.float32)
        return _signal

    @staticmethod
    def add_waves(_waves):
        _new_wave = 0
        for _w in _waves:
            _new_wave = _new_wave + _w
        _max = _new_wave.max()
        return (1/_max) * _new_wave


if __name__ == '__main__':
    frequency = 440
    sample_rate = 44000
    amplitude = 1

    start = 0
    stop = 5
    time, signal = Wave.sin(amplitude, frequency, start, stop, sample_rate)

    start = 0
    stop = 6
    time_c, signal_c = Wave.cut_signal(time, signal, start, stop)

    time_sh, signal_sh = Wave.signal_shape(time, signal, frequency)

    frequency_n1 = frequency*2
    amplitude_n1 = amplitude/2
    signal_n1 = Wave.sin_noise(time, amplitude_n1, frequency_n1)
    _, signal_n1_sh = Wave.signal_shape(time, signal_n1, frequency)

    frequency_n2 = frequency * 4
    amplitude_n2 = amplitude / 4
    signal_n2 = Wave.sin_noise(time, amplitude_n2, frequency_n2)
    _, signal_n2_sh = Wave.signal_shape(time, signal_n2, frequency)

    signal_add = Wave.add_waves([signal, signal_n1, signal_n2])
    _, signal_add_sh = Wave.signal_shape(time, signal_add, frequency)

    print(signal_add.min())
    # Wave.plot_wave(time, signal)
    # Wave.plot_wave(time_c, signal_c)

    Wave.plot_wave(time_sh, signal_sh)
    # Wave.plot_wave(time_sh, signal_n1_sh)
    Wave.plot_waves(time_sh, [signal_sh, signal_n1_sh, signal_n2_sh])
    Wave.plot_wave(time_sh, signal_add_sh)

    Wave.show()

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    stream.write(0.5 * signal)
    stream.write(0.5 * signal_add)
    stream.stop_stream()
    stream.close()
    p.terminate()


import numpy as np

def generate_sine_wave(frequency, duration, sample_rate, amplitude):
    t = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)

    # t: time axis
    # def: defines a function
    # (0, duration: from 0 second to duration second
    # sample_rate * duration: number of samples needed
    # endpoint=False: dont include the last point

    # y: signal values
    # np.sin: sine wave
    # 2 * np.pi * frequency * t: 2pif --> ANGULAR FREQUENCY!!   

    def generate_square_wave(frequency, duration, sample_rate, amplitude):
    t = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    y = amplitude * signal.square(2 * np.pi * frequency * t)
    return t,y

    # singal.square: generates a periodic square-wave waveform
    # 2 * np.pi * frequency * t: converts t into radians
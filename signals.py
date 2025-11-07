import numpy as np
import matplotlib.pyplot as plt


def generate_sine_wave(frequency, duration, sample_rate, amplitude):

  """
    Generate a discrete-time sine wave.

    Parameters:
        frequency (float): Frequency of the sine wave in Hz.
        duration: Length of the signal in seconds.
        sample_rate: Number of samples per second (Hz).
        amplitude (float): Amplitude of the sine wave.

    Returns:
        tuple: (t, y)
            t (numpy.ndarray): Time axis from 0 to duration (exclusive).
            y (numpy.ndarray): Sine wave values corresponding to t.
    """

    t = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    return t,y

    # t: time axis
    # def: defines a function
    # (0, duration: from 0 second to duration second
    # sample_rate * duration: number of samples needed
    # endpoint=False: dont include the last point

    # y: signal values
    # np.sin: sine wave
    # 2 * np.pi * frequency * t: 2pif --> ANGULAR FREQUENCY!!   

def generate_square_wave(frequency, duration, sample_rate, amplitude):

   """
    Generate a discrete-time square wave.

    Parameters:
        frequency (float): Frequency of the square wave in Hz.
        duration: Length of the signal in seconds.
        sample_rate: Number of samples per second (Hz).
        amplitude (float): Peak amplitude of the square wave.

    Returns:
        tuple: (t, y)
            t (numpy.ndarray): Time axis from 0 to duration.
            y (numpy.ndarray): Square wave values (amplitude).
    """

    t = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    # y = amplitude * signals.square(2 * np.pi * frequency * t). --> Code didn't work using SciPy so I use alternative code below that doesnt require SciPy.
    y = amplitude * np.where(np.sin(2 * np.pi * frequency * t) >= 0, 1, -1)
    return t,y

    # singal.square: generates a periodic square-wave waveform
    # 2 * np.pi * frequency * t: converts t into radians


# Operations:

# Time-shifting
def time_shift(t, y, shift_by):

 """
    Shift a signal in time.

    Parameters:
        t (numpy.ndarray): Original time axis.
        y (numpy.ndarray): Signal samples.
        shift_by (float): Amount of shift to apply. 
                          Positive = shift right, negative = shift left.

    Returns:
        tuple: (shifted_t, shifted_y)
            shifted_t (numpy.ndarray): Time axis shifted by 'shift_by'.
            shifted_y (numpy.ndarray): Original signal values.
    """
    
    shifted = t + shift_by
    return shifted, y

# Time-scaling
def time_scale(t, y, scale_by):
    scaled = t * scale_by
    scaled_y = np.interp(scaled, t, y)
    return scaled, scaled_y
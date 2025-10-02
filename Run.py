import sys
sys.path.append('/Users/lisaokada/Desktop/6182089-sands-python')

import numpy as np
import matplotlib.pyplot as plt
from signals import *
# *: Import all the functions from sigal.py


# Sinusoidal Wave
frequency = 2
duration = 1
sample_rate = 100
amplitude = 1

t, wave = generate_sine_wave(frequency, duration, sample_rate, amplitude)

# array of time values and sine values
# sample_rate: controls the smoothness of the graph

plt.plot(t,wave)
plt.title("Sine Wave")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()


# Square Wave
frequency = 2
duration = 1
sample_rate = 100
amplitude = 1

t2, wave2 = generate_square_wave(frequency, duration, sample_rate, amplitude)

plt.plot(t2,wave2)
plt.title("Square Wave")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
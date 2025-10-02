import sys
sys.path.append('/Users/lisaokada/Desktop/6182089-sands-python')

import numpy as np
import matplotlib.pyplot as plt
from signals import generate_sine_wave, generate_square_wave

# Sinusoidal Wave
frequency = 2
duration = 1
sample_rate = 100
amplitude = 1

t, wave = generate_sine_wave(frequency, duration, sample_rate, amplitude)

# array of time values and sine values
# sample_rate: controls the smoothness of the graph
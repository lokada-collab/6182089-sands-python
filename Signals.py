import numpy as np

def generate_sine_wave(frequency, duration, sample_rate, amplitude):
    t = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)


import numpy as np
from signals import generate_sine_wave, generate_square_wave, time_shift, time_scale

# Normal test for sine wave
t, y = generate_sine_wave(1, 2, 1)
assert len(t) == 1000 
assert len(y) == 1000 

# Edge test for sine wave
t, y = generate_sine_wave(5, 0, 1)
assert np.allclose(y, 0)


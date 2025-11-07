import numpy as np
from signals import generate_sine_wave, generate_square_wave, time_shift, time_scale

# Normal test for sine wave
t, y = generate_sine_wave(1, 2, 1)
assert len(t) == 1000 
assert len(y) == 1000 

# Edge test for sine wave
t, y = generate_sine_wave(5, 0, 1)
assert np.allclose(y, 0)

# Normal test for square wave
t, y = generate_square_wave(2, 1, 100, 3)
assert len(t) == len(y)
assert set(np.unique(y)) == {-3, 3}

# Edge test for square wave
t, y = generate_square_wave(2, 1, 100, 0)
assert np.allclose(y, 0)

# Normal test for time shift
t, y = generate_sine_wave(2, 1, 100, 1)
t_shift, y_shift = time_shift(t, y, 0.5)
assert np.array_equal(y_shift, y) 
assert np.allclose(t_shift, t + 0.5)  

# Edge test for time shift
t_shift, y_shift = time_shift(t, y, 0)
assert np.array_equal(t_shift, t)
assert np.array_equal(y_shift, y)

# Normal test for time scale
t_scaled, y_scaled = time_scale(t, y, 0.5)  # compress
assert len(t_scaled) == len(y_scaled)
assert np.allclose(t_scaled, t * 0.5)

# Edge test for time scale
t_scaled, y_scaled = time_scale(t, y, 1)
assert np.array_equal(t_scaled, t)
assert np.allclose(y_scaled, y)
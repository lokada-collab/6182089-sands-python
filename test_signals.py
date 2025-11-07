import numpy as np
from matplotlib.pyplot as plt

t, y = generate_sine_wave(1, 2, 1)
assert len(t) == 1000 
assert len(y) == 1000 

t, y = generate_sine_wave(5, 3, 1)
assert np.isclose(max(y), 3, atol=1e-6)

t, y = generate_sine_wave(5, 0, 1)
assert np.allclose(y, 0)
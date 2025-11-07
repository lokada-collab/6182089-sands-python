import numpy as np
from matplotlib.pyplot as plt

t, y = generate_sine_wave(1, 2, 1)
assert len(t) == 1000 
assert len(y) == 1000 
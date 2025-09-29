# Signals and Systems Python project - Lisa Okada (6182089)

import numpy as np, matplotlib.pyplot as plt

# Time axis
fs = 2000
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second, 2000 samples

# Signals (5 Hz)
f = 5.0

# Sinusoid:

sine   = np.sin(2*np.pi*f*t)

plt.figure(); plt.plot(t, sine);   #new blank canvas
plt.title("Figure 1 - Sinusoid (5 Hz)");   
plt.xlabel("t [s]"); 
plt.ylabel("Amplitude"); 
plt.grid(True);     #Adding line grid onto the graph so that its easier to read

plt.show()
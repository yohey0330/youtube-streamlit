import numpy as np
import matplotlib.pyplot as plt
import IPython.display
 
A = 0.8
f = 440
samplingrate_hz = 44100
 
t = np.arange(0, 1, 1 / samplingrate_hz)
y = A * np.sin(2*np.pi*f*t)
 
plt.plot(t, y)
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.show()
 
IPython.display.Audio(y, rate = samplingrate_hz)
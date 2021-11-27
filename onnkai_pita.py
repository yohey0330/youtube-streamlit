import numpy as np
import IPython as IP

from time import sleep

fs = 48000
duration = 1.0

def play_sine(f):
    t = np.linspace(0., duration, int(fs * duration))  # ( start, stop, num of data )
    x = np.sin(f * (2. * np.pi) * t)
    IP.display.display(IP.display.Audio(x, rate=fs, autoplay=True))

l = [1]
i = 1
gosa = 0.1

i *= 3
while i > 2:
    i /= 2
    if i < 2 - gosa:
        l.append(i)
        i *= 3
    elif abs(2 - i) <= gosa:
        l.append(i)
        break

l.sort()
l_n = list(map(lambda x: x * 440, l))

A = 0.8
samplingrate_hz = 44100
t = np.arange(0, 1, 1 / samplingrate_hz)

for f in l_n:
    if 469<f<470 or 528<f<529 or 626<f<627 or 704<f<705 or 792<f<793:
        continue
    else:
        print(f)
        play_sine(f)
        sleep(1)
# AM modulation
import numpy as np
import math
import matplotlib.pyplot as plt

# Carrier wave
fc=10
wc=2*math.pi*fc
Ac=1
t=np.arange(0, 5, 0.01)
yc=Ac*np.sin(wc*t)

# Wave modulation
fm=1
wm=2*np.pi*fm
Am=1
ym=Am*np.sin(wm*t)
m=Am/Ac

# Modulated wave
y=(1+m*ym)*0.1*yc


plt.plot(t, y)
plt.show()
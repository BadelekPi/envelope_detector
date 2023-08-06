"""
 Discrete Fourier transform quarantee to be completely reversible with Inverse Discrete Fourier transform
 It's limited only by rounding error, so its great for computers
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy

y = np.linspace(-50, 50, 1000)
# Analytical formula
F = (y*np.cos(y) - np.sin(y))*1j/(np.pi*y**2)

plt.subplot(1,2,1)
plt.plot(y, np.imag(F), label="imag")
plt.plot(y, np.real(F), label="real")
plt.legend()

plt.subplot(1,2,2)
plt.plot(y, abs(F), "r", label="magnitude")
plt.legend()

### Denoising data : FFT 
dt = 0.001
t = np.arange(0, 1, dt)
# Sum of 2 freqs
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
pure_f = f
# Adding noise
f = f + 2.5*np.random.randn(len(t))

## Compute the FFT, power spectrum, x-axis, plot half
n = len(t)
fhat = np.fft.fft(f,n)
PSD = fhat * np.conj(fhat) / n
freq = (1/(dt*n)) * np.arange(n)
L = np.arange(1, np.floor(n/2), dtype='int')

fig, axs = plt.subplots(2, 1)
plt.sca(axs[0])
plt.plot(t, f, color='c', label='Noisy')
plt.plot(t, pure_f, color='k', label='Clean')
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(freq[L], PSD[L], color='c', label='Noisy')
plt.xlim(freq[L[0]],freq[L[-1]])
plt.legend()

## Use the PSD to filter out noise
indices = PSD > 100         # Find all freqs with large power
PSDclean = PSD * indices    # Zero out all others
fhat = indices * fhat       # Zero out small Fourier coeffs in Y
ffilt = np.fft.ifft(fhat)   # Iverse FFT for filtered time signal

## Plots
fig, axs = plt.subplots(3, 1)
plt.sca(axs[0])
plt.plot(t, f, color='c', label='Noisy')
plt.plot(t, pure_f, color='k', label='Clean')
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(t, ffilt, color='k', label='Filtered')
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[2])
plt.plot(freq[L], PSD[L], color='c', label='Noisy')
plt.plot(freq[L], PSDclean[L], color='k', label='Filtered')
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()

plt.show()


import numpy as np
import matplotlib.pyplot as plt

sr = 80
range = 20001
freq = np.linspace(1, range, range*sr)
# w = 2 * np.pi * freq


A = 1
def x_max() :
    return np.full_like(freq, A)
def v_max(f) :
    return A*2*np.pi*f
def a_max(f) :
    return A*pow(2*np.pi*f,2)

def rms(x):
    return x/np.sqrt(2) 

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

ax1.plot(freq, x_max(), color='blue', linewidth=2)
ax1.plot(freq, rms(x_max()), linestyle="--",label="rms")
ax1.set_ylabel('$x_{RMS}$ ')
ax1.set_title('Charakterystyka drgań w dziedzinie częstotliwości ($A=1$)')
ax1.grid(True, which="both", ls="-", alpha=0.5)

ax2.plot(freq, v_max(freq), color='green', linewidth=2)
ax2.plot(freq, rms(v_max(freq)), linestyle="--",label="rms")
ax2.set_ylabel('$v_{RMS}$')
ax2.grid(True, which="both", ls="-", alpha=0.5)

ax3.plot(freq, a_max(freq), color='red', linewidth=2)
ax3.plot(freq, rms(a_max(freq)), linestyle="--", label="rms")
ax3.set_ylabel('$a_{RMS}$')
ax3.set_xlabel('Częstotliwość $f$ [Hz]')
ax3.grid(True, which="both", ls="-", alpha=0.5)

plt.tight_layout() 

plt.show()
print(freq)

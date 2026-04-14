import numpy as np
import matplotlib.pyplot as plt


_c = 343 #m/s
_fmaxHz = 20000 #Hz
l6 = _c/_fmaxHz/6

_b = 0.3 #m Połowa szerokości rozpraszacza
_w = 0.025# m Szerokość jednej studzienki
_hmax = 0.06 #m
_N = 7 #Długość ciągu pseudolosowego
n = np.arange(0, _N, 1) # Numeracja studzienek rozpraszazcza  
sn = (n+1)**2%_N #Wyrazy ciągu pseudolosowego
f = np.arange(100, _fmaxHz+0.01, 2) #Częstotliwość

_r0 = 10 #m Odległość źródła dźwięku od próbki
_r = 5 #m Odległość mikrofonów od próbki
_phi =  np.arange(-1*np.pi/2, np.pi/2+0.01, np.pi/180) # Kąt analizy odbicia fali dźwiękowej


xs = np.arange(-(_N-1)/2*_w, (_N+1)/2*_w, l6) # Pozycja wzdłuż osi x, 𝜆𝜆6 = - lambda dla częstotliwości fmax


depth_factor = _hmax/np.max(sn)
hn = sn*depth_factor

hx = []
for x in xs:
    x = x+ np.abs(xs[0])
    hx.append(hn[int(np.floor(x/_w))])
hx = np.array(hx)


# Przydatne funkcje:
# nx = histcounts(xs,edges) i
# repelem(hn, nx)

#R = np.exp(-1j * k * 2 * hx)

#Zakres częstotliwości w których rozpraszacz jest skuteczny:

lmin = 2*_w
lmax = 2*_N*_hmax/np.max(sn)

freqmin = _c/lmax
freqmax = _c/lmin

# print(f"fmin: {lmin},  fmax:{}")
print(f"fmin: {freqmin},  fmax:{freqmax}")
for i in n:
    print(f"{n[i]}, {sn[i]}, {hn[i]} ")


plt.plot(xs, 0-hx)
plt.show()
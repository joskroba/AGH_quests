#Zad 1: wyznaczenie znormalizowanego poziomu uderzeniowego stropu std. 16 cm

import numpy as np

n = 0.2 #współczynnik strat dla betonu
d = 2500 #[kg/m3] gęstość betonu
h = 0.16 #[m] grubość stropu
Ms = d*0.16 #[kg/m2] masa powierzchniowa stropu
f = [100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150] #[Hz] pasma tercjowe
lw = [67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72,72,72,72,72]
lo = [62,62,62,62,62,62,61,60,59,58,57,54,51,48,45,42]
#print(len(f), len(lw), len(lo))
s = 1 #wsp promieniowania dla płyt skończonych pow. częstotliwości koincydencji
c = 343 #[m/s] #v dzwieku w powietrzu
cl = 3800 #[m/s] prędkość fali w betonie
#fc_2 = c**2/(2*np.pi())*np.sqrt(Ms/B) # B to sztywność w zginaniu [Nm]
fc = c**2*np.sqrt(3)/(np.pi*cl*h) # [Hz] freq krytyczna - koincydencji
for fi in f:
    Ln = 10*np.log10(fc/(n*Ms**2)) + 10*np.log10(4*n*fi/(np.pi*fc)+s) + 82.3
    print(fi, Ln,  "\n")

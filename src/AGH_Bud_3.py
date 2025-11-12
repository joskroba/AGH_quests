import matplotlib.pyplot as plt
import numpy as np


# Fs = 8000
# f = 5
# sample = 8000
# x = np.arange(sample)
# y = np.sin(2 * np.pi * f * x / Fs)
# plt.plot(x, y)
# plt.xlabel('sample(n)')
# plt.ylabel('voltage(V)')
# plt.show()

#kd - 
kd = 1 #[N/m^3]
#pow. styku elem wspornikowego
s = 1 #[m^2]
#sztywność dynamiczna elementu wspornilkowego
#                   kdp = kd * s
#masa pow. podłogi
Ms1 = -1 #[kg/m^2]
#pow. podłogi
Sc = 1 #[m^2]
#ilość wsporników
Np = 6
#czestotliwosc rezonansowa podłogi
                                      #f0 = np.sqrt(kdp*Np/(Ms1*s))/(2*np.pi)

#==============================================================
#zmniejszenie poz. uderzeniowego 

n = 0.02 #współczynnik strat dla betonu
d = 2500 #[kg/m3] gęstość betonu
h = 0.16 #[m] grubość stropu
                                #Ms = d*h #[kg/m2] masa powierzchniowa stropu
f = [100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150] #[Hz] pasma tercjowe
lw = [67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72,72,72,72,72]
lo = [62,62,62,62,62,62,61,60,59,58,57,54,51,48,45,42]
#print(len(f), len(lw), len(lo))
s = 1 #wsp promieniowania dla płyt skończonych pow. częstotliwości koincydencji
c = 343 #[m/s] #v dzwieku w powietrzu
cl = 3800 #[m/s] prędkość fali w betonie
#fc_2 = c**2/(2*np.pi())*np.sqrt(Ms/B) # B to sztywność w zginaniu [Nm]

                    #fc = c**2*np.sqrt(3)/(np.pi*cl*h) # [Hz] freq krytyczna - koincydencji
wynik_tercjowo = []
def zm_poz():
    for fi in f:
        i = 0
        Ms1 = d*h
        kdp = kd * s
        f0 = np.sqrt(kdp*Np/(Ms1*Sc))/(2*np.pi)
        fc = c**2*np.sqrt(3)/(np.pi*cl*h)
        dL = 10*np.log10(32*np.pi**2*c**2*Sc*Ms1**2*n*pow(fi,3)/(kdp**2*Np*fc))
        print(fi, dL)
        #wynik_tercjowo = []
        wynik_tercjowo.append(dL)
    print("krytyczna", fc, "\n rezonans", f0)
    print("param check", kd, s, Np, d, h, kdp, Ms1, Sc)
    return wynik_tercjowo
#========================================================================
#zadanie 1 
kd = 400*pow(10,6)
s = 9 * pow(10, -4)
Np = 10
d = 2400
h = 80*pow(10, -3)


wynik = zm_poz()
#print("krytyczna", fc, "\n rezonans", f0)
print(len(f), len(wynik_tercjowo))
plt.plot(f, wynik)
plt.xlabel('freq')
plt.ylabel('dL')
plt.xscale("log")
plt.grid()
plt.show()
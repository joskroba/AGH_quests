




import numpy as np
import matplotlib.pyplot as plt
from BUD_AGH_lib import Material , poz_dzw_plyta_mat, plt_terc, licz_wazony

# Fs = 8000
# f = 5
# sample = 8000
# x = np.arange(sample)
# y = np.sin(2 * np.pi * f * x / Fs)
# plt.plot(x, y)
# plt.xlabel('sample(n)')
# plt.ylabel('voltage(V)')
# plt.show()

#kd - #sztywność dynamiczna elementu wspornilkowego
kd = 1 #[N/m^3]
#pow. styku elem wspornikowego
s = 1 #[m^2]
#pow. podłogi
Sc = 1 #[m^2]
#ilość wsporników
Np = 6
#czestotliwosc rezonansowa podłogi
                                      #f0 = np.sqrt(kdp*Np/(Ms1*s))/(2*np.pi)

#==============================================================
#zmniejszenie poz. uderzeniowego 

# n = 0.02 #współczynnik strat dla betonu
# d = 2500 #[kg/m3] gęstość betonu
# h = 0.16 #[m] grubość stropu
                                #Ms = d*h #[kg/m2] masa powierzchniowa stropu
f = np.array([100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150]) #[Hz] pasma tercjowe
lw = [67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72,72,72,72,72]
lo = [62,62,62,62,62,62,61,60,59,58,57,54,51,48,45,42]
#print(len(f), len(lw), len(lo))
# s = 1 #wsp promieniowania dla płyt skończonych pow. częstotliwości koincydencji
# c = 343 #[m/s] #v dzwieku w powietrzu
# cl = 3800 #[m/s] prędkość fali w betonie
# #fc_2 = c**2/(2*np.pi())*np.sqrt(Ms/B) # B to sztywność w zginaniu [Nm]

                    #fc = c**2*np.sqrt(3)/(np.pi*cl*h) # [Hz] freq krytyczna - koincydencji
# Class Plyw_param:
#     def 

def zm_poz(h:float, mat:Material):
    wynik_tercjowo = []
    for fi in f:
        Ms1 = mat.gestosc*h
        kdp = kd * s
        f0 = np.sqrt(kdp*Np/(Ms1*Sc))/(2*np.pi)
        fc = mat.c**2*np.sqrt(3)/(np.pi*mat.v_fali_mat*h)
        dL = 10*np.log10(32*np.pi**2*mat.c**2*Sc*Ms1**2*mat.w_strat*pow(fi,3)/(kdp**2*Np*fc))
        # print(fi, dL)
        #wynik_tercjowo = []
        wynik_tercjowo.append(dL)
    print("krytyczna", fc, "\n rezonans", f0)
    #print("param check", kd, s, Np, d, h, kdp, Ms1, Sc)
    return wynik_tercjowo
#========================================================================
#zadanie 1 
# Wykorzystując przestawione zależności, wyznaczyć zmniejszenie poziomu uderzeniowego ∆𝐿𝐿
# oraz wskaźnik ważony ∆𝐿𝐿𝑤𝑤 dla specjalnej podłogi pływającej dla zadanych parametrów:
kd = 400*pow(10,6)
s = 9 * pow(10, -4)
Np = 10

h = 80*pow(10, -3)


Beton = Material(2400, 3800, 0.02)



wynik = zm_poz(h, Beton)
plt_terc(wynik, "Zmniejszenie poz. udzerzeniowego")


#================================ZAD 2 =====================================================
# Wykorzystując przestawione zależności, sprawdzić, jak gęstość rozmieszczenia elementów
# wspornikowych wpłynie na częstotliwość rezonansową podłogi oraz na zmniejszenie poziomu
# uderzeniowego ∆𝐿𝐿 danej podłogi. Proszę p
Np = 1
print("1 wspornik / m^2")
wynik_1_wsp = zm_poz(h, Beton)
Np = 5
print("5 wsporników / m^2")
wynik_5_wsp = zm_poz(h, Beton)
Np = 10
print("10 wsporników / m^2")
wynik_10_wsp = zm_poz(h, Beton)

plt.figure(figsize=(10, 6))
plt.plot(f, wynik_1_wsp, '-o', color="#1e88e5", linewidth=2.5, markersize=6, label='1 wspornik')
plt.plot(f, wynik_5_wsp, '-o', color="#951ee5", linewidth=2.5, markersize=6, label='5 wsporników')
plt.plot(f, wynik_10_wsp, '-o', color="#e51e60", linewidth=2.5, markersize=6, label='10 wsporników')
#plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
plt.xscale('log')
plt.xticks(f, f, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('dL [dB]')
plt.title('Zmniejszenie poz. dzwięków uderzeniowych w zal od ilości wsporników /m^2')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()



plt.tight_layout()
plt.show()


#=======================================ZAD 3=============================================
# Wykorzystując przestawione zależności, sprawdzić, jak sztywność zastosowanych elementów
# wpłynie na zmniejszenie poziomu uderzeniowego ∆𝐿𝐿 przez da



#dane jak w zad 1 (Np = 10)

kd = 200*pow(10,6)
print("sztywność 200MN/m^3")
wynik_s200 = zm_poz(h, Beton)
kd = 400*pow(10,6)
print("sztywność 400MN/m^3")
wynik_s400 = zm_poz(h, Beton)
kd = 600*pow(10,6)
print("sztywność 600MN/m^3")
wynik_s600 = zm_poz(h, Beton)

plt.figure(figsize=(10, 6))
plt.plot(f, wynik_s200, '-o', color="#1e88e5", linewidth=2.5, markersize=6, label='200MN/m^3')
plt.plot(f, wynik_s400, '-o', color="#951ee5", linewidth=2.5, markersize=6, label='400MN/m^3')
plt.plot(f, wynik_s600, '-o', color="#e51e60", linewidth=2.5, markersize=6, label='600MN/m^3')
#plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
plt.xscale('log')
plt.xticks(f, f, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('dL [dB]')
plt.title('Zmniejszenie poz. dzwięków uderzeniowych w zal od sztywności mat')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()



plt.tight_layout()
plt.show()

#=====================================ZAD 4=====================================================
# Wykorzystując przestawione zależności, sprawdzić, jak grubość wylewki wpłynie na
# zmniejszenie poziomu uderzeniowego ∆𝐿𝐿 danej podłogi; ℎ = 50, 80 i 120 mm. Pozostałe dane
# proszę przyjąć jak w zadaniu 1.
kd = 400*pow(10,6)


# Grubości stropu [m]
h = 50 * pow(10, -3)
print("grubość h = 50 mm")
wynik_h50 = zm_poz(h, Beton)

h = 80 * pow(10, -3)
print("grubość h = 80 mm")
wynik_h80 = zm_poz(h, Beton)

h = 120 * pow(10, -3)
print("grubość h = 120 mm")
wynik_h120 = zm_poz(h, Beton)


plt.figure(figsize=(10, 6))
plt.plot(f, wynik_h50,  '-o', color="#1e88e5", linewidth=2.5, markersize=6, label='h = 50 mm')
plt.plot(f, wynik_h80,  '-o', color="#951ee5", linewidth=2.5, markersize=6, label='h = 80 mm')
plt.plot(f, wynik_h120, '-o', color="#e51e60", linewidth=2.5, markersize=6, label='h = 120 mm')

plt.xscale('log')
plt.xticks(f, f, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('dL [dB]')
plt.title('Zmniejszenie poziomu dźwięków uderzeniowych w zależności od grubości wylewki')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()

plt.tight_layout()
plt.show()

#==========================================zad 5=====================================================
# Proszę porównać, które rozwiązanie da najlepsze efekty (najniższy znormalizowany poziom
# uderzeniowy):
# - 30 cm strop masywny
# - 16 cm strop z warstwą podłogi pływającej o specjalnej konstrukcji (jak w zadaniu 1)

    # n = 0.2 #współczynnik strat dla betonu
    # d = 2500 #[kg/m3] gęstość betonu
    # s = 1 #wsp promieniowania dla płyt skończonych pow. częstotliwości koincydencji
    # c = 343 #[m/s] #v dzwieku w powietrzu
    # cl = 3800 #[m/s] prędkość fali w betonie

#wartosci potrzebne w zm_plyw
kd = 400*pow(10,6)
s = 9 * pow(10, -4)
Np = 10
Sc = 1
h = 80*pow(10, -3)

strop_mas_30 = poz_dzw_plyta_mat(0.30, Beton)
strop_mas_16 = poz_dzw_plyta_mat(0.16, Beton)
zm_plyw = zm_poz(h, Beton)

efekt_poz_plyw = np.subtract(strop_mas_16, zm_plyw)
freqs = f
plt.figure(figsize=(10,6))

plt.plot(freqs, strop_mas_30, '-o', color="#e51e74", linewidth=2.5, markersize=6, label='mas_30')
plt.plot(freqs, efekt_poz_plyw, '-o', color="#1ee550", linewidth=2.5, markersize=6, label='16+plyw')
#plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
plt.xscale('log')
plt.xticks(freqs, freqs, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Poziom [dB]')
plt.title('Porównanie poz. dzw. ud. stropu masywnego oraz podłogi pływającej o podobnych grubościach')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

print(licz_wazony(strop_mas_30,1))
print(licz_wazony(efekt_poz_plyw,1))

del Beton
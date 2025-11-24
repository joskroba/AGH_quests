#Zad 1: wyznaczenie znormalizowanego poziomu uderzeniowego stropu std. 16 cm

import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.pyplot import cm

#ta klasa jest uywana w innym pliku (cw.3)
class Material:
    # n = 0.2 #współczynnik strat dla betonu
    # d = 2500 #[kg/m3] gęstość betonu
    # s = 1 #wsp promieniowania dla płyt skończonych pow. częstotliwości koincydencji
    # c = 343 #[m/s] #v dzwieku w powietrzu
    # cl = 3800 #[m/s] prędkość fali w betonie

    def __init__(self, gestosc:float, v_fali_mat:float,  w_strat:float, w_prom:float = 1, c:float = 343 ):
        self.gestosc = gestosc  #[kg/m3] gęstość materiału
        self.v_fali_mat = v_fali_mat  #[m/s] prędkość fali w  materiale
        self.w_strat = w_strat #współczynnik strat dla materiału
        self.w_prom = w_prom #wsp promieniowania dla płyt skończonych pow. częstotliwości koincydencji
        self.c = c #[m/s] #v dzwieku w powietrzu

    def __str__(self):
        return ("MATERIAL INFO\n"
                f"Gęstość = {self.gestosc} [kg/m^3],\n"
                f"prędkość fali = {self.v_fali_mat} [m/s]\n"
                f"wsp. strat = {self.w_strat} [-]\n"
                f"wsp. promieniowania dla płyt = {self.w_prom} [-]\n"
                f"predkość dźw. w otoczeniu = {self.c} [m/s]\n")


n = 0.02 #współczynnik strat dla betonu
d = 2500 #[kg/m3] gęstość betonu
h = 0.16 #[m] grubość stropu

f = [100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150] #[Hz] pasma tercjowe

#print(len(f), len(lw), len(lo))
s = 1 #wsp promieniowania dla płyt skończonych pow. częstotliwości koincydencji
c = 343 #[m/s] #v dzwieku w powietrzu
cl = 3800 #[m/s] prędkość fali w betonie


#fc_2 = c**2/(2*np.pi())*np.sqrt(Ms/B) # B to sztywność w zginaniu [Nm]

Beton = Material(2500, 3800, 0.2) 

#ta funkcja jest uywana w innym pliku cw3
def poz_dzw_plyta_mat(h: float, mat:Material):
    Ms = mat.gestosc*h #[kg/m2] masa powierzchniowa stropu
    fc = mat.c**2*np.sqrt(3)/(np.pi*mat.v_fali_mat*h) # [Hz] freq krytyczna - koincydencji
    wynik = []
    for fi in f:
        Ln = 10*np.log10(fc/(mat.w_strat*Ms**2)) + 10*np.log10(4*mat.w_strat*fi/(np.pi*fc)+mat.w_prom) + 82.3
        # print(fi, Ln,  "\n")
        wynik.append(Ln)
    # print(wynik)
    return wynik
wynik = poz_dzw_plyta_mat(0.16, Beton)

def plt_terc(val: np.array):
    freqs = np.array([100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150])

    plt.figure(figsize=(10, 6))
    plt.plot(freqs, val, '-o', color="#1e88e5", linewidth=2.5, markersize=6, label='L_imp')
    #plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
    plt.xscale('log')
    plt.xticks(freqs, freqs, rotation=45)
    plt.xlabel('Częstotliwość [Hz]')
    plt.ylabel('Poziom dźwięku uderzeniowego [dB]')
    plt.title('Poziomy dźwięków uderzeniowych w pasmach tercjowych – wykres liniowy')
    plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
    plt.legend()
    plt.ylim(min(val) - 5,
            max(val) + 5)
    plt.tight_layout()
    plt.show()

plt_terc(wynik)

# ===========================ZAD 2 ==================================
Ln = wynik
print(Ln)
h2_tests = [0.08, 0.12, 0.16, 0.20, 0.25, 0.30] #cm



plt.figure(figsize=(10, 6))

color = iter(plt.cm.rainbow(np.linspace(0, 1, len(h2_tests))))

for hi in h2_tests:
    wynik2 = []
    for li in Ln:
        wynik2.append(li + 30*np.log10(h/hi))
        # print(30*np.log10(h/hi))
    plt.plot(f, wynik2, '-o', color=next(color), linewidth=2.5, markersize=6, label=hi)

#plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
plt.xscale('log')
plt.xticks(f, f, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Poziom dźwięku uderzeniowego [dB]')
plt.title('Poziomy dźwięków uderzeniowych w pasmach tercjowych – wykres liniowy')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()


# =======================================Zad 3 =======================================
#Obliczenie zmniejszenia poziomu uderzeniowego warstwy wykładziny (ang. Impact
# Sound Improvment with Floor Coverings) – korka o grubości 3 cm.



def omega(f: int):
    return 2*np.pi*f

mh = 0.5 #[kg] masa młotka stukacza
#dla korka:
Edc = 0.025*pow(10,9) #[Pa] dynam. moduł younga
nt = 0.15 #wsp. strat 
hc = 0.03 #[m] grubość wykładziny(korka)
Sh = 0.0007 #[m^2]

def spadek_poz_korek(hc: float):
    f0 = np.sqrt(Sh*Edc/(mh*hc))/(2*np.pi)
    k = mh*omega(f0)**2

    wynik3 = []
    for fi in f:
        Yh = 1/(1j* omega(fi)* mh) #ruchliwość młotka
        Yc = (1j* omega(fi) )/(k*(1+1j*nt)) #ruchliwość wykładziny
        if(fi <= f0):
            wynik3.append(0)
        else:
            wynik3.append(20*np.log10(abs(Yc/Yh)))
    return wynik3
korek_3cm = spadek_poz_korek(0.03)
plt_terc(korek_3cm)




#===================================ZAD 4 ===================================
strop30 = poz_dzw_plyta_mat(0.3, Beton)
strop16 = poz_dzw_plyta_mat(0.16, Beton)
korek_1cm = spadek_poz_korek(0.01)

strop16_wykladzina_3cm = np.subtract(strop16, korek_3cm)
strop16_wykladzina_1cm = np.subtract(strop16, korek_1cm)


plt.figure(figsize=(10, 6))

color = iter(plt.cm.rainbow(np.linspace(0, 1, 4)))



plt.plot(f, strop30, '-o', color=next(color), linewidth=2, label='strop30')
plt.plot(f, strop16, '-o', color=next(color), linewidth=2, label='strop16')
plt.plot(f, strop16_wykladzina_3cm, '-o', color=next(color), linewidth=2, label='strop16 z wykladziną 3cm')
plt.plot(f, strop16_wykladzina_1cm, '-o', color=next(color), linewidth=2, label='strop16 z wykladziną 1cm')

plt.xscale('log')
plt.xticks(f, f, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Poziom dźwięku uderzeniowego [dB]')
plt.title('Poziomy dźwięków uderzeniowych w pasmach tercjowych – wykres liniowy')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()



# ============================LICZENIE WSKAŹNIKA WAŻONEGO================================
f = [100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150] #[Hz] pasma tercjowe  
lw = [67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72,72,72,72,72]
lo = [62,62,62,62,62,62,61,60,59,58,57,54,51,48,45,42]

def licz_wazony(strop: np.array, odn: np.array = None):
    if not odn:
        odn = [62,62,62,62,62,62,61,60,59,58,57,54,51,48,45,42]

    if len(strop) != len(odn):
        print("wrong array length - not third octaves")
        return -1
    
    sumator_negatywny = 0
    reduced = False
    while(sumator_negatywny < 32):
        sumator_negatywny = 0
        for s, o in zip(strop, odn):
            if(o - s < 0):
                sumator_negatywny += abs(o-s) 
                
        # print("sumator", sumator_negatywny)
        if(sumator_negatywny > 32 and not reduced):
            odn = np.add(odn,10)
            sumator_negatywny = 0
            # print("too low odn")
        else:
            odn = np.subtract(odn,1)
            reduced = True
           # print("going lower")
    odn = np.add(odn,1) #przekroczono próg, zatem krok wstecz

    plt.figure(figsize=(10, 6))
    plt.plot(f, odn)
    plt.plot(f, strop)
    plt.xscale('log')
    plt.xticks(f, f, rotation=45)
    plt.xlabel('Częstotliwość [Hz]')
    plt.ylabel('Poziom dźwięku uderzeniowego [dB]')
    plt.title('Poziomy dźwięków uderzeniowych w pasmach tercjowych – wykres liniowy')
    plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return odn[7] #return
        

print("30  ",licz_wazony(strop30, lo))
print("16  ",licz_wazony(strop16, lo))
print("16,1  ", licz_wazony(strop16_wykladzina_1cm, lo))
print("16,3  ", licz_wazony(strop16_wykladzina_3cm, lo))
del Beton

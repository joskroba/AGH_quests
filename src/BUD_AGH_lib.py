import matplotlib.pyplot as plt
import numpy as np
#dupadupadupa
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
    
def poz_dzw_plyta_mat(h: float, mat:Material):
    freqs = np.array([100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150])
    Ms = mat.gestosc*h #[kg/m2] masa powierzchniowa stropu
    fc = mat.c**2*np.sqrt(3)/(np.pi*mat.v_fali_mat*h) # [Hz] freq krytyczna - koincydencji
    wynik = []
    for fi in freqs:
        Ln = 10*np.log10(fc/(mat.w_strat*Ms**2)) + 10*np.log10(4*mat.w_strat*fi/(np.pi*fc)+mat.w_prom) + 82.3
        # print(fi, Ln,  "\n")
        wynik.append(Ln)
    # print(wynik)
    return wynik
    
def plt_terc(val: np.array, title: str):
    freqs = np.array([100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150])

    plt.figure(figsize=(10, 6))
    plt.plot(freqs, val, '-o', color="#1e88e5", linewidth=2.5, markersize=6, label='L_imp')
    #plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
    plt.xscale('log')
    plt.xticks(freqs, freqs, rotation=45)
    plt.xlabel('Częstotliwość [Hz]')
    plt.ylabel('Poziom [dB]')
    plt.title(f'{title} w pasmach tercjowych')
    plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
    plt.legend()
    plt.ylim(min(val) - 5,
            max(val) + 5)
    plt.tight_layout()
    plt.show()


# dupa = 1
# del dupa
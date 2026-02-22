import numpy as np
import matplotlib.pyplot as plt
from BUD_AGH_lib import Material , poz_dzw_plyta_mat, plt_terc, licz_wazony, omega



class Params:
    def __init__(self, a, b, h, E, u):
        self.a = a
        self.b = b
        self.h = h
        self.E = E
        self.u = u

def Vmat(E, d, u):
    return np.sqrt(E/(d*(1-u**2)))

def Analyze(mat:Material, params:Params, freq):
    Ms = mat.gestosc*params.h
    # air:
    d0 = 1.293 #[kg/m^3]
    c = 343

    k_eff = (pow(np.pi,8)*params.E*pow(params.h,3)*(pow(params.a,-2)+pow(params.b,-2))**2)/(768*(1-params.u**2))

    f_11 = np.pi*mat.v_fali_mat*params.h/(4*np.sqrt(3))*(pow(params.a,-2) + pow(params.b,-2))

    Ks = (2*omega(freq)*d0*c)/k_eff
    R_nl = 10*np.log10(1+pow(Ks,-2))
    R_low=[]
    for i, f in enumerate(freq):
        if(f < f_11):
            R_low.append((-20)*np.log10(Ks[i])-10*np.log10(R_nl[i])+(6.4))

   

    R_masy = 10*np.log10(1+(np.pi*freq*Ms)/(d0*c)) - 5
    
    fc = c**2*np.sqrt(3)/(np.pi*mat.v_fali_mat*params.h)
    Rn = 10*np.log10(1+(np.pi*Ms*fc/(d0*c))**2)
    R_hi = Rn + 10*np.log10(mat.w_strat)+ 33.22*np.log10(freq/fc) -5.7

    combo = []
    for i, f in enumerate(freq):
        if(f < f_11):
            combo.append(R_low[i])
        elif(f < fc):
            combo.append(R_masy[i])
        else:
            combo.append(R_hi[i])


    return{'R_lo': R_low, 'f_11': f_11, 'R_mid': R_masy, 'f_c': fc, 'R_hi': R_hi, 'combo': combo }

#--------------------------------------------
Beton = Material(2400, 3800, 0.02)

f = np.array([100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150]) #[Hz] pasma tercjowe

# d0 = 1293 #[kg/m^3]
# c = 343

defPar = Params(1,1,0.16, 29* pow(10, 9), 0.2)
#--------------zad 1-------------------------

a1 = Analyze(Beton,defPar, f)
# print(Beton)
# print(f"Częstotliwość rzeonansowa modu 1.1 = {a1['f_11']}")
# print(a1['R_mid'])


plt.figure(figsize=(8,5))
plt.axvline(a1['f_11'], c='purple')
plt.axvline(a1['f_c'], c = 'red')
plt.plot(f, a1['R_mid'], '-o', linewidth=2.5, markersize=6, label='L_imp')
plt.xscale('log')
# plt.xticks(freqs, freqs, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Poziom [dB]')
# plt.title(f'{title} w pasmach tercjowych')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
# if(min(val) & max(val) & min(val) != float("-inf") & max(val) != float("inf") ):
    # plt.ylim(min(val) - 5,
    #         max(val) + 5)
plt.tight_layout()
# plt.show()
plt.savefig("/Users/janek/Documents/AGH/DZW_BUD/cwp4/wykresy/1.png")

print("zad1 vals  ", a1['R_mid'])

# plt_terc(a1['combo'], "izol. dzw. pow. 16cm beton", None)

print(f"zad1 f11:{a1['f_11']}, fc:{a1['f_c']}")


#--------------zad 2-------------------------

grubosci = np.arange(0.08, 0.31, 0.02)
grubosci = grubosci.round(decimals=2)


colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(grubosci))))
plt.figure(figsize=(10, 6))
for g in grubosci:
    defPar.h = g
    a2 = Analyze(Beton, defPar, f)
    c = next(colors)
    plt.plot(f, a2['R_mid'], '-o', color=c, linewidth=2.5, markersize=6, label=f"{g}")
    # plt.axvline(f0, color=c)
    # plt.axvline(a2["f_11"], color=c)
plt.xscale('log')
plt.xticks(f, f, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Poziom dźwięku uderzeniowego [dB]')
plt.title('Zmiana grubości stropu')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
# plt.show()
plt.savefig("/Users/janek/Documents/AGH/DZW_BUD/cwp4/wykresy/2.png")

##--------------zad 3-------------------------
drewno = Material(640, Vmat(13.4* pow(10, 9), 640, 0.15), 0.02)
drzwi = Params(1, 1.7, 0.04, 13.4* pow(10, 9), 0.15)

# f = np.array([63, 250, 1000])
f = np.array([100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150]) #[Hz] pasma tercjowe

a3 = Analyze(drewno, drzwi, f )

plt.figure(figsize=(8,4))
plt.plot(f, a3['combo'], '-o', linewidth=2.5, markersize=6)
plt.xscale('log')
plt.axvline(a3['f_11'], c='purple')
plt.axvline(a3['f_c'], c = 'red')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.xticks(f,f, rotation=45)

# plt.show()
plt.savefig("/Users/janek/Documents/AGH/DZW_BUD/cwp4/wykresy/3.png")

print(f"zad3 f11:{a3['f_11']}, fc:{a3['f_c']}")

print("zad3 vals  ", a3['combo'])

##--------------zad 4-------------------------

GK = Material(900, Vmat(15 * pow(10, 9), 900, 0.2), 0.02)
plyta = Params(10, 5, 0.013, 15*pow(10,9), 0.2)

freqs = np.arange(1, 10001, 1)
a4 = Analyze(GK, plyta, freqs)

plt.figure(figsize=(8,4))
plt.plot(freqs, a4['combo'], '-', linewidth=2.5, markersize=6)
plt.xscale('log')
plt.axvline(a4['f_11'], c='purple')
plt.axvline(a4['f_c'], c = 'red')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
# plt.show()
plt.savefig("/Users/janek/Documents/AGH/DZW_BUD/cwp4/wykresy/4.png")

print(f"zad4 f11:{a4['f_11']}, fc:{a4['f_c']}")

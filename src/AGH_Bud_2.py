import numpy as np
import matplotlib.pyplot as plt
from BUD_AGH_lib import omega, plt_terc

# =============================================
# WZORY Z INSTRUKCJI (1) - (11) - dosłownie
# =============================================

# (1)
def delta_L_from_velocities(v2b, v2c):
    """Zmniejszenie poziomu uderzeniowego z prędkości [dB]"""
    return 20 * np.log10(v2b / v2c)

# (5) - przybliżenie podstawowe (najczęściej używane)
def delta_L_approx(Z1, Zd):
    """ΔL ≈ 20 log |Z1 / Zd|"""
    return 20 * np.log10(np.abs(Z1 / Zd))

# (6)
def Z1(fi, Ms1):
    """Impedancja warstwy podłogi (masowa)"""
    return 1j * omega(fi) * Ms1


# (7) - moduł impedancji warstwy sprężystej
def Zd_mod(fi, fd, rho_m, c_m, d):
    if fi <= fd:
        return (rho_m * c_m**2) / (omega(fi)*d)
    else:   
        return rho_m * c_m 


# (8)
def f_d(c_m, d):
    """Częstotliwość odcięcia warstwy sprężystej [Hz]"""
    return c_m / (2 * np.pi * d)



# (9) i (10) – końcowe wzory na ΔL w dwóch zakresach
def delta_L(f, Ms1, Ms2, rho_m, c_m, d, kd):
    """Główne wzory (9) i (10)"""

    fd = f_d(c_m, d)
    f0 = f_0(kd, Ms1, Ms2)
    wynik = []

    for fi in f:
        if (fi < f0):
            wynik.append(0)
        else:
            wynik.append(delta_L_approx(Z1(fi, Ms1),Zd_mod(fi, fd, rho_m, c_m, d)))
    return wynik, f0, fd

# (11)
def f_0(kd, Ms1, Ms2):
    """Częstotliwość rezonansowa układu [Hz]"""
    return 1 / (2 * np.pi) * np.sqrt( kd * (1/Ms1 + 1/Ms2) )

from BUD_AGH_lib import waz_spadek




# =============================================
# STAŁE Z ZADANIA
# =============================================

rho_beton = 2400          # kg/m³
D_strop   = 0.160         # m
Ms2       = rho_beton * D_strop   # masa powierzchniowa stropu ≈ 384 kg/m²

rho_m = 160               # kg/m³ warstwy sprężystej
kd    = 12  *pow(10,6)              # N/m³  → 12 MN/m³
E_dyn = 0.4 *pow(10,6)             # N/m² → ρ_m * c_m² = 0.4 MN/m²
c_m   = np.sqrt(E_dyn / rho_m)   # ≈ 50 m/s

# W_sprez = Material(rho_m, c_m, 0.02)

f_terc = np.array([100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150]) #[Hz] pasma tercjowe


###zad----------------
###SPR róne grubości warstwy spręystej
d_spr_tests = np.round(np.linspace(0.01, 0.1, 4),3) #cm
#wylewka:
dp = 0.050    
Ms1 = rho_beton * dp

plt.figure(figsize=(10, 6))

colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(d_spr_tests))))
tab = []
for di in d_spr_tests:
    dL, f0, fd = delta_L(f_terc, Ms1, Ms2, rho_m, c_m, di, kd)
    c = next(colors)
    plt.plot(f_terc, dL, '-o', color=c, linewidth=2.5, markersize=6, label=f"{di}, dLw = {waz_spadek(dL)}")
    plt.axvline(f0, color="black")
    plt.axvline(fd, color=c)
    # tab.append(wynik2)
    ###############################2026
    print("zmienne d spr.\n",
          f"rezonans: {f0}\n",
          f"odcoiecia: {fd}\n",
          f"dla grubosci: {di}\n",
          "===================")

#plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
plt.xscale('log')
plt.xticks(f_terc, f_terc, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Zmniejszenie poziomu dźwięku uderzeniowego [dB]')
plt.title('Zmiana grubości warstwy spręzystej - zmniejszenie poz. dzw. uderz. w pasmach tercjowych')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig("/Users/janek/Documents/AGH/DZW_BUD/cwp2/wykresy/1_sprez.png")



d  = 0.1
###SPR róne grubości warstwy podłogi pływ.
d_pod_tests = np.round(np.linspace(0.05, 0.12, 3),3) #cm

plt.figure(figsize=(10, 6))

colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(d_spr_tests))))
tab = []
for dpi in d_pod_tests:
    Msi = rho_beton*dpi
    dL, f0, fd = delta_L(f_terc, Msi, Ms2, rho_m, c_m, d, kd)
    c=next(colors)
    plt.plot(f_terc, dL, '-o', color=c, linewidth=2.5, markersize=6, label=f"{dpi}, dLw = {waz_spadek(dL)}")
    # plt.axvline(f0, color=c)
    plt.axvline(fd, color=c)

    # tab.append(wynik2)
    #############################2026
    print("zmienne d wylewki\n",
        f"rezonans: {f0}\n",
        f"f. odcoiecia: {fd}\n",
        f"dla grubosci: {dpi}\n",
        "===================")

#plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
plt.xscale('log')
plt.xticks(f_terc, f_terc, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Zmniejszenie poziomu dźwięku uderzeniowego [dB]')
plt.title('Zmiana grubości warstwy podłogi - zmniejszenie poz. dzw. uderz. w pasmach tercjowych')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig("/Users/janek/Documents/AGH/DZW_BUD/cwp2/wykresy/2_strop.png")


##############single case2026

# rho_beton = 2400          # kg/m³
# D_strop   = 0.160         # m
# Ms2       = rho_beton * D_strop   # masa powierzchniowa stropu ≈ 384 kg/m²

# rho_m = 160               # kg/m³ warstwy sprężystej
# kd    = 12  *pow(10,6)              # N/m³  → 12 MN/m³
# E_dyn = 0.4 *pow(10,6)             # N/m² → ρ_m * c_m² = 0.4 MN/m²
# c_m   = np.sqrt(E_dyn / rho_m)   # ≈ 50 m/s


d_wylewki = 0.1 
d_spr = 0.06
Ms1 = rho_beton * d_wylewki

dL, f0, fd = delta_L(f_terc, Ms1, Ms2, rho_m, c_m, d_spr, kd)
for i, dLi in enumerate(dL):
    print(f"{f_terc[i]}Hz --- {round(dLi,1)} dB" )
print("+ + + + + + + + + + + + ")
print(f"rezonans: {f0}\n",
    f"odciecia: {fd}\n",
    f"dla grubosci: {dpi}\n",
    "===================")


fig = plt.figure(figsize=(10, 6))
txt = (f"g. wylewki: {d_wylewki*100}cm, g. w. spr.: {d_spr*100}cm, f0={round(f0, 1)}Hz, fodc={round(fd,1)}Hz ")
plt.figtext(0.5, 0.01, txt, ha ="center")
plt.title("single case")
plt.semilogx(f_terc, dL, '-o', color=c, linewidth=2.5, markersize=6, label=f"dLw = {waz_spadek(dL)}")
plt.legend()
plt.grid()
plt.xticks(f_terc, f_terc, rotation=45)
plt.axvline(fd, color=c)
plt.show()
plt.tight_layout()

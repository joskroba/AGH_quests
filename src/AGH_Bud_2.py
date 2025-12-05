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
    return wynik

# (11)
def f_0(kd, Ms1, Ms2):
    """Częstotliwość rezonansowa układu [Hz]"""
    return 1 / (2 * np.pi * np.sqrt( kd * (1/Ms1 + 1/Ms2) ))

from BUD_AGH_lib import licz_wazony

def waz_spadek(dL):
    strop_odn = [67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72,72,72,72,72]
    dd_L = np.subtract(strop_odn, dL)
    lw = licz_wazony(dd_L)
    return 78-lw


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



d  = 0.040    # przykład: 40 mm warstwy sprężystej
dp = 0.050    # przykład: 60 mm jastrychu
Ms1 = rho_beton * dp

###zad----------------
###SPR róne grubości warstwy spręystej
d_spr_tests = np.round(np.linspace(0.01, 0.1, 4),3) #cm
dp = 0.050    # przykład: 60 mm jastrychu
Ms1 = rho_beton * dp

plt.figure(figsize=(10, 6))

color = iter(plt.cm.rainbow(np.linspace(0, 1, len(d_spr_tests))))
tab = []
for di in d_spr_tests:
    dL = delta_L(f_terc, Ms1, Ms2, rho_m, c_m, di, kd)
    plt.plot(f_terc, dL, '-o', color=next(color), linewidth=2.5, markersize=6, label=f"{di}, dLw = {waz_spadek(dL)}")
    # tab.append(wynik2)

#plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
plt.xscale('log')
plt.xticks(f_terc, f_terc, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Poziom dźwięku uderzeniowego [dB]')
plt.title('Poziomy dźwięków uderzeniowych w pasmach tercjowych')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()



d  = 0.1
###SPR róne grubości warstwy podłogi pływ.
d_pod_tests = np.round(np.linspace(0.05, 0.12, 3),3) #cm

plt.figure(figsize=(10, 6))

color = iter(plt.cm.rainbow(np.linspace(0, 1, len(d_spr_tests))))
tab = []
for dpi in d_pod_tests:
    Msi = rho_beton*dpi
    dL = delta_L(f_terc, Msi, Ms2, rho_m, c_m, d, kd)
    plt.plot(f_terc, dL, '-o', color=next(color), linewidth=2.5, markersize=6, label=f"{dpi}, dLw = {waz_spadek(dL)}")
    # tab.append(wynik2)

#plt.plot(freqs, reference, '--', color="#d62728", linewidth=2, label='Odniesienie')
plt.xscale('log')
plt.xticks(f_terc, f_terc, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Poziom dźwięku uderzeniowego [dB]')
plt.title('Poziomy dźwięków uderzeniowych w pasmach tercjowych')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()



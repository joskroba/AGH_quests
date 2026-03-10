import numpy as np
import matplotlib.pyplot as plt

def omega(f):
    return 2*np.pi*f

def DB(rho0, c0, opor, f):
    X = rho0*f/opor
    
    Zc = rho0*c0 * (1 + 0.0571 * pow(X, -0.754) - (1j*0.087 * pow(X,-0.732)))
    Kc = (omega(f)/c0) * (1 + 0.0978 * pow(X,-0.700) - 1j*0.189 * pow(X, -0.595))
    return Zc, Kc

def Miki(rho0, c0, opor, f):
    Zc = rho0*c0*(1 + 0.07*pow(f/opor,-0.632) - 1j*0.107*pow(f/opor,-0.632))
    Kc = omega(f)/c0 * (1 + 0.109 * pow(f/opor, -0.618) - 1j*0.160*pow(f/opor, -0.618))
    return Zc, Kc

def SurfaceImp0(Zmat, Kmat, d):
    #dla pustki powietrznej Zmat = rho0*c0, Kmat = k0 = omega(f)/c0 (mat = powietrze) 
    Zpow = -1j*Zmat*pow(np.tan(Kmat*d), -1)
    return Zpow

def SurfaceImpNext(Zmat, Kmat, d, prev):
    Zpow = (-1j*prev*Zmat*pow(np.tan(Kmat*d), -1) + Zmat**2)/(prev - 1j*Zmat*pow(np.tan(Kmat*d), -1))
    return Zpow

def R(Zpow, rho0, c0, phi):
    z0 = rho0*c0
    R = (Zpow/z0 * np.cos(phi) - 1) / (Zpow/z0 * np.cos(phi) + 1)
    return R

def alfa(R):
    return 1 - pow(np.abs(R), 2)


### consts:

_rho0 = 1.21 #[kg/m3]
_freqs = np.arange(50, 1601, 2) 
_c0 = 343 #[m/s]

################----ZADANIA----#####################


#zad1

_opor_welna = 20000  #[Pa/m2]
_d1 = 0.05           #[m]
_phi0 = 0

DB_Z, DB_K = DB(_rho0, _c0, _opor_welna, _freqs)
Miki_Z, Miki_K = Miki(_rho0, _c0, _opor_welna, _freqs)

DB_imp_pow = SurfaceImp0(DB_Z, DB_K, _d1)
Miki_imp_pow = SurfaceImp0(Miki_Z, Miki_K, _d1)

poch_DB = alfa(R(DB_imp_pow, _rho0, _c0, _phi0))
poch_Miki = alfa(R(Miki_imp_pow, _rho0, _c0, _phi0))

# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
# ax1.set_title("Zc")
# ax1.plot(freqs,DB_Z, label="DB")

# ax2.set_title("Kc")
# ax2.plot(freqs,DB_K, label="DB")

# ax3.set_title("Surf")
# ax3.plot(freqs,DB_imp_pow, label = "DB")

# plt.show()

plt.figure(figsize = (10, 6))
plt.title("porównanie DB - Miki")
plt.plot(_freqs, poch_DB, label = "DB")
plt.plot(_freqs, poch_Miki, label = "Miki")
plt.legend()
# plt.xticks(np.array([63.5, 125, 250, 500, 1000]))
plt.grid()
plt.show()

print(isinstance(poch_DB, np.ndarray))

#################### ZADANIE 2 ############################################


import pandas as pd
from scipy.optimize import minimize_scalar

_d_prob = 0.05

df = pd.read_excel('src/material50mm_edited.xlsx')
alfa_pomiar= df['Real Part'].to_numpy()



def alfa_miki(rho0, c0, opor, d, phi, f):
    Miki_Z, Miki_K = Miki(rho0, c0, opor, f)
    Miki_imp_pow = SurfaceImp0(Miki_Z, Miki_K, d)
    poch_Miki = alfa(R(Miki_imp_pow, rho0, c0, phi))
    return poch_Miki


def alfa_miki_forminim(opor_mat):
    return alfa_miki(_rho0, _c0, opor_mat, _d_prob, _phi0, _freqs)


def funkcja_bledu(opor_param, alfa_pomiar):
    r = np.mean((alfa_pomiar - alfa_miki_forminim(opor_param) )**2)
    return r

# print(f"QUICK DEBUG\n\n"
#       f"len model{len(alfa_miki_forminim(_opor_welna))}\n"
#       f"len pomiar{len(alfa_pomiar)}\n"
#       f"len freqs{len(_freqs)}\n\n\n")

# # print (_freqs)

# ##### WIELKIE ODKRYCIE - pomiar jest od 0 Hz, nasz model od 50.
# ## w takim razie, skoro model uwaamy za skuteczny od 50 Hz - obetnę pomiar i będę
# #  liczył dopasowanie od 50Hz w górę. 
# #  obcięcia dokonałem ręcznie w pliku .xlsx - nieelegancko - nalezy zostawic
#    nazwe kolumny w pierwszym wierszu, usunac wiersze o indeksach ,<0-48>  


wynik = minimize_scalar(funkcja_bledu, args=(alfa_pomiar))

print(f"Optymalny parametr: {wynik.x:.4f}")
print(f"Minimalny błąd: {wynik.fun:.4f}")

plt.figure(figsize = (10, 6))
plt.title(f"{wynik.x:.3f}")
plt.plot(_freqs, alfa_pomiar)
plt.plot(_freqs, alfa_miki_forminim(wynik.x))
# plt.xticks(np.array([63.5, 125, 250, 500, 1000]))
plt.grid()
plt.show()

#################### ZADANIE 3 ##########################

_opor_lab = round(wynik.x, 3)  # 31170.998
_d3 = 0.05
_rho0 = 1.21 #[kg/m3]
_freqs = np.arange(50, 1601, 2) 
_c0 = 343 #[m/s]
_phi=0
Z0 = _rho0 * _c0
K0 = omega(_freqs)/_c0

#uzyty zostanie model miki tak jak w zad 2

#Aby Zmienić model naley podmienic nazwe funkcji Miki() na DB()

# S - W
Zw, Kw = Miki(_rho0, _c0, _opor_lab, _freqs)
s_w = SurfaceImp0(Miki_Z, Miki_K, _d3)
poch_s_w = alfa(R(s_w, _rho0, _c0, _phi0))

# S - P - W
Zw, Kw = Miki(_rho0, _c0, _opor_lab, _freqs)
s_p = SurfaceImp0(Z0, K0, _d3)
s_p_w = SurfaceImpNext(Zw, Kw, _d3, s_p)
poch_s_p_w = alfa(R(s_p_w, _rho0, _c0, _phi0))

# S - P - P - W
Zw, Kw = Miki(_rho0, _c0, _opor_lab, _freqs)
s_p_p = SurfaceImp0(Z0, K0, 2*_d3)
s_p_p_w = SurfaceImpNext(Zw, Kw, _d3, s_p_p)
poch_s_p_p_w = alfa(R(s_p_p_w, _rho0, _c0, _phi0))


# S - W - W
Zw, Kw = Miki(_rho0, _c0, _opor_lab, _freqs)
s_w_w = SurfaceImp0(Miki_Z, Miki_K, 2*_d3)
poch_s_w_w = alfa(R(s_w_w, _rho0, _c0, _phi0))


plt.figure(figsize = (10, 6))
plt.title(f"Porównanie ułozenia warstw")
plt.plot(_freqs, poch_s_w, label = "s-w")
plt.plot(_freqs, poch_s_p_w, label = "s-p-w")
plt.plot(_freqs, poch_s_p_p_w, label = "s-p-p-w")
plt.plot(_freqs, poch_s_w_w, label = "s-w-w")
plt.legend()
plt.grid()
plt.show()

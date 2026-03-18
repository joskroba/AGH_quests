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




def alfa_miki(rho0, c0, opor, d, phi, f):
    Miki_Z, Miki_K = Miki(rho0, c0, opor, f)
    Miki_imp_pow = SurfaceImp0(Miki_Z, Miki_K, d)
    poch_Miki = alfa(R(Miki_imp_pow, rho0, c0, phi))
    return poch_Miki

def alfa_miki_forminim(opor_mat, d_prob, phi0):
    return alfa_miki(_rho0, _c0, opor_mat, d_prob, phi0, _freqs)

def funkcja_bledu(opor_param, alfa_pomiar):
    r = np.mean((alfa_pomiar - alfa_miki_forminim(opor_param) )**2)
    return r


#################################### NEW DEFSS

def Paris_alfa(Zpow, rho0, c0):
    res = 90
    range = np.pi/2
    step = range/res
    phi = np.linspace(0,range, res)
    

    integral = 0.0
    for p in phi:
        integral = integral + (alfa(R(Zpow, rho0, c0, p))*np.sin(2*p)*step)
    return integral



_opor_lab = 31170.998
_d3 = 0.05
_rho0 = 1.21 #[kg/m3]
_freqs = np.arange(50, 6401, 2) 

_c0 = 343 #[m/s]
_phi=0
Z0 = _rho0 * _c0
K0 = omega(_freqs)/_c0

#uzyty zostanie model miki tak jak w zad 2

#Aby Zmienić model naley podmienic nazwe funkcji Miki() na DB()

# S - W
Zw, Kw = Miki(_rho0, _c0, _opor_lab, _freqs)
s_w = SurfaceImp0(Zw, Kw, _d3)
poch_s_w = alfa(R(s_w, _rho0, _c0, _phi))

# S - P - W
Zw, Kw = Miki(_rho0, _c0, _opor_lab, _freqs)
s_p = SurfaceImp0(Z0, K0, _d3)
s_p_w = SurfaceImpNext(Zw, Kw, _d3, s_p)
poch_s_p_w = alfa(R(s_p_w, _rho0, _c0, _phi))

# S - P - P - W
Zw, Kw = Miki(_rho0, _c0, _opor_lab, _freqs)
s_p_p = SurfaceImp0(Z0, K0, 2*_d3)
s_p_p_w = SurfaceImpNext(Zw, Kw, _d3, s_p_p)
poch_s_p_p_w = alfa(R(s_p_p_w, _rho0, _c0, _phi))


# S - W - W
Zw, Kw = Miki(_rho0, _c0, _opor_lab, _freqs)
s_w_w = SurfaceImp0(Zw, Kw, 2*_d3)
poch_s_w_w = alfa(R(s_w_w, _rho0, _c0, _phi))


plt.figure(figsize = (10, 6))
plt.title(f"Porównanie ułozenia warstw")
plt.plot(_freqs, poch_s_w, label = "s-w")
plt.plot(_freqs, poch_s_p_w, label = "s-p-w")
plt.plot(_freqs, poch_s_p_p_w, label = "s-p-p-w")
plt.plot(_freqs, poch_s_w_w, label = "s-w-w")
plt.ylim(0,1)
plt.legend()
plt.grid()
plt.show()



################################################ ZAD 2
# S - W
paris_s_w = Paris_alfa(s_w, _rho0, _c0)

# S - P - W
paris_s_p_w = Paris_alfa(s_p_w, _rho0, _c0)

# S - P - P - W
paris_s_p_p_w = Paris_alfa(s_p_p_w, _rho0, _c0)

# S - W - W
paris_s_w_w = Paris_alfa(s_w_w, _rho0, _c0)

plt.figure(figsize = (10, 6))
plt.title(f"Porównanie ułozenia warstw w polu rozproszonym (PARIS)")
plt.plot(_freqs, paris_s_w, label = "s-w")
plt.plot(_freqs, paris_s_p_w, label = "s-p-w")
plt.plot(_freqs, paris_s_p_p_w, label = "s-p-p-w")
plt.plot(_freqs, paris_s_w_w, label = "s-w-w")
plt.ylim(0,1)
plt.legend()
plt.grid()
plt.show()


######################  TABELKA MADNESS #######################

import pandas as pd


# 1. Import macierzy liczb rzeczywistych (ke)
# Zakładamy, że to pojedyncza kolumna lub prosta macierz
ke_df = pd.read_csv('src/ke.csv', header=None)
ke = ke_df.values.flatten()  # Konwersja na jednowymiarową tablicę numpy

# 2. Import macierzy liczb zespolonych (ZFT)
# Wymaga zamiany 'i' na 'j' przed konwersją na typ zespolony
zft_df = pd.read_csv('src/ZFT.csv', header=None, dtype=str)

# Funkcja konwertująca format MATLAB 'i' na Python 'j'
zft = zft_df.applymap(lambda x: complex(str(x).replace('i', 'j'))).values

# Teraz możesz używać ke i zft w scipy, np.:
# from scipy import signal
# result = signal.lfilter(zft[0], [1], some_data)

print(f"Załadowano ke: {ke.shape}")
print(f"Załadowano ZFT: {zft.shape}")

print( isinstance(ke, np.ndarray))
print( isinstance(zft, np.ndarray))


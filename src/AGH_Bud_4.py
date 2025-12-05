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


Beton = Material(2400, 3800, 0.02)

f = np.array([100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150]) #[Hz] pasma tercjowe

d0 = 1293 #[kg/m^3]
c = 343

def Vmat(E, d, u):
    return np.sqrt(E/(d*(1-u**2)))


def Analyze(mat:Material, params:Params):
    Ms = mat.gestosc*params.h
    R_masy = 10*np.log10(1+(np.pi*f*Ms)/(d0*c)) - 5

    k_eff = (pow(np.pi,8)*params.E*pow(params.h,3)(pow(params.a,-2)+pow(params.b,-2))**2)/(768*(1-params.u**2))

    Ks = (2*omega(f)*d0*c)/k_eff

    R_nl = 10*np.log10(1+pow(Ks,-2))
    R_low = -20*np.log10*Ks-10*np.log10(R_nl)+6,4


    fc = c**2*np.sqrt(3)/(np.pi*mat.v_fali_mat*params.h)
    Rn = 10*np.log10(1+(np.pi*Ms*fc/(d0*c))**2)
    R_hi = Rn(fc) + 10*np.log10*params.u + 33.22*np.log10(f/fc) -5.7

    f_11 = np.pi*mat.v_fali_mat*params.h/(4*np.sqrt(3))*(pow(params.a,-2) + pow(params.b,-2))


#--------------zad 1-------------------------
wyniki1 = []
Ms = 0.16*2400
for fi in f:
    R_masy = 10*np.log10(1+(np.pi*fi*Ms)/(d0*c)) - 5
    wyniki1.append(R_masy)

plt_terc(wyniki1, "izol. dzw. pow. 16cm beton")

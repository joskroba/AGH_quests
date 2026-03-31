import numpy as np
import matplotlib.pyplot as plt

def simple_plot(f, x, lab):
    plt.figure(figsize = (10, 6))
    plt.title(f"simple plot")
    plt.semilogx(f, x, label = lab)
    # plt.plot(_freqs, poch_s_p_w, label = "s-p-w")
    # plt.plot(_freqs, poch_s_p_p_w, label = "s-p-p-w")
    # plt.plot(_freqs, poch_s_w_w, label = "s-w-w")
    plt.ylim(0,1)
    plt.legend()
    plt.grid()
    plt.show()

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


######################### LABY PERFOROWANE

def SurfaceImpPerf(rm_opor, f, m_air, prev_imp):
    z3 = rm_opor + 1j*omega(f)*m_air + prev_imp 
    return z3

def air_part_eps(D, a):
    return np.pi*a**2/(D**2)

def opor_perf(rho0, eps, lep_v, g, a, f):
    rm = (rho0/eps) * np.sqrt(8 * lep_v * omega(f)) * (1+g/(2*a))
    return rm

def air_mass(rho0, eps, lep_v, g, a, f):
    m = (rho0/eps) * (g + 2*delta_round(eps)*a + np.sqrt( (8*lep_v/omega(f)) * (1+g/(2*a)) ) )
    return m

def delta_round(eps):
    d = 0.8*(1 - eps*1.4)
    return d

def alfa_avg(alfa_vec):
    return np.mean(alfa_vec)

def D_from_eps(eps, a):
    D = np.sqrt(np.pi*a**2/eps)
    return D

##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

######################### ZADANIA

#ZAD 1

_a = 0.0025 #[m]
_eps = 0.15
_g = 0.0125 #[m]
_D_sciana = 0.1 #[m]
_freqs = np.arange(100,5001,2)

_rho0 = 1.21 #[kg/m3] 
_c0 = 343 #[m/s]
_phi = 0
_lep_v = 1.84*pow(10,-5)
Z0 = _rho0 * _c0
K0 = omega(_freqs)/_c0

rm = opor_perf(_rho0, _eps, _lep_v, _g, _a, _freqs)
airmass = air_mass(_rho0, _eps, _lep_v, _g, _a, _freqs)
imp_z_perf = SurfaceImpPerf(rm, _freqs, airmass, SurfaceImp0(Z0, K0, _D_sciana))
wsp_odb = R(imp_z_perf, _rho0, _c0, _phi)
alfa1 = alfa(wsp_odb)

simple_plot(_freqs, alfa1, "just perf")


##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################


#ZAD 2


_opor_welna = 5000
_d_warstwa = 0.05 #[m]
Zc, Kc = Miki(_rho0, _c0, _opor_welna, _freqs)

#S - P - W - Perf
imp_air = SurfaceImp0(Z0, K0, _d_warstwa)
imp_wool = SurfaceImpNext(Zc, Kc, _d_warstwa, imp_air)
imp_total =  SurfaceImpPerf(rm, _freqs, airmass, imp_wool)

R_total = R(imp_total, _rho0, _c0, _phi)
alfa2 = alfa(R_total)

print(f"zad2, alfa avg ukladu = {alfa_avg(alfa2)}")
# simple_plot(_freqs, alfa2, "S-P-W-perf")
########################################################################
#S - P - W - Perf
imp_wool = SurfaceImp0(Zc, Kc, _d_warstwa)
imp_air = SurfaceImpNext(Z0, K0, _d_warstwa, imp_wool)
imp_total =  SurfaceImpPerf(rm, _freqs, airmass, imp_air)

R_total = R(imp_total, _rho0, _c0, _phi)
alfa22 = alfa(R_total)

print(f"zad2, alfa avg ukladu = {alfa_avg(alfa2)}")
# simple_plot(_freqs, alfa2, "S-P-W-perf")

plt.figure(figsize = (10, 6))
plt.title(f"porównanie kolejności ułozenia warstw")
plt.semilogx(_freqs, alfa2, label = "s-p-w-perf")
plt.semilogx(_freqs, alfa22, label = "s-w-p-perf")
plt.ylim(0,1)
plt.legend()
plt.grid()
plt.show()

##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################


#ZAD 3  - S-P-W-perf
#alfa(a)
a_var = np.arange(2, 20.2, 0.5) * 0.001 / 2 #[m], a - promień, zakres 2-20 jest dla średnic
ans_a = []
_D = D_from_eps(_eps, _a)
print(f"d = {_D}")
for a in a_var :
    eps = air_part_eps(_D, a)
    rm = opor_perf(_rho0, eps, _lep_v, _g, a, _freqs)
    airmass = air_mass(_rho0, eps, _lep_v, _g, a, _freqs)

    imp_air = SurfaceImp0(Z0, K0, _d_warstwa)
    imp_wool = SurfaceImpNext(Zc, Kc, _d_warstwa, imp_air)
    imp_total =  SurfaceImpPerf(rm, _freqs, airmass, imp_wool)

    R_total = R(imp_total, _rho0, _c0, _phi)
    alfa_vec = alfa(R_total)
    ans_a.append(alfa_avg(alfa_vec))

ans_a2 = []
#_D = D_from_eps(_eps, _a)
for a in a_var :
 #   eps = air_part_eps(_D, a)
    rm = opor_perf(_rho0, _eps, _lep_v, _g, a, _freqs)
    airmass = air_mass(_rho0, _eps, _lep_v, _g, a, _freqs)

    imp_air = SurfaceImp0(Z0, K0, _d_warstwa)
    imp_wool = SurfaceImpNext(Zc, Kc, _d_warstwa, imp_air)
    imp_total =  SurfaceImpPerf(rm, _freqs, airmass, imp_wool)

    R_total = R(imp_total, _rho0, _c0, _phi)
    alfa_vec = alfa(R_total)
    # print(D_from_eps(_eps, a))
    ans_a2.append(alfa_avg(alfa_vec))
    
#simple_plot(a_var, ans_a, "a_var")


#alfa(eps)
eps_var = np.arange(1, 60.2, 0.5) * 0.01 #[%]
ans_eps = []
for eps in eps_var :
    rm = opor_perf(_rho0, eps, _lep_v, _g, _a, _freqs)
    airmass = air_mass(_rho0, eps, _lep_v, _g, _a, _freqs)

    imp_air = SurfaceImp0(Z0, K0, _d_warstwa)
    imp_wool = SurfaceImpNext(Zc, Kc, _d_warstwa, imp_air)
    imp_total =  SurfaceImpPerf(rm, _freqs, airmass, imp_wool)


    R_total = R(imp_total, _rho0, _c0, _phi)
    alfa_vec = alfa(R_total)
    ans_eps.append(alfa_avg(alfa_vec))

#alfa(opor_welna)
reso = 100
opor_var = np.linspace(2000,60000,reso) #[%]
ans_opor = []

rm = opor_perf(_rho0, _eps, _lep_v, _g, _a, _freqs)
airmass = air_mass(_rho0, _eps, _lep_v, _g, _a, _freqs)
for opor in opor_var :
   
    Zc, Kc = Miki(_rho0, _c0, opor, _freqs)

    imp_air = SurfaceImp0(Z0, K0, _d_warstwa)
    imp_wool = SurfaceImpNext(Zc, Kc, _d_warstwa, imp_air)
    imp_total =  SurfaceImpPerf(rm, _freqs, airmass, imp_wool)

    R_total = R(imp_total, _rho0, _c0, _phi)
    alfa_vec = alfa(R_total)
    ans_opor.append(alfa_avg(alfa_vec))


fig, (ax1, ax11, ax2, ax3) = plt.subplots(4, 1, figsize=(12, 8))
plt.title(f"simple plot")

ax1.plot(a_var, ans_a)
ax1.set_title("promien a, eps = eps(a)")
ax1.grid(True)
ax1.vlines(_D/2, 0, 1)

ax11.plot(a_var, ans_a2)
ax11.set_title("promien a, eps = 15%")
ax11.grid(True)

ax2.plot(eps_var, ans_eps)
ax2.set_title("u. pow. epsilon")
ax2.grid(True)

ax3.plot(opor_var, ans_opor)
ax3.set_title("opor. wełny")
ax3.grid(True)
fig.suptitle("S-P-W-Perf")
# plt.ylim(0,1)
plt.legend()
plt.tight_layout()

plt.show()


# z instrukcji nie jest jasne co robić z epsilonem przy liczeniu średniego alfa w zal od a.
# w przypadku uzmienniania eps(a), zakres wartości 2a (2-20) jest niedobry, D = 11.4 < 20, otwory nachodzą na siebie..
# moment D = 2a zaznaczono na wykresie pionową linią.

# tu zastanawiam się jak interpretować otrzymane wykresy.
# stałe eps sprawia, ze badamy proporcjonalne skalowanie panelu - czyli zmiejszamy udział
# strat termowiskotycznych 
# ?(czy juz dla podanego zakresu)
# 
# uzmiennione eps natomiast zmienia proporcje geometrii panelu, zwiększa odsłonięcie materiału porowatego, 
# stąd tłumienie rośnie az do wartości ok. 0.8 czyli wartości odpowiednich dla odkrytej wełny mineralnej



##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################


# zad4 #######################################################################################

fc_tercje = np.array([100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 
                      1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000])


def to_thirds(x):
    alfa_tercje = []
    for fc in fc_tercje:
        fd = fc * (2 ** (-1/6))
        fg = fc * (2 ** (1/6))
        
        mask = (_freqs >= fd) & (_freqs <= fg)
   
        alfa_avg = np.mean(x[mask])
        alfa_tercje.append(alfa_avg)

    return np.array(alfa_tercje)

plt.figure(figsize = (10, 6))
plt.title(f"porównanie kolejności ułozenia warstw tercjowo")
plt.semilogx(fc_tercje, to_thirds(alfa2),"-o", label = "s-p-w-perf")
plt.semilogx(fc_tercje, to_thirds(alfa22),"-o", label = "s-w-p-perf")
plt.ylim(0,1)
plt.xticks(fc_tercje, fc_tercje, rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()




import numpy as np
import matplotlib.pyplot as plt
# from BUD_AGH_lib import Material , poz_dzw_plyta_mat, plt_terc, licz_wazony, waz_spadek

#chłonnośc na podstawie objętości i czasu pogłosu pom., default 0.5 (instrukcja)
def chlonnoscA(V, T = 0.5):
    return 0.16 * (V/T)

#ta funkcja realizuje wzór (1) z pdf projekt-wstęp
def izol_zewn_ra2(Lzew, Lwew_odn, S, A):
    return Lzew - Lwew_odn - 10* np.log10(S/A) + 3


# def izol_agg(Lzew, Lwew_odn, S, V, T, l_scian):
#     a = chlonnoscA(V, T)
#     izol = izol_zewn_ra2(Lzew, Lwew_odn, S, a)
    
    

#####-----POKOJ_001--------############################################
h = 3.2 #[m]
T = 0.5 #[s]
L_zewn = 70 #dBA
L_wewn = 32 #dBA

V = 13.42 * h
S_scian_zewn = (5.0+6.7)*h
a = chlonnoscA(V,T)

R_a2_zelbet = izol_zewn_ra2(L_zewn, L_wewn, S_scian_zewn, a)
### poniewaz są okna + są 2 przegrody zewnn, dodajemy 10db do przegród zelbet. zaraz doliczymy okna
R_a2_zelbet = R_a2_zelbet + 10
#print(R_a2_zelbet)

#----izol okien-----

S_okien = 2*1.8*1.95
R_a2_okna = izol_zewn_ra2(L_zewn, L_wewn, S_okien, a)
print("\n\n\n")
print(f"POKOJ BIUROWY 001:\n\
      Wymagania PN-B-02151-3_2015-10P, TAB 7, p 9.1 (s.38): Laeq_zewn = 40dB dla pom. biurowych\n\
izolacyjność przegrody pełnej: {R_a2_zelbet}\n\
izolacyjność przeszklenia: {R_a2_okna}")
#########################################################################

#####--------GRUBOŚĆ PRZEGRODY PEŁNEJ POK 001--------###

rho_beton = 2400
masa_pow = np.pow(10,(R_a2_zelbet + 29.6)/30.9)
S_beton = S_scian_zewn - S_okien
grubosc_beton = masa_pow/rho_beton
print(f"GRUBOSC PRZEGRODY PELNEJ ZEWN. : {np.round(grubosc_beton, 2)} [m]")
print('#######')
########################################################

###---ściana 001 na korytarz
dlugosc_sciany = 3.47 + 6.5 - 4.89
# print(dlugosc_sciany)
wild_guess = 0.10                                                   ######<------check check
ms = rho_beton * wild_guess
R_a1r = 30.9*np.log10(ms) - 26.1
#print(R_a1r)                                #####<-- roboczy print do zgadywaniaa

#poprawka przen. bocz: (STG)
Ka = 1                                                              #####<-------check check
R_a1 = R_a1r - Ka
print(f"Izolacyjność przegr. wewn bez drzwi:  {np.round(R_a1, 2)}, grubość: {wild_guess} [m]  === Wymaganie 40dB OK")
print("Izolacyjnosć drzwi wprost z tabeli = 30dB")


################################################

#####---sciana 001 do 002(DYR) DO ROZMOW POUFNYCH
#3.41.03 R_a1 = 63 dB # ! uwaga wariant 2x100mm wełny
R_a1 = 63
R_a1r = R_a1 - 2 # ~~60
Ka = 9 # strona 117 zalacznik cz. II.3 
R_a1r_prim = R_a1r - Ka #wczesniej nie było potrzeby nazywania zmiennej z primem, zbyt dluga nazwa
#poprawka przen. bocz: (STG)
print(f"Izolacyjność przegr. wewn systemowej 001/002:  {np.round(R_a1r_prim, 2)} dBA, wymaganie 50 - TAB 5., VIII.3.1 (s.26)")
print("proponowany system: 3.41.03, wariant 2x100mm ")


###Dla tego pokoju zostało tylko policzyć grubość betonowej wesnętrznej z lab 2 
# --- komment z 12.01:  ???? ju jest napisana grubość 0.1 wiec nie wiem o co tu chodziło
                        ##coś gadaliśmy z Matim Gajewskim ze lepiej zgadywać niz wyliczac ale nie pamietam dokladnie

###TODO jeszcze trzeba dla 001 policzyc przegrode zewn. bez okien. berdzie inna grubosc. nie dodajemy poprawki na okno.

print("\n\n--- KONIEC POKOJU 001---\n\n")


############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################

#####-----POKOJ_002--------############################################
h = 3.2 #[m]
T = 0.5 #[s]
L_zewn = 70 #dBA
L_wewn = 35 #dBA

V = 13.42 * h
S_scian_zewn = 3.15*h
a = chlonnoscA(V,T)

R_a2_zelbet = izol_zewn_ra2(L_zewn, L_wewn, S_scian_zewn, a)
### poniewaz są okna + są 2 przegrody zewnn, dodajemy 10db do przegród zelbet. zaraz doliczymy okna
R_a2_zelbet = R_a2_zelbet + 10
#print(R_a2_zelbet)

#----izol okien-----

S_okien = 1.8*1.95
R_a2_okna = izol_zewn_ra2(L_zewn, L_wewn, S_okien, a)
print("\n\n\n")
print(f"POKOJ DYR 002:\n\
      Wymagania PN-B-02151-3_2015-10P, TAB 7, p 9.1 (s.38): Laeq_zewn = 35dB dla pom. biurowych\n\
izolacyjność przegrody pełnej: {R_a2_zelbet}\n\
izolacyjność przeszklenia: {R_a2_okna}")
#########################################################################

#####--------GRUBOŚĆ PRZEGRODY PEŁNEJ POK 001--------###

rho_beton = 2400
masa_pow = np.pow(10,(R_a2_zelbet + 29.6)/30.9)
S_beton = S_scian_zewn - S_okien
grubosc_beton = masa_pow/rho_beton
print(f"GRUBOSC PRZEGRODY PELNEJ ZEWN. : {np.round(grubosc_beton, 2)} [m]")
print('#######')
########################################################

###---ściana 001 na korytarz
dlugosc_sciany = 3.15
# print(dlugosc_sciany)
wild_guess = 0.14                                                   ######<------check check
ms = rho_beton * wild_guess
R_a1r = 30.9*np.log10(ms) - 26.1
print(R_a1r)                                #####<-- roboczy print do zgadywaniaa

#poprawka przen. bocz: (STG)
Ka = 1                                                              #####<-------check check
R_a1 = R_a1r - Ka
print(f"Izolacyjność przegr. wewn bez drzwi:  {np.round(R_a1, 2)}, grubość: {wild_guess} [m]  === Wymaganie 50dB OK")
print("Izolacyjnosć drzwi wprost z tabeli = 40dB")


################################################

#####---sciana 002 do 003(DYR) DO ROZMOW POUFNYCH
#3.41.03 R_a1 = 63 dB # ! uwaga wariant 2x100mm wełny
R_a1 = 63
R_a1r = R_a1 - 2 # ~~60
Ka = 9 # strona 117 zalacznik cz. II.3 
R_a1r_prim = R_a1r - Ka #wczesniej nie było potrzeby nazywania zmiennej z primem, zbyt dluga nazwa
#poprawka przen. bocz: (STG)
print(f"Izolacyjność przegr. wewn systemowej 001/002:  {np.round(R_a1r_prim, 2)} dBA, wymaganie 50 - TAB 5., VIII.3.1 (s.26)")
print("proponowany system: 3.41.03, wariant 2x100mm ")


###Dla tego pokoju zostało tylko policzyć grubość betonowej wesnętrznej z lab 2 
# --- komment z 12.01:  ???? ju jest napisana grubość 0.1 wiec nie wiem o co tu chodziło
                        ##coś gadaliśmy z Matim Gajewskim ze lepiej zgadywać niz wyliczac ale nie pamietam dokladnie

###TODO jeszcze trzeba dla 001 policzyc przegrode zewn. bez okien. berdzie inna grubosc. nie dodajemy poprawki na okno.

print("\n\n--- KONIEC POKOJU DYR 002---\n\n")


############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################



#####-----POKOJ_005--------############################################
h = 3.2 #[m]
T = 0.5 #[s]
L_zewn = 70 #dBA
L_wewn = 32 #dBA

V = 27.54 * h
S_scian_zewn = (5.0+5.35)*h
a = chlonnoscA(V,T)

R_a2_zelbet = izol_zewn_ra2(L_zewn, L_wewn, S_scian_zewn, a)
### poniewaz są okna + są 2 przegrody zewnn, dodajemy 10db do przegród zelbet. zaraz doliczymy okna
R_a2_zelbet = R_a2_zelbet + 10
#print(R_a2_zelbet)

#----izol okien-----

S_okien = 2*1.8*1.95
R_a2_okna = izol_zewn_ra2(L_zewn, L_wewn, S_okien, a)
print("\n\n\n")
print(f"SALA KONFERENCYJNA 005:\n\
      Wymagania PN-B-02151-3_2015-10P:  32dB dla pom. do pracy koncepcyjnej\n\
izolacyjność przegrody pełnej: {R_a2_zelbet}\n\
izolacyjność przeszklenia: {R_a2_okna}")
#########################################################################

#####--------GRUBOŚĆ PRZEGRODY PEŁNEJ POK 005--------###

rho_beton = 2400
masa_pow = np.pow(10,(R_a2_zelbet + 29.6)/30.9)  ##hardcoded omninumerki inyzniera boga, jest dobrze
S_beton = S_scian_zewn - S_okien
grubosc_beton = masa_pow/rho_beton
print(f"GRUBOSC PRZEGRODY PELNEJ ZEWN. : {np.round(grubosc_beton, 2)} [m]")
print('#######')
########################################################

#####--------ŚCIANA 005 NA KORYTARZ--------###
dlugosc_sciany = 6.3
# print(dlugosc_sciany)
wild_guess = 0.12                                                   ######<------check check
ms = rho_beton * wild_guess
R_a1r = 30.9*np.log10(ms) - 26.1
#print(R_a1r)                                #####<-- roboczy print do zgadywaniaa

#poprawka przen. bocz: (STG)
Ka = 1                                                              #####<-------check check
R_a1 = R_a1r - Ka
print(f"Izolacyjność przegr. wewn bez drzwi:  {np.round(R_a1, 2)}, grubość: {wild_guess} [m]  === Wymaganie 48dB OK")
print("Izolacyjnosć drzwi wprost z tabeli = 35dB")


################################################

#####---sciana 005 do 004 KONFERENCYJNA
# #3.40.03 AKU
R_a1 = 54
R_a1r = R_a1 - 2 
Ka = 3 # strona 117 zalacznik cz. II.3 
R_a1r_prim = R_a1r - Ka #wczesniej nie było potrzeby nazywania zmiennej z primem, zbyt dluga nazwa
#poprawka przen. bocz: (STG)
print(f"Izolacyjność przegr. wewn systemowej 001/002:  {np.round(R_a1r_prim, 2)} dBA, wymaganie 48dB do konf.")
print("proponowany system: 3.40.03 ")


###Dla tego pokoju zostało tylko policzyć grubość betonowej wesnętrznej z lab 2 
# --- komment z 12.01:  ???? ju jest napisana grubość 0.1 wiec nie wiem o co tu chodziło
                        ##coś gadaliśmy z Matim Gajewskim ze lepiej zgadywać niz wyliczac ale nie pamietam dokladnie

###TODO jeszcze trzeba dla 001 policzyc przegrode zewn. bez okien. berdzie inna grubosc. nie dodajemy poprawki na okno.

print("\n\n--- KONIEC KONF 005---\n\n")


############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################


#####-----POKOJE 003 | 004--------############################################
h = 3.2 #[m]
T = 0.5 #[s]
L_zewn = 70 #dBA
L_wewn = 40 #dBA

s_avg = (26.81 + 27.84)/2
V = s_avg * h        #pokoje 3 i 4 są niemal identyczne, dla oszczędzenia ilości obliczeń uśredniono powierzchnię
S_scian_zewn = 5.35*h
a = chlonnoscA(V,T)

R_a2_zelbet = izol_zewn_ra2(L_zewn, L_wewn, S_scian_zewn, a)
### poniewaz są okna + są 2 przegrody zewnn, dodajemy 10db do przegród zelbet. zaraz doliczymy okna - ??? nie mogę znaleźc jakie znaczenie ma to, e są dwie przegrody a nie jedna
R_a2_zelbet = R_a2_zelbet + 10
#print(R_a2_zelbet)

#----izol okien-----

S_okien = 2*1.8*1.95
R_a2_okna = izol_zewn_ra2(L_zewn, L_wewn, S_okien, a)
print("\n\n\n")
print(f"SALA BIUROWA 003 (004):\n\
      Wymagania PN-B-02151-3_2015-10P:  40dB dla pom. biurowegp\n\
izolacyjność przegrody pełnej: {R_a2_zelbet}\n\
izolacyjność przeszklenia: {R_a2_okna}")
#########################################################################

#####--------GRUBOŚĆ PRZEGRODY PEŁNEJ POK 003/4--------###

rho_beton = 2400
masa_pow = np.pow(10,(R_a2_zelbet + 29.6)/30.9)  ##hardcoded omninumerki inyzniera boga, jest dobrze
S_beton = S_scian_zewn - S_okien
grubosc_beton = masa_pow/rho_beton
print(f"GRUBOSC PRZEGRODY PELNEJ ZEWN. : {np.round(grubosc_beton, 2)} [m]")
print('#######')
########################################################

#####--------ŚCIANA 003/4 NA KORYTARZ--------###
dlugosc_sciany = 5.35
# print(dlugosc_sciany)
wild_guess = 0.07                                                   ######<------check check
ms = rho_beton * wild_guess
R_a1r = 30.9*np.log10(ms) - 26.1
#print(R_a1r)                                #####<-- roboczy print do zgadywaniaa

#poprawka przen. bocz: (STG)
Ka = 1                                                              #####<-------check check
R_a1 = R_a1r - Ka
print(f"Izolacyjność przegr. wewn bez drzwi:  {np.round(R_a1, 2)}, grubość: {wild_guess} [m]  === Wymaganie 40dB OK")
print("Izolacyjnosć drzwi wprost z tabeli = 30dB")


################################################

#####---sciana 003 do 004
# #3.40.03 AKU
R_a1 = 42
R_a1r = R_a1 - 2 
Ka = 0 # strona 117 zalacznik cz. II.3 
R_a1r_prim = R_a1r - Ka #wczesniej nie było potrzeby nazywania zmiennej z primem, zbyt dluga nazwa
#poprawka przen. bocz: (STG)
print(f"Izolacyjność przegr. wewn systemowej 001/002:  {np.round(R_a1r_prim, 2)} dBA, wymaganie 40dB.")
print("proponowany system: 3.40.01 15mm ")


###Dla tego pokoju zostało tylko policzyć grubość betonowej wesnętrznej z lab 2 
# --- komment z 12.01:  ???? ju jest napisana grubość 0.1 wiec nie wiem o co tu chodziło
                        ##coś gadaliśmy z Matim Gajewskim ze lepiej zgadywać niz wyliczac ale nie pamietam dokladnie

###TODO jeszcze trzeba dla 001 policzyc przegrode zewn. bez okien. berdzie inna grubosc. nie dodajemy poprawki na okno.

print("\n\n--- KONIEC pok 003 004---\n\n")











print('\n\n\n---------STROP---------\n\n')

#strop wymaganie dzw. uderzeniowe - 60dB

#ponizszy kod z lab.1
class Material:
    # n = 0.02 #współczynnik strat dla betonu
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

Beton = Material(2500, 3800, 0.02) 

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

def omega(f: int):
    return 2*np.pi*f

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

    # plt.figure(figsize=(10, 6))
    # plt.plot(f, odn)
    # plt.plot(f, strop)
    # plt.xscale('log')
    # plt.xticks(f, f, rotation=45)
    # plt.xlabel('Częstotliwość [Hz]')
    # plt.ylabel('Poziom dźwięku uderzeniowego [dB]')
    # plt.title('Poziomy dźwięków uderzeniowych w pasmach tercjowych')
    # plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
    # plt.legend()
    # plt.tight_layout()
    # plt.show()

    return odn[7] #return

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

f = [100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150] #[Hz] pasma tercjowe  
lw = [67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72,72,72,72,72]
lo = [62,62,62,62,62,62,61,60,59,58,57,54,51,48,45,42]

mh = 0.5 #[kg] masa młotka stukacza
#dla korka:
Edc = 0.025*pow(10,9) #[Pa] dynam. moduł younga
nt = 0.15 #wsp. strat 
hc = 0.03 #[m] grubość wykładziny(korka)
Sh = 0.0007 #[m^2]


strop16 = poz_dzw_plyta_mat(0.16, Beton)
korek_3cm = spadek_poz_korek(0.03)
strop16_wykladzina_3cm = np.subtract(strop16, korek_3cm)

print("L n,w")
print("16 beton, 3 korek  ", licz_wazony(strop16_wykladzina_3cm, lo))

plt.figure(figsize=(10, 6))

color = iter(plt.cm.rainbow(np.linspace(0, 1, 4)))
plt.plot(f, strop16_wykladzina_3cm, '-o', color=next(color), linewidth=2, label='strop16 z wykladziną 3cm')

plt.xscale('log')
plt.xticks(f, f, rotation=45)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Poziom dźwięku uderzeniowego [dB]')
plt.title('[zad 4] Poziomy dźwięków uderzeniowych w pasmach tercjowych')
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()








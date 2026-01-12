
import numpy as np
import matplotlib.pyplot as plt
from BUD_AGH_lib import Material , poz_dzw_plyta_mat, plt_terc, licz_wazony, waz_spadek

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
L_wewn = 40 #dBA

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

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

#strop od powietrznych - 50dB
#strop ogólnie - 60dB




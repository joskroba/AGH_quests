import numpy as np
import matplotlib.pyplot as plt

# Interfejs: [X,W] = mydft(x,sr,k) :
# Argumenty wejściowe
# x - sygnał próbkowany z szybkością sr (liczba próbek na sekundę)
# sr - szybkość próbkowania (liczba próbek na sekudę)
# k - opcjonalny argument zawierający wektor prążkow dla którego będzie obliczona transformata, zgodnie ze wzorem 
# Argumenty wyjściowe:
# X - obliczona transformata
# W - macierz transformacji

_N = 41 #dft sample rate
_n = np.arange(0, _N, 1) # indeks czasowy
_k = np.arange(0, _N/2, 1) #indeks częstotliwościowy
print(round(_N/2, 0))
# _k = np.arange

def dft(x, sr, k):

    return


def mydft(x, sr, k):
    N = _N #dft sample rate



    X = []
    # W = [][]
    # return X, W


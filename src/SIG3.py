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

def dft(x, sr, k = None):
    N = len(x)
    k = np.arange(N)
    n = np.arange(N)
    
    K, N_idx = np.meshgrid(k, n, indexing='ij')
    # print(K)
    # print(N_idx)
    
    W = np.exp(-2j * np.pi * K * N_idx / N)

    # print(W)
    return np.dot(W, x)


def mydft(x, sr, k):
    N = _N #dft sample rate



    X = []
    # W = [][]
    # return X, W



x = np.array([1,0,1,0])
sr = 4

mod = np.abs(dft(x, 4))
print()
print()

plt.figure(figsize=(8,10))
plt.plot([1,2,3,4], mod)
plt.show()
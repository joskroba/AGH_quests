import time
import numpy as np
import matplotlib.pyplot as plt
import random

M = 30#            % ile razy powinna zostac wywolana funkcja dla tych samych danych wejściowych (do usrednienia wyniku)
N = np.arange(100, 501, 100)
random.seed(time.time())
tElapsed = np.array(M,len(N))
for n in N:
    for m in M:
        x = random.rand(n)
        start_time = time.time()
        np.fft(N(n))#   % Funkcja której czas wykonanie jest mierzony
        tElapsed[m,n] = time.time() - start_time
    print(f"{N}, czas: %3.3f +/- %3.3f ms\n', N(n) {mean(tElapsed(:,n))*1000}, {std(tElapsed(:,n))*1000})
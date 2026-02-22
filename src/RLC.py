import numpy as np
import matplotlib.pyplot as plt

R = 10 #[ohm] [r?]
L = 260 * pow(10, -6) #[H]
C = 150 * pow(10, -9) #[F]
E = 5 #[V]

f_r = 1/(2*np.pi*np.sqrt(L*C))
print("1:" , f_r)
######################
E = 3.5 #V
X_l = 1j*2*np.pi*f_r*L
X_c = -(1j)/(2*np.pi*f_r*C)
Z = R +  (1j*X_l) + (1j*X_c) # chyba błąd w instrukcji - plus nie minus
I = E/Z 
print 
# print(1j * X_c)

print("2: ","X_l: ", X_l, "X_c: ", X_c, "Z:", Z, "I: ", I)

U_l = I*X_l
U_c = I*X_c
U_r = I*R

print("3: ", U_l, U_c, U_r )

def Z_abs(f):
    return np.sqrt(R**2 + pow(2*np.pi*f*L - 1/(2*np.pi*f*C), 2))

ts = 30000
sr = 1
freq = np.linspace(1,ts*sr+1, sr*ts)
plt.figure(figsize = (8, 4))
plt.plot(freq, Z_abs(freq))
plt.axvline(f_r)
plt.show() #hmmm?
import numpy as np
import matplotlib.pyplot as plt

k1 = 5 #[N/m]
k2 = 8 #[N/m]
m = 10 #[kg]

kz1 = 2*k1 
w1 = np.sqrt(kz1/m)

kz2 = 2*k2 
w2 = np.sqrt(kz2/m)

start_x=(-0.1, 0)
start_y=(-0.2, 0)
def x_t(t, start_x):
    return start_x[0]*np.cos(w2*t) + start_x[1]*np.sin(w2*t)

def y_t(t, start_y):
    return start_y[0]*np.cos(w1*t) + start_y[1]*np.sin(w1*t)



n_s = 20
ticks_per_sec = 20
time = np.linspace(0,n_s,n_s*ticks_per_sec)

plt.figure(figsize=(10,10))
plt.plot(x_t(time, start_x),y_t(time, start_y))
plt.plot(0, 0, 'k+', markersize=15, label='Mid') 
plt.plot(start_x[0], start_y[0], 'x', markersize=15, label='start') 
plt.xlabel(' X [m]')
plt.ylabel(' Y [m]')
plt.show()

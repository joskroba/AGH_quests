import numpy as np
import matplotlib.pyplot as plt

k1 = 5 #[N/m]
k2 = 70 #[N/m]
m = 20 #[kg]
c = 1.5 #[kg/s]

kz1 = 2*k1 
w1 = np.sqrt(kz1/m)

kz2 = 2*k2 
w2 = np.sqrt(kz2/m)


start_x=(-0.1, 0)
start_y=(-0.2, 0)
def xy_t(t, start, w):
    return start[0]*np.cos(w*t) + start[1]*np.sin(w*t)

def v_xy(t, start, w):
    A = np.sqrt(start[0]**2 + start[1]**2)
    return A * w *np.sin(w*t)




n_s = 20
ticks_per_sec = 20
time = np.linspace(0,n_s,n_s*ticks_per_sec)

plt.figure(figsize=(8,8))
plt.plot(xy_t(time, start_x, w2),xy_t(time, start_y, w1))
plt.plot(0, 0, 'k+', markersize=15, label='Mid') 
plt.plot(start_x[0], start_y[0], 'x', markersize=15, label='start') 
plt.xlabel(' X [m]')
plt.ylabel(' Y [m]')
plt.axis('equal')
plt.suptitle(f"ky: {k1}N/m, kx: {k2}N/m, m: {m}kg, pos: {start_x[0]}m,{start_y[0]}m, v: {start_x[1]},{start_y[1]}m/s")
plt.show()

def e_kin(t, start, w):
    return m*pow(v_xy(t,start,w),2)/2

def e_pot(t, start, w):
    return w**2*m*pow(xy_t(t,start,w),2)/2

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
ax1.set_title("X")
ax1.plot(time,e_pot(time, start_y, w1), label="e_pot")
ax1.plot(time,e_kin(time, start_y, w1), label="e_kin")
ax1.plot(time,e_pot(time, start_y, w1)+e_kin(time, start_y, w1), label="e_tot")

ax2.set_title("Y")
ax2.plot(time,e_pot(time, start_x, w2), label="e_pot")
ax2.plot(time,e_kin(time, start_x, w2), label="e_kin")
ax2.plot(time,e_pot(time, start_x, w2)+e_kin(time, start_x, w2), label="e_tot")

ax3.set_title("SUM")
ax3.plot(time,e_pot(time, start_y, w1)+e_pot(time, start_x, w2), label="e_pot")
ax3.plot(time,e_kin(time, start_y, w1)+e_kin(time, start_x, w2), label="e_kin")
ax3.plot(time,e_pot(time, start_y, w1)+e_kin(time, start_y, w1)+e_pot(time, start_x, w2)+e_kin(time, start_x, w2), label="e_tot")

plt.tight_layout() 
plt.legend(loc="lower center")
plt.show()
# plt.savefig("energies.png")
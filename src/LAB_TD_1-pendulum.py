import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sp
from scipy.signal import find_peaks

n_s = 20
ticks_per_sec = 20
t_span = (0, n_s)
time = np.linspace(0,n_s,n_s*ticks_per_sec)

# A = 0.2
phi = np.pi/3
g=9.81
r = 1
w = np.sqrt(g/r)
def wychylenie_upr(t):
     return phi*np.cos(w*t)


def model_lin(t, y, g, r, beta, u_t):
     phi, omega = y
     dphi_dt = omega
     domega_dt = -(g/r) * phi - beta*omega - u_t*np.sign(omega)
     return [dphi_dt,domega_dt]

def model_nonlin(t, y, g, r, beta, u_t):
     phi, omega = y
     dphi_dt = omega
     domega_dt = -(g/r) * np.sin(phi) - beta*omega - u_t*np.sign(omega)
     return [dphi_dt,domega_dt]


start = (phi, 0)
beta = 0
u_t = 0
sol_lin = sp.solve_ivp(model_lin, t_span, start, args=(g, r, beta, u_t), t_eval=time)
sol_nonlin = sp.solve_ivp(model_nonlin, t_span, start, args=(g, r, beta, u_t), t_eval=time)

err = np.sqrt(np.abs(sol_nonlin.y[0]**2 - sol_lin.y[0]**2))

plt.figure(figsize=(10, 6))


# plt.plot(time, wychylenie_upr(time), 
#          label=f'Model liniowy ($\phi$)', color='red', linewidth=2)
plt.plot(time, sol_lin.y[0], 
         label=f'Model liniowy ($\phi$)', color='green', linewidth=2)
plt.plot( time, sol_nonlin.y[0],
         label=f'Model nieliniowy ', color='blue', linewidth=2)
plt.plot( time, err,
         label=f'err', color='grey', linewidth=1)

plt.title(f'Symulacja ruchu wahadła bez tarć', fontsize=14)
plt.xlabel('Czas t [s]', fontsize=12)
plt.ylabel('Kąt wychylenia $\phi(t)$ [stopnie]', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.axhline(0, color='black', linewidth=1)
plt.tight_layout()
# plt.show()
plt.savefig("1.png")

peaks_x, _ = find_peaks(sol_nonlin.y[0])
periods = np.diff(peaks_x)
T_num = np.mean(periods/ticks_per_sec)
T_an = np.pi*2/w
print(f"period numeric equals {T_num} seconds; "\
      f"period linear equals {T_an} seconds")
print(f"err względny = {(T_num-T_an)/T_num * 100}%")
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

#TARCIEE WISKOTYCZNE



start = (phi, 0)
beta = 0.3
u_t = 0
sol_lin = sp.solve_ivp(model_lin, t_span, start, args=(g, r, beta, u_t), t_eval=time)
sol_nonlin = sp.solve_ivp(model_nonlin, t_span, start, args=(g, r, beta, u_t), t_eval=time)

def plt_obw(t):
    return phi*np.exp(-beta/2*t)


plt.figure(figsize=(10, 6))


# plt.plot(time, wychylenie_upr(time), 
#          label=f'Model liniowy ($\phi$)', color='red', linewidth=2)
plt.plot(time, sol_lin.y[0], 
         label=f'Model liniowy ($\phi$)', color='green', linewidth=2)
plt.plot( time, sol_nonlin.y[0],
         label=f'Model nieliniowy ', color='blue', linewidth=2)
plt.plot( time, plt_obw(time),
         label=f'obwiednia liniowa ', color='black',linestyle="--" , linewidth=2)


plt.title(f'Symulacja ruchu wahadła z tłumieniem wiskotycznym', fontsize=14)
plt.xlabel('Czas t [s]', fontsize=12)
plt.ylabel('Kąt wychylenia $\phi(t)$ [stopnie]', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.axhline(0, color='black', linewidth=1)
plt.tight_layout()
# plt.show()
plt.savefig("2.png")

peaks_x, _ = find_peaks(sol_nonlin.y[0])
periods = np.diff(peaks_x)
T_num = np.mean(periods/ticks_per_sec)
T_an = np.pi*2/w
print(f"period numeric equals {T_num} seconds; "\
      f"period linear equals {T_an} seconds - wiskotyczne")
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

#TARCIEE siłowe



start = (phi, 0)
beta = 0
u_t = 0.1
sol_lin = sp.solve_ivp(model_lin, t_span, start, args=(g, r, beta, u_t), t_eval=time)
sol_nonlin = sp.solve_ivp(model_nonlin, t_span, start, args=(g, r, beta, u_t), t_eval=time)

def plt_obw(t):
    return phi*np.exp(-beta/2*t)


plt.figure(figsize=(10, 6))


# plt.plot(time, wychylenie_upr(time), 
#          label=f'Model liniowy ($\phi$)', color='red', linewidth=2)
plt.plot(time, sol_lin.y[0], 
         label=f'Model liniowy ($\phi$)', color='green', linewidth=2)
plt.plot( time, sol_nonlin.y[0],
         label=f'Model nieliniowy ', color='blue', linewidth=2)
# plt.plot( time, plt_obw(time),
        #  label=f'obwiednia liniowa ', color='black',linestyle="--" , linewidth=2)


plt.title(f'Symulacja ruchu wahadła z tłumieniem tarciowym', fontsize=14)
plt.xlabel('Czas t [s]', fontsize=12)
plt.ylabel('Kąt wychylenia $\phi(t)$ [stopnie]', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.axhline(0, color='black', linewidth=1)
plt.tight_layout()
# plt.show()
plt.savefig("3.png")

peaks_x, _ = find_peaks(sol_nonlin.y[0])
periods = np.diff(peaks_x)
T_num = np.mean(periods/ticks_per_sec)
T_an = np.pi*2/w
print(f"period numeric equals {T_num} seconds; "\
      f"period linear equals {T_an} seconds - tarciowe")
print(f"wychylenie początkowe{np.degrees(phi)} stopni")


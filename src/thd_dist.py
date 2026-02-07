import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams.update({
    'font.size': 15,          # Domyślna wielkość wszystkiego
    'axes.labelsize': 17,     # Wielkość podpisów osi (np. "Częstotliwość [Hz]")
    'axes.titlesize': 24,     # Wielkość tytułu wykresu
    # 'xtick.labelsize': 12,    # Wielkość liczb na osi X
    # 'ytick.labelsize': 12,    # Wielkość liczb na osi Y
    # 'legend.fontsize': 12     # Wielkość legendy
})

df_bk = pd.read_csv("resources/amps_rew/LabAmpB_K.txt", sep="\t", comment='*', usecols=[0,1], header=None)
df_bk.columns = ['freq', 'BK-U[V]']
# df_bk.set_index('freq', inplace=True)
df_MS_34D = pd.read_csv("resources/amps_rew/HiFi_type_MS-34D.txt", sep="\t", comment='*', usecols=[0,1], header=None)
df_MS_34D.columns = ['freq', 'MS_34D-U[V]']

df_D7K = pd.read_csv("resources/amps_rew/PA_type_D7K.txt", sep="\t", comment='*', usecols=[0,1], header=None)
df_D7K.columns = ['freq', 'D7K-U[V]']

# print(df_bk.head())
# print(df_bk.shape)

temp = pd.merge(df_bk, df_D7K, how="outer", on='freq')
amps = pd.merge(temp, df_MS_34D, how='outer', on='freq')

# print(amps.describe())
# print(amps.head())
amps.set_index('freq', inplace=True)
print(amps.head())

amps_dB = 20 * np.log10(amps)
amps_dB.columns = amps_dB.columns.str.replace('-U[V]', '-dBV', regex=False)

print(amps_dB.describe(), '\n', amps_dB.head())

usable_range_mask = (amps_dB.index >= 200) & (amps_dB.index <= 8000)

for col in amps_dB.columns :
    avg = amps_dB.loc[usable_range_mask, col].mean()
    amps_dB[col] = amps_dB[col] - avg

amps_dB.head()



plt.figure(figsize=(12, 7))


trivia_mask = (amps_dB.index >= 20) & (amps_dB.index <= 20000)

for col in amps_dB.columns:
    plt.semilogx(amps_dB.index, amps_dB[col], label=col)
    print(col, f"+{amps_dB.loc[trivia_mask,col].max()}, -{amps_dB.loc[trivia_mask, col].min()}")

plt.xlabel('Frequency [Hz]')
plt.ylabel('Signal Voltage level (normalised) [dBV]')
plt.title('Aplifiers\' Frequency Response curves')
plt.ylim(-30, 10)
plt.grid(True, which="both", ls="-", alpha=0.4)
plt.legend(loc='lower left')
plt.tight_layout()

plt.savefig('resources/amps_rew/freq_resp.png', dpi=300)
# plt.show()

###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################


df_thd_bk = pd.read_csv("resources/amps_rew/THD_BK.txt", sep="\t", comment='*', usecols=[0, 2, 4], header=0)
df_thd_bk.columns = ['freq', 'BK-THD[%]', 'BK-H5[%]']

df_thd_D7K = pd.read_csv("resources/amps_rew/THD_D7K.txt", sep="\t", comment='*', usecols=[0, 2, 4], header=0)
df_thd_D7K.columns = ['freq', 'D7K-THD[%]', 'D7K-H5[%]']

df_thd_MS_34D = pd.read_csv("resources/amps_rew/THD_MS_34D.txt", sep="\t", comment='*', usecols=[0, 2, 4], header=0)
df_thd_MS_34D.columns = ['freq', 'MS_34D-THD[%]', 'MS_34D-H5[%]']


temp_thd = pd.merge(df_thd_bk, df_thd_D7K, how="outer", on='freq')
thd_final = pd.merge(temp_thd, df_thd_MS_34D, how='outer', on='freq')

thd_final.set_index('freq', inplace=True)
print(thd_final.describe(), '\n', thd_final.head())
plt.figure(figsize=(12, 7))
for col in thd_final.columns:
    if 'THD' in col:
        plt.semilogx(thd_final.index, thd_final[col], label=col)


plt.xlabel('Frequency [Hz]')
plt.ylabel('THD [%]')
plt.title('Amplifiers\' Total Harmonic Distortion ')
plt.grid(True, which="both", ls="-", alpha=0.4)
plt.xlim(20, 20000)
plt.ylim(0, 2) 
plt.legend(loc='upper right')
plt.tight_layout()

thd_mask = (thd_final.index >= 20) & (thd_final.index <= 20000)

plt.savefig('resources/amps_rew/THD.png', dpi=300)
# plt.show()
print(thd_final.loc[thd_mask, thd_final.columns.str.startswith('BK')].max())
print(thd_final.loc[thd_mask, thd_final.columns.str.startswith('MS')].max())
print(thd_final.loc[thd_mask, thd_final.columns.str.startswith('D7K')].max())

#ostatecznie niepotrzebnie liczyłem samą 5th harmonic
import librosa
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# from scipy.fft import fft, ifft, fftshift
import scipy as sp
from scipy.signal import find_peaks
from functools import partial
from scipy.signal import medfilt
from scipy.io.wavfile import write
import logging

recs = ["drut miękki standard.wav",
            "drut twardy 1-2.wav",
            "drut twardy 1-3.wav",
            "drut twardy 1-4.wav",
            "drut twardy mostek.wav",
            "drut twardy standard.wav",
            "flażolet 12 próg.wav",
            "flażolet 5 próg.wav",
            "flażolet 7 próg.wav",
            "flażolet 9 próg.wav",
            "kostka 1-2.wav",
            "kostka 1-3.wav",
            "kostka 1-4.wav",
            "kostka mostek.wav",
            "kostka standard.wav",
            "smczek umiarkowany 1-4.wav",
            "smyczek szybko standard.wav",
            "smyczek umiarkowany 1-2.wav",
            "smyczek umiarkowany 1-3.wav",
            "smyczek umiarkowany mostek.wav",
            "smyczek umiarkowany standard.wav",
            "smyczek wolno standard #2.wav",
            "smyczek wolno standard.wav",
            "struna E niskie 5 razy.wav",
            "struna E wysokie 5 razy.wav",
            "struna pusta G.wav"
            ]

def plot_fft(fft: np.array, sampling_rate) -> None:
        """
        Plot amplitude spectrum of given fft.
        """
        max_ix = int(len(fft)/2)

        ixs = np.linspace(0, sampling_rate/2, max_ix, endpoint=False)

        y = fft[:max_ix]

        plt.semilogy(ixs, y)
        
        plt.grid()
        plt.show()


def path(n):
    if n < 26 and n >=0 :
        return ("./src/guit_rec/"+recs[n])

def spath(s):
    
    return ("./src/guit_rec/"+s)
 
# y, sr = librosa.load(path(0), sr=None)
# print(sr)

for s in recs:
    y, sr = librosa.load(spath(s), sr=None)
    sd.play(y, sr)
    sd.wait()
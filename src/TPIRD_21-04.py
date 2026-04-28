import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.io import wavfile
from scipy import signal as sig

folder_path = "resources/diffuser_meas"

nbinarni_folder = sorted(Path(folder_path + "/nbinarni").iterdir())
plyta_folder = sorted(Path(folder_path + "/plyta").iterdir())
pusta_folder = sorted(Path(folder_path + "/pusta").iterdir())

print(nbinarni_folder, "xxx\n")
# nbinarni_angles 
# plyta_angles
# pusta_angles

def import_waves_from_folder_to_array(folder):
    ans_list = []
    sr_mem = None
    for file in folder:
        sr, data = wavfile.read(file)
        if (sr_mem and sr != sr_mem ):
            x = np.linspace(0, 1, 100)
            plt.plot(x, np.sin(np.exp(x)))
            plt.title(f"error inconsistent sample rate in {str(folder)}")
            plt.show()
            print("error inconsistent sample rate")
        sr_mem = sr
        ans_list.append(data)
    return sr, ans_list

# sr, nbinarni_angles = import_waves_from_folder_to_array(nbinarni_folder)
sr, plyta_angles = import_waves_from_folder_to_array(plyta_folder)
# sr, pusta_angles = import_waves_from_folder_to_array(pusta_folder)

# print(plyta_angles[0])
s = plyta_angles[0]
time = len(s)/ sr
print(time)
timewekt = np.linspace(0, time-1/sr, len(s))
# mask = 
plt.plot(timewekt, s[:,0])
plt.legend()
plt.show()


#UWAGA NIE LICZYMY RMS W PUNKCIE 5
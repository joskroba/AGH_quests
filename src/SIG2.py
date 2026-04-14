import numpy as np
import matplotlib.pyplot as plt

# print(20*np.log10(1/pow(2,15)))
# print(20*np.log10(1/pow(2,23)))


def omega(f):
    return np.pi*2*f

def mysinTbase(A, f, fs, tstart, tstop):

    if(f <= 0 or fs <= 0 or tstop <= tstart):
        print("wrong parameters")
        return -1
    
    time = tstop-tstart
    numsamp = (time)*fs
    tsam = np.linspace(tstart, tstop-1/fs, numsamp)
    # print(tsam)
    xsam = A * np.sin((omega(f))*tsam)

    fsref = f*200
    refnumsamp = (tstop-tstart)*fsref
    tref = np.linspace(tstart, tstop-1/fsref, refnumsamp)
    xref = A * np.sin((omega(f))*tref)
    return xsam, tsam ,xref, tref

def sinePlotting(xsam, tsam, xref, tref, title):
    plt.figure(figsize=(10,6))
    plt.plot(tsam, xsam,"o", label = "sampled")
    plt.plot(tref, xref,"-", label = "ref")
    plt.title(title)
    plt.legend()
    plt.show()

def sinePlotting2(xsam, tsam, xref, tref, xmanual, title):
    plt.figure(figsize=(10,6))
    plt.plot(tsam, xsam,"o", label = "sampled")
    plt.plot(tref, xref,"-", label = "ref")
    plt.plot(tref, xmanual,"-", label = "manual")
    plt.title(title)
    plt.legend()
    plt.show()

def mysinT(A, f, fs, tstart, tstop):
    xsam, tsam ,xref, tref = mysinTbase(A, f, fs, tstart, tstop)

    time = tstop-tstart
    title = f"{time*f} okresów"
    sinePlotting(xsam, tsam, xref, tref, title)
    return xsam
  

def mysinT2(A1, f1, fs, tstart, tstop, A2, f2):
    xsam, tsam, xref, tref, = mysinTbase(A1, f1, fs, tstart, tstop)
    time = tstop-tstart
    title = f"{time*f1} okresów"
    xmanual = A2 * np.sin(omega(f2)*tref)
    sinePlotting2(xsam, tsam, xref, tref, xmanual, title )
    return xsam
    



# mysinT(-2, 4, 5, 3,4)

# for i in (1,2,3,4,5):
#     mysinT(2, 20, 80 + i, 4, 5)

A1 = 2   #  % amplituda sygnalu zrodlowego
f1 = 3    # % częstotliwośc sygnalu zrodlowego w Hz
fs = 4     #% czestotliwosc probkowania w Hz
tstart = 2  #% czas rozpoczecia sygnalu w sekundach
tstop = 4  #% czas końca sygnau sygnalu w sekundach

A2 = -2
f2 = 1


# x2 = mysinT(A1, f1, fs, tstart, tstop)
x3 = mysinT2(A1, f1, fs, tstart, tstop, A2, f2)
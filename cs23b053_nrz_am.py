import matplotlib.pyplot as plt
import numpy as np

def sig(bits):
    signal = []
    time = []

    for bit in bits:
        level = 1 if bit == 1 else -1
        signal.extend([level] * 200)
        time.extend(np.linspace(0, 1, 200))

    return signal, time

bits = [1, 0, 1, 0, 1, 1, 0]
signal, time = sig(bits)
signal = np.array(signal)

print(signal[:20])

time_signal = np.linspace(0, len(bits), len(signal), endpoint=False)

plt.figure(figsize=(10, 4))
plt.subplot(3, 1, 1)
plt.plot(time_signal, signal)
plt.title("Modulating Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.savefig("nrz.png")

f = 20
tim = np.linspace(0, 7, 1400)

carrier = np.sin(2 * np.pi * f * tim)

plt.subplot(3, 1, 2)
plt.plot(tim, carrier)
plt.title("Carrier Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.savefig("carrier.png")

Ac = 1  
m = 0.5  

modulating_signal = signal[:len(tim)]  
modulating_signal = np.interp(modulating_signal, (modulating_signal.min(), modulating_signal.max()), (-1, 1))

am_signal = modulating_signal * carrier

plt.subplot(3,1,3)
plt.plot(tim, am_signal)
plt.title("Amplitude Modulated (AM) Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.savefig("am.png")

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# Paramètres du signal
fs = 1000  # Fréquence d'échantillonnage (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Temps (1 seconde, échantillonné à 1000 Hz)

# Création d'un signal avec deux fréquences
f1 = 50  # Première fréquence (Hz)
f2 = 150  # Deuxième fréquence (Hz)
A1 = 1.0  # Amplitude de la première fréquence
A2 = 0.5  # Amplitude de la deuxième fréquence

# Signal composé de deux sinusoïdes
signal = A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.sin(2 * np.pi * f2 * t)

# Ajout de bruit blanc
noise = 0.1 * np.random.normal(size=t.shape)
signal += noise

# Calcul de la DSP (avec Welch)
frequencies, psd = welch(signal, fs, nperseg=256)

# Plot du signal temporel
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal, label="Signal")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.title("Signal temporel")
plt.legend()

# Plot de la densité spectrale de puissance
plt.subplot(2, 1, 2)
plt.semilogy(frequencies, psd, label="DSP")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Densité spectrale de puissance (V²/Hz)")
plt.title("Densité spectrale de puissance (DSP)")
plt.legend()

plt.tight_layout()
plt.show()

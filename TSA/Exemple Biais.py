import numpy as np
import matplotlib.pyplot as plt

# Générer un signal
np.random.seed(42)  # Pour la reproductibilité
n = 1000
x = np.linspace(0, 10, n)

# Signal théorique (courbe réelle)
signal_theorique = np.sin(x)

# Cas 1 : Estimation biaisée avec bruit
biais = 0.2  # Ajout d'un biais constant
signal_biais = signal_theorique + biais
bruit = 0.1 * np.random.normal(size=n)
signal_estime = signal_theorique + bruit

# Calcul de la variance des résidus pour le cas 1
residus_cas1 = signal_estime - signal_theorique
variance_cas1 = np.var(residus_cas1)

# Cas 2 : Réduction du biais et du bruit
biais_reduit = 0.01  # Biais réduit
signal_biais_reduit = signal_theorique + biais_reduit
bruit_reduit = 0.02 * np.random.normal(size=n)  # Amplitude du bruit réduite
signal_estime_reduit = signal_theorique + bruit_reduit

# Calcul de la variance des résidus pour le cas 2
residus_cas2 = signal_estime_reduit - signal_theorique
variance_cas2 = np.var(residus_cas2)

# Visualisation des deux cas
plt.figure(figsize=(12, 8))

# Cas 1 : Biais initial et bruit
plt.subplot(2, 1, 1)
plt.plot(x, signal_theorique, label="Signal théorique", color="blue", linewidth=2)
plt.plot(x, signal_biais, label="Signal biaisé (Biais = 0.2)", color="red", linestyle="--", linewidth=2)
plt.plot(x, signal_estime, label="Signal estimé (Bruit)", color="green", alpha=0.6)
plt.fill_between(
    x,
    signal_theorique - np.sqrt(variance_cas1),
    signal_theorique + np.sqrt(variance_cas1),
    color="green",
    alpha=0.2,
    label="Zone de ±1 écart-type (Bruit)"
)
plt.title(f"Cas 1 : Biais élevé et bruit (Variance: {variance_cas1:.4f})")
plt.xlabel("Temps")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Cas 2 : Biais réduit et bruit réduit
plt.subplot(2, 1, 2)
plt.plot(x, signal_theorique, label="Signal théorique", color="blue", linewidth=2)
plt.plot(x, signal_biais_reduit, label="Signal biaisé réduit (Biais = 0.01)", color="orange", linestyle="--", linewidth=2)
plt.plot(x, signal_estime_reduit, label="Signal estimé (Bruit réduit)", color="green", alpha=0.8)
plt.fill_between(
    x,
    signal_theorique - np.sqrt(variance_cas2),
    signal_theorique + np.sqrt(variance_cas2),
    color="green",
    alpha=0.2,
    label="Zone de ±1 écart-type (Bruit réduit)"
)
plt.title(f"Cas 2 : Biais et bruit réduits (Variance: {variance_cas2:.4f})")
plt.xlabel("Temps")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

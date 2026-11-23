import numpy as np
import matplotlib.pyplot as plt

# 1. Daten einlesen (Spalte 3 = Zeit in s, Spalte 4 = Spannung in V)
t1, u1 = np.loadtxt("F0018CH1.CSV", delimiter=",", usecols=(3, 4), unpack=True)
t2, u2 = np.loadtxt("F0018CH2.CSV", delimiter=",", usecols=(3, 4), unpack=True)

# Zeit in ms umrechnen und um +10 ms verschieben, damit 0 ganz links liegt
t1 = t1 * 1e3 + 10.0
t2 = t2 * 1e3 + 10.0
u2 = u2 * 1e3   # CH2 in mV (CH1 bleibt in V)

# 2. Plot erstellen (CH2 links in Königsblau, CH1 rechts grau gestrichelt)
fig, ax1 = plt.subplots(figsize=(8, 4.5))
ax1.plot(t2, u2, color="royalblue", lw=1.2)

# Beschriftung der 4 Rb-Linien auf der steigenden Piezo-Flanke
peaks = [
    (9.36, -826.0, r"$^{87}\mathrm{Rb}$ a"),
    (15.20, -858.0, r"$^{85}\mathrm{Rb}$ a"),
    (22.28, -856.0, r"$^{85}\mathrm{Rb}$ b"),
    (25.04, -954.0, r"$^{87}\mathrm{Rb}$ b"),
]
for x_p, y_p, lbl in peaks:
    ax1.annotate(
        lbl,
        xy=(x_p, y_p),
        xytext=(x_p, y_p + 55),
        ha="center",
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
    )

ax1.set_xlim(0, 35)
ax1.set_ylim(-1160, -700)
ax1.set_xlabel(r"Zeit $t$ / ms")
ax1.set_ylabel(r"Photodiodenspannung $U_{\mathrm{CH2}}$ / mV", color="royalblue")
ax1.tick_params(axis="y", labelcolor="royalblue")
ax1.grid(True, ls="--", alpha=0.5)

# Zweite y-Achse für die Piezo-Dreiecksrampe (CH1)
ax2 = ax1.twinx()
ax2.plot(t1, u1, color="dimgray", lw=1.0, ls="--")
ax2.set_ylabel(r"Piezomonitor $U_{\mathrm{CH1}}$ / V", color="dimgray")
ax2.tick_params(axis="y", labelcolor="dimgray")

plt.tight_layout()
plt.savefig("1PD_spektrum_ch1_ch2.pdf")
plt.show()
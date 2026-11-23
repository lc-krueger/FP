import numpy as np
import matplotlib.pyplot as plt

# 1. Daten einlesen (Spalte 3 = Zeit in s, Spalte 4 = Spannung in V)
t, u = np.loadtxt("F0017CH2.CSV", delimiter=",", usecols=(3, 4), unpack=True)
t = t * 1e3   # Umrechnung in ms
u = u * 1e3   # Umrechnung in mV

# 2. Plot erstellen (Ausschnitt auf die steigende Flanke mit allen 4 Peaks)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(t, u, color="royalblue", lw=1.2)

# Beschriftung der 4 Rb-Linien auf der steigenden Flanke
peaks = [
    (7.04, -87.4, r"$^{87}\mathrm{Rb}$ b"),
    (9.96, -78.2, r"$^{85}\mathrm{Rb}$ b"),
    (16.36, -79.0, r"$^{85}\mathrm{Rb}$ a"),
    (22.16, -76.0, r"$^{87}\mathrm{Rb}$ a"),
]
for x_p, y_p, lbl in peaks:
    ax.annotate(
        lbl,
        xy=(x_p, y_p),
        xytext=(x_p, y_p + 5.5),
        ha="center",
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
    )

ax.set_xlim(0, 35)
ax.set_ylim(-105, -60)
ax.set_xlabel(r"Zeit $t$ / ms")
ax.set_ylabel(r"Photodiodenspannung $U$ / mV")
ax.grid(True, ls="--", alpha=0.5)

plt.tight_layout()
plt.savefig("1PD_spektrum.pdf")
plt.show()
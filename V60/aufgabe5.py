import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, u = np.loadtxt("F0019CH1.CSV", delimiter=",", usecols=(3, 4), unpack=True)
t = t * 1e3   # ms
u = u * 1e3   # mV

def four_gauss(x, c0, c1, A1, mu1, s1, A2, mu2, s2, A3, mu3, s3, A4, mu4, s4):
    bg = c0 + c1 * x
    g1 = A1 * np.exp(-0.5 * ((x - mu1) / s1) ** 2)
    g2 = A2 * np.exp(-0.5 * ((x - mu2) / s2) ** 2)
    g3 = A3 * np.exp(-0.5 * ((x - mu3) / s3) ** 2)
    g4 = A4 * np.exp(-0.5 * ((x - mu4) / s4) ** 2)
    return bg - g1 - g2 - g3 - g4

p0_t = [330.0, 0.2, 18.0, -13.4, 0.5, 52.0, -7.2, 0.5, 108.0, -0.5, 0.5, 44.0, 1.9, 0.5]
popt_t, _ = curve_fit(four_gauss, t, u, p0=p0_t, maxfev=20000)
t_peaks = np.array([popt_t[3], popt_t[6], popt_t[9], popt_t[12]])

# Gewichtete Literaturwerte nach Siddons et al. (2008), Table 1(a) in GHz (87a, 85a, 85b, 87b)
nu_lit = np.array([4.153, 1.676, -1.235, -2.399])
p_cal, cov_cal = curve_fit(lambda x, m, b: m * x + b, t_peaks, nu_lit)
m_cal, b_cal = p_cal
dm_cal, db_cal = np.sqrt(np.diag(cov_cal))
print(f"Kalibrierung: m = {m_cal:.4f} +/- {dm_cal:.4f} GHz/ms, b = {b_cal:.4f} +/- {db_cal:.4f} GHz")

nu = m_cal * t + b_cal

p0_nu = [330.0, -0.7, 46.0, -2.40, 0.22, 109.0, -1.24, 0.22, 53.0, 1.68, 0.23, 16.0, 4.15, 0.25]
popt_nu, pcov_nu = curve_fit(four_gauss, nu, u, p0=p0_nu, maxfev=20000)
perr_nu = np.sqrt(np.diag(pcov_nu))

names = ["87Rb b", "85Rb b", "85Rb a", "87Rb a"]
areas, area_errs = [], []
for i, name in enumerate(names):
    idx = 2 + 3 * i
    A, mu, s = popt_nu[idx], popt_nu[idx + 1], abs(popt_nu[idx + 2])
    dA, dmu, ds = perr_nu[idx], perr_nu[idx + 1], perr_nu[idx + 2]
    cov_As = pcov_nu[idx, idx + 2]
    area = A * s * np.sqrt(2 * np.pi)
    d_area = np.sqrt(2 * np.pi) * np.sqrt((s * dA) ** 2 + (A * ds) ** 2 + 2 * A * s * cov_As)
    areas.append(area)
    area_errs.append(d_area)
    print(f"{name}: nu0 = {mu:+.3f} +/- {dmu:.3f} GHz, A = {A:.2f} +/- {dA:.2f} mV, "
          f"FWHM = {2.3548*s*1e3:.1f} MHz, Fläche = {area:.2f} +/- {d_area:.2f} mV*GHz")

A_85 = areas[1] + areas[2]
dA_85 = np.sqrt(area_errs[1] ** 2 + area_errs[2] ** 2)
A_87 = areas[0] + areas[3]
dA_87 = np.sqrt(area_errs[0] ** 2 + area_errs[3] ** 2)
R = A_85 / A_87
dR = R * np.sqrt((dA_85 / A_85) ** 2 + (dA_87 / A_87) ** 2)
p85 = A_85 / (A_85 + A_87) * 100
p87 = A_87 / (A_85 + A_87) * 100
print(f"\nAnteil 85Rb: {p85:.2f} %, Anteil 87Rb: {p87:.2f} %")
print(f"Verhältnis 85Rb / 87Rb = {R:.3f} +/- {dR:.3f} (Literatur: 2.593)")

nu_fit = np.linspace(nu.min(), nu.max(), 1000)
u_fit = four_gauss(nu_fit, *popt_nu)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(nu, u, color="cornflowerblue", lw=1.4)
ax.plot(nu_fit, u_fit, color="crimson", lw=1.4, ls="-")

labels = [
    (popt_nu[3],  popt_nu[0] + popt_nu[1]*popt_nu[3]  - popt_nu[2],  r"$^{87}\mathrm{Rb}$ b"),
    (popt_nu[6],  popt_nu[0] + popt_nu[1]*popt_nu[6]  - popt_nu[5],  r"$^{85}\mathrm{Rb}$ b"),
    (popt_nu[9],  popt_nu[0] + popt_nu[1]*popt_nu[9]  - popt_nu[8],  r"$^{85}\mathrm{Rb}$ a"),
    (popt_nu[12], popt_nu[0] + popt_nu[1]*popt_nu[12] - popt_nu[11], r"$^{87}\mathrm{Rb}$ a"),
]
for x_p, y_p, lbl in labels:
    ax.annotate(
        lbl,
        xy=(x_p, y_p),
        xytext=(x_p, y_p - 14),
        ha="center",
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
    )

ax.set_xlim(-4.5, 5.5)
ax.set_ylim(200, 345)
ax.set_xlabel(r"Frequenzverstimmung $\Delta\nu$ / GHz")
ax.set_ylabel(r"Differenzspannung $U_{\mathrm{CH1}}$ / mV")
ax.grid(True, ls="-", alpha=0.5)

plt.tight_layout()
plt.savefig("2PD_spektrum_fit.pdf")
plt.show()
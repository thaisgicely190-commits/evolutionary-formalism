import numpy as np
import matplotlib.pyplot as plt

# --- 1. PARÂMETROS FÍSICOS ---
G = 6.67430e-11
c = 299792458
M_sun = 1.98847e30

# --- 2. INPUT DO EVENTO ---
M_bh_solar = 66  # Massa do evento (ex: GW250114)
M_total = M_bh_solar * M_sun

# --- 3. CÁLCULO DA LEI DE HIPÁTIA (AJUSTADO PARA 2*PI) ---
# Delta_t = 2 * pi * G * M / c^3
delta_t_hipatia = (2 * np.pi * G * M_total) / (c**3)

print("-" * 50)
print(f"RESULTADO DO PROTOCOLO HIPÁTIA (v2.0)")
print(f"Fórmula: 2πGM/c³")
print(f"Massa do evento: {M_bh_solar} M_sun")
print(f"Atraso do eco previsto: {delta_t_hipatia * 1000:.2f} ms")
print("-" * 50)

# --- 4. SIMULAÇÃO DO GRÁFICO ---
sample_rate = 16384
t = np.linspace(0, 0.08, int(0.08 * sample_rate))

# Criando o Ringdown e o Eco
def signal(time):
    # Ringdown principal
    s = np.exp(-150 * time) * np.cos(2 * np.pi * 250 * time)
    # Eco (Atrasado por delta_t_hipatia)
    mask = time > delta_t_hipatia
    s[mask] += 0.25 * np.exp(-150 * (time[mask] - delta_t_hipatia)) * \
               np.cos(2 * np.pi * 250 * (time[mask] - delta_t_hipatia))
    return s

sinal_com_eco = signal(t)

plt.figure(figsize=(12, 5))
plt.plot(t * 1000, sinal_com_eco, color='#1f77b4', label="Onda Gravitacional")
plt.axvline(x=delta_t_hipatia * 1000, color='red', linestyle='--', label=f"Eco Previsto: {delta_t_hipatia*1000:.2f}ms")

plt.title(f"Predição da Lei de Hipátia para M={M_bh_solar}M⊙")
plt.xlabel("Tempo (ms)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()

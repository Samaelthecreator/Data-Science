"""
Generador de datasets sintéticos — Clase 3
Análisis de Datos en Python (curso intensivo)

Cada dataset está diseñado para exhibir UN comportamiento estadístico concreto,
con la "verdad" conocida (parámetros generadores). Semilla fija => reproducible.

Ejecutar:  python3 generar_datasets.py
Genera:    dataset_A_asimetria.csv, dataset_B_outliers.csv, dataset_C_confusion.csv
"""
import numpy as np
import pandas as pd

SEED = 2024
rng = np.random.default_rng(SEED)

# ----------------------------------------------------------------------
# DATASET A — Asimetría fuerte (ingreso mensual de hogares, lognormal)
# Verdad: mediana = exp(mu) = 2500 €.  Media teórica = exp(mu + sigma^2/2).
# Objetivo didáctico: media >> mediana; elegir mediana para imputar nulos.
# ----------------------------------------------------------------------
n_A = 500
mu, sigma = np.log(2500), 0.85          # parámetros del normal subyacente
ingreso = rng.lognormal(mean=mu, sigma=sigma, size=n_A)
ingreso = np.round(ingreso, 0)

# Introducimos ~5% de nulos NO al azar del todo: más nulos en ingresos altos
# (los hogares de mayor ingreso reportan menos) -> refuerza discusión de sesgo.
prob_nulo = 0.02 + 0.10 * (ingreso > np.quantile(ingreso, 0.80))
mask_nulo = rng.random(n_A) < prob_nulo
ingreso_con_nulos = ingreso.copy()
ingreso_con_nulos[mask_nulo] = np.nan

df_A = pd.DataFrame({
    "hogar_id": np.arange(1, n_A + 1),
    "ingreso_mensual": ingreso_con_nulos,
})
df_A.to_csv("dataset_A_asimetria.csv", index=False)

media_teorica_A = np.exp(mu + sigma**2 / 2)
print("=== DATASET A — asimetría ===")
print(f"n = {n_A} | nulos = {mask_nulo.sum()} ({100*mask_nulo.mean():.1f}%)")
print(f"Mediana teórica (verdad) = 2500.0")
print(f"Media teórica  (verdad) = {media_teorica_A:.1f}")
print(f"Media observada (sin nulos)   = {np.nanmean(ingreso_con_nulos):.1f}")
print(f"Mediana observada (sin nulos) = {np.nanmedian(ingreso_con_nulos):.1f}")
print()

# ----------------------------------------------------------------------
# DATASET B — Outliers influyentes (horas de estudio vs. puntuación)
# Verdad: relación lineal fuerte y = 30 + 3.0*x + ruido, r ~ 0.8 SIN outliers.
# Se inyectan puntos de alto apalancamiento (errores de captura) que
# distorsionan media, desviación y la r de Pearson.
# ----------------------------------------------------------------------
n_B = 200
horas = rng.uniform(0, 20, size=n_B)
puntuacion = 30 + 3.0 * horas + rng.normal(0, 6, size=n_B)
puntuacion = np.clip(puntuacion, 0, 100)

df_clean = pd.DataFrame({"horas_estudio": horas, "puntuacion": puntuacion})

# 6 outliers de alto apalancamiento: muchísimas horas, puntuación baja
# (p. ej. error de digitación: se anotó 40 en vez de 4).
outliers = pd.DataFrame({
    "horas_estudio": [40, 42, 38, 45, 41, 39],
    "puntuacion":    [22, 18, 25, 15, 20, 24],
})
df_B = pd.concat([df_clean, outliers], ignore_index=True)
df_B.insert(0, "estudiante_id", np.arange(1, len(df_B) + 1))
df_B.to_csv("dataset_B_outliers.csv", index=False)

r_sin = np.corrcoef(df_clean["horas_estudio"], df_clean["puntuacion"])[0, 1]
r_con = np.corrcoef(df_B["horas_estudio"], df_B["puntuacion"])[0, 1]
print("=== DATASET B — outliers ===")
print(f"n = {len(df_B)} (200 limpios + 6 outliers)")
print(f"Pendiente verdadera = 3.0")
print(f"r de Pearson SIN outliers = {r_sin:.3f}")
print(f"r de Pearson CON outliers = {r_con:.3f}  <- se degrada")
print()

# ----------------------------------------------------------------------
# DATASET C — Correlación espuria por confusión (temperatura)
# Confundidor Z = temperatura. X = ventas_helados, Y = ahogamientos.
# Ambos dependen de la temperatura; NO hay relación causal directa X->Y.
# Verdad: corr(X,Y) alta, pero correlación PARCIAL dado Z ~ 0.
# ----------------------------------------------------------------------
n_C = 365
temperatura = rng.uniform(5, 35, size=n_C)                      # Z (confundidor)
ventas_helados = 50 + 8.0 * temperatura + rng.normal(0, 25, n_C)   # X = f(Z)
ahogamientos = rng.poisson(np.clip(0.15 * temperatura, 0, None))   # Y = g(Z)
ventas_helados = np.round(np.clip(ventas_helados, 0, None), 0)

df_C = pd.DataFrame({
    "dia": np.arange(1, n_C + 1),
    "temperatura_C": np.round(temperatura, 1),
    "ventas_helados": ventas_helados,
    "ahogamientos": ahogamientos,
})
df_C.to_csv("dataset_C_confusion.csv", index=False)

def partial_corr(x, y, z):
    # correlación parcial de x,y controlando z (residuales de regresiones lineales)
    def resid(a, b):
        b1 = np.polyfit(b, a, 1)
        return a - np.polyval(b1, b)
    rx = resid(x, z)
    ry = resid(y, z)
    return np.corrcoef(rx, ry)[0, 1]

r_xy = np.corrcoef(df_C["ventas_helados"], df_C["ahogamientos"])[0, 1]
r_xy_z = partial_corr(df_C["ventas_helados"].values.astype(float),
                      df_C["ahogamientos"].values.astype(float),
                      df_C["temperatura_C"].values.astype(float))
print("=== DATASET C — confusión ===")
print(f"n = {n_C}")
print(f"corr(helados, ahogamientos)            = {r_xy:.3f}  <- parece fuerte")
print(f"corr parcial dado la temperatura       = {r_xy_z:.3f}  <- se desvanece")
print()
print("CSVs generados: dataset_A_asimetria.csv, dataset_B_outliers.csv, dataset_C_confusion.csv")

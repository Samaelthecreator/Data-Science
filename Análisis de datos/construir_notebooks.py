# -*- coding: utf-8 -*-
"""Construye los notebooks de la Clase 3 (docente resuelto + alumno con TODOs)."""
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

# Cada entrada: ("md", texto)  ->  celda igual en ambos notebooks
#               ("code", teacher_src, student_src)  ->  código distinto
CELLS = []
def md(t):   CELLS.append(("md", t))
def code(teacher, student): CELLS.append(("code", teacher, student))

# ======================================================================
md("""# Clase 3 — Visualización y Análisis Controlado (Casos Sintéticos)
### Análisis de Datos en Python · Curso intensivo

**Idea central:** hoy no aprendemos a "hacer gráficos". Aprendemos a **usar la vista como
instrumento de verificación** de la estadística de la Clase 1. Cada gráfico es una *hipótesis*
que después confirmamos o refutamos con un número.

Trabajamos con **datos sintéticos**: conocemos la verdad (la media real, la σ real, la
correlación real), así que podemos comprobar si nuestros métodos la recuperan. Ese lujo
desaparece en la Clase 4 (datos reales).

**Datasets de hoy** (generados con semilla fija, verdad conocida):
| Archivo | Fenómeno diseñado | Concepto de la Clase 1 que reaparece |
|---|---|---|
| `dataset_A_asimetria.csv` | Asimetría fuerte a la derecha | Media vs. mediana, imputación |
| `dataset_B_outliers.csv` | Outliers de alto apalancamiento | Dispersión, IQR, correlación |
| `dataset_C_confusion.csv` | Correlación espuria por confusión | Correlación, causalidad |
""")

# ---- Setup ----
md("## 0 · Preparación del entorno")
code(
"""%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (7, 4)
pd.set_option("display.float_format", lambda v: f"{v:,.2f}")

# Los CSV deben estar en la misma carpeta que este notebook.
df_A = pd.read_csv("dataset_A_asimetria.csv")
df_B = pd.read_csv("dataset_B_outliers.csv")
df_C = pd.read_csv("dataset_C_confusion.csv")
print("A:", df_A.shape, "| B:", df_B.shape, "| C:", df_C.shape)""",
"""%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (7, 4)

# TODO: carga los tres CSV en df_A, df_B, df_C con pd.read_csv(...)
df_A = ...
df_B = ...
df_C = ...
# TODO: imprime la forma (shape) de cada uno para comprobar que cargaron"""
)

# ======================================================================
md("""## Bloque 0 (10 min) · ¿Por qué visualizar? El cuarteto de Anscombe

**El "por qué".** Cuatro conjuntos con **la misma media, la misma desviación y la misma
correlación de Pearson**... y cuatro realidades completamente distintas. Moraleja que guía
toda la clase: *un resumen numérico nunca sustituye a mirar los datos.*""")

code(
"""# Cuarteto de Anscombe (valores clásicos)
x123 = np.array([10,8,13,9,11,14,6,4,12,7,5], float)
x4   = np.array([8,8,8,8,8,8,8,19,8,8,8], float)
ans = {
    "I":   (x123, np.array([8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68])),
    "II":  (x123, np.array([9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74])),
    "III": (x123, np.array([7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73])),
    "IV":  (x4,   np.array([6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89])),
}
print(f"{'set':>4} {'media_x':>8} {'media_y':>8} {'std_y':>7} {'r':>7}")
for k,(x,y) in ans.items():
    r = np.corrcoef(x,y)[0,1]
    print(f"{k:>4} {x.mean():8.2f} {y.mean():8.2f} {y.std(ddof=1):7.2f} {r:7.3f}")""",
"""# Cuarteto de Anscombe (valores clásicos, ya provistos)
x123 = np.array([10,8,13,9,11,14,6,4,12,7,5], float)
x4   = np.array([8,8,8,8,8,8,8,19,8,8,8], float)
ans = {
    "I":   (x123, np.array([8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68])),
    "II":  (x123, np.array([9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74])),
    "III": (x123, np.array([7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73])),
    "IV":  (x4,   np.array([6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89])),
}
# TODO: para cada set imprime media_x, media_y, std_y y r de Pearson.
# ¿Son casi idénticos los cuatro resúmenes?"""
)
code(
"""fig, axs = plt.subplots(2, 2, figsize=(9, 7))
for ax,(k,(x,y)) in zip(axs.ravel(), ans.items()):
    ax.scatter(x, y)
    b, a = np.polyfit(x, y, 1)          # misma recta para los 4
    ax.plot(x, a + b*x, color="crimson")
    ax.set_title(f"Anscombe {k}")
fig.suptitle("Mismos números, cuatro realidades", y=1.02)
plt.tight_layout(); plt.show()""",
"""# TODO: dibuja un scatter de cada uno de los 4 sets en una rejilla 2x2
#       y superpón la recta de ajuste (usa np.polyfit(x, y, 1)).
#       Observa: ¿la misma recta describe bien los cuatro casos?"""
)
md("""> **Conclusión del bloque.** Nunca confíes en `r` (ni en la media) sin mirar la nube.
> El set II es curvo, el III está dominado por un outlier, el IV es una recta vertical + 1 punto.""")

# ======================================================================
md("""## Bloque 1 (20 min) · Histogramas → Dataset A (asimetría)

**El "por qué".** El histograma es la versión gráfica de la **tabla de frecuencias** de la
Clase 1. En una distribución asimétrica a la derecha, la **media se desplaza hacia la cola**
y deja de representar al hogar típico; la **mediana** se mantiene en el centro de masa de los
datos. Por eso, para *imputar* y para *reportar*, la mediana suele ser la elección honesta.

### 🔁 Ejercicio repetitivo #1
Recalcula media y mediana (Clase 1), márcalas sobre el histograma y decide con qué imputar.""")

code(
"""col = df_A["ingreso_mensual"]
media  = col.mean()
mediana = col.median()
print(f"nulos = {col.isna().sum()}")
print(f"media   = {media:,.1f}")
print(f"mediana = {mediana:,.1f}")
print(f"¿media > mediana?  -> asimetría a la derecha: {media > mediana}")

ax = col.plot.hist(bins=40, edgecolor="white")
ax.axvline(media,   color="crimson", ls="--", label=f"media {media:,.0f}")
ax.axvline(mediana, color="green",   ls="-",  label=f"mediana {mediana:,.0f}")
ax.set_xlabel("ingreso mensual (€)"); ax.legend(); plt.show()""",
"""col = df_A["ingreso_mensual"]
# TODO: calcula media y mediana; imprime cuántos nulos hay.
# TODO: dibuja el histograma (prueba bins=40) y traza dos líneas verticales
#       (plt.axvline) para la media y la mediana.
# Pregunta: ¿cuál queda más a la derecha y por qué?"""
)
code(
"""# Imputación: comparamos rellenar con media vs. mediana
imp_media   = col.fillna(col.mean())
imp_mediana = col.fillna(col.median())
print("Tras imputar con MEDIA   -> media:", round(imp_media.mean(),1),
      "| mediana:", round(imp_media.median(),1))
print("Tras imputar con MEDIANA -> media:", round(imp_mediana.mean(),1),
      "| mediana:", round(imp_mediana.median(),1))
# La imputación por media infla artificialmente la cola; la mediana preserva la forma.""",
"""# TODO: crea dos versiones imputando los nulos con fillna():
#   imp_media   = col.fillna( ??? )
#   imp_mediana = col.fillna( ??? )
# Compara la media y la mediana resultantes. ¿Cuál deforma menos la distribución?"""
)
md("""> **Decisión justificada:** en esta columna asimétrica imputamos con **mediana**. Rellenar
> con la media empuja los valores faltantes hacia arriba (recuerda: los nulos eran más
> frecuentes en ingresos altos), amplificando el sesgo.""")

# ======================================================================
md("""## Bloque 2 (20 min) · Boxplot y atípicos → Dataset B

**El "por qué".** El boxplot codifica los **cuartiles y el IQR** de la Clase 1 y define
formalmente un atípico: fuera de `[Q1 − 1.5·IQR, Q3 + 1.5·IQR]`. Pero detectar no es borrar:
un atípico puede ser un error de captura **o** el dato más informativo. Aquí son errores de
digitación (se anotó 40 h en vez de 4) y **degradan la correlación**.

### 🔁 Ejercicio repetitivo #2
Detecta outliers con la regla IQR, decide qué hacer y **recalcula la correlación** (Clase 1).""")

code(
"""def limites_iqr(s):
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5*iqr, q3 + 1.5*iqr

fig, ax = plt.subplots(1, 2, figsize=(10,4))
df_B.boxplot(column="horas_estudio", ax=ax[0]); ax[0].set_title("horas_estudio")
df_B.boxplot(column="puntuacion",    ax=ax[1]); ax[1].set_title("puntuacion")
plt.show()

low, high = limites_iqr(df_B["horas_estudio"])
outliers = df_B[(df_B["horas_estudio"] < low) | (df_B["horas_estudio"] > high)]
print(f"Límite IQR horas_estudio: [{low:.1f}, {high:.1f}]")
print(f"Outliers detectados: {len(outliers)}")
print(outliers.to_string(index=False))""",
"""def limites_iqr(s):
    # TODO: devuelve (Q1 - 1.5*IQR, Q3 + 1.5*IQR) usando s.quantile(...)
    ...

# TODO: dibuja el boxplot de 'horas_estudio' y 'puntuacion'.
# TODO: usa limites_iqr() para marcar las filas atípicas de 'horas_estudio'
#       e imprímelas. ¿Cuántas hay? ¿Qué tienen de raro?"""
)
code(
"""r_con = df_B["horas_estudio"].corr(df_B["puntuacion"])
limpio = df_B.drop(outliers.index)
r_sin  = limpio["horas_estudio"].corr(limpio["puntuacion"])
print(f"r CON outliers = {r_con:.3f}")
print(f"r SIN outliers = {r_sin:.3f}   <- la relación real era mucho más fuerte")
print(f"std horas CON = {df_B['horas_estudio'].std():.2f} | SIN = {limpio['horas_estudio'].std():.2f}")""",
"""# TODO: calcula la correlación de Pearson horas_estudio vs puntuacion
#       (a) con los outliers y (b) tras quitarlos con df_B.drop(outliers.index).
# TODO: compara también la desviación estándar antes y después.
# Pregunta: ¿cuánto cambió la conclusión por 6 puntos mal capturados?"""
)
md("""> **Decisión justificada:** documentamos y removemos (o corregimos) esos 6 registros porque
> son errores de captura verificables, no observaciones legítimas. La correlación pasa de
> engañosa a real. Siempre se justifica *por qué* se toca un dato.""")

# ======================================================================
md("""## Bloque 3 (20 min) · Scatter y correlación → Anscombe revisitado

**El "por qué".** Un mismo `r` puede esconder una recta, una curva o un outlier dominante.
Por eso el scatter **precede** al coeficiente, nunca al revés. Pearson mide relación *lineal*;
Spearman capta monotonía (útil cuando la relación es curva pero creciente).

### 🔁 Ejercicio repetitivo #3
Confirma que los 4 sets de Anscombe tienen (casi) el mismo `r` pese a nubes distintas.""")
code(
"""from math import isclose
for k,(x,y) in ans.items():
    rp = np.corrcoef(x,y)[0,1]
    # Spearman = Pearson sobre los rangos
    rs = np.corrcoef(pd.Series(x).rank(), pd.Series(y).rank())[0,1]
    print(f"Set {k:>3}: Pearson={rp:.3f}  Spearman={rs:.3f}")
print("\\nMisma r de Pearson, comportamientos distintos => grafica SIEMPRE.")""",
"""# TODO: recorre los 4 sets de 'ans' y calcula para cada uno
#       la correlación de Pearson y la de Spearman (Pearson sobre los rangos, .rank()).
# ¿Confirmas que la Pearson es casi idéntica en los cuatro?"""
)

# ======================================================================
md("""## Bloque integrador (30 min) · Ciclo iterativo sobre los 3 casos

**El "por qué".** El análisis real es **iterativo**: *conjeturar → graficar → medir → corregir
→ volver a medir*. Aquí el foco es el Dataset C, donde una correlación fuerte **se desvanece**
al condicionar por una tercera variable (confusión / semilla de la paradoja de Simpson).

**Historia:** en una ciudad costera, los días de más **ventas de helados** coinciden con más
**ahogamientos**. ¿Comer helado es peligroso? Conjetura, grafica y decide.""")
code(
"""# Paso 1 — conjeturar y medir la correlación aparente
r_xy = df_C["ventas_helados"].corr(df_C["ahogamientos"])
print(f"corr(helados, ahogamientos) = {r_xy:.3f}  (parece fuerte)")

plt.scatter(df_C["ventas_helados"], df_C["ahogamientos"], alpha=0.5)
plt.xlabel("ventas de helados"); plt.ylabel("ahogamientos")
plt.title("¿Relación causal?"); plt.show()""",
"""# Paso 1 — TODO: mide corr(ventas_helados, ahogamientos) y dibuja el scatter.
# ¿La correlación sugiere causalidad?"""
)
code(
"""# Paso 2 — introducir el confundidor: colorear por temperatura
sc = plt.scatter(df_C["ventas_helados"], df_C["ahogamientos"],
                 c=df_C["temperatura_C"], cmap="coolwarm", alpha=0.7)
plt.colorbar(sc, label="temperatura (°C)")
plt.xlabel("ventas de helados"); plt.ylabel("ahogamientos")
plt.title("El color revela la variable oculta"); plt.show()""",
"""# Paso 2 — TODO: repite el scatter pero colorea los puntos por 'temperatura_C'
#          (argumento c=..., cmap='coolwarm') y añade plt.colorbar().
# ¿Qué patrón aparece con el color?"""
)
code(
"""# Paso 3 — condicionar: correlación dentro de franjas de temperatura similar
df_C["franja_temp"] = pd.cut(df_C["temperatura_C"], bins=[0,15,25,35])
por_franja = (df_C.groupby("franja_temp", observed=True)[["ventas_helados","ahogamientos"]]
                  .apply(lambda g: g["ventas_helados"].corr(g["ahogamientos"])))
print("Correlación helados-ahogamientos DENTRO de cada franja de temperatura:")
print(por_franja.round(3))
print("\\nAl fijar la temperatura, la relación se desvanece: era espuria.")""",
"""# Paso 3 — TODO: crea franjas de temperatura con pd.cut(..., bins=[0,15,25,35])
#          y calcula la correlación helados-ahogamientos DENTRO de cada franja
#          (groupby + apply). ¿Se mantiene la correlación o desaparece?"""
)
md("""> **Cierre del ciclo.** La temperatura es la **causa común**: días calurosos → más helados
> y más gente en el agua. Correlación ≠ causalidad. Reúso simultáneo de: correlación,
> agrupamiento, y pensamiento crítico. *Repite este ciclo con A (¿imputar cambia la media?)
> y con B (¿los outliers cambian la pendiente?).*""")

# ======================================================================
md("""## Bloque de síntesis (20 min) · Elegir el gráfico correcto y no mentir

**El "por qué".** El tipo de variable determina el gráfico: **1 variable numérica → histograma
/ boxplot**; **2 numéricas → scatter**; **categórica vs numérica → boxplot por grupo**;
**categórica → barras**. Y un gráfico es un *argumento*: los ejes truncados exageran
diferencias. Elegir mal el gráfico es un error analítico, no estético.""")
code(
"""# Demostración de eje engañoso: mismos datos, distinta escala vertical
grupos = ["A","B"]; valores = [102, 100]
fig, ax = plt.subplots(1,2, figsize=(9,3.5))
ax[0].bar(grupos, valores); ax[0].set_ylim(99, 103); ax[0].set_title("Eje truncado (engañoso)")
ax[1].bar(grupos, valores); ax[1].set_ylim(0, 110);  ax[1].set_title("Eje desde 0 (honesto)")
plt.tight_layout(); plt.show()
print("Misma diferencia (2%), dos narrativas visuales opuestas.")""",
"""# TODO: reproduce dos barras con valores [102, 100].
#   Gráfico 1: set_ylim(99, 103)  -> exagera la diferencia
#   Gráfico 2: set_ylim(0, 110)   -> muestra la diferencia real
# Comenta qué ves."""
)
md("""### ✅ Checklist de visualización (para llevar a la Clase 4)
1. ¿Qué **tipo** de variable(s) tengo? → elige el gráfico adecuado.
2. ¿El **histograma** confirma la forma que asumí (simetría, modas)?
3. ¿Hay **atípicos** (boxplot/IQR)? ¿Son error o señal? Justifica la decisión.
4. Antes de confiar en `r`, **¿grafiqué la nube?** (recuerda Anscombe).
5. ¿Hay una **variable oculta** que explique la correlación? (confusión).
6. ¿Mis **ejes** cuentan la verdad o exageran?

**Puente a la Clase 4:** estas tres alertas — asimetría, atípicos y confusión — reaparecerán
en datos reales, donde ya no conoceremos la verdad de antemano.""")

# ======================================================================
def build(is_teacher):
    nb = new_notebook()
    cells = []
    for c in CELLS:
        if c[0] == "md":
            cells.append(new_markdown_cell(c[1]))
        else:
            cells.append(new_code_cell(c[1] if is_teacher else c[2]))
    nb["cells"] = cells
    nb["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
    }
    return nb

nbf.write(build(True),  "Clase3_DOCENTE_resuelto.ipynb")
nbf.write(build(True),  "Clase3_DOCENTE_resuelto.ipynb")
nbf.write(build(False), "Clase3_ALUMNO_ejercicios.ipynb")
print("Notebooks escritos OK. Total de celdas:", len(CELLS))

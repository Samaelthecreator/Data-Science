# Clase 2 — Fundamentos II: Inferencia, Asociación, Regresión y Cálculo Estocástico

> **Documento de desarrollo académico (v2.0).** Redactado desde el rol de un profesional con maestría en cálculo estadístico y estocástico, enfoque en cómputo estadístico. **Enfoque *just-in-time*:** la teoría manda; Python entra en el momento en que hay que estimar, contrastar, ajustar o simular. Esta clase cierra el arco de los fundamentos: de la muestra a la conclusión, y del azar estático al azar en el tiempo.
>
> **Estructura:** (1) Glosario; (2) Desarrollo tema por tema (teoría → necesidad → herramienta), con casos idóneos/no idóneos; (3) Ejemplos de mejor y peor caso; (4) Apéndice de herramientas de Python usadas.

---

## 1. Glosario de conceptos

| # | Concepto | Definición operativa |
|---|---|---|
| 1 | **Estimador** | Regla que aproxima un parámetro poblacional desde la muestra ($\bar{x}$ estima $\mu$). |
| 2 | **Error estándar** | Desviación del estimador: $\text{SE}(\bar{x})=s/\sqrt{n}$. |
| 3 | **Ley de los Grandes Números (LGN)** | La media muestral converge a $\mu$ cuando $n\to\infty$. |
| 4 | **Teorema del Límite Central (TLC)** | La media de $n$ VA i.i.d. con varianza finita tiende a Normal. |
| 5 | **Intervalo de confianza (IC)** | Rango que, bajo muestreo repetido, cubre el parámetro con confianza $1-\alpha$. |
| 6 | **Hipótesis nula/alternativa** | $H_0$ (sin efecto) vs. $H_1$ (efecto). |
| 7 | **Error tipo I / II** | Rechazar $H_0$ cierta ($\alpha$) / no rechazar $H_0$ falsa ($\beta$). |
| 8 | **p-valor** | $P(\text{estadístico tan extremo}\mid H_0)$. **No** es $P(H_0)$. |
| 9 | **Potencia** | $1-\beta$: probabilidad de detectar un efecto real. |
| 10 | **Covarianza** | $E[(X-\mu_X)(Y-\mu_Y)]$; signo de la relación lineal. |
| 11 | **Correlación de Pearson** ($r$) | Covarianza estandarizada, $[-1,1]$; relación **lineal**. |
| 12 | **Correlación de Spearman** ($\rho$) | Pearson sobre rangos; relación **monótona**, robusta. |
| 13 | **Regresión lineal** | Modelo $y=\beta_0+\beta_1 x_1+\dots+\varepsilon$ ajustado por mínimos cuadrados. |
| 14 | **R²** | Proporción de varianza de $y$ explicada por el modelo. |
| 15 | **Residuo** | $y_i-\hat{y}_i$; su diagnóstico valida (o refuta) los supuestos. |
| 16 | **Supuestos de MCO** | Linealidad, independencia, homocedasticidad, normalidad de residuos. |
| 17 | **Proceso estocástico** | Familia de VA indexadas por el tiempo $\{X_t\}$. |
| 18 | **Caminata aleatoria** | $X_t=X_{t-1}+\varepsilon_t$; suma acumulada de choques. |
| 19 | **Cadena de Markov** | Proceso donde el futuro depende solo del estado presente (sin memoria). |
| 20 | **Matriz de transición** | Probabilidades de pasar de un estado a otro en un paso. |
| 21 | **Monte Carlo** | Estimación por simulación repetida (aquí, de procesos e intervalos). |
| — | *Python:* `numpy`, `scipy.stats`, `statsmodels`, `scikit-learn`, `matplotlib` | Introducidas *just-in-time*. |

---

## 2. Desarrollo tema por tema (teoría → necesidad → herramienta)

### 2.1 De la muestra a la población: estimadores y la LGN

**Teoría.** Nunca observamos la población; solo una muestra. Un estimador es una regla; su calidad se mide por sesgo y por **error estándar**, que decrece como $1/\sqrt{n}$: cuadruplicar la muestra solo duplica la precisión. La **LGN** garantiza que la media muestral converge al valor esperado.

**Necesidad → herramienta.** Se *ve* la convergencia simulándola:

```python
import numpy as np
rng = np.random.default_rng(7)
tiradas = rng.integers(1, 7, size=100_000)          # dado justo, E[X]=3.5
medias = np.cumsum(tiradas) / np.arange(1, 100_001) # media acumulada
# medias[-1] ≈ 3.5  y la curva se estabiliza -> LGN
```

- *Idóneo:* justificar por qué más datos ⇒ estimaciones más estables.
- *No sirve / cuidado:* la LGN no salva de un muestreo **sesgado**: converge, pero al valor equivocado si la muestra no es representativa.

### 2.2 Teorema del Límite Central

**Teoría.** El TLC explica por qué la Normal aparece incluso cuando los datos no lo son: lo que se normaliza es la **media muestral**, no los datos crudos. Requiere varianza finita y $n$ suficiente (mayor cuanto más asimétricos sean los datos).

**Necesidad → herramienta.**

```python
import matplotlib.pyplot as plt
pob = rng.exponential(scale=1.0, size=1_000_000)     # población MUY asimétrica
medias = [rng.choice(pob, 40).mean() for _ in range(5000)]  # medias de n=40
plt.hist(medias, bins=40)   # ¡campana! aunque la población sea exponencial
```

### 2.3 Intervalos de confianza

**Teoría.** Un IC al 95 % significa que el 95 % de los intervalos así construidos, **bajo muestreo repetido**, contienen el parámetro. *No* significa "hay 95 % de probabilidad de que $\mu$ esté en este intervalo concreto" (ese es el intervalo creíble bayesiano de la Clase 1).

**Necesidad → herramienta.**

```python
from scipy import stats
x = df["valor"]
ic = stats.t.interval(0.95, df=len(x)-1, loc=x.mean(), scale=stats.sem(x))
```

- *Idóneo:* comunicar incertidumbre de una estimación.
- *No sirve:* interpretarlo como probabilidad del parámetro; construirlo con $n$ minúsculo y datos muy sesgados sin corrección.

### 2.4 Pruebas de hipótesis y p-valor

**Teoría.** Se fija $H_0$, un $\alpha$ y un diseño **antes** de ver los datos. El p-valor mide la compatibilidad del dato con $H_0$, no la verdad de $H_0$ ni el tamaño del efecto. Con $n$ enorme, un efecto trivial sale "significativo"; con $n$ pequeño, uno real puede pasar desapercibido (baja potencia). Reportar **siempre** el tamaño del efecto junto al p-valor.

**Necesidad → herramienta.**

```python
from scipy import stats
a = df[df["grupo"]=="A"]["y"]; b = df[df["grupo"]=="B"]["y"]
t, p = stats.ttest_ind(a, b, equal_var=False)     # Welch: no asume varianzas iguales
d = (a.mean()-b.mean()) / np.sqrt((a.std()**2 + b.std()**2)/2)  # d de Cohen (efecto)
```

- *No sirve / se abusa:* probar muchas hipótesis y reportar solo la significativa (**p-hacking**); leer "no significativo" como "no hay efecto".

### 2.5 Asociación: covarianza y correlación

**Teoría.** La covarianza da el signo pero depende de las unidades. **Pearson** la estandariza a $[-1,1]$ pero solo capta lo **lineal**: puede ser 0 con dependencia perfecta no lineal ($Y=X^2$). **Spearman** capta cualquier relación monótona y resiste atípicos. Y, siempre: correlación **no implica** causalidad.

**Necesidad → herramienta.**

```python
df[["x","y"]].corr()                       # matriz de Pearson
stats.spearmanr(df["x"], df["y"])          # alternativa robusta / monótona
```

### 2.6 Regresión lineal simple y múltiple *(tema ampliado)*

**Teoría.** La regresión modela $y=\beta_0+\beta_1x_1+\dots+\beta_kx_k+\varepsilon$ minimizando la suma de residuos al cuadrado (MCO). Los coeficientes se interpretan como el cambio esperado en $y$ por unidad de $x_j$ **manteniendo las demás constantes**. El **R²** mide la varianza explicada, pero un R² alto no valida el modelo: hay que **diagnosticar residuos** (deben ser aproximadamente aleatorios, centrados en cero y homocedásticos). Supuestos: linealidad, independencia, homocedasticidad y normalidad de los residuos.

- *Idónea:* relación aproximadamente lineal; interpretación de efectos; predicción dentro del rango observado.
- *No sirve / cuidado:* extrapolar fuera del rango; ignorar heterocedasticidad o no linealidad (residuos con forma de embudo o de curva); multicolinealidad severa (coeficientes inestables); confundir asociación con causalidad.

**Necesidad → herramienta.**

```python
import statsmodels.formula.api as smf
modelo = smf.ols("precio ~ superficie + habitaciones", data=df).fit()
modelo.params        # coeficientes β
modelo.rsquared      # R²
modelo.summary()     # p-valores, IC, diagnósticos
# Diagnóstico visual imprescindible:
plt.scatter(modelo.fittedvalues, modelo.resid); plt.axhline(0)  # ¿residuos sin patrón?
```

Para predicción pura, la interfaz equivalente en `scikit-learn` es `LinearRegression().fit(X, y)`.

### 2.7 Introducción al cálculo estocástico aplicado *(tema ampliado)*

**Teoría.** Un **proceso estocástico** $\{X_t\}$ es una familia de variables aleatorias indexadas por el tiempo. Tres piezas fundamentales:

- **Caminata aleatoria:** $X_t = X_{t-1} + \varepsilon_t$. Es la suma acumulada de choques independientes; modela precios, difusión y errores acumulados. Su varianza crece con $t$ (no es estacionaria).
- **Cadena de Markov:** proceso "sin memoria": la probabilidad del siguiente estado depende **solo** del estado actual, no de la historia. Se describe con una **matriz de transición**. Modela clima, navegación web, colas, cambios de régimen.
- **Monte Carlo sobre procesos:** simular muchas trayectorias para estimar cantidades difíciles (probabilidad de ruina, tiempo de primer paso, distribución estacionaria).

- *Idóneo:* fenómenos que evolucionan en el tiempo con aleatoriedad; estimar comportamientos agregados por simulación.
- *No sirve / cuidado:* asumir Markov cuando hay memoria larga (dependencia del pasado lejano); interpretar una sola trayectoria simulada como "la" predicción (se necesita el conjunto de trayectorias).

**Necesidad → herramienta.**

```python
# (a) Caminata aleatoria: una trayectoria
pasos = rng.choice([-1, 1], size=1000)
trayectoria = np.cumsum(pasos)
plt.plot(trayectoria)

# (b) Cadena de Markov: clima {0=sol, 1=lluvia}
P = np.array([[0.9, 0.1],
              [0.5, 0.5]])          # matriz de transición
estado, hist = 0, []
for _ in range(10_000):
    estado = rng.choice([0, 1], p=P[estado]); hist.append(estado)
np.bincount(hist) / len(hist)       # distribución estacionaria empírica ≈ [0.83, 0.17]

# (c) Monte Carlo: P(la caminata cruce +20 en 1000 pasos)
cruces = [ (np.cumsum(rng.choice([-1,1], 1000)).max() >= 20) for _ in range(5000) ]
np.mean(cruces)                     # estimación de la probabilidad
```

---

## 3. Ejemplos: el mejor y el peor caso de uso

### Ejemplo A — p-valor y tamaño del efecto

**✅ Mejor caso.** Ensayo con hipótesis, $\alpha$ y $n$ fijados de antemano; `ttest_ind` da $p=0.003$ y la `d` de Cohen indica un efecto grande. Se reporta *ambos*: significancia y magnitud.

**❌ Peor caso.** Se corren 40 pruebas `ttest_ind`, se halla una con $p=0.04$ y se titula "hallazgo significativo" sin corrección por comparaciones múltiples ni tamaño de efecto. Con $\alpha=0.05$ se esperan ~2 falsos positivos por azar: es p-hacking.

### Ejemplo B — Regresión: diagnóstico de residuos

**✅ Mejor caso.** `precio ~ log(superficie)` en viviendas: residuos sin patrón alrededor de cero, homocedásticos; los coeficientes son interpretables y el R² es honesto. El modelo predice bien dentro del rango.

**❌ Peor caso.** `precio ~ superficie` sobre el precio crudo, muy asimétrico: los residuos forman un **embudo** (heterocedasticidad) y el modelo subestima sistemáticamente las casas caras. Un R² "aceptable" oculta que los supuestos están rotos. La solución era transformar con logaritmo, no confiar en el R².

### Ejemplo C — Interpretación causal de una regresión

**✅ Mejor caso.** Se reporta: "por cada m² adicional, el precio esperado sube ~X, manteniendo constantes las demás variables; es una asociación observacional, no un experimento".

**❌ Peor caso.** "Añadir una habitación **causa** +Y de valor": se extrapola una regresión observacional a una intervención, ignorando confusores (barrio, superficie) y la posible causalidad inversa.

### Ejemplo D — Cadena de Markov

**✅ Mejor caso.** Modelar el clima diario con la matriz `P` de la §2.7: la distribución estacionaria empírica coincide con la teórica, y sirve para estimar la fracción de días lluviosos a largo plazo.

**❌ Peor caso.** Aplicar Markov a una serie con **memoria larga** (p. ej. tendencia y estacionalidad anual fuertes): el supuesto "sin memoria" falla y la cadena predice mal, porque el mañana depende de mucho más que el hoy.

### Ejemplo E — Monte Carlo vs. solución exacta

**✅ Mejor caso.** Estimar la probabilidad de que una caminata aleatoria cruce un umbral: no hay fórmula simple cómoda, así que 5.000 trayectorias dan una estimación fiable con su margen de error.

**❌ Peor caso.** Estimar por Monte Carlo algo con solución cerrada trivial (p. ej. la media de una Normal): se introduce ruido de muestreo innecesario donde la respuesta exacta era inmediata.

---

## 4. Apéndice — Caja de herramientas de Python (Clase 2)

| Tarea analítica | Herramienta | Nota |
|---|---|---|
| Convergencia / LGN | `np.cumsum`, medias acumuladas | Visualizar estabilización. |
| TLC | muestreo repetido + `hist` | La media se normaliza aunque los datos no. |
| Error estándar / IC | `scipy.stats.sem`, `stats.t.interval` | Interpretación frecuentista. |
| Prueba de hipótesis | `stats.ttest_ind` / `ttest_1samp` | Welch con `equal_var=False`; reportar efecto. |
| Tamaño del efecto | fórmula de `d` de Cohen | Acompaña siempre al p-valor. |
| Correlación | `df.corr`, `stats.spearmanr` | Pearson (lineal) vs. Spearman (monótona). |
| Regresión | `statsmodels.formula.api.ols`, `.summary()` | Coeficientes, R², diagnóstico de residuos. |
| Regresión (predicción) | `sklearn.linear_model.LinearRegression` | Interfaz `fit`/`predict`. |
| Caminata aleatoria | `rng.choice` + `np.cumsum` | Proceso no estacionario. |
| Cadena de Markov | matriz `P` + bucle con `rng.choice` | Distribución estacionaria empírica. |
| Monte Carlo de procesos | simular muchas trayectorias + `.mean()` | Estimar probabilidades y tiempos. |

> **Cierre de la clase (y de los fundamentos).** El alumno ya recorre el arco completo: describir (Clase 1) → inferir, relacionar y modelar (Clase 2). Sabe estimar con incertidumbre, contrastar hipótesis con honestidad, ajustar y **diagnosticar** una regresión, y simular el azar en el tiempo con caminatas, cadenas de Markov y Monte Carlo. Todo el Python apareció al servicio de una necesidad analítica concreta. Con esta base, las Clases 3 (visualización y análisis controlado) y 4 (mundo real) aplican el criterio sobre datos sintéticos y reales.

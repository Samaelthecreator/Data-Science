# Clase 1 — Fundamentos I: Pensamiento Analítico, Estadística Descriptiva y Probabilidad

> **Documento de desarrollo académico (v2.0).** Redactado desde el rol de un profesional con maestría en cálculo estadístico y estocástico, enfoque en cómputo estadístico. **Enfoque *just-in-time*:** primero la teoría; cuando un concepto exige calcular, filtrar o graficar, se introduce en ese punto la herramienta de Python que lo resuelve. No hay explicación del lenguaje "por adelantado": Python aparece anclado al problema.
>
> **Estructura:** (1) Glosario; (2) Desarrollo tema por tema (teoría → necesidad → herramienta), con casos idóneos/no idóneos; (3) Ejemplos de mejor y peor caso; (4) Apéndice de herramientas de Python usadas.

---

## 1. Glosario de conceptos

| # | Concepto | Definición operativa |
|---|---|---|
| 1 | **Población / Muestra** | Conjunto total objetivo / subconjunto observado del que se infiere. |
| 2 | **Variable** | Característica medible: cualitativa (nominal/ordinal) o cuantitativa (discreta/continua). |
| 3 | **Media** ($\bar{x}$) | $\frac{1}{n}\sum x_i$. Minimiza el error cuadrático; sensible a atípicos. |
| 4 | **Mediana** | Valor central por orden; minimiza el error absoluto; robusta (ruptura 50 %). |
| 5 | **Moda** | Valor más frecuente; única válida para nominales. |
| 6 | **Rango / Varianza / Desv. estándar** | Medidas de dispersión: $\max-\min$; $s^2=\frac{1}{n-1}\sum(x_i-\bar{x})^2$; $s=\sqrt{s^2}$. |
| 7 | **IQR** | $Q_3-Q_1$; dispersión robusta del 50 % central. |
| 8 | **Coeficiente de variación** | $s/\bar{x}$; dispersión relativa adimensional. |
| 9 | **Distribución de frecuencias** | Agrupación en clases; regla de Sturges $k=1+\log_2 n$. |
| 10 | **Asimetría (skewness)** | Falta de simetría; positiva ⇒ media > mediana. |
| 11 | **Espacio muestral** ($\Omega$) | Todos los resultados posibles de un experimento aleatorio. |
| 12 | **Axiomas de Kolmogórov** | $P(A)\ge 0$; $P(\Omega)=1$; aditividad en disjuntos. |
| 13 | **Probabilidad condicional** | $P(A\mid B)=P(A\cap B)/P(B)$. |
| 14 | **Independencia** | $P(A\cap B)=P(A)P(B)$. |
| 15 | **Teorema de Bayes** | $P(A\mid B)=\dfrac{P(B\mid A)P(A)}{P(B)}$. |
| 16 | **Inferencia bayesiana** | Priori × verosimilitud ∝ posteriori; actualización de creencias con datos. |
| 17 | **Variable aleatoria (VA)** | Función de $\Omega$ en $\mathbb{R}$; discreta o continua. |
| 18 | **Valor esperado** ($E[X]$) | Centro de masa: $\sum x\,p(x)$ o $\int x f(x)\,dx$. |
| 19 | **Varianza de una VA** | $E[X^2]-E[X]^2$. |
| 20 | **Bernoulli / Binomial** | Éxito-fracaso / número de éxitos en $n$ ensayos. |
| 21 | **Poisson** | Conteo de eventos raros con tasa $\lambda$; $E[X]=\operatorname{Var}=\lambda$. |
| 22 | **Uniforme / Normal** | Equiprobable en $[a,b]$ / $\mathcal{N}(\mu,\sigma^2)$, base del TLC. |
| 23 | **Monte Carlo** | Estimar probabilidades/esperanzas mediante simulación repetida. |
| — | *Python:* `numpy`, `pandas`, `scipy.stats`, `matplotlib` | Herramientas introducidas *just-in-time* en este documento. |

---

## 2. Desarrollo tema por tema (teoría → necesidad → herramienta)

### 2.1 El proceso analítico

**Teoría.** Analizar empieza con una **pregunta**, no con un dataset. El dato no habla solo: el analista impone una estructura y su principal enemigo es el sesgo de confirmación. El primer gesto profesional ante una tabla es *diagnosticarla*, no graficarla.

**Necesidad → herramienta (Python JIT).** Para ese primer diagnóstico basta con tres operaciones:

```python
import pandas as pd
df = pd.read_csv("datos.csv")   # importar
df.shape        # (n_filas, n_columnas) -> tamaño muestral y dimensionalidad
df.head()       # primeras filas -> estructura
df.describe()   # resumen estadístico por columna -> la estadística de esta clase, condensada
```

`describe()` ya contiene media, desviación y cuartiles: leerlo bien evita trabajar a ciegas.

- *Idóneo:* como paso cero de cualquier análisis numérico.
- *No sirve:* sobre variables categóricas (usar `value_counts()`); `describe` es univariado (no ve relaciones).

### 2.2 Tendencia central

**Teoría.** La **media** minimiza el error cuadrático y es lineal, pero su punto de ruptura es 0 %: un solo extremo la desplaza sin límite. La **mediana** minimiza el error absoluto y resiste hasta el 50 % de contaminación, a costa de ignorar la magnitud. La **moda** es la única válida en nominales.

- *Media idónea:* distribución simétrica sin atípicos; se harán operaciones algebraicas.
- *Media no sirve:* asimetría, colas pesadas, variable ordinal/nominal.
- *Mediana idónea:* asimetría o atípicos; valor "típico".
- *Mediana no sirve:* cuando se requiere aditividad.

**Necesidad → herramienta.**

```python
col = df["ingreso"]
col.mean(), col.median(), col.mode().iloc[0]
# Diagnóstico rápido de asimetría sin graficar:
col.mean() > col.median()   # True -> cola a la derecha
```

### 2.3 Dispersión y frecuencias

**Teoría.** "El promedio sin la dispersión no significa nada." La **varianza** usa $n-1$ (corrección de Bessel: se pierde un grado de libertad al estimar $\bar{x}$). El **IQR** es la alternativa robusta; el **CV** permite comparar variabilidad entre escalas distintas. Agrupar en **clases** pierde detalle pero revela forma.

- *σ idónea:* datos aproximadamente normales; inferencia paramétrica posterior.
- *σ no sirve:* atípicos o colas pesadas → usar IQR.
- *CV no sirve:* media cercana a 0 o escalas de intervalo (°C).

**Necesidad → herramienta.**

```python
import numpy as np
col.std(ddof=1)                     # desviación muestral (n-1)
q1, q3 = col.quantile([.25, .75]); iqr = q3 - q1
cv = col.std(ddof=1) / col.mean()   # dispersión relativa
# Tabla de frecuencias por clases (Sturges):
k = int(1 + np.log2(len(col)))
pd.cut(col, bins=k).value_counts().sort_index()
```

### 2.4 Probabilidad y Teorema de Bayes

**Teoría.** La probabilidad condicional es el motor del razonamiento bajo evidencia. Bayes convierte $P(\text{evidencia}\mid\text{hipótesis})$ en $P(\text{hipótesis}\mid\text{evidencia})$ —que rara vez coinciden—. El error clásico es ignorar la **probabilidad base** (prevalencia): un test casi perfecto sobre una enfermedad rara produce mayoría de falsos positivos.

**Necesidad → herramienta.** Cuando la intuición falla, se **simula** para verificar la fórmula:

```python
rng = np.random.default_rng(42)
N = 1_000_000
enfermo = rng.random(N) < 0.001            # prevalencia 0.1 %
positivo = np.where(enfermo, rng.random(N) < 0.99,   # sensibilidad
                             rng.random(N) < 0.05)   # 1 - especificidad
p_enfermo_dado_positivo = enfermo[positivo].mean()   # ≈ 0.019  -> ¡solo ~2 %!
```

La simulación confirma el resultado de Bayes y lo hace tangible.

- *Idóneo:* diagnóstico, filtrado, actualización secuencial.
- *No sirve / se abusa:* ignorar la prevalencia; asumir independencia cuando no la hay.

### 2.5 Introducción a la inferencia bayesiana *(tema ampliado)*

**Teoría.** La inferencia bayesiana trata al parámetro como incierto y le asigna una distribución. La regla es: **posteriori ∝ verosimilitud × priori**. Con datos binarios, la familia Beta es conjugada de la Binomial: si la priori es $\text{Beta}(a,b)$ y se observan $k$ éxitos en $n$ ensayos, la posteriori es $\text{Beta}(a+k,\,b+n-k)$. La priori codifica el conocimiento previo; los datos la actualizan.

- *Idónea:* muestras pequeñas con conocimiento previo legítimo; actualización secuencial; cuando interesa una distribución completa del parámetro, no solo un punto.
- *No sirve / cuidado:* cuando la priori se elige para forzar el resultado (priori "informativa" injustificada); si se necesita una respuesta frecuentista comparable con la literatura clásica.

**Necesidad → herramienta.**

```python
from scipy import stats
a, b = 2, 2                 # priori Beta(2,2): creencia previa "moneda casi justa"
k, n = 8, 10                # datos: 8 caras en 10 lanzamientos
post = stats.beta(a + k, b + n - k)   # posteriori Beta(10,4)
post.mean(), post.interval(0.95)      # estimación puntual e intervalo creíble
```

### 2.6 Variables aleatorias y distribuciones

**Teoría.** Cada distribución **modela un mecanismo generador**: Bernoulli/Binomial (éxito-fracaso con $p$ constante), Poisson (conteos raros con tasa estable), Uniforme (ignorancia acotada), Normal (suma de muchos efectos pequeños, vía TLC). El **valor esperado** es el centro de masa, no necesariamente un valor observable.

- *Poisson idónea:* llegadas, defectos, siniestros con tasa constante.
- *Poisson no sirve:* sobredispersión (varianza ≫ media) → Binomial Negativa.
- *Normal no sirve:* variables acotadas, positivas y asimétricas (ingresos), o conteos.

**Necesidad → herramienta.**

```python
from scipy import stats
import matplotlib.pyplot as plt
x = np.arange(0, 15)
plt.bar(x, stats.poisson.pmf(x, mu=4))     # PMF de Poisson(λ=4)
# Verificar E[X]=λ por simulación:
muestras = stats.poisson.rvs(mu=4, size=100_000, random_state=rng)
muestras.mean()   # ≈ 4.0
```

### 2.7 Primer contacto con Monte Carlo *(puente a la Clase 2)*

**Teoría.** Cuando una probabilidad o una esperanza es difícil de calcular analíticamente, se **estima por simulación**: se genera un gran número de realizaciones y se promedia. Es la idea que, formalizada, sostiene el bootstrap y buena parte del cálculo estocástico de la Clase 2.

**Necesidad → herramienta.**

```python
# Estimar π por Monte Carlo (puntos en el cuadrado unitario)
pts = rng.random((1_000_000, 2))
dentro = (pts**2).sum(axis=1) <= 1
pi_estimado = 4 * dentro.mean()   # ≈ 3.14
```

- *Idóneo:* problemas sin solución cerrada; validar fórmulas; propagar incertidumbre.
- *No sirve:* cuando existe solución exacta barata (simular por simular desperdicia precisión y tiempo).

---

## 3. Ejemplos: el mejor y el peor caso de uso

### Ejemplo A — Media vs. mediana con Python

**✅ Mejor caso.** Estaturas simétricas: `df["estatura"].mean()` ≈ `df["estatura"].median()` ≈ 175 cm. La media describe al individuo típico y habilita inferencia paramétrica.

**❌ Peor caso.** Ingresos con un multimillonario: `df["ingreso"].mean()` ≈ 3.000.000 mientras nueve de cada diez ganan 30.000. Reportar esa media como "ingreso promedio" es correcto y engañoso; el diagnóstico `mean() > median()` lo delata de inmediato.

### Ejemplo B — Bayes por simulación

**✅ Mejor caso.** Prevalencia 10 %: la simulación de la §2.4 da `p_enfermo_dado_positivo` ≈ 0.69; el test es útil porque la base no es despreciable.

**❌ Peor caso.** Prevalencia 0.1 %: la misma simulación da ≈ 0.02. Interpretar un positivo como "casi seguro enfermo" ignora que el 98 % son falsos positivos. La simulación evita el error que la intuición comete.

### Ejemplo C — Elección de distribución

**✅ Mejor caso.** Correos por minuto: Poisson ajusta y `muestras.mean()` ≈ `muestras.var()` ≈ λ, comprobable en los datos.

**❌ Peor caso.** Goles por partido con rachas y expulsiones: hay sobredispersión (varianza > media); ajustar Poisson subestima los extremos. El diagnóstico `var/mean ≫ 1` señala que el modelo es inadecuado.

### Ejemplo D — Priori bayesiana

**✅ Mejor caso.** Estimar la tasa de conversión de una web nueva con pocos datos: una priori débil `Beta(1,1)` (uniforme) deja hablar a los datos y entrega un intervalo creíble honesto.

**❌ Peor caso.** Usar una priori fuerte `Beta(50,1)` ("casi siempre convierte") sin justificación: la posteriori queda dominada por la creencia, no por la evidencia. La priori se volvió un sesgo disfrazado de método.

---

## 4. Apéndice — Caja de herramientas de Python (Clase 1)

Consolidación de todo lo introducido *just-in-time*, para que nada quede suelto.

| Tarea analítica | Herramienta | Nota |
|---|---|---|
| Importar datos | `pd.read_csv` | Base de todo el flujo. |
| Diagnóstico inicial | `df.shape`, `df.head`, `df.describe`, `df.info` | `describe` = estadística descriptiva condensada. |
| Categóricas | `df["c"].value_counts()` | Sustituto de `describe` en nominales. |
| Tendencia central | `mean`, `median`, `mode` | Elegir según asimetría. |
| Dispersión | `std(ddof=1)`, `var`, `quantile`, IQR | `ddof=1` = corrección de Bessel. |
| Frecuencias por clases | `pd.cut`, `value_counts` | Sturges: `1+log2(n)`. |
| Aleatoriedad reproducible | `np.random.default_rng(seed)` | Semilla fija = reproducibilidad. |
| Distribuciones | `scipy.stats` (`poisson`, `norm`, `binom`, `beta`) | PMF/PDF, `rvs`, `mean`, `interval`. |
| Simulación / Monte Carlo | operaciones vectorizadas de `numpy` + `.mean()` | Estimar probabilidades y esperanzas. |
| Gráfica básica | `matplotlib.pyplot` (`bar`, `hist`) | Se profundiza en la Clase 3. |

> **Cierre de la clase.** El alumno ya sabe *qué* hacer con una variable: resumir su centro y su dispersión sin engañarse, razonar su incertidumbre con probabilidad y Bayes, elegir la distribución que modela su mecanismo y estimar por Monte Carlo lo que no se puede calcular. Todo el Python visto surgió de esas necesidades. La Clase 2 pasa de describir a **concluir**: inferencia, regresión y la dinámica del azar en el tiempo.

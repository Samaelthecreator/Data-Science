# Análisis de Datos en Python — Curso Intensivo (8 horas)
### Temario detallado · 4 clases de 2 horas

> **Filosofía del curso.** Python y Pandas son *herramientas*, no el objetivo. El objetivo es enseñar **el proceso analítico** y el **pensamiento crítico estadístico**, con rigor de licenciatura en probabilidad y estadística. El código siempre llega *después* de la pregunta analítica y de la justificación teórica (el "por qué").

---

## Arquitectura pedagógica del curso

El curso está diseñado como una espiral, no como una lista lineal de temas. Los conceptos estadísticos formales se introducen en la Clase 1 y luego **reaparecen obligatoriamente** en las Clases 2, 3 y 4 con creciente exigencia (repetición espaciada). La regla de diseño es: *ningún ejercicio práctico de las Clases 3 y 4 puede resolverse sin volver a invocar al menos un concepto de la Clase 1.*

| Concepto base (Clase 1) | Reaparece en Clase 2 | Reaparece en Clase 3 | Reaparece en Clase 4 |
|---|---|---|---|
| Media vs. mediana / asimetría | Imputación de nulos | Lectura de histogramas | Limpieza de datos reales |
| Dispersión (σ, IQR) | `describe()`, percentiles | Boxplots y atípicos | Comparación entre grupos |
| Correlación / covarianza | — | Scatter plots, cuarteto de Anscombe | Relaciones espurias en datos reales |
| Distribuciones | Generación sintética | Forma esperada vs. observada | Ajuste a fenómenos reales |
| Inferencia / hipótesis | — | Validación visual previa | Prueba formal y conclusión |

---

# Clase 1 — Fundamentos del Pensamiento Analítico y Estadístico

**Duración:** 120 min · **Modalidad:** teoría con micro-demostraciones en Python (la herramienta se usa como pizarra, no como foco).

**Objetivos de aprendizaje.** Al finalizar, el estudiante podrá: (1) distinguir cuándo una medida resumen *engaña* y por qué; (2) construir e interpretar una distribución de frecuencias por clases; (3) razonar formalmente sobre incertidumbre usando probabilidad y distribuciones; (4) enunciar correctamente una prueba de hipótesis y explicar qué afirma —y qué *no* afirma— un p-valor; (5) diferenciar correlación, covarianza y causalidad.

| Bloque (min) | Tema / Concepto | Enfoque teórico — "El Por Qué" | Función en Python / Ejercicio |
|---|---|---|---|
| **0–15** | Apertura: ¿qué es analizar datos? El ciclo pregunta → dato → modelo → decisión. Diferencia entre *describir*, *inferir* y *predecir*. | Por qué el análisis empieza con una **pregunta**, no con un dataset. El dato no "habla solo": el analista impone una estructura. Sesgo de confirmación como riesgo central del pensamiento crítico. | Discusión guiada. Sin código aún, deliberadamente. |
| **15–40** | Estadística descriptiva I: tendencia central (media, mediana, moda). Robustez frente a atípicos. | Por qué la **mediana resiste** valores extremos y la media no (la media minimiza el error cuadrático; la mediana, el error absoluto). Por qué reportar la media de un ingreso o un precio de vivienda puede ser *deshonesto* en distribuciones asimétricas. | `np.mean`, `np.median`, `statistics.mode`. Demostración: insertar un outlier y observar qué medida se mueve. |
| **40–60** | Estadística descriptiva II: dispersión (rango, varianza, desviación estándar, IQR, coeficiente de variación) y **frecuencia por clases** (regla de Sturges, ancho de clase). | Por qué "el promedio sin la dispersión no significa nada" (dos clases con la misma media y distinta σ). Por qué `n−1` en la varianza muestral (corrección de Bessel / grados de libertad). Por qué agrupar en clases *pierde* información pero *revela* forma. | `np.std(ddof=1)`, `np.var`, cálculo de IQR con `np.percentile`. Construcción manual de una tabla de frecuencias. |
| **60–80** | Bases de probabilidad (nivel licenciatura): espacio muestral, axiomas de Kolmogórov, probabilidad condicional, independencia, **Teorema de Bayes**. | Por qué la probabilidad condicional es la base de *todo razonamiento bajo evidencia*. Por qué la intuición falla (paradoja de la prueba médica: alta sensibilidad ≠ alta probabilidad posterior). El "por qué" de la independencia: cuándo se puede multiplicar. | Simulación de Bayes con `np.random` (frecuencia relativa que converge a la probabilidad teórica). |
| **80–100** | Variables aleatorias y distribuciones principales: Bernoulli, Binomial, Poisson, Uniforme, **Normal**. Valor esperado E[X] y varianza como propiedades de la distribución. | Por qué cada distribución *modela un mecanismo generador* distinto (conteos raros → Poisson; éxito/fracaso → Binomial; suma de muchos efectos → Normal vía TLC). Por qué E[X] es el "centro de masa" y no necesariamente un valor observable. | `scipy.stats` (`norm`, `binom`, `poisson`): graficar PMF/PDF y comparar E[X] teórico vs. media simulada. |
| **100–120** | Inferencia: del estimador al **Teorema del Límite Central**, intervalos de confianza y **prueba de hipótesis** (H₀/H₁, error tipo I/II, α, p-valor). Covarianza y **correlación** (Pearson vs. Spearman). | Por qué inferimos: nunca tenemos la población, solo una muestra. Qué afirma realmente un p-valor (probabilidad del dato bajo H₀, **no** la probabilidad de que H₀ sea cierta). Por qué correlación ≠ causalidad y por qué Pearson solo capta relaciones *lineales*. | `scipy.stats.ttest_1samp`, `pearsonr`, `spearmanr`. Demostración del TLC promediando muestras de una distribución no normal. |

**Cierre / tarea puente:** cada estudiante anota una pregunta de investigación propia y qué medida descriptiva e hipótesis usaría. Se retomará en la Clase 4.

---

# Clase 2 — Herramientas Analíticas (Pandas Fundamentals)

**Duración:** 120 min · **Modalidad:** laboratorio guiado. *Toda* operación de Pandas se justifica con su contraparte estadística de la Clase 1.

**Objetivos de aprendizaje.** El estudiante podrá: (1) explicar la diferencia estructural entre `Series` y `DataFrame` y el rol del índice; (2) crear, importar y **generar datasets sintéticos controlados**; (3) explorar un dataset con los métodos básicos e interpretarlos estadísticamente; (4) filtrar e imputar nulos *eligiendo la medida correcta según la forma de la distribución*; (5) evitar los errores idiomáticos más comunes (`inplace`, `axis`, encadenamiento).

| Bloque (min) | Tema / Concepto | Enfoque teórico — "El Por Qué" | Función en Python / Ejercicio repetitivo |
|---|---|---|---|
| **0–10** | Repaso activo de la Clase 1 (recuperación). ¿Por qué necesitamos una herramienta tabular? Del array de NumPy al DataFrame. | Por qué el dato real es *tabular y etiquetado*: las filas son observaciones (unidades muestrales) y las columnas son variables. Conexión directa con "muestra" de la Clase 1. | Preguntas relámpago: "¿media o mediana para precios?" (re-anclaje del concepto). |
| **10–30** | Objetos `Series` y `DataFrame`: el índice como ciudadano de primera clase, `dtype`, alineación por etiqueta. | Por qué Pandas *no es una hoja de cálculo*: alinea por índice, no por posición. Por qué el `dtype` correcto (categórico vs. numérico) determina qué estadística es válida. | Construir una `Series` y un `DataFrame` a mano; inspeccionar `.index`, `.dtypes`. |
| **30–50** | Creación, importación y **generación de DataFrames sintéticos** (`read_csv`, `pd.DataFrame`, `np.random` con semilla fija). | Por qué los datos sintéticos son didácticamente superiores al inicio: **conocemos la verdad** (la media real, la σ real) y podemos verificar si el método la recupera. Por qué fijar la semilla = reproducibilidad científica. | `pd.DataFrame`, `np.random.default_rng(seed)`. Generar una columna `Normal(μ,σ)` *conocida* para usarla en la Clase 3. |
| **50–65** | Métodos de exploración: `head`, `tail`, `shape`, `columns`, `info`, `dtypes`, **`describe`**. | Por qué `describe()` es la Clase 1 condensada: count, media, σ, min, **cuartiles**, max. Leerlo como diagnóstico (¿media ≫ mediana? → asimetría a la derecha, *antes* de graficar). | `df.describe()`, `df.info()`. Ejercicio: predecir la asimetría solo leyendo media vs. percentil 50. |
| **65–85** | Selección y filtrado: `loc`, `iloc`, máscaras booleanas, condiciones múltiples. | Por qué el filtrado es *submuestreo* y cambia la población de referencia (riesgo de sesgo de selección). Por qué `loc` (etiqueta) e `iloc` (posición) no son intercambiables. | `df.loc[mask]`, `df[(c1) & (c2)]`. Ejercicio: filtrar y recalcular la media → discutir cómo cambió la muestra. |
| **85–105** | Valores nulos: detección (`isna`, `sum`) e **imputación** (`fillna` con media, mediana, moda; `dropna`). | **(Concepto eje del "por qué")** Por qué imputar con la **mediana en distribuciones asimétricas** (la media arrastra el sesgo del outlier hacia el valor imputado y deforma la distribución); por qué la media solo es defendible en datos simétricos; por qué borrar filas puede sesgar si los nulos *no* son aleatorios (MCAR vs. MNAR). | `df.isna().sum()`, `df['x'].fillna(df['x'].median())`. Ejercicio: imputar la *misma* columna con media y con mediana, comparar histograma resultante. |
| **105–120** | `inplace`, `axis` y **errores más comunes**: `SettingWithCopyWarning`, indexación encadenada, confundir `axis=0/1`, mutación silenciosa. | Por qué `inplace=True` está cayendo en desuso (rompe el encadenamiento y oculta copias); por qué `axis=0` = "a lo largo de las filas" confunde a todos y cómo razonarlo. Por qué un *warning* no es un error pero sí una bandera roja. | Reproducir a propósito un `SettingWithCopyWarning` y corregirlo con `.loc`. Tabla-resumen de errores. |

**Cierre:** el DataFrame sintético creado aquí se "ensucia" con nulos y atípicos y se entrega como insumo de la Clase 3.

---

# Clase 3 — Visualización y Análisis Controlado (Casos Sintéticos)

**Duración:** 120 min · **Modalidad:** laboratorio iterativo. Se trabaja con **datasets sintéticos diseñados** para exhibir un comportamiento estadístico concreto, de modo que la verdad sea conocida y el estudiante *verifique* en lugar de adivinar.

**Objetivos de aprendizaje.** El estudiante podrá: (1) elegir el gráfico correcto según el tipo y número de variables; (2) usar el histograma para diagnosticar forma, asimetría y modas; (3) detectar atípicos con boxplot y regla IQR, conectándolo con la decisión de imputación; (4) interpretar un scatter plot y entender por qué un coeficiente de correlación puede mentir (cuarteto de Anscombe); (5) ejecutar un ciclo iterativo "hipótesis visual → cálculo → revisión".

| Bloque (min) | Tema / Concepto | Enfoque teórico — "El Por Qué" | Función en Python / Ejercicio repetitivo |
|---|---|---|---|
| **0–10** | Repaso (recuperación espaciada): ¿qué medidas de la Clase 1 vamos a *ver* hoy? Por qué visualizar antes de modelar. | Por qué el ojo detecta patrones que un resumen numérico esconde. Introducción del **cuarteto de Anscombe** como advertencia: misma media, misma σ, misma correlación... cuatro realidades distintas. | Preview de las 4 nubes de Anscombe (gancho). |
| **10–30** | Histogramas y distribución de frecuencias. Efecto del número de *bins*. Simetría, asimetría, bimodalidad. | Por qué el histograma es la versión gráfica de la tabla de frecuencias (Clase 1) y por qué un `bin` mal elegido *fabrica o borra* estructura. Conexión: media vs. mediana ahora se *ven*. | `df.hist`, `plt.hist(bins=...)`. **Ejercicio repetitivo #1:** sobre un set asimétrico, recalcular media y mediana (Clase 1) y marcarlas sobre el histograma. |
| **30–50** | Boxplot y **detección de atípicos** (regla 1.5·IQR), comparación entre grupos. | Por qué el boxplot codifica los cuartiles e IQR de la Clase 1 y define formalmente "atípico". Por qué un atípico **no se borra por defecto**: puede ser error de medición *o* la observación más interesante (pensamiento crítico). | `df.boxplot`, `plt.boxplot`. **Ejercicio repetitivo #2:** detectar outliers, decidir si imputar (mediana, Clase 2) y recalcular la dispersión. |
| **50–70** | Scatter plots, relación entre dos variables y **cuarteto de Anscombe**. Correlación visual vs. numérica. | Por qué un mismo `r` de Pearson (Clase 1) corresponde a relaciones lineales, curvas, o dominadas por un único punto. Por qué *siempre* se grafica antes de confiar en un coeficiente. Pearson vs. Spearman revisitados. | `plt.scatter`, `df.corr`, `pearsonr`. **Ejercicio repetitivo #3:** calcular `r` en los 4 sets de Anscombe y comprobar que son (casi) idénticos pese a las nubes distintas. |
| **70–100** | **Bloque iterativo integrador.** Tres mini-datasets sintéticos: (A) asimetría fuerte, (B) outliers influyentes, (C) correlación espuria por variable de confusión. Ciclo: *conjeturar → graficar → medir → corregir → volver a medir*. | Por qué el análisis real es **iterativo y no lineal**: cada gráfico genera una nueva hipótesis. Por qué una correlación alta puede desaparecer al condicionar por una tercera variable (intro a confusión / paradoja de Simpson). Refuerzo simultáneo de tendencia central, dispersión, imputación y correlación. | Pipeline completo con Pandas + Matplotlib. Cada equipo documenta: medida elegida, gráfico, decisión y *justificación del porqué*. Reúso obligatorio de `describe`, `fillna(median)`, `corr`. |
| **100–120** | Síntesis: mapa "tipo de variable → gráfico correcto". Errores de visualización (ejes truncados, escalas engañosas, sobre-binning). | Por qué un gráfico es un *argumento* y puede manipular: ética de la visualización. Por qué elegir el gráfico equivocado es un error analítico, no estético. | Checklist de visualización. Mini-crítica de un gráfico "tramposo" preparado por el docente. |

**Cierre:** los tres patrones (asimetría, atípicos, confusión) quedan como "alertas" que el estudiante deberá reconocer en datos reales en la Clase 4.

---

# Clase 4 — Análisis del Mundo Real

**Duración:** 120 min · **Modalidad:** estudio de casos de alto impacto. Datos *reales, sucios y ambiguos*. Aquí toda la teoría se aplica de extremo a extremo.

**Objetivos de aprendizaje.** El estudiante podrá: (1) ejecutar un flujo analítico completo (pregunta → limpieza → EDA → inferencia → comunicación) sobre datos reales; (2) transferir las decisiones aprendidas con datos sintéticos a la ambigüedad del mundo real; (3) formular y probar una hipótesis con `scipy`; (4) interpretar resultados con honestidad crítica (incertidumbre, confusión, causalidad); (5) comunicar un insight de forma defendible.

| Bloque (min) | Tema / Concepto | Enfoque teórico — "El Por Qué" | Función en Python / Ejercicio repetitivo |
|---|---|---|---|
| **0–10** | Marco del análisis end-to-end. De la pregunta de la Clase 1 (tarea puente) al insight. Diferencia entre dato sintético (verdad conocida) y dato real (verdad desconocida). | Por qué en el mundo real *no hay respuesta correcta verificable*: el rigor lo aporta el método, no el resultado. Por qué documentar supuestos es parte de la ciencia. | Planteamiento de las preguntas de investigación de cada caso. |
| **10–35** | **Caso A — Ciencias sociales (Esperanza de vida / WHO).** Carga, inspección, limpieza: nulos e inconsistencias reales. | Por qué los datos reales llegan con nulos *no aleatorios* (países con menos infraestructura reportan menos): decidir imputación (mediana, Clase 2) **con conciencia del sesgo**. Reúso de `describe` para diagnosticar asimetría antes de actuar. | `read_csv`, `isna().sum()`, `fillna(median)`, `describe`. **Repetición:** media vs. mediana, ahora con consecuencias reales. |
| **35–60** | Caso A (cont.): EDA, correlación y **prueba de hipótesis** (p. ej. ¿difiere la esperanza de vida entre grupos de ingreso?). Correlación ≠ causalidad. | Por qué una correlación fuerte (escolaridad ↔ esperanza de vida) **no autoriza** una conclusión causal: variables de confusión, causalidad inversa. Qué concluye y qué *no* concluye el p-valor (re-anclaje Clase 1). | `corr`, `scatter`, `ttest_ind`. **Repetición:** Pearson/Spearman + interpretación crítica del p-valor. |
| **60–85** | **Caso B — Ciencias naturales (Temperatura global / Berkeley Earth).** Serie temporal, tendencia, anomalías, variabilidad estacional. | Por qué una *tendencia* no es una *fluctuación*: distinguir señal de ruido. Por qué la dispersión (σ, Clase 1) define qué cambio es "anómalo". Por qué el rango temporal y la línea base elegidos cambian la narrativa (pensamiento crítico). | `resample`/agrupación temporal, media móvil, `plt.plot`, detección de anomalías por IQR. **Repetición:** atípicos y dispersión sobre datos reales. |
| **85–105** | Síntesis comparativa de ambos casos: ¿qué tienen en común una pregunta social y una natural? Comunicación del insight (1 gráfico + 1 frase defendible). | Por qué el *mismo* andamiaje estadístico sirve para dominios distintos: la transferencia es la prueba de que se aprendió el proceso, no la herramienta. Por qué un buen insight es falsable y acotado en incertidumbre. | Cada equipo produce una "ficha de hallazgo": afirmación, evidencia, limitación. |
| **105–120** | Cierre del curso: checklist analítico permanente, catálogo de sesgos (selección, supervivencia, confusión, p-hacking), próximos pasos. | Por qué el pensamiento crítico es el verdadero entregable: la herramienta cambiará, el método no. Por qué reportar la incertidumbre y los límites es señal de madurez analítica, no de debilidad. | Entrega del checklist reutilizable. Reflexión final conectada con la pregunta inicial de la Clase 1. |

---

## Datasets reales sugeridos para la Clase 4

Los tres cumplen los requisitos del curso: son **públicos**, están **vigentes y descargables**, contienen **nulos e imperfecciones reales** (forzando el reúso de la imputación y el diagnóstico de la Clase 2), y permiten aplicar correlación, comparación de grupos e inferencia. Cubren los dos dominios solicitados (ciencias sociales y ciencias naturales) más bienes raíces como caso clásico de regresión/EDA.

**1. Bienes raíces — Ames Housing (De Cock, 2011).**
Aproximadamente 2.930 ventas de viviendas en Ames, Iowa (2006–2010) con ~80 variables (área, calidad, año, barrio, precio). Ideal para tendencia central robusta (precio con fuerte asimetría a la derecha → media vs. mediana), atípicos y correlación precio↔superficie. Tiene nulos *significativos* (p. ej. `PoolQC`, `Alley`) que obligan a razonar la imputación. Descarga: documentación oficial en el [Journal of Statistics Education (De Cock)](https://jse.amstat.org/v19n3/decock/DataDocumentation.txt), versión limpia en [OpenIntro](https://www.openintro.org/data/index.php?data=ames) y en [Kaggle](https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset).

**2. Clima / ciencias naturales — Berkeley Earth, Temperatura Superficial Global.**
Series de temperatura/anomalías a escala global, nacional y local, en CSV y NetCDF. Excelente para series temporales, tendencia vs. ruido, media móvil y detección de anomalías por dispersión. Licencia CC BY-NC. Portal oficial: [berkeleyearth.org/data](https://berkeleyearth.org/data/); versión histórica popular en [Kaggle: Earth Surface Temperature Data](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data).

**3. Salud / ciencias sociales — WHO Life Expectancy (Global Health Observatory).**
193 países, 2000–2015, 22 columnas (mortalidad, inmunización, VIH, GDP, escolaridad, IMC, esperanza de vida). Perfecto para correlación, comparación de grupos (`ttest_ind`), discusión de confusión y de correlación≠causalidad, y manejo de nulos no aleatorios. Descarga: [Kaggle: Life Expectancy (WHO)](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who). Alternativa socioeconómica con la misma lógica: [Gapminder](https://www.gapminder.org/data/) (esperanza de vida, GDP per cápita, población por país).

> **Nota de diseño.** Recomiendo asignar Ames o WHO al **Caso A (social)** y Berkeley Earth al **Caso B (natural)**, dejando el tercero como dataset de práctica/tarea para reforzar la repetición espaciada fuera del aula.

---

### Resumen de cumplimiento de las restricciones pedagógicas

- **Repetición espaciada:** cada bloque de las Clases 3 y 4 marca explícitamente el reúso obligatorio de conceptos de la Clase 1 (media/mediana, σ/IQR, correlación, hipótesis), con ejercicios numerados e iterativos.
- **Enfoque en el "por qué":** la columna central de cada tabla justifica el método (caso testigo: imputar con mediana en distribuciones asimétricas porque la media arrastra el sesgo del outlier y deforma la distribución), no solo el "cómo".
- **Tiempos:** cada clase suma exactamente 120 minutos.
- **Progresión:** teoría (1) → herramienta (2) → verificación controlada con verdad conocida (3) → aplicación real con verdad desconocida (4).

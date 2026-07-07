# Análisis de Datos en Python — Curso Intensivo (versión 2.0)
### Temario reestructurado · 4 sesiones

> **Cambio de filosofía respecto a la v1.0.** Python deja de tener una clase propia. El lenguaje se enseña **"según se necesita"** (*just-in-time*): primero se explica el concepto estadístico y, en el momento en que hace falta una herramienta —un filtro, una operación, una gráfica— se recurre a Python. La apuesta pedagógica es explícita: *es más valioso saber **qué** hacer con los datos (el análisis) y luego buscar qué código lo ejecuta, que dominar la sintaxis sin saber qué análisis aplicar.* Por eso los fundamentos estadísticos ganan tiempo y la explicación del lenguaje se reduce a lo que cada tema exige.

---

## Estructura general

| Sesión | Título | Rol |
|---|---|---|
| **Clase 1** | Fundamentos I — Pensamiento analítico, estadística descriptiva y probabilidad | Todo el bloque descriptivo y probabilístico, con Python JIT. |
| **Clase 2** | Fundamentos II — Inferencia, asociación, regresión y cálculo estocástico | Cierre teórico: del dato a la conclusión, con Python JIT. |
| **Clase 3** | Visualización y análisis controlado (casos sintéticos) | **Sin cambios** respecto a la v1.0. |
| **Clase 4** | Análisis del mundo real | **Sin cambios** respecto a la v1.0. |

Las Clases 1 y 2 juntas cubren —y amplían— todo el contenido del antiguo "Módulo 1 (fundamentos estadísticos)". El antiguo módulo dedicado a Pandas se **disuelve**: sus herramientas (DataFrame/Series, filtrado, imputación, `describe`, `axis`, errores comunes) aparecen distribuidas en el punto exacto donde el análisis las reclama, y quedan consolidadas en el **Apéndice de herramientas de Python** al final de cada clase para garantizar que nada se pierda.

---

## Principio operativo "Just-in-Time"

En cada tema se sigue el mismo patrón de tres pasos:

1. **Concepto** — se desarrolla la teoría (qué es, qué supone, cuándo es idóneo y cuándo no).
2. **Necesidad** — surge una tarea concreta que exige cómputo (calcular, filtrar, simular, graficar).
3. **Herramienta** — se introduce **solo** la pieza de Python que resuelve esa tarea, con su porqué.

El código nunca precede a la pregunta analítica. El alumno termina el curso con un criterio estadístico sólido y un repertorio de Python *anclado a problemas reales*, no a una lista de funciones memorizadas.

---

## Clase 1 — Fundamentos I: pensamiento analítico, descriptiva y probabilidad

**Objetivo.** Que el estudiante razone sobre un conjunto de datos: qué medida resume sin engañar, cómo describir su dispersión y forma, y cómo cuantificar la incertidumbre con probabilidad y distribuciones. Python entra como calculadora y como laboratorio de simulación.

**Secuencia temática (flujo, sin bloques de tiempo):**

1. El proceso analítico y el pensamiento crítico. *(Python JIT: cargar un dataset, `shape`, `head`, `describe` como primer diagnóstico.)*
2. Tendencia central: media, mediana, moda; robustez y asimetría. *(Python JIT: `mean`, `median`, `mode`; efecto de un atípico.)*
3. Dispersión: rango, varianza, desviación estándar, IQR, coeficiente de variación; frecuencias por clases. *(Python JIT: `std(ddof=1)`, `quantile`, tabla de frecuencias, primer histograma.)*
4. Probabilidad de licenciatura: espacio muestral, axiomas, condicional, independencia y **Teorema de Bayes**. *(Python JIT: simulación de frecuencias con `numpy.random`, verificación de Bayes.)*
5. **Introducción a la inferencia bayesiana** (nuevo): priori, verosimilitud, posteriori; actualización de creencias. *(Python JIT: cálculo y gráfica de una posteriori simple.)*
6. Variables aleatorias y distribuciones: Bernoulli, Binomial, Poisson, Uniforme, Normal; valor esperado y varianza. *(Python JIT: `scipy.stats`, PMF/PDF, media simulada vs. teórica.)*
7. **Primer contacto con Monte Carlo** (puente a la Clase 2): estimar probabilidades y esperanzas por simulación.

**Apéndice de herramientas de Python de la Clase 1.**

---

## Clase 2 — Fundamentos II: inferencia, asociación, regresión y estocástico

**Objetivo.** Cerrar el arco teórico: pasar de la muestra a la conclusión (inferencia), medir relaciones (correlación y regresión) e introducir la dinámica del azar en el tiempo (cálculo estocástico aplicado). Python entra como motor de inferencia y de simulación de procesos.

**Secuencia temática (flujo, sin bloques de tiempo):**

1. De la muestra a la población: estimadores, error estándar y **Ley de los Grandes Números**. *(Python JIT: simular la LGN promediando muestras crecientes.)*
2. **Teorema del Límite Central**: por qué aparece la Normal. *(Python JIT: histograma de medias muestrales de una distribución no normal.)*
3. Intervalos de confianza: construcción e interpretación frecuentista correcta. *(Python JIT: IC con `scipy.stats`.)*
4. Pruebas de hipótesis: H₀/H₁, errores tipo I/II, α, **p-valor**, potencia. *(Python JIT: `ttest_1samp`, `ttest_ind`.)*
5. Asociación: covarianza y correlación (Pearson vs. Spearman). *(Python JIT: `corr`, `pearsonr`, `spearmanr`.)*
6. **Regresión lineal** simple y múltiple (nuevo): ajuste, coeficientes, R², residuos y supuestos. *(Python JIT: `numpy.polyfit` y `statsmodels`/`scikit-learn`; diagnóstico de residuos.)*
7. **Introducción al cálculo estocástico aplicado** (nuevo): procesos aleatorios, **caminata aleatoria**, **cadenas de Markov** y **Monte Carlo**. *(Python JIT: simular una caminata aleatoria, una cadena de Markov y una estimación Monte Carlo.)*

**Apéndice de herramientas de Python de la Clase 2.**

---

## Clase 3 — Visualización y análisis controlado (sin cambios)

Histogramas, boxplots y detección de atípicos, dispersión y cuarteto de Anscombe, ciclo iterativo sobre datasets sintéticos (asimetría, outliers, confusión) y honestidad visual. Materiales: `Clase3_DOCENTE_resuelto.ipynb`, `Clase3_ALUMNO_ejercicios.ipynb` y los tres CSV sintéticos. Ver `Clase_3_Visualizacion_Analisis_Controlado.md`.

## Clase 4 — Análisis del mundo real (sin cambios)

Flujo end-to-end sobre datos reales (Ames Housing, Berkeley Earth, WHO Life Expectancy): limpieza, EDA, inferencia, series temporales y comunicación de insights, con vigilancia de sesgos. Ver `Clase_4_Analisis_Mundo_Real.md`.

---

## Trazabilidad de la repetición espaciada (actualizada)

| Concepto base (Clases 1–2) | Reaparece en Clase 3 | Reaparece en Clase 4 |
|---|---|---|
| Media vs. mediana / asimetría | Lectura de histogramas | Limpieza de datos reales |
| Dispersión (σ, IQR) | Boxplots y atípicos | Comparación entre grupos |
| Correlación / regresión | Scatter, Anscombe | Relaciones (¿espurias?) en datos reales |
| Distribuciones / Monte Carlo | Forma esperada vs. observada | Ajuste a fenómenos reales |
| Inferencia / hipótesis | Validación visual previa | Prueba formal y conclusión |

---

## Datasets reales para la Clase 4 (sin cambios)

Bienes raíces (**Ames Housing**), clima (**Berkeley Earth**) y salud/sociales (**WHO Life Expectancy**). Detalles y enlaces en el documento de la Clase 4 y en el temario v1.0.

---

### Nota de versión
Esta v2.0 conserva íntegras las Clases 3 y 4. Los cambios se concentran en: (1) fusionar teoría estadística y Python en las Clases 1 y 2 bajo el enfoque *just-in-time*; (2) ampliar el Módulo 1 con **inferencia bayesiana**, **regresión lineal** y una **introducción aplicada al cálculo estocástico** (procesos aleatorios, caminata aleatoria, cadenas de Markov y Monte Carlo).

# Clase 4 — Análisis del Mundo Real

> **Documento de desarrollo académico.** Redactado desde el rol de un profesional con maestría en cálculo estadístico y estocástico, enfoque en cómputo estadístico. Aquí toda la teoría se aplica de extremo a extremo sobre datos **reales, sucios y ambiguos**, donde la verdad ya no viene inyectada. El rigor lo aporta el **método**, no un resultado verificable. Casos de referencia: *Ames Housing* (bienes raíces), *Berkeley Earth* (clima, ciencias naturales) y *WHO Life Expectancy* (salud, ciencias sociales).
>
> **Estructura:** (1) Glosario; (2) Desarrollo con casos idóneos y no idóneos; (3) Ejemplos con el mejor y el peor caso.

---

## 1. Glosario de conceptos

| # | Concepto | Definición operativa |
|---|---|---|
| 1 | **Flujo analítico end-to-end** | Ciclo pregunta → datos → limpieza → EDA → inferencia → comunicación. |
| 2 | **EDA (análisis exploratorio)** | Fase iterativa de graficar y resumir para formular hipótesis. |
| 3 | **Data cleaning** | Detección y tratamiento de nulos, duplicados, tipos e inconsistencias. |
| 4 | **Prueba $t$ (dos muestras)** | Compara las medias de dos grupos. |
| 5 | **ANOVA** | Compara las medias de tres o más grupos. |
| 6 | **Prueba $\chi^2$** | Evalúa asociación entre dos variables categóricas. |
| 7 | **Tamaño del efecto** | Magnitud de la diferencia (p. ej. $d$ de Cohen), independiente de $n$. |
| 8 | **Confusión (real)** | Variable de fondo que explica una asociación observacional. |
| 9 | **Causalidad vs. correlación** | Una asociación no autoriza una conclusión causal sin diseño o supuestos. |
| 10 | **Serie temporal** | Observaciones ordenadas en el tiempo; permite tendencia y estacionalidad. |
| 11 | **Tendencia** | Componente de largo plazo de una serie. |
| 12 | **Estacionalidad** | Patrón periódico (diario, anual). |
| 13 | **Media móvil** | Promedio en ventana deslizante; suaviza ruido para revelar tendencia. |
| 14 | **Anomalía** | Desviación respecto de la línea base esperada. |
| 15 | **Línea base (baseline)** | Período de referencia contra el que se miden anomalías; su elección cambia la narrativa. |
| 16 | **Sesgo de selección** | La muestra no representa a la población objetivo. |
| 17 | **Sesgo de supervivencia** | Solo se observan los casos que "sobrevivieron" a un filtro. |
| 18 | **p-hacking** | Probar múltiples hipótesis y reportar solo lo significativo. |
| 19 | **Comparaciones múltiples** | Inflación del error tipo I al hacer muchas pruebas; corrección Bonferroni/FDR. |
| 20 | **Reproducibilidad** | Que otro obtenga el mismo resultado con los mismos datos y código (semilla, versiones). |
| 21 | **Insight defendible** | Afirmación falsable, acotada en incertidumbre y en su alcance. |

---

## 2. Desarrollo de cada concepto: cuándo es idóneo y cuándo no

### 2.1 El flujo analítico y la limpieza

El análisis real es **iterativo**, no lineal: cada gráfico genera una hipótesis que obliga a volver atrás. La limpieza consume la mayor parte del tiempo y es donde se reutilizan las decisiones de la Clase 2 (imputar con mediana en variables asimétricas, `dropna` solo si el mecanismo lo permite). La diferencia con los datos sintéticos es que aquí **no conocemos la verdad**: la honestidad metodológica reemplaza a la verificación.

- *Idóneo:* documentar cada decisión de limpieza y su supuesto; versionar datos y código con semilla.
- *No sirve:* "limpiar" hasta que el resultado confirme la hipótesis previa (equivale a fabricar el resultado).

### 2.2 Pruebas de hipótesis sobre datos reales

- **Prueba $t$:** comparar dos medias (p. ej. esperanza de vida entre países de ingreso alto vs. bajo). Supone independencia y, en su versión clásica, aproximada normalidad de las medias (respaldada por el TLC si $n$ es suficiente).
- **ANOVA:** tres o más grupos; evita inflar el error tipo I que resultaría de muchas pruebas $t$ por pares.
- **$\chi^2$:** asociación entre categóricas (p. ej. región × nivel de inmunización).

- *Idóneo:* con hipótesis, $\alpha$ y diseño fijados **antes** de mirar los datos, y reportando el **tamaño del efecto** junto al p-valor.
- *No sirve:* con $n$ enorme, donde diferencias triviales salen "significativas" (reportar siempre magnitud); con muchos contrastes sin corrección (comparaciones múltiples); como sustituto de un diseño causal.

### 2.3 Correlación, causalidad y confusión en datos observacionales

En datos no experimentales, casi toda asociación está potencialmente confundida. Antes de insinuar causalidad hay que preguntarse: ¿existe una tercera variable que cause ambas? ¿podría ser causalidad inversa? La estrategia mínima es **condicionar** por confusores plausibles y mostrar que la asociación persiste; aun así, sin diseño experimental o supuestos causales explícitos, la conclusión se enuncia como asociación, no como causa.

- *Idóneo:* estratificar/controlar por confusores conocidos; declarar los no observados como limitación.
- *No sirve:* saltar de $r$ alto a "X causa Y"; controlar por un **mediador** (borra el efecto real).

### 2.4 Series temporales (clima)

Distinguir **tendencia** (largo plazo) de **ruido** y **estacionalidad** (periódico) es el corazón del análisis climático. La **media móvil** suaviza el ruido para revelar la tendencia; la dispersión (σ, IQR) define qué desviación es una **anomalía**. La elección de la **línea base** es una decisión con consecuencias narrativas: una base fría hace que todo parezca cálido y viceversa.

- *Idóneo:* medias móviles y anomalías respecto de una base transparente y justificada; suficiente historia para separar tendencia de ciclo.
- *No sirve:* concluir tendencia a partir de una ventana corta (confunde fluctuación con señal); comparar contra una línea base elegida para maximizar el efecto (cherry-picking del período).

### 2.5 Sesgos y reproducibilidad

Los sesgos son el enemigo silencioso: **selección** (la muestra no representa), **supervivencia** (solo se ven los que pasaron el filtro), **confusión** (tercera variable) y **p-hacking** (buscar hasta encontrar significancia). La reproducibilidad —semilla fija, versiones registradas, código compartido— es la defensa institucional contra el autoengaño.

- *Idóneo:* preguntarse "¿quién falta en estos datos?" antes de concluir; preinscribir hipótesis; publicar código y datos.
- *No sirve:* generalizar de una muestra sesgada a toda la población; presentar como confirmatorio un análisis exploratorio.

### 2.6 Comunicación del insight

Un buen hallazgo es **falsable, acotado en incertidumbre y limitado en alcance**. Se comunica idealmente con un gráfico honesto y una frase defendible que incluya la magnitud, la incertidumbre y las limitaciones. Reportar la incertidumbre no es debilidad: es madurez analítica.

---

## 3. Ejemplos: el mejor y el peor caso de uso

### Ejemplo A — Limpieza e imputación en *WHO Life Expectancy*

**✅ Mejor caso.** La columna `GDP` tiene nulos concentrados en países de bajos ingresos (mecanismo MAR/MNAR, no aleatorio). Se imputa la mediana **por grupo de región** (imputación condicional), se documenta el supuesto y se marca una bandera `gdp_imputado` para análisis de sensibilidad. La decisión es trazable y defendible.

**❌ Peor caso.** Se ejecuta `df.dropna()` sobre todo el `DataFrame`. Como los países con peores indicadores tienen más nulos, desaparecen justamente los casos más informativos: la esperanza de vida "promedio" sube artificialmente y el análisis concluye un mundo más sano de lo que es. El sesgo entró por la puerta de la limpieza.

### Ejemplo B — Prueba de hipótesis en *WHO*

**✅ Mejor caso.**
```python
from scipy import stats
alto = df[df["income_group"]=="alto"]["life_expectancy"]
bajo = df[df["income_group"]=="bajo"]["life_expectancy"]
t, p = stats.ttest_ind(alto, bajo, equal_var=False)   # Welch
d = (alto.mean()-bajo.mean())/np.sqrt((alto.std()**2+bajo.std()**2)/2)  # tamaño del efecto
```
Hipótesis definida de antemano, prueba de Welch (no asume varianzas iguales) y se reporta el **tamaño del efecto** (diferencia de ~18 años) junto al p-valor. La conclusión distingue significancia de magnitud y se enuncia como asociación.

**❌ Peor caso.** Se corre `ttest_ind` entre 30 pares de subgrupos improvisados, se encuentra uno con $p=0.04$ y se titula "diferencia significativa" sin corregir por comparaciones múltiples ni reportar el efecto. Con $\alpha=0.05$ y 30 pruebas, ~1.5 falsos positivos son esperables por puro azar: el hallazgo es probablemente ruido.

### Ejemplo C — Correlación vs. causalidad en *WHO*

**✅ Mejor caso.** Se observa correlación fuerte entre `schooling` y `life_expectancy`. Antes de concluir, se **estratifica por ingreso** y se discute que ambos dependen del desarrollo económico. Se comunica: "escolaridad y esperanza de vida están asociadas; parte de la relación se explica por el ingreso; con datos observacionales no podemos aislar causalidad".

**❌ Peor caso.** Se reporta "más años de escuela **causan** más años de vida, luego invertir en educación aumentará la longevidad X años", extrapolando una regresión observacional a una política, sin controlar confusores ni reconocer la causalidad inversa (países más ricos tienen más de ambas).

### Ejemplo D — Serie temporal en *Berkeley Earth*

**✅ Mejor caso.**
```python
serie = df.set_index("date")["temp_anomaly"]
serie.rolling(120).mean().plot()   # media móvil de 10 años sobre datos mensuales
```
Una media móvil larga separa la tendencia de la variabilidad interanual; las anomalías se miden contra una línea base explícita (p. ej. 1951–1980, la de referencia estándar). La afirmación resultante acota período, base e incertidumbre.

**❌ Peor caso.** Se toman dos años consecuivos, uno frío y otro cálido, y se proclama una tendencia. O peor, se elige la línea base más fría del registro para maximizar la anomalía. Confundir ruido de corto plazo con señal, o manipular la base, produce narrativas opuestas con los mismos datos: es *cherry-picking* temporal.

### Ejemplo E — *Ames Housing* y la asimetría del precio

**✅ Mejor caso.** `SalePrice` es fuertemente asimétrico. Para el resumen se usa la **mediana**; para modelar, se transforma con **logaritmo** (linealiza y estabiliza la varianza), se detectan atípicos con IQR y se estudia la correlación `GrLivArea`↔`SalePrice` tras el log. Cada paso reutiliza la Clase 1 y la 3.

**❌ Peor caso.** Se reporta el precio **medio** como "precio típico" (inflado por mansiones), se ajusta una regresión lineal sobre el precio crudo (residuos con forma de embudo por heterocedasticidad) y se conserva un atípico de un terreno agrícola como si fuera una casa. Las tres decisiones ignoran la asimetría y contaminan la conclusión.

### Ejemplo F — Sesgo de supervivencia (transversal)

**✅ Mejor caso.** Al estudiar "hábitos de empresas exitosas", se incluye deliberadamente una muestra de empresas fracasadas para comparar; solo así los hábitos "ganadores" son distinguibles del azar.

**❌ Peor caso.** Se analizan únicamente las empresas que hoy existen y se concluye que su estrategia causa el éxito. Las que aplicaron la misma estrategia y quebraron no están en los datos (no "sobrevivieron"), así que la conclusión está sesgada por construcción —el mismo error que el análisis de los aviones de la Segunda Guerra Mundial que solo veían los que regresaban—.

---

## 4. Síntesis de la clase y cierre del curso

La Clase 4 demuestra que el **mismo andamiaje estadístico** sirve para una pregunta social (WHO) y una natural (Berkeley Earth): esa transferencia es la prueba de que se aprendió el *proceso*, no la *herramienta*. Los datos reales añaden dos exigencias sobre los sintéticos: la limpieza honesta (porque no hay verdad que verificar) y la vigilancia de los sesgos (selección, supervivencia, confusión, p-hacking). El entregable final del curso no es un gráfico ni un p-valor, sino un **criterio**: reconocer el mecanismo generador, elegir la herramienta cuyo supuesto coincide con él, condicionar ante la confusión, y comunicar hallazgos falsables que declaren su incertidumbre y sus límites. La herramienta cambiará; el método, no.

---

> **Nota sobre sensibilidad de datos.** Los casos de salud (esperanza de vida, mortalidad) tocan temas delicados. Al comunicarlos conviene evitar conclusiones causales apresuradas sobre poblaciones vulnerables y presentar la incertidumbre con claridad; el objetivo pedagógico es el rigor, no titulares.

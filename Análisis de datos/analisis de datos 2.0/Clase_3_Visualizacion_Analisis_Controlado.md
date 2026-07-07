# Clase 3 — Visualización y Análisis Controlado (Casos Sintéticos)

> **Documento de desarrollo académico.** Redactado desde el rol de un profesional con maestría en cálculo estadístico y estocástico, enfoque en cómputo estadístico. La visualización no es decoración: es un **instrumento de verificación** de la estadística de la Clase 1 y un **argumento** que puede iluminar o engañar. Trabajamos con datasets sintéticos de verdad conocida (`dataset_A_asimetria`, `dataset_B_outliers`, `dataset_C_confusion`), de modo que podamos contrastar lo que el gráfico sugiere contra la verdad inyectada.
>
> **Estructura:** (1) Glosario; (2) Desarrollo con casos idóneos y no idóneos; (3) Ejemplos con el mejor y el peor caso.

---

## 1. Glosario de conceptos

| # | Concepto | Definición operativa |
|---|---|---|
| 1 | **Histograma** | Gráfico de frecuencias por clases de una variable continua. Versión visual de la tabla de frecuencias. |
| 2 | **`bins` (clases)** | Número/ancho de intervalos del histograma. Gobierna el equilibrio sesgo–ruido. |
| 3 | **Regla de Sturges** | $k=1+\log_2 n$: heurística para elegir el número de clases. |
| 4 | **KDE (densidad kernel)** | Estimación suave de la densidad; alternativa continua al histograma. |
| 5 | **Escala logarítmica** | Transformación que linealiza colas pesadas y relaciones multiplicativas. |
| 6 | **Diagrama de caja (boxplot)** | Resumen visual de mediana, cuartiles, IQR y atípicos. |
| 7 | **Regla $1.5\times$IQR** | Umbral de atípico: fuera de $[Q_1-1.5\,\text{IQR},\,Q_3+1.5\,\text{IQR}]$. |
| 8 | **Atípico (outlier)** | Observación anómalamente lejana. Puede ser error o señal genuina. |
| 9 | **Apalancamiento (leverage)** | Influencia de un punto por su posición extrema en $x$; distorsiona ajustes y correlaciones. |
| 10 | **Diagrama de dispersión (scatter)** | Grafica dos variables numéricas; base para juzgar relación y forma. |
| 11 | **Cuarteto de Anscombe** | Cuatro conjuntos con idéntica media, varianza y $r$, pero nubes distintas. |
| 12 | **Correlación espuria** | Asociación estadística sin vínculo causal directo. |
| 13 | **Variable de confusión** | Tercera variable que causa a las otras dos y genera correlación aparente. |
| 14 | **Correlación parcial** | Correlación entre $X$ e $Y$ tras remover el efecto de una tercera variable $Z$. |
| 15 | **Paradoja de Simpson** | Una tendencia que se invierte al condicionar por un grupo. |
| 16 | **Eje truncado** | Eje que no arranca en cero (o recortado), exagerando diferencias. |
| 17 | **Sobre-/sub-binning** | Demasiadas clases (ruido) o muy pocas (oculta estructura). |
| 18 | **Mapa variable→gráfico** | Criterio de selección del gráfico según tipo y número de variables. |

---

## 2. Desarrollo de cada concepto: cuándo es idóneo y cuándo no

### 2.1 Histograma

Traduce la distribución de frecuencias a imagen y permite *ver* simetría, modas y asimetría. Su parámetro crítico es el número de clases: pocas ocultan estructura (sub-binning); demasiadas la fragmentan en ruido (sobre-binning). Sturges es un punto de partida, no un dogma, y falla con $n$ grande o muy asimétrico.

- *Idóneo cuando:* una variable continua, $n$ moderado/grande, se busca forma global.
- *No sirve cuando:* $n$ es pequeño (la forma es artefacto del binning) o la variable es categórica (usar barras). Con colas muy pesadas, conviene **escala logarítmica** para que la cola no aplaste el cuerpo.

### 2.2 KDE y escala logarítmica

La KDE suaviza el histograma pero introduce su propio parámetro (el ancho de banda): demasiado ancho borra modas, demasiado estrecho inventa picos. La escala log es la herramienta natural para ingresos, precios o poblaciones, donde lo relevante es el orden de magnitud.

- *No sirve:* KDE con datos acotados (fuga de densidad más allá del límite físico, p. ej. densidad positiva en edades negativas); escala log con ceros o negativos.

### 2.3 Boxplot y detección de atípicos

Codifica los cuartiles y el IQR (Clase 1) y define atípico con la regla $1.5\times$IQR. Es insuperable para **comparar la dispersión de varios grupos** de un vistazo. Su límite: oculta la forma interna (no distingue unimodal de bimodal) porque solo muestra cinco números.

- *Idóneo:* comparar grupos; señalar atípicos candidatos; distribuciones asimétricas.
- *No sirve:* como única vista de una distribución (puede esconder bimodalidad); con muestras minúsculas (los cuartiles son inestables). **Detectar un atípico no autoriza a borrarlo:** primero hay que decidir si es error o señal.

### 2.4 Scatter y el cuarteto de Anscombe

El diagrama de dispersión es el juez de cualquier coeficiente de correlación. Anscombe demuestra el principio rector: **cuatro nubes distintas comparten el mismo $r=0.816$**. Por eso el gráfico **precede** al número. Añadir la recta de ajuste ayuda, pero también puede sugerir linealidad donde no la hay.

- *Idóneo:* dos variables continuas; juzgar forma (lineal, curva), dispersión y outliers antes de calcular $r$.
- *No sirve:* con muchísimos puntos superpuestos (overplotting) → usar transparencia, hexbin o densidad; con variables categóricas.

### 2.5 Confusión, correlación espuria y correlación parcial

Una correlación alta entre $X$ e $Y$ puede provenir de una **variable de confusión** $Z$ que causa ambas. La prueba diagnóstica es condicionar: calcular la correlación **dentro** de franjas de $Z$ o la correlación parcial. Si la asociación se desvanece al fijar $Z$, era espuria. La paradoja de Simpson es el caso extremo: la tendencia global se **invierte** dentro de cada grupo.

- *Idóneo:* siempre que dos variables observacionales correlacionen y se sospeche un factor común (temperatura, edad, nivel socioeconómico).
- *No sirve / limita:* condicionar por una variable que en realidad es un **mediador** (está en la cadena causal $X\to Z\to Y$) elimina el efecto que sí queremos medir. Distinguir confusor de mediador exige razonamiento causal, no solo estadística.

### 2.6 Selección del gráfico y honestidad visual

El tipo de variable dicta el gráfico: **1 numérica** → histograma/boxplot; **2 numéricas** → scatter; **categórica vs. numérica** → boxplot por grupo o barras de medias; **categórica** → barras; **serie temporal** → líneas. Un eje truncado exagera diferencias triviales; elegir el gráfico equivocado es un error analítico, no estético.

- *Idóneo:* barras desde cero para magnitudes; líneas para evolución temporal.
- *No sirve:* gráficos de pastel con muchas categorías (el ojo no compara ángulos); ejes truncados salvo justificación explícita y señalada.

---

## 3. Ejemplos: el mejor y el peor caso de uso

### Ejemplo A — Histograma sobre `dataset_A_asimetria`

**✅ Mejor caso.**
```python
ax = df_A["ingreso_mensual"].plot.hist(bins=40, edgecolor="white")
ax.axvline(df_A["ingreso_mensual"].mean(),   color="crimson", ls="--")  # media
ax.axvline(df_A["ingreso_mensual"].median(), color="green")             # mediana
```
Con 40 clases se ve la cola derecha y, al marcar media (≈3.443) y mediana (≈2.429), el estudiante *ve* por qué la media no representa al hogar típico. El gráfico confirma la lectura numérica de `describe`.

**❌ Peor caso.**
```python
df_A["ingreso_mensual"].plot.hist(bins=3)   # sub-binning brutal
```
Tres barras colapsan toda la estructura: la asimetría desaparece y el histograma "parece" casi uniforme. Una decisión de binning arruina el diagnóstico. (El error simétrico sería `bins=300`: puro ruido dentado.)

### Ejemplo B — Boxplot sobre `dataset_B_outliers`

**✅ Mejor caso.**
```python
df_B.boxplot(column="horas_estudio")
# La regla 1.5*IQR marca los 6 registros con 38–45 h como atípicos
```
El boxplot expone de inmediato los seis puntos de alto apalancamiento (errores de captura: se anotó 40 en vez de 4). Se documenta la decisión de corregirlos y se recalcula la correlación, que pasa de $r=0.43$ (engañosa) a $r=0.94$ (real).

**❌ Peor caso.**
```python
# Se detecta el atípico y se borra automáticamente, sin preguntarse qué es
df_B = df_B[df_B["horas_estudio"] < 31]
```
Aquí funcionó porque eran errores. Pero **borrar por regla automática** es peligroso: en otro dataset, ese punto lejano podría ser el fraude, el paciente crítico o el terremoto —la observación más importante—. El boxplot **detecta**; la decisión de eliminar exige criterio, no un umbral ciego.

### Ejemplo C — Scatter y Anscombe

**✅ Mejor caso.**
```python
for k,(x,y) in ans.items():
    plt.scatter(x, y); plt.plot(x, np.poly1d(np.polyfit(x,y,1))(x))
```
Graficar los cuatro sets *antes* de reportar $r$ revela que solo el set I justifica una recta; el II es curvo (pide un modelo no lineal), el III está dominado por un outlier y el IV es casi vertical. La misma $r=0.816$ significaría cuatro cosas distintas.

**❌ Peor caso.**
```python
r = np.corrcoef(x, y)[0,1]   # se reporta 0.816 para el set II (curvo) y se concluye "relación lineal fuerte"
```
Confiar en el coeficiente sin mirar la nube produce una afirmación falsa: en el set II la relación es determinista pero **cuadrática**; Pearson la subrepresenta y el analista modela una recta sobre una parábola.

### Ejemplo D — Confusión sobre `dataset_C_confusion`

**✅ Mejor caso.**
```python
plt.scatter(df_C["ventas_helados"], df_C["ahogamientos"], c=df_C["temperatura_C"], cmap="coolwarm")
# y condicionar:
df_C.groupby(pd.cut(df_C["temperatura_C"], [0,15,25,35]), observed=True)[["ventas_helados","ahogamientos"]] \
    .apply(lambda g: g["ventas_helados"].corr(g["ahogamientos"]))
```
Colorear por temperatura revela la variable oculta; condicionar por franjas hace caer la correlación de 0.57 a ~0.04–0.20. Conclusión correcta: la asociación helados↔ahogamientos es **espuria**, mediada por el calor. Correlación ≠ causalidad, demostrado computacionalmente.

**❌ Peor caso.**
```python
r = df_C["ventas_helados"].corr(df_C["ahogamientos"])   # 0.57
# titular: "Comer helado aumenta el riesgo de ahogamiento"
```
Se toma la correlación marginal como evidencia causal, se ignora la temperatura y se propone una intervención absurda (prohibir helados para salvar vidas). Es el arquetipo del error de confusión.

### Ejemplo E — Honestidad del eje

**✅ Mejor caso.** Dos grupos con medias 100 y 102 graficados con eje desde 0: la diferencia (2 %) se ve pequeña, que es lo que es.

**❌ Peor caso.** Los mismos datos con `set_ylim(99, 103)`: una barra "duplica" visualmente a la otra. La diferencia real no cambió; la percepción sí. Es manipulación aunque cada número sea correcto.

---

## 4. Síntesis de la clase

La visualización cierra el circuito entre el número (Clase 1) y la herramienta (Clase 2): el histograma verifica la asimetría, el boxplot materializa el IQR y sus atípicos, el scatter juzga la correlación y el coloreo/condicionado desenmascara la confusión. El principio transversal es doble: **grafica antes de confiar en un estadístico** (Anscombe) y **recuerda que un gráfico es un argumento** (ejes honestos). Con estos hábitos, la Clase 4 aplica el mismo criterio a datos reales, donde la verdad ya no viene inyectada y el juicio del analista es lo único que separa el insight del espejismo.

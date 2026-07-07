# Clase 1 — Fundamentos del Pensamiento Analítico y Estadístico

> **Documento de desarrollo académico.** Redactado desde el rol de un profesional con grado de maestría en cálculo estadístico y estocástico, con enfoque en cómputo estadístico. El objetivo no es "memorizar fórmulas", sino entender el **mecanismo** de cada herramienta: qué supone, cuándo es la elección correcta y cuándo su uso constituye un error metodológico.
>
> **Estructura del documento:** (1) Glosario de todos los conceptos; (2) Desarrollo de cada concepto con casos idóneos y no idóneos; (3) Ejemplos con el mejor y el peor caso de uso.

---

## 1. Glosario de conceptos

| # | Concepto | Definición operativa (rigurosa y breve) |
|---|---|---|
| 1 | **Población** | Conjunto completo de unidades sobre las que se quiere concluir. Casi siempre inaccesible en su totalidad. |
| 2 | **Muestra** | Subconjunto observado de la población. Toda la inferencia parte de aquí. |
| 3 | **Variable** | Característica medible de cada unidad. Puede ser cualitativa (nominal/ordinal) o cuantitativa (discreta/continua). |
| 4 | **Media aritmética** ($\bar{x}$) | $\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$. Punto que minimiza la suma de errores al cuadrado. |
| 5 | **Mediana** | Valor que deja el 50 % de los datos a cada lado. Minimiza la suma de errores absolutos. |
| 6 | **Moda** | Valor (o valores) de máxima frecuencia. Única medida válida para variables nominales. |
| 7 | **Rango** | $\max(x)-\min(x)$. Medida de dispersión más simple y más frágil. |
| 8 | **Varianza** ($s^2$) | $s^2=\frac{1}{n-1}\sum(x_i-\bar{x})^2$. Dispersión media al cuadrado. El divisor $n-1$ es la corrección de Bessel. |
| 9 | **Desviación estándar** ($s$) | $\sqrt{s^2}$. Dispersión en las unidades originales. |
| 10 | **Rango intercuartílico (IQR)** | $Q_3-Q_1$. Dispersión del 50 % central; robusta a atípicos. |
| 11 | **Coeficiente de variación (CV)** | $s/\bar{x}$. Dispersión relativa, adimensional. Permite comparar variables de distinta escala. |
| 12 | **Distribución de frecuencias por clases** | Agrupación de datos continuos en intervalos. Regla de Sturges: $k=1+\log_2 n$. |
| 13 | **Asimetría (skewness)** | Grado de falta de simetría. Positiva = cola a la derecha; la media supera a la mediana. |
| 14 | **Espacio muestral** ($\Omega$) | Conjunto de todos los resultados posibles de un experimento aleatorio. |
| 15 | **Axiomas de Kolmogórov** | $P(A)\ge 0$; $P(\Omega)=1$; aditividad para eventos disjuntos. Base formal de la probabilidad. |
| 16 | **Probabilidad condicional** | $P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}$, con $P(B)>0$. |
| 17 | **Independencia** | $A,B$ independientes $\iff P(A\cap B)=P(A)P(B)$. |
| 18 | **Teorema de Bayes** | $P(A\mid B)=\dfrac{P(B\mid A)P(A)}{P(B)}$. Actualiza creencias ante evidencia. |
| 19 | **Variable aleatoria (VA)** | Función que asigna un número real a cada resultado de $\Omega$. Discreta o continua. |
| 20 | **Valor esperado** ($E[X]$) | $\sum x\,p(x)$ (discreta) o $\int x f(x)\,dx$ (continua). Centro de masa de la distribución. |
| 21 | **Varianza de una VA** | $\operatorname{Var}(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2$. |
| 22 | **Distribución Bernoulli** | Un ensayo éxito/fracaso. $E[X]=p$, $\operatorname{Var}=p(1-p)$. |
| 23 | **Distribución Binomial** | Número de éxitos en $n$ ensayos Bernoulli independientes. $E[X]=np$. |
| 24 | **Distribución Poisson** | Conteo de eventos raros en un intervalo. $E[X]=\operatorname{Var}=\lambda$. |
| 25 | **Distribución Uniforme** | Todos los valores igualmente probables en $[a,b]$. |
| 26 | **Distribución Normal** | $X\sim\mathcal{N}(\mu,\sigma^2)$. Simétrica, base del TLC y de casi toda la inferencia clásica. |
| 27 | **Teorema del Límite Central (TLC)** | La media de $n$ VA i.i.d. con varianza finita tiende a una Normal cuando $n\to\infty$. |
| 28 | **Estimador** | Regla para aproximar un parámetro poblacional a partir de la muestra (p. ej. $\bar{x}$ estima $\mu$). |
| 29 | **Error estándar** | Desviación estándar de un estimador: $\text{SE}(\bar{x})=s/\sqrt{n}$. |
| 30 | **Intervalo de confianza (IC)** | Rango que, con confianza $1-\alpha$, contiene el parámetro bajo muestreo repetido. |
| 31 | **Prueba de hipótesis** | Procedimiento para decidir entre $H_0$ (nula) y $H_1$ (alternativa) con evidencia muestral. |
| 32 | **Error tipo I / tipo II** | Rechazar $H_0$ siendo cierta ($\alpha$) / no rechazarla siendo falsa ($\beta$). |
| 33 | **Nivel de significancia** ($\alpha$) | Probabilidad máxima tolerada de error tipo I (típico 0.05). |
| 34 | **p-valor** | Probabilidad de observar un estadístico tan extremo o más, **suponiendo $H_0$ cierta**. |
| 35 | **Potencia** | $1-\beta$. Probabilidad de detectar un efecto real cuando existe. |
| 36 | **Covarianza** | $\operatorname{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]$. Signo de la relación lineal; escala dependiente. |
| 37 | **Correlación de Pearson** ($r$) | Covarianza estandarizada, $r\in[-1,1]$. Mide relación **lineal**. |
| 38 | **Correlación de Spearman** ($\rho$) | Pearson sobre los rangos. Mide relación **monótona**, robusta a atípicos. |

---

## 2. Desarrollo de cada concepto: cuándo es idóneo y cuándo no

### 2.1 Medidas de tendencia central

**Media aritmética.** Resume el "centro" minimizando el error cuadrático. Su punto débil es estructural: cada observación pesa por su magnitud, así que un solo valor extremo la desplaza sin límite (punto de ruptura = 0 %).

- *Idónea cuando:* la distribución es aproximadamente simétrica y sin atípicos; se van a hacer operaciones algebraicas posteriores (la media es lineal: $E[aX+b]=aE[X]+b$); la variable es de intervalo o razón.
- *No sirve cuando:* la distribución es asimétrica o tiene colas pesadas (ingresos, precios, tiempos de espera); la variable es ordinal o nominal; hay atípicos no depurados.

**Mediana.** Minimiza el error absoluto; su punto de ruptura es 50 %, la máxima robustez posible. El precio de esa robustez es que ignora la magnitud (solo usa el orden), por lo que es "ciega" a cambios en las colas.

- *Idónea cuando:* hay asimetría o atípicos; la variable es ordinal; se busca el valor "típico" representativo.
- *No sirve cuando:* se requiere aditividad (la mediana de una suma ≠ suma de medianas); la muestra es muy pequeña y discreta (salta de forma inestable).

**Moda.** La única aplicable a datos nominales. En continuos casi nunca se usa sobre datos crudos (cada valor aparece una vez); se define sobre el histograma.

- *Idónea cuando:* variable nominal ("¿color más vendido?"); detección de bimodalidad (dos poblaciones mezcladas).
- *No sirve cuando:* la variable es continua sin agrupar; los datos son casi uniformes (moda no informativa).

### 2.2 Medidas de dispersión

**Rango.** Solo dos datos lo determinan; su valor esperado crece con $n$ (a más datos, más probable un extremo). Útil como diagnóstico rápido, nunca como medida final.

**Varianza y desviación estándar.** La varianza es el segundo momento central; su unidad es la del dato al cuadrado (poco interpretable), por eso se reporta la desviación estándar. El divisor $n-1$ corrige el sesgo por descontar un grado de libertad al estimar $\bar{x}$ desde la misma muestra.

- *Idóneas cuando:* la distribución es aproximadamente normal; se harán inferencias paramétricas (IC, pruebas $t$, ANOVA).
- *No sirven cuando:* hay atípicos (la varianza los amplifica al cuadrado) o colas muy pesadas (en algunas distribuciones la varianza teórica ni siquiera existe). Ahí se prefiere el IQR.

**IQR.** Robusto (punto de ruptura 25 %). Es la base de la detección de atípicos por la regla $1.5\times$IQR y del diagrama de caja.

- *Idóneo cuando:* distribuciones asimétricas o con atípicos; comparación robusta entre grupos.
- *No sirve cuando:* se necesita una medida que use toda la información de la cola (p. ej. gestión de riesgo extremo, donde precisamente las colas importan).

**Coeficiente de variación.** Adimensional; permite comparar la variabilidad relativa de cosas distintas (¿varía más el peso o la estatura?).

- *No sirve cuando:* la media es cercana a cero (el CV explota) o la variable tiene cero verdadero arbitrario (escalas de intervalo como °C).

### 2.3 Distribución de frecuencias por clases

Agrupar en clases convierte datos continuos en una tabla/histograma. Se pierde información puntual pero se **revela la forma**. El número de clases $k$ gobierna el equilibrio sesgo–ruido: pocas clases ocultan estructura; muchas la fragmentan en ruido.

- *Idónea cuando:* $n$ es grande y se quiere ver forma, modas y asimetría.
- *No sirve cuando:* $n$ es pequeño (cada clase queda casi vacía) o la variable es categórica (usar frecuencias sin agrupar).

### 2.4 Probabilidad

**Condicional y Bayes.** La probabilidad condicional es el motor de todo razonamiento bajo evidencia. Bayes formaliza cómo pasar de $P(\text{evidencia}\mid\text{hipótesis})$ a $P(\text{hipótesis}\mid\text{evidencia})$, que rara vez son iguales. El error clásico (falacia del fiscal) es confundir ambas.

- *Idónea cuando:* diagnóstico, filtrado, actualización secuencial de creencias.
- *No sirve / se abusa cuando:* se ignora la probabilidad base (prevalencia). Un test con 99 % de sensibilidad sobre una enfermedad rara produce mayoría de falsos positivos.

**Independencia.** Supuesto que permite multiplicar probabilidades. Es una simplificación potente y peligrosa: asumirla cuando no se cumple subestima la probabilidad conjunta de eventos correlacionados (raíz de muchos fallos de modelos de riesgo).

### 2.5 Distribuciones de probabilidad

Cada distribución **modela un mecanismo generador**. Elegir la distribución correcta es elegir la física del problema, no un detalle técnico.

- **Bernoulli/Binomial:** procesos éxito/fracaso con $p$ constante e independencia. *No sirve* si $p$ cambia entre ensayos o si hay dependencia (contagio).
- **Poisson:** conteos de eventos raros con tasa $\lambda$ constante. *Idónea* para llegadas, defectos, siniestros. *No sirve* si hay sobredispersión (varianza ≫ media): ahí se usa Binomial Negativa.
- **Uniforme:** ignorancia máxima en un rango acotado. Raramente describe datos reales; sí describe generadores aleatorios.
- **Normal:** aparece por el TLC cuando el resultado es suma de muchos efectos pequeños e independientes. *No sirve* para variables acotadas, estrictamente positivas y asimétricas (ingresos), ni para conteos.

**Valor esperado.** Es el centro de masa, no necesariamente un valor observable ni el más probable. En distribuciones asimétricas, $E[X]$ puede caer en una zona de baja densidad.

### 2.6 Inferencia

**TLC.** Justifica por qué la Normal aparece incluso cuando los datos no lo son: la *media muestral* se normaliza. Requiere varianza finita y, en la práctica, $n$ moderado (más grande cuanto más asimétricos sean los datos).

**Intervalo de confianza.** Su interpretación correcta es frecuentista: el 95 % de los IC construidos así, bajo muestreo repetido, contienen el parámetro. *No* significa "hay 95 % de probabilidad de que $\mu$ esté en este intervalo concreto".

**Prueba de hipótesis y p-valor.** El p-valor mide compatibilidad del dato con $H_0$, no la verdad de $H_0$ ni el tamaño del efecto. Un p-valor pequeño con $n$ enorme puede señalar un efecto trivial; uno grande con $n$ pequeño puede ocultar un efecto real (baja potencia).

- *Idónea cuando:* hay una hipótesis previa, un diseño y un $\alpha$ fijados **antes** de ver los datos.
- *No sirve / se abusa cuando:* se prueban muchas hipótesis y se reporta solo la significativa (p-hacking); se interpreta "no significativo" como "no hay efecto"; se confunde significancia estadística con relevancia práctica.

### 2.7 Asociación entre variables

**Covarianza** da el signo pero depende de las unidades. **Pearson** la estandariza a $[-1,1]$ pero solo capta la parte **lineal**: puede ser 0 con una dependencia perfecta no lineal (p. ej. $Y=X^2$). **Spearman** capta cualquier relación monótona y resiste atípicos.

- *Pearson idóneo cuando:* relación aproximadamente lineal, sin atípicos dominantes, variables continuas.
- *Pearson no sirve cuando:* relación curva, atípicos influyentes, variables ordinales → usar Spearman.
- **Advertencia transversal:** correlación (de cualquier tipo) **no implica causalidad**. Puede deberse a azar, causalidad inversa o a una variable de confusión.

---

## 3. Ejemplos: el mejor y el peor caso de uso

### Ejemplo A — Media aritmética

**✅ Mejor caso.** Estaturas de 1.000 adultos varones. La distribución es casi simétrica y sin atípicos; la media (≈ 175 cm) coincide con la mediana y describe fielmente al individuo típico. Además, al ser simétrica, la media es también el estimador de máxima verosimilitud de $\mu$.

**❌ Peor caso.** Ingreso anual de una muestra donde aparece un multimillonario. Si nueve personas ganan ~30.000 y una gana 30 millones, la **media** ≈ 3 millones "describe" a un grupo donde *nadie* gana eso. Reportar esa media como "ingreso promedio" es técnicamente correcto y comunicativamente engañoso. Aquí la **mediana** (30.000) es la medida honesta.

> *Regla operativa:* si `media` y `mediana` difieren notablemente, la distribución es asimétrica y la media, sospechosa.

### Ejemplo B — Desviación estándar vs. IQR

**✅ Mejor caso (σ).** Error de medición de un instrumento calibrado: ruido gaussiano centrado en cero. La σ resume toda la incertidumbre y alimenta directamente intervalos de confianza válidos.

**❌ Peor caso (σ).** Tiempos de respuesta de un servidor con algunas peticiones "colgadas" de 30 s entre miles de 0.2 s. Esos pocos atípicos, elevados al cuadrado, inflan la σ hasta volverla inútil como "dispersión típica". El **IQR** describe correctamente el 50 % central; los percentiles altos (p95, p99) describen la cola. Es el estándar en ingeniería de rendimiento por esta razón.

### Ejemplo C — Teorema de Bayes (prueba médica)

**✅ Mejor caso.** Enfermedad con prevalencia 10 %, test con sensibilidad 99 % y especificidad 95 %. La probabilidad posterior de estar enfermo dado un positivo es alta (~69 %): el test es útil porque la base no es despreciable.

**❌ Peor caso.** Misma prueba, pero enfermedad con prevalencia 0.1 %. Ahora, dado un positivo, la probabilidad de estar realmente enfermo cae a ~2 %: el 98 % de los positivos son falsos. Ignorar la prevalencia (base rate neglect) lleva a sobrediagnóstico masivo. El "por qué" es puro Bayes: el denominador $P(\text{positivo})$ está dominado por los falsos positivos de una población sana enorme.

### Ejemplo D — Distribución de Poisson

**✅ Mejor caso.** Número de correos que llegan por minuto a un servidor: eventos independientes, tasa estable. Poisson predice bien la probabilidad de saturación y la media iguala a la varianza (comprobable en los datos).

**❌ Peor caso.** Número de goles por partido cuando existen rachas y expulsiones que cambian la tasa dentro del juego: aparece **sobredispersión** (varianza > media). Ajustar Poisson subestima la probabilidad de resultados extremos; la Binomial Negativa es el modelo correcto.

### Ejemplo E — Correlación de Pearson

**✅ Mejor caso.** Altura y peso en adultos: relación aproximadamente lineal y monótona; $r\approx 0.7$ resume bien la asociación y es estable ante remuestreo.

**❌ Peor caso.** Cuarteto de Anscombe (que veremos en la Clase 3): cuatro nubes radicalmente distintas —una lineal, una curva, una con outlier dominante y una casi vertical— comparten el **mismo** $r=0.816$. Confiar en el número sin graficar produce cuatro conclusiones erróneas. La lección: **Pearson resume, no describe**; siempre precede el diagrama de dispersión al coeficiente.

### Ejemplo F — p-valor

**✅ Mejor caso.** Ensayo clínico con hipótesis, tamaño muestral y $\alpha=0.05$ definidos de antemano; se obtiene $p=0.003$ para una diferencia clínicamente relevante. El p-valor cumple su función: cuantifica la sorpresa bajo $H_0$ dentro de un diseño preespecificado.

**❌ Peor caso.** Un analista prueba 40 variables contra un resultado, encuentra dos con $p<0.05$ y titula "asociación significativa". Con $\alpha=0.05$ se esperan ~2 falsos positivos solo por azar (problema de comparaciones múltiples). Sin corrección (Bonferroni, FDR) ni replicación, el hallazgo es probablemente ruido: es el mecanismo del **p-hacking**.

---

## 4. Síntesis de la clase

El hilo conductor es que **cada medida encapsula un supuesto**, y usarla fuera de ese supuesto no es un error de cálculo sino de razonamiento. La media supone simetría; la varianza supone colas ligeras; Pearson supone linealidad; el p-valor supone un diseño preespecificado; Poisson supone tasa constante. El analista competente no memoriza fórmulas: reconoce el mecanismo generador de los datos y elige la herramienta cuyo supuesto coincide con él. Todo lo que sigue en el curso —Pandas, visualización, casos reales— es la puesta en práctica computacional de este criterio.

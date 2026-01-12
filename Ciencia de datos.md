# Ciencia de Datos: Fundamentos Teóricos y Matemáticos

## 1. ¿Qué es la Ciencia de Datos?

La Ciencia de Datos es un campo interdisciplinario que utiliza métodos científicos, procesos, algoritmos y sistemas para extraer conocimiento e ideas (insights) de datos estructurados y no estructurados. 

**Definición:**
Sea $D$ un conjunto de datos (dataset) que representa un fenómeno observable. La Ciencia de Datos se define como el estudio de funciones computables $f: D \to I$, donde $I$ representa información o conocimiento procesable. Este proceso implica la intersección de la **Estadística** (para modelar la incertidumbre y la variabilidad), las **Matemáticas** (Álgebra Lineal y Cálculo para la optimización y representación vectorial) y las **Ciencias de la Computación** (para la algoritmia y el procesamiento eficiente).

A diferencia del análisis de datos tradicional, la Ciencia de Datos no solo busca describir el pasado, sino utilizar modelos predictivos y prescriptivos para inferir $P(Y|X)$, la probabilidad de un resultado futuro $Y$ dado un conjunto de variables observadas $X$.

---

## 2. Historia de la Ciencia de Datos: Definiciones, Evolución y Actualidad

La Ciencia de Datos no surgió de la nada, sino que es la evolución natural de la estadística combinada con el poder computacional.

*   **1962 - El inicio conceptual (John Tukey):** En su paper *"The Future of Data Analysis"*, John Tukey advirtió que la estadística debía alejarse de la teoría pura y centrarse más en el análisis de los datos en sí mismos, sugiriendo una nueva ciencia empírica.
*   **1974 - El término (Peter Naur):** Utiliza el término "Data Science" en su libro *"Concise Survey of Computer Methods"*, definiéndolo como el procesamiento de datos para ser utilizados por humanos.
*   **1996 - KDD (Knowledge Discovery in Databases):** Se formaliza el proceso de extracción de conocimiento, consolidando técnicas de minería de datos.
*   **2001 - El nacimiento oficial (William S. Cleveland):** En su artículo *"Data Science: An Action Plan for Expanding the Technical Areas of the Field of Statistics"*, Cleveland propuso unificar la estadística con la computación, estableciendo la Ciencia de Datos como una disciplina independiente con su propio rigor.
*   **2010s - La era del Big Data y Deep Learning:** Con el auge de internet y la capacidad de cómputo (GPUs), algoritmos teóricos de redes neuronales (como el Perceptrón Multicapa) se volvieron viables, permitiendo el procesamiento de datos no estructurados (imágenes, texto).
*   **Actualidad:** La Ciencia de Datos es el motor de la Inteligencia Artificial Generativa y la toma de decisiones automatizada en tiempo real.

---

## 3. Ramas del Conocimiento

La Ciencia de Datos extrae sus métodos principalmente de:

1.  **Probabilidad y Estadística:**
    *   **Inferencia Estadística:** Para generalizar conclusiones de una muestra a una población.
    *   **Teoría de Probabilidad:** Para modelar la incertidumbre y procesos estocásticos ($P(A|B) = \frac{P(B|A)P(A)}{P(B)}$ - Teorema de Bayes).
2.  **Matemáticas Aplicadas:**
    *   **Álgebra Lineal:** Fundamental para manipular estructuras de datos (matrices, tensores) y transformaciones espaciales (ej. PCA).
    *   **Cálculo Multivariable:** Esencial para la optimización de funciones de costo (Gradiente Descendente: $\theta_{new} = \theta_{old} - \alpha \nabla J(\theta)$).
3.  **Teoría de la Información (Claude Shannon):** Conceptos como la entropía ($H(X) = -\sum p(x) \log p(x)$) son básicos para árboles de decisión y compresión.
4.  **Ciencias de la Computación:** Estructuras de datos, complejidad algorítmica y teoría de grafos.

## 4. Roadmap de Ciencia de Datos

El camino desde los conceptos fundamentales hasta la complejidad de la IA moderna:

1.  **Fundamentos Matemáticos:** Logica, Teoría de Conjuntos, Álgebra Lineal, Cálculo Diferencial.
2.  **Estadística Descriptiva:** Medidas de tendencia central, dispersión y distribuciones.
3.  **Probabilidad e Inferencia:** Teorema de Bayes, Pruebas de Hipótesis, Intervalos de Confianza.
4.  **Modelado Predictivo (Aprendizaje Supervisado Clásico):** Regresión Lineal, Logística, Árboles de Decisión.
5.  **Aprendizaje No Supervisado:** Clustering (K-Means), Reducción de Dimensionalidad (PCA).
6.  **Machine Learning Avanzado:** Ensemble Methods (Random Forest, XGBoost), SVM (Support Vector Machines).
7.  **Deep Learning (Redes Neuronales):** Perceptrones, CNNs (visión), RNNs/Transformers (lenguaje).
8.  **Ciencia de Datos Avanzada:** Cálculo Estocástico, Teoría de Grafos, Modelado NoSQL.
9.  **Ingeniería de Datos y Big Data:** Procesamiento distribuido, ML Ops.

## 5. Naturaleza y Flujo de los Datos

A continuación, se desarrollan los métodos clave con rigor matemático, respondiendo a su utilidad y ejemplos.
Antes de aplicar cualquier algoritmo, es fundamental entender la materia prima: el dato. El objetivo final no es tener datos, sino tomar decisiones sabias.

### A. Pruebas de Hipótesis (Hypothesis Testing)
### 5.1 Del Dato a la Sabiduría (Jerarquía DIKW)

**¿Qué resuelve?**
Determina si existe evidencia suficiente en una muestra de datos para inferir que una cierta condición es verdadera para toda la población. Resuelve el problema de distinguir entre un efecto real y el azar.
El flujo de trabajo en ciencia de datos sigue una transformación progresiva de valor:

**¿Por qué es importante?**
Es la base del método científico cuantitativo. Sin ella, no podríamos validar si un nuevo medicamento funciona o si un cambio en una estrategia de marketing realmente aumentó las ventas.
1.  **Datos (Data):** Símbolos brutos, hechos o señales sin contexto. 
    *   *Ejemplo:* "38", "Rojo", "10:00 AM".
2.  **Información (Information):** Datos procesados, estructurados y puestos en contexto para que tengan significado. Responde a "¿Quién?", "¿Qué?", "¿Dónde?".
    *   *Ejemplo:* "La temperatura del paciente a las 10:00 AM fue de 38 grados y tiene la garganta roja".
3.  **Conocimiento (Knowledge):** Información organizada, sintetizada e internalizada que permite comprender relaciones y patrones. Responde a "¿Cómo?".
    *   *Ejemplo:* "Una temperatura de 38 grados con garganta roja suele indicar una infección bacteriana o viral".
4.  **Sabiduría (Wisdom):** Conocimiento aplicado para la toma de decisiones y la predicción, incorporando juicio ético y pragmático. Responde a "¿Por qué?" y "¿Qué debemos hacer?".
    *   *Ejemplo:* "Dado el historial de alergias del paciente, no recetaremos penicilina y monitorearemos la fiebre 24 horas antes de intervenir".

**Definición Técnica:**
Sea $H_0$ la hipótesis nula (ej. "no hay efecto") y $H_1$ la hipótesis alternativa. Un test de hipótesis busca calcular un estadístico de prueba $T$ a partir de los datos $X$ y determinar la probabilidad de observar $T$ bajo el supuesto de que $H_0$ es cierta (p-valor).
Formalmente, definimos una región crítica $C_\alpha$ tal que:
$$ P(T \in C_\alpha | H_0) = \alpha $$
Donde $\alpha$ es el nivel de significancia (error Tipo I). Rechazamos $H_0$ si el estadístico observado $t \in C_\alpha$.
### 5.2 Estructuración y Manipulación de Datos

**Ejemplos:**
*   **Cotidiano:** Determinar si una moneda está trucada. Lanzamos la moneda 100 veces; si salen 90 caras ($H_0$: probabilidad=0.5), la probabilidad de que esto ocurra por azar es infinitesimal, por lo que concluimos que está trucada.
*   **Científico:** Un ensayo clínico para un nuevo fármaco oncológico. Se compara la tasa de supervivencia del grupo de control ($H_0$) vs el grupo experimental. Si la diferencia es estadísticamente significativa (p < 0.05), se aprueba el fármaco.
Para que un algoritmo matemático pueda "digerir" la realidad, esta debe abstraerse en una estructura numérica.

---
*   **Datos Estructurados:** Información altamente organizada, fácilmente buscable en bases de datos relacionales (SQL).
    *   *Forma:* Tablas (filas y columnas).
    *   *Manipulación:* Dataframes (Pandas/R), Álgebra Relacional.
    *   *Ejemplo:* Una hoja de Excel con ventas por mes.
*   **Datos No Estructurados:** Información sin un modelo predefinido. Representan la mayoría de los datos modernos (80%+).
    *   *Forma:* Texto libre, imágenes (matrices de píxeles), audio (ondas), video.
    *   *Manipulación:* Requieren preprocesamiento complejo para convertirse en tensores.
        *   **Tensores:** Generalización de matrices a n-dimensiones. Una imagen a color es un tensor de (Alto x Ancho x 3 canales RGB).
        *   **Embeddings:** Convertir palabras o entidades en vectores numéricos densos que capturan su significado semántico.


---


# PARTE : FUNDAMENTOS Y MÉTODOS ESENCIALES
A continuación, se presentan los métodos fundamentales agrupados por su paradigma de aprendizaje.

## 6. Inferencia Estadística Básica
Antes del Machine Learning, la inferencia estadística nos permite sacar conclusiones sobre una población total observando solo una pequeña muestra.

### A. Pruebas de Hipótesis (Hypothesis Testing)
*   **Conceptos Clave:**
    *   *Hipótesis Nula ($H_0$):* La suposición por defecto (ej. "no hay efecto", "es azar").
    *   *Nivel de Significancia ($\alpha$):* El umbral de error aceptable (usualmente 0.05).

**¿Qué resuelve?**
 Determina si existe evidencia suficiente en una muestra de datos para inferir que una cierta condición es verdadera para toda la población. Resuelve el problema de distinguir entre un efecto real y el, distinguiendo efectos reales del azar

**¿Por qué es importante?**
Es la base del método científico. Sin ella, no podríamos validar si un nuevo medicamento funciona realmente o es coincidencia.

**Definición Técnica:**
Sea $H_0$ la hipótesis nula (ej. "no hay efecto") y $H_1$ la hipótesis alternativa. Un test de hipótesis busca calcular un estadístico de prueba $T$ a partir de los datos $X$ y determinar la probabilidad de observar $T$ bajo el supuesto de que $H_0$ es cierta (p-valor).
Formalmente, definimos una región crítica $C_\alpha$ tal que:
$$ P(T \in C_\alpha | H_0) = \alpha $$
Donde $\alpha$ es el nivel de significancia (error Tipo I). Rechazamos $H_0$ si el estadístico observado $t \in C_\alpha$.

**Definición Simple:**
Imagina que eres un juez. La "Hipótesis Nula" es que el acusado es inocente. Las "pruebas" son los datos. Si las pruebas son muy contundentes (la probabilidad de que sea inocente con esas pruebas es bajísima, casi cero), entonces dictas sentencia de "culpable". Si las pruebas son débiles, mantienes la inocencia. No pruebas que es inocente, solo que no hay pruebas suficientes para condenarlo.

**Ejemplos:**

*   **Cotidiano:** Determinar si una moneda está trucada. Lanzamos la moneda 100 veces; si salen 90 caras ($H_0$: probabilidad=0.5), la probabilidad de que esto ocurra por azar es infinitesimal, por lo que concluimos que está trucada.
*   **Científico:** Un ensayo clínico para un nuevo fármaco oncológico. Se compara la tasa de supervivencia del grupo de control ($H_0$) vs el grupo experimental. Si la diferencia es estadísticamente significativa (p < 0.05), se aprueba el fármaco.

## 7. Aprendizaje Supervisado
En este tipo de aprendizaje, "enseñamos" a la computadora con ejemplos. Le damos los datos de entrada (
X
) y la respuesta correcta (
Y
). El objetivo es que la máquina aprenda la relación para predecir 
Y
 en datos nuevos (*Modelo $f(X) \to Y$ entrenado con ejemplos etiquetados.*).

**Si la respuesta 
Y
 es un número, se llama Regresión. Si es una categoría, Clasificación.**

### B. Regresión Lineal (Linear Regression)
*   **Conceptos Clave:**
    *   *Residuos:* La diferencia entre el valor real y el predicho ($y - \hat{y}$).
    *   *Mínimos Cuadrados:* Método para minimizar la suma de los errores al cuadrado ($SSE$).

**¿Qué resuelve?**
Modela la relación entre una variable dependiente continua 
y y una o más variables independientes 
X . Predice el valor de y basándose en X.

**¿Por qué es importante?**
Permite cuantificar el impacto de variables (ej. precio, temperatura) sobre un resultado y hacer predicciones numéricas precisas. Es simple, interpretable y fundamento de métodos más complejos

**Definición Técnica:**
Dado un conjunto de datos $\{ (x_i, y_i) \}_{i=1}^n$, asumimos una relación lineal:
$$ y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip} + \epsilon_i $$
O en notación matricial: $Y = X\beta + \epsilon$.
El objetivo es encontrar el vector de coeficientes $\hat{\beta}$ que minimice la Suma de los Errores Cuadráticos (SSE):
$$ J(\beta) = \sum_{i=1}^{n} (y_i - x_i^T \beta)^2 = ||Y - X\beta||^2 $$
La solución analítica (Estimador de Mínimos Cuadrados Ordinarios) es:
$$ \hat{\beta} = (X^T X)^{-1} X^T Y $$

**Definición Simple:**
Tienes una hoja de papel con muchos puntos dispersos. Tu tarea es usar una regla y un lápiz para dibujar una sola línea recta que pase lo más cerca posible de todos los puntos al mismo tiempo. Esa línea te permite "adivinar" dónde caerán futuros puntos..

### C. Regresión Logística (Logistic Regression)
*   **Conceptos Clave:**
    *   *Sigmoide:* Función $1/(1+e^{-z})$ que aplasta cualquier número a un rango entre 0 y 1.
    *   *Probabilidad:* Certeza de que ocurra un evento.

**¿Qué resuelve?**
Clasifica datos en dos opciones (Sí/No) calculando la probabilidad de pertenencia.

**¿Por qué es importante?**
Es el estándar para predicción de riesgo binario en medicina (diagnosticos de enfermedades) y finanzas (predicción de riesgo de fraude).

**Definición Técnica:**

Modelamos la probabilidad 
P(Y=1|X)usando la función sigmoide (logística)(z)=11+e−z, que mapea cualquier valor real al intervalo (0,1). $$ P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta^T X)}} $$ Para ajustar los parámetros 
β
, no minimizamos el error cuadrático, sino que maximizamos la Verosimilitud (Likelihood) o minimizamos la entropía cruzada (Cross-Entropy Loss): $$ J(\beta) = -\sum_{i=1}^n [y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i)] $.

**Definición Simple:**
Imagina que quieres separar manzanas rojas de manzanas verdes en una mesa. La regresión logística es como poner una vara (frontera) en la mesa. Todo lo que esté a un lado de la vara se etiqueta como "Posiblemente Rojo" y al otro como "Posiblemente Verde". Además, te dice qué tan seguro está (ej: "Estoy 90% seguro de que esto es rojo").

Ejemplos:

- Cotidiano: El filtro de spam de tu correo electrónico. Determina la probabilidad de que un email sea "Spam" o "No Spam" basándose en palabras clave.
- Científico: Determinar si un paciente tiene una enfermedad coronaria (Sí/No) basándose en niveles de colesterol, presión arterial y edad.


## 8. Aprendizaje No Supervisado (Básico)
Aquí, la computadora trabaja sola, sin maestro. Le damos datos (X) pero no le damos respuestas (Y). Su tarea es encontrar estructuras, grupos o patrones ocultos por sí misma

### D. K-Means Clustering
*   **Conceptos Clave:**
    *   *Centroide:* El punto promedio central de un grupo.
    *   *Distancia Euclidiana:* La línea recta entre dos puntos.
¿Qué resuelve? Agrupa un conjunto de datos en 
k
 grupos (clusters) distintos basándose en su similitud, sin conocer a priori las etiquetas de los datos (Aprendizaje No Supervisado).

¿Por qué es importante? Permite descubrir estructuras ocultas en los datos, segmentar poblaciones y organizar información no etiquetada.

Definición Técnica: Dado un conjunto de datos x1,…,xn, queremos dividirlo en k conjuntos S=S1,
…,Sk para minimizar la suma de cuadrados dentro del cluster (WCSS): $$ \arg \min_S \sum_{i=1}^{k} \sum_{x \in S_i} ||x - \mu_i||^2 $$ Donde μi es la media (centroide) de los puntos en Si
. El algoritmo itera entre dos pasos:

Asignación: Asignar cada punto al centroide μi más cercano (Distancia Euclidiana).
Actualización: Recalcular μ i como el promedio de los puntos asignados a su cluster.
¿Qué resuelve? Agrupa objetos similares en "clusters" o montones, sin saber qué son esos objetos de antemano.

¿Por qué es importante? Ayuda a descubrir segmentos naturales en datos caóticos (clientes, especies biológicas).

Definición Técnica: Particiona datos en k conjuntos minimizando la varianza intra-cluster (distancia euclidiana al centroide 
μ
). Algoritmo iterativo Expectation-Maximization.

Definición Simple (Secundaria): Imagina que tienes una bolsa de canicas de muchos colores mezclados y te pido que las separes en 3 montones. No te digo qué colores buscar, solo que pongas las que se parecen juntas. Al final tendrás un montón de "rojizas", otro de "azuladas", etc., sin que yo te dijera cómo hacerlo.

Ejemplos:

- Cotidiano: Segmentación de clientes de un supermercado para campañas de marketing (ej. "compradores impulsivos", "familias ahorradoras").
- Científico: Clasificación taxonómica de nuevas especies de plantas basándose en características fenotípicas (tamaño de hoja, altura) sin conocer su especie previamente
---

E. Análisis de Componentes Principales (PCA)
¿Qué resuelve? Reduce la dimensionalidad de un conjunto de datos, transformando muchas variables correlacionadas en un número menor de variables no correlacionadas (componentes principales), conservando la mayor cantidad de varianza (información) posible.

¿Por qué es importante? Permite visualizar datos complejos, eliminar ruido y mejorar la eficiencia de otros algoritmos al reducir el número de variables a procesar (maldición de la dimensionalidad).

Definición Técnica: PCA busca una transformación ortogonal tal que el primer componente principal tenga la mayor varianza posible. Matemáticamente, se basa en la descomposición en valores propios (eigendecomposition) de la matriz de covarianza 
Σ
 de los datos centrados. Si 
Σ
=
1
n
−
1
X
T
X
, buscamos los vectores propios 
v
 y valores propios 
λ
 tales que: $$ \Sigma v = \lambda v $$ Los vectores propios correspondientes a los mayores valores propios 
λ
 definen el nuevo subespacio donde se proyectarán los datos.

¿Qué resuelve? Simplifica datos complejos reduciendo su cantidad de variables, pero conservando la información importante.

¿Por qué es importante? Permite visualizar datos de muchas dimensiones (imposibles de ver para humanos) y elimina el "ruido".

Definición Técnica: Transformación ortogonal que proyecta datos a un nuevo sistema de coordenadas (componentes principales) donde la varianza se maximiza progresivamente. Utiliza valores propios de la matriz de covarianza.

Definición Simple (Secundaria): Imagina la sombra de un objeto 3D (como una tetera) en la pared. El objeto es complejo, pero la sombra es plana (2D). Si giras la tetera hasta que la sombra muestre su forma más clara (donde se ve el mango y el pico), has hecho un PCA: has reducido un objeto 3D a una imagen 2D perdiendo la menor cantidad de detalle posible.

Ejemplos:

Cotidiano: Compresión de imágenes. Reducir el tamaño de un archivo de imagen eliminando componentes que aportan poca información visual (varianza baja).
Científico: Análisis de datos genómicos (Microarrays). Un estudio puede tener miles de genes (variables) pero pocas muestras. PCA reduce estos miles de genes a unos pocos "supergetes" que explican las diferencias biológicas principales.
F. Redes Neuronales (Deep Learning - Perceptrón Multicapa)
¿Qué resuelve? Modela relaciones extremadamente no lineales y complejas. Resuelve problemas que los algoritmos tradicionales no pueden, como reconocimiento de patrones en imágenes, audio y texto.

¿Por qué es importante? Es la base de la IA moderna. Su capacidad de aprender representaciones jerárquicas de los datos ha revolucionado la tecnología (conducción autónoma, traducción automática).

Definición Técnica: Un Perceptrón Multicapa (MLP) es una función compuesta 
f
(
x
)
=
f
(
L
)
(
…
f
(
2
)
(
f
(
1
)
(
x
)
)
)
. Cada capa 
l
 computa una transformación afín seguida de una función de activación no lineal 
σ
 (como ReLU o Sigmoide): $$ h^{(l)} = \sigma(W^{(l)} h^{(l-1)} + b^{(l)}) $$ Donde 
W
(
l
)
 es la matriz de pesos y 
b
(
l
)
 el vector de sesgo (bias). El aprendizaje se realiza mediante el algoritmo de Backpropagation (Regla de la Cadena), ajustando los pesos para minimizar una función de pérdida global: $$ \frac{\partial J}{\partial W^{(l)}} = \text{propagar el error desde la salida hacia atrás} $$

Ejemplos:

Determinar: Determinar si una persona pertenece a un grupo de Facebook (Sugerencia de amigos basada en grafos y comportamiento).
Científico: Determinar si una secuencia de nucleótidos tiene un patrón específico (Promotores genéticos) mediante modelos de secuencia (RNNs o CNNs 1D).
Cotidiano: Comprimir una imagen JPG (quitas datos pero la foto se ve casi igual).
Científico: Analizar miles de genes y encontrar los 2 o 3 "super-genes" responsables de una enfermedad.


# PARTE II: CIENCIA DE DATOS AVANZADA
*Temas especializados para modelado complejo y validación rigurosa.*

## 9. Evaluación y Validación de Clusters

### E. Coeficiente de Silhouette
*   **Conceptos Clave:**
    *   *Cohesión ($a$):* Distancia media a puntos del mismo cluster.
    *   *Separación ($b$):* Distancia media al cluster vecino más cercano.

**¿Qué resuelve?**
Evalúa la calidad de un cluster individual sin tener etiquetas reales.

**¿Por qué es importante?**
Valida si la agrupación tiene sentido físico o es artificial.

**Definición Técnica:**
$S = \frac{b - a}{\max(a, b)}$. Varía de -1 (mal asignado) a +1 (perfectamente asignado).

### F. Estadístico GAP
*   **Conceptos Clave:**
    *   *Distribución Nula:* Datos aleatorios uniformes sin patrones.
    *   *Dispersión:* Medida de "desorden".

**¿Qué resuelve?**
Determina el número óptimo de clusters ($k$) comparando contra el azar.

**¿Por qué es importante?**
Evita ver patrones donde no los hay.

**Definición Técnica:**
Compara la dispersión del modelo ($W_k$) contra la dispersión esperada de una distribución aleatoria ($W_k^{ref}$). $\text{Gap}(k) = E[\log(W_k^{ref})] - \log(W_k)$.

### G. Criterios de Selección (AIC / BIC)
*   **Conceptos Clave:**
    *   *Verosimilitud ($L$):* Qué tan bien ajusta el modelo a los datos.
    *   *Penalización:* Castigo matemático por complejidad (número de parámetros).

**¿Qué resuelve?**
Elige el mejor modelo balanceando precisión vs simplicidad.

**¿Por qué es importante?**
Evita el sobreajuste (overfitting).

**Definición Técnica:**
*   AIC = $2k - 2\ln(L)$
*   BIC = $k \ln(n) - 2\ln(L)$ (Más estricto con muchos datos).

## 10. Regresión Avanzada (Alta Dimensión)

### H. Regularización (Ridge, Lasso, Elastic Net)
*   **Conceptos Clave:**
    *   *Norma L1:* Suma de valores absolutos ($|\beta|$).
    *   *Norma L2:* Suma de valores al cuadrado ($\beta^2$).
    *   *Hiperparámetro $\lambda$:* Fuerza del castigo de regularización.

**¿Qué resuelve?**
Entrena modelos estables cuando hay muchas variables o correlación (multicolinealidad).

**¿Por qué es importante?**
Esencial para Big Data y Genómica donde variables > muestras.

**Definición Técnica:**
*   **Ridge:** Minimiza Error + $\lambda ||\beta||_2^2$. (Contrae coeficientes).
*   **Lasso:** Minimiza Error + $\lambda ||\beta||_1$. (Elimina variables irrelevantes).

**Definición Simple:**
Ridge reparte la culpa entre todas las variables. Lasso busca pocos culpables principales y descarta el resto.

### I. Inferencia Post-Lasso
*   **Conceptos Clave:**
    *   *Sesgo de Selección:* Error por usar los mismos datos para elegir y testear.
    *   *Active Set:* Conjunto de variables elegidas por Lasso.

**¿Qué resuelve?**
Permite calcular Valores P válidos después de usar Lasso.

**¿Por qué es importante?**
Lasso normal destruye la validez de los intervalos de confianza; Post-Lasso la restaura.

**Definición Técnica:**
1) Seleccionar variables con Lasso. 2) Re-estimar coeficientes usando OLS estándar solo con las variables seleccionadas.

## 11. Clasificación Avanzada

### J. Máquinas de Soporte Vectorial (SVM)
*   **Conceptos Clave:**
    *   *Hiperplano:* Frontera de decisión óptima.
    *   *Margen:* Distancia a los puntos más cercanos.
    *   *Kernel:* Función matemática para elevar dimensiones ($K(x,y)$).

**¿Qué resuelve?**
Clasifica datos complejos y no lineales maximizando la separación.

**¿Por qué es importante?**
Robusto en altas dimensiones (imágenes).

**Definición Técnica:**
Maximiza el margen $\frac{2}{||w||}$ usando Kernels para proyectar datos a un espacio donde sean separables linealmente.

**Definición Simple:**
Separar canicas golpeando la mesa para que salten (Kernel) y pasando una hoja entre ellas en el aire.

### K. Métodos de Ensamble (Trees & Forests)
*   **Conceptos Clave:**
    *   *Entropía:* Medida de impureza/desorden de un nodo.
    *   *Bagging:* Promediar modelos paralelos e independientes.
    *   *Boosting:* Entrenar modelos secuenciales que corrigen errores.

**¿Qué resuelve?**
Captura relaciones no lineales complejas combinando muchos modelos simples.

**¿Por qué es importante?**
Son los algoritmos más potentes para datos tabulares (ej. Random Forest, XGBoost).

**Definición Técnica:**
*   *Random Forest:* Promedio de múltiples árboles entrenados con submuestras aleatorias (Bagging).
*   *Boosting:* Suma ponderada de árboles débiles entrenados sobre los residuos del anterior.

## 12. Modelado Probabilístico Avanzado

### L. Clustering Probabilístico (GMM)
*   **Conceptos Clave:**
    *   *Variable Latente:* Pertenencia oculta a un grupo.
    *   *Algoritmo EM:* Esperanza-Maximización.

**¿Qué resuelve?**
Clustering "suave" donde un punto puede pertenecer parcialmente a varios grupos.

**¿Por qué es importante?**
Modela la incertidumbre en la asignación de grupos.

**Definición Técnica:**
Asume que los datos vienen de una mezcla de distribuciones Gaussianas y optimiza sus parámetros iterativamente con EM.

### M. Asignación Latente de Dirichlet (LDA)
*   **Conceptos Clave:**
    *   *Tópico:* Distribución de palabras.
    *   *Inferencia Variacional:* Aproximación de la distribución posterior mediante optimización.

**¿Qué resuelve?**
Descubre temas abstractos en grandes corpus de texto.

**¿Por qué es importante?**
Organiza información no estructurada masiva automática.

**Definición Técnica:**
Modelo generativo donde cada documento es una mezcla de tópicos (dirichlet) y cada tópico una mezcla de palabras.

## 13. Sistemas Complejos

### N. Teoría de Grafos
*   **Conceptos Clave:**
    *   *Matriz Laplaciana:* ($D - A$) Describe la conectividad.
    *   *Eigenvector:* Vector propio de la matriz.

**¿Qué resuelve?**
Encuentra comunidades en redes basándose en conexiones, no distancia.

**¿Por qué es importante?**
Fundamental para redes sociales y conexiones neuronales.

**Definición Técnica:**
Clustering Espectral: Usa los eigenvectores asociados a los valores propios más pequeños del Laplaciano para particionar el grafo (Min-Cut).

### O. Cálculo Estocástico
*   **Conceptos Clave:**
    *   *Proceso de Wiener:* Movimiento Browniano (ruido aleatorio continuo).
    *   *Integral de Itô:* Integral respecto a un proceso aleatorio.

**¿Qué resuelve?**
Modela sistemas dinámicos con ruido intrínseco.

**¿Por qué es importante?**
Base de modelos financieros y físicos (difusión).

**Definición Técnica:**
Resuelve Ecuaciones Diferenciales Estocásticas (SDE): $dX_t = \mu dt + \sigma dW_t$.

---

## 14. Bibliografía
1.  **Bishop, C. M.** *Pattern Recognition and Machine Learning*.
2.  **Hastie, T.** *The Elements of Statistical Learning*.
3.  **Goodfellow, I.** *Deep Learning*.
4.  **Pearl, J.** *Causality*.
5.  **Chernozhukov, V.** *Post-Selection Inference*.

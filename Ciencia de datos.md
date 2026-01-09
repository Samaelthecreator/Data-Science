# Ciencia de Datos: Fundamentos Teóricos y Matemáticos

## 1. ¿Qué es la Ciencia de Datos?

La Ciencia de Datos es un campo interdisciplinario que utiliza métodos científicos, procesos, algoritmos y sistemas para extraer conocimiento e ideas (insights) de datos estructurados y no estructurados. 

**Definición Técnica Rigurosa:**
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

---

## 4. Roadmap de Ciencia de Datos

El camino desde los conceptos fundamentales hasta la complejidad de la IA moderna:

1.  **Fundamentos Matemáticos:** Logica, Teoría de Conjuntos, Álgebra Lineal, Cálculo Diferencial.
2.  **Estadística Descriptiva:** Medidas de tendencia central, dispersión y distribuciones.
3.  **Probabilidad e Inferencia:** Teorema de Bayes, Pruebas de Hipótesis, Intervalos de Confianza, Teoremas Lasso/Post-Lasso.
4.  **Modelado Predictivo (Aprendizaje Supervisado Clásico):** Regresiones (Lineal, Logística, Ridge, Lasso), SVM, KNN, Árboles (Random Forest, Boosting).
5.  **Aprendizaje No Supervisado:** Clustering (K-Means, Jerárquico, GMM), Reducción de Dimensionalidad (PCA, LDA).
6.  **Ciencia de Datos Avanzada:** Cálculo Estocástico, Teoría de Grafos, Modelado NoSQL, Inferencia Variacional.

---

## 5. Naturaleza y Flujo de los Datos

Antes de aplicar cualquier algoritmo, es fundamental entender la materia prima: el dato. El objetivo final no es tener datos, sino tomar decisiones sabias.

### 5.1 Del Dato a la Sabiduría (Jerarquía DIKW)

El flujo de trabajo en ciencia de datos sigue una transformación progresiva de valor:

1.  **Datos (Data):** Símbolos brutos, hechos o señales sin contexto. 
    *   *Ejemplo:* "38", "Rojo", "10:00 AM".
2.  **Información (Information):** Datos procesados, estructurados y puestos en contexto para que tengan significado. Responde a "¿Quién?", "¿Qué?", "¿Dónde?".
    *   *Ejemplo:* "La temperatura del paciente a las 10:00 AM fue de 38 grados y tiene la garganta roja".
3.  **Conocimiento (Knowledge):** Información organizada, sintetizada e internalizada que permite comprender relaciones y patrones. Responde a "¿Cómo?".
    *   *Ejemplo:* "Una temperatura de 38 grados con garganta roja suele indicar una infección bacteriana o viral".
4.  **Sabiduría (Wisdom):** Conocimiento aplicado para la toma de decisiones y la predicción, incorporando juicio ético y pragmático. Responde a "¿Por qué?" y "¿Qué debemos hacer?".
    *   *Ejemplo:* "Dado el historial de alergias del paciente, no recetaremos penicilina y monitorearemos la fiebre 24 horas antes de intervenir".

### 5.2 Estructuración y Manipulación de Datos

Para que un algoritmo matemático pueda "digerir" la realidad, esta debe abstraerse en una estructura numérica.

*   **Datos Estructurados:** Información altamente organizada, fácilmente buscable en bases de datos relacionales (SQL).
    *   *Forma:* Tablas (filas y columnas).
    *   *Manipulación:* Dataframes (Pandas/R), Álgebra Relacional.
    *   *Ejemplo:* Una hoja de Excel con ventas por mes.
*   **Datos No Estructurados:** Información sin un modelo predefinido. Representan la mayoría de los datos modernos (80%+).
    *   *Forma:* Texto libre, imágenes (matrices de píxeles), audio (ondas), video.
    *   *Manipulación:* Requieren preprocesamiento complejo para convertirse en tensores.
        *   **Tensores:** Generalización de matrices a n-dimensiones. Una imagen a color es un tensor de (Alto x Ancho x 3 canales RGB).
        *   **Embeddings:** Convertir palabras o entidades en vectores numéricos densos que capturan su significado semántico.

**¿Qué pasa cuando no hay estructura?**
Cuando los datos son caóticos, se aplica **Ingeniería de Características (Feature Engineering)** y **ETL (Extract, Transform, Load)** para imponer una estructura o extraer señales interpretables. Si esto no es posible, se utilizan modelos de Deep Learning que pueden aprender directamente de datos crudos ("End-to-End Learning"), aunque a un costo computacional mayor.

---

## 6. Desarrollo de Métodos y Temas

A continuación, se presentan los métodos fundamentales agrupados por su paradigma de aprendizaje y función.

### 6.1 Inferencia Estadística y Validación

#### A. Pruebas de Hipótesis y Valor P (P-Value)

**¿Qué resuelve?**
Determina si existe evidencia estadística suficiente para rechazar una conjetura sobre una población, cuantificando la probabilidad de que los resultados sean producto del azar.

**Definición Técnica:**
Dado un estadístico de prueba $T$ y una hipótesis nula $H_0$, el valor P es la probabilidad de observar un valor tan extremo como $T$ asumiendo que $H_0$ es cierta: $\text{P-valor} = P(T \ge t_{obs} | H_0)$. Si P-valor < $\alpha$ (nivel de significancia), rechazamos $H_0$.

**Definición Simple:**
Imagina un juicio. La hipótesis nula es "Inocente". El valor P es la probabilidad de que las pruebas en su contra hayan aparecido por pura casualidad. Si esa probabilidad es minúscula (ej. 0.001%), entonces es "demasiada casualidad" y decides que es culpable.

**Ejemplos:**
*   **Cotidiano:** ¿Ese dado está cargado? Si sacas '6' veinte veces seguidas, el valor P es bajísimo; por tanto, el dado está cargado.
*   **Científico:** Comparar efectividad de fármacos usando intervalos de confianza (IC).

#### B. Métodos de Verosimilitud (Likelihood)

**¿Qué resuelve?**
Estima los parámetros de un modelo probabilístico que "mejor explican" los datos observados.

**Definición Técnica:**
Dada una función de densidad de probabilidad $f(x|\theta)$, la función de verosimilitud es $L(\theta|x) = f(x|\theta)$. El Estimador de Máxima Verosimilitud (MLE) busca $\hat{\theta} = \arg\max_\theta L(\theta|x)$.

**Definición Simple:**
Si encuentras una huella de zapato talla 45 en el barro (datos). La verosimilitud te ayuda a calcular cuál de tus sospechosos (parámetros) es el más probable dueño del zapato. Maximizas esa probabilidad para encontrar al culpable.

---

### 6.2 Aprendizaje Supervisado: Regresión y Clasificación

En este tipo de aprendizaje, entrenamos un modelo $f(X) \to Y$ usando pares de datos etiquetados.

#### C. Regresiones Avanzadas (Ridge, Lasso, Elastic Net)

**¿Qué resuelve?**
Mejora la regresión lineal tradicional cuando hay muchas variables o correlación entre ellas (multicolinealidad), evitando el sobreajuste (overfitting).

**Definición Técnica:**
Añaden un término de penalización (regularización) a la función de pérdida original $J(\theta)$:
*   **Ridge (L2):** Minimiza $SSE + \lambda \sum \beta_j^2$. (Contrae coeficientes hacia cero, pero no los elimina).
*   **Lasso (L1):** Minimiza $SSE + \lambda \sum |\beta_j|$. (Puede hacer coeficientes exactamente cero, actuando como selector de variables).
*   **Elastic Net:** Combina L1 y L2: $SSE + \lambda_1 \sum |\beta_j| + \lambda_2 \sum \beta_j^2$.

**Definición Simple:**
Imagina que intentas explicar el éxito con 100 razones. La regresión normal intentará usarlas todas y se confundirá.
*   Ridge: "Usa todas las razones, pero dales menos importancia a cada una para no exagerar".
*   Lasso: "Elige solo las 3 razones más importantes e ignora el resto".

**Ejemplos:**
*   **Cotidiano:** Predecir precios de casas usando 500 características (color de pared, tipo de grifo...). Lasso seleccionará solo las cruciales (metros, zona).
*   **Científico:** GWAS (Estudios de asociación del genoma completo) donde hay millones de variantes genéticas y solo pocas causan la enfermedad.

#### D. Clasificación: Máquinas de Soporte Vectorial (SVM)

**¿Qué resuelve?**
Encuentra la mejor frontera (hiperplano) que separa dos clases de datos con el máximo margen posible.

**Definición Técnica:**
Busca maximizar el margen $\frac{2}{||w||}$ entre el hiperplano $w^T x + b = 0$ y los puntos de datos más cercanos (vectores de soporte). Se resuelve como un problema de optimización convexa cuadrática. Para datos no separables linealmente, usa el "Kernel Trick" mapeando datos a una dimensión superior $K(x_i, x_j) = \phi(x_i)^T \phi(x_j)$.
*   *Soft-margin:* Permite algunos errores (violaciones del margen) controlados por un parámetro de penalización $C$.

**Definición Simple:**
Es como construir una carretera entre dos pueblos (grupos de datos). Quieres que la carretera sea lo más ancha posible para que estén bien separados. Los "vectores de soporte" son las casas más cercanas a la carretera que definen su anchura. Si no puedes trazar una recta, elevas los pueblos en el aire (Kernel) hasta que puedas pasar una plancha plana entre ellos.

#### E. Árboles de Decisión y Métodos de Ensamble

**¿Qué resuelve?**
Modelos no lineales que dividen el espacio de datos en regiones rectangulares simples mediante reglas de decisión secuenciales.

*   **Árbol de Decisión:** Divide los datos recursivamente preguntando reglas tipo "SI/NO" para maximizar la pureza (Gini/Entropía) de los nodos hijos.
*   **Random Forest (Bagging):** Crea muchos árboles distintos entrenados con subconjuntos aleatorios de datos y promedia sus resultados (Agregación Bootstrap) para reducir varianza.
*   **Boosting (Gradient Boosting/XGBoost):** Entrena árboles secuencialmente, donde cada nuevo árbol corrige los errores del anterior.

**Definición Simple:**
*   *Árbol:* Juego de "Adivina quién". ¿Es hombre? Sí. ¿Tiene gafas? No.
*   *Random Forest:* Preguntar a 100 expertos diferentes y votar por la respuesta más común (Sabiduría de las masas).
*   *Boosting:* Un estudiante hace un examen, ve qué falló, y estudia específicamente esos temas para el siguiente. Así mejora paso a paso.

**Ejemplos:**
*   **Cotidiano:** El banco decidiendo si darte un crédito (¿Tienes trabajo? -> Sí. ¿Ganas más de X? -> Sí...).
*   **Científico:** Clasificación de partículas en el Gran Colisionador de Hadrones (CERN) usando XGBoost.

#### F. K-Vecinos Más Cercanos (K-NN)

**¿Qué resuelve?**
Algoritmo simple ("lazy learning") que clasifica un punto nuevo basándose en la mayoría de sus vecinos.

**Definición Técnica:**
Dado un punto $x_q$, encuentra los $k$ puntos $x_i$ más cercanos en distancia (Euclidiana, Manhattan) y asigna la etiqueta más frecuente (moda) o el promedio (regresión).

**Definición Simple:**
"Dime con quién andas y te diré quién eres". Si tus 5 vecinos más cercanos votan por el Partido A, probablemente tú también.

---

### 6.3 Aprendizaje No Supervisado: Clustering y Reducción

#### G. K-Means (Algoritmo de Lloyd)

**¿Qué resuelve?**
Particiona datos en $k$ clusters minimizando la distancia intracluster.

**Definición Técnica:**
Itera dos pasos hasta converger: 1) Asignación: Cada punto va al centroide más cercano. 2) Actualización: Se recalcula el centroide como el promedio de los puntos asignados. (Minimiza Varianza).

**Definición Simple:**
Organizar invitados en 3 mesas. Primero se sientan al azar. Luego se mueven a la mesa donde se sientan más "parecidos" a ellos. Luego calculamos el "centro" de personalidad de la mesa. Repetimos hasta que nadie se cambie de mesa.

#### H. Clustering Jerárquico y Aglomerativo

**¿Qué resuelve?**
Crea una jerarquía de clusters (dendrograma) sin necesitar definir el número de grupos $k$ de antemano.

**Definición Técnica:**
*   *Aglomerativo (Bottom-Up):* Empieza con $n$ clusters (uno por dato) y fusiona los dos más cercanos iterativamente usando una métrica de enlace (Linkage: ward, single, complete) hasta tener un solo cluster.

**Definición Simple:**
Imagina un árbol genealógico al revés. Empiezas con individuos, luego juntas hermanos, luego primos, hasta llegar al ancestro común. Puedes "cortar" el árbol a la altura que quieras para obtener los grupos.

#### I. Evaluación de Calidad de Clusters

¿Cómo sabemos si los grupos son buenos sin tener etiquetas?
*   **Coeficiente de Silhouette:** Mide qué tan similar es un punto a su propio cluster comparado con otros clusters (Rango -1 a 1).
*   **Índice de Rand Ajustado (ARI):** Mide la similitud entre dos asignaciones de clusters, ajustado por el azar.
*   **Estadístico GAP:** Compara la dispersión del cluster con una distribución aleatoria nula uniforme.
*   **AIC / BIC:** Criterios de Información (Akaike/Bayesiano) que penalizan la complejidad del modelo (número de clusters) para evitar sobreajuste.

#### J. Modelos de Mezcla Gaussiana (GMM) y Algoritmo EM

**¿Qué resuelve?**
Clustering "suave" probabilístico. Asume que los datos vienen de una mezcla de distribuciones normales.

**Definición Técnica:**
Utiliza el algoritmo **Esperanza-Maximización (EM)**.
1.  **E-step:** Calcula la probabilidad de pertenencia de cada punto a cada gaussiana.
2.  **M-step:** Actualiza los parámetros (media, covarianza) de las gaussianas basándose en esas probabilidades.

**Definición Simple:**
K-Means dibuja círculos duros. GMM dibuja nubes difusas. Un punto puede ser "70% del cluster A y 30% del cluster B".

---

### 6.4 Inferencia Causal y Métodos Avanzados

#### K. Causalidad vs Correlación

**¿Qué resuelve?**
Distingue si X *causa* Y o si solo se mueven juntos.

*   **Variable de Confusión:** Una variable Z que influye tanto en X como en Y, creando una falsa asociación. (Ej: Consumo de helado y ataques de tiburón correlacionan, pero la causa común es el "Verano").
*   **Exogeneidad Condicional:** Supuesto de que, controlando por ciertas variables, el error es independiente de las variables explicativas.

#### L. Inferencia en Alta Dimensión (High-Dimensional Inference)

**¿Qué resuelve?**
Hacer estadística válida cuando hay más variables que datos ($p > n$).

*   **Teorema Post-Lasso (Chernozhukov):** Procedimiento de dos pasos para inferencia válida. 1) Usar Lasso para seleccionar variables relevantes (Active Set). 2) Hacer OLS estándar solo con esas variables seleccionadas para reducir el sesgo de contracción.
*   **Método LAVA (Local Aggregate / Variational):** Técnicas modernas para manejar estructuras latentes complejas o señales mixtas (sparsas y densas) en genómica y big data.

---

## 7. Ciencia de Datos Avanzada: Grafos y Procesos Estocásticos

### M. Teoría de Grafos y Clustering Espectral
*   **Matriz de Adyacencia:** Representa conexiones.
*   **Clustering Espectral:** Usa los eigenvectores del Laplaciano para separar grafos cortando pocas aristas (Min-Cut).
*   **Modularidad:** Medida de la estructura de una red; compara la densidad de bordes dentro de comunidades con la esperada al azar.
*   **Embeddings (Encajes):** Mapear nodos de un grafo complejo a vectores en $R^n$ (ej. Node2Vec) preservando su vecindad.

### N. Procesos de Márkov y LDA
*   **Cadenas de Márkov:** Sistemas donde el estado futuro depende solo del estado actual, no del pasado ("falta de memoria"). Base de algoritmos como PageRank.
*   **Latent Dirichlet Allocation (LDA):** Modelo generativo para descubrir temas abstractos en documentos (Topic Modeling). Usa **Inferencia Variacional Estocástica (SVI)** para aproximar distribuciones posteriores complejas mediante optimización, escalando a millones de documentos.

---

## 8. Herramientas de Aplicación

*   **Python:** Scikit-Learn (ML clásico), PyTorch/TensorFlow (Deep Learning), NetworkX (Grafos).
*   **R:** `glmnet` (Lasso/Ridge), `caret`.
*   **SQL/NoSQL:** MongoDB, Neo4j.

---

## 9. Referencias Bibliográficas Serias

1.  **Bishop, C. M. (2006).** *Pattern Recognition and Machine Learning*. Springer.
2.  **Hastie, T., Tibshirani, R., & Friedman, J. (2009).** *The Elements of Statistical Learning*. Springer.
3.  **Goodfellow, I., Bengio, Y., & Courville, A. (2016).** *Deep Learning*. MIT Press.
4.  **Casella, G., & Berger, R. L. (2002).** *Statistical Inference*. Duxbury.
5.  **Chernozhukov, V., et al. (2015).** *Post-Selection and Post-Regularization Inference in Linear Models with Many Controls and Instruments*. American Economic Review. (Referencia clave para Post-Lasso).
6.  **Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003).** *Latent Dirichlet Allocation*. Journal of Machine Learning Research. (Referencia clave para LDA).
7.  **Newman, M. (2018).** *Networks*. Oxford University Press.
8.  **Vapnik, V. N. (1995).** *The Nature of Statistical Learning Theory*. Springer. (Fundador de las SVM).
9.  **Pearl, J. (2009).** *Causality*. Cambridge University Press. (La referencia definitiva en inferencia causal).
10. **Tukey, J. W. (1962).** *The Future of Data Analysis*.

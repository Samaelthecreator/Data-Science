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
3.  **Probabilidad e Inferencia:** Teorema de Bayes, Pruebas de Hipótesis, Intervalos de Confianza.
4.  **Modelado Predictivo (Aprendizaje Supervisado Clásico):** Regresión Lineal, Logística, Árboles de Decisión.
5.  **Aprendizaje No Supervisado:** Clustering (K-Means), Reducción de Dimensionalidad (PCA).
6.  **Machine Learning Avanzado:** Ensemble Methods (Random Forest, XGBoost), SVM (Support Vector Machines).
7.  **Deep Learning (Redes Neuronales):** Perceptrones, CNNs (visión), RNNs/Transformers (lenguaje).
8.  **Ciencia de Datos Avanzada:** Cálculo Estocástico, Teoría de Grafos, Modelado NoSQL.
9.  **Ingeniería de Datos y Big Data:** Procesamiento distribuido, ML Ops.

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
Cuando los datos son caóticos (ej. logs de servidor mezclados, tweets con emojis), se aplica **Ingeniería de Características (Feature Engineering)** y **ETL (Extract, Transform, Load)** para imponer una estructura o extraer señales interpretables. Si esto no es posible, se utilizan modelos de Deep Learning que pueden aprender directamente de datos crudos ("End-to-End Learning"), aunque a un costo computacional mayor.

### 5.3 La Importancia de la Estructura en el Modelado

El esquema de datos dicta el método. Un algoritmo de regresión lineal espera un vector de números (estructura fija). Si le das texto, fallará. Gran parte del trabajo del científico de datos es convertir el mundo real en esa estructura matricial ($X$) que los métodos matemáticos exigen. Sin una estructura de datos limpia y representativa, el modelo más avanzado solo producirá ruido ("Garbage In, Garbage Out").

---

## 6. Desarrollo de Métodos y Temas

A continuación, se presentan los métodos fundamentales agrupados por su paradigma de aprendizaje.

### 6.1 Inferencia Estadística

Antes del Machine Learning, la inferencia estadística nos permite sacar conclusiones sobre una población total observando solo una pequeña muestra.

#### A. Pruebas de Hipótesis (Hypothesis Testing)

**¿Qué resuelve?**
Determina si existe evidencia suficiente en una muestra para inferir que una condición es verdadera para toda la población, distinguiendo efectos reales del azar.

**¿Por qué es importante?**
Es la base del método científico. Valida si un medicamento funciona o si una estrategia de ventas surtió efecto.

**Definición Técnica:**
Un test calcula la probabilidad (p-valor) de observar un estadístico $T$ bajo el supuesto de una hipótesis nula $H_0$. Si $P(T|H_0) < \alpha$, rechazamos $H_0$.

**Definición Simple (Secundaria):**
Imagina que eres un juez. La "Hipótesis Nula" es que el acusado es inocente. Las "pruebas" son los datos. Si las pruebas son muy contundentes (la probabilidad de que sea inocente con esas pruebas es bajísima, casi cero), entonces dictas sentencia de "culpable". Si las pruebas son débiles, mantienes la inocencia. No pruebas que es inocente, solo que no hay pruebas suficientes para condenarlo.

**Ejemplos:**
*   **Cotidiano:** ¿La moneda está trucada? Si lanzo 100 veces y salen 99 caras, es casi imposible que sea suerte.
*   **Científico:** Comparar si la vacuna A es más efectiva que la vacuna B en un ensayo clínico.

---

### 6.2 Aprendizaje Supervisado

En este tipo de aprendizaje, "enseñamos" a la computadora con ejemplos. Le damos los datos de entrada ($X$) y la respuesta correcta ($Y$). El objetivo es que la máquina aprenda la relación para predecir $Y$ en datos nuevos.

**(Si la respuesta $Y$ es un número, se llama Regresión. Si es una categoría, Clasificación).**

#### B. Regresión Lineal (Linear Regression)

**¿Qué resuelve?**
Predice un valor numérico continuo basándose en otras variables relacionadas.

**¿Por qué es importante?**
Permite estimar cantidades futuras (ventas, precios) de forma simple e interpretable.

**Definición Técnica:**
Minimiza el error cuadrático medio entre los datos observados y una función lineal: $\hat{y} = \beta_0 + \beta_1 x$. Se optimiza encontrando $\beta$ tal que $\nabla ||Y - X\beta||^2 = 0$.

**Definición Simple (Secundaria):**
Tienes una hoja de papel con muchos puntos dispersos. Tu tarea es usar una regla y un lápiz para dibujar una sola línea recta que pase lo más cerca posible de todos los puntos al mismo tiempo. Esa línea te permite "adivinar" dónde caerán futuros puntos.

**Ejemplos:**
*   **Cotidiano:** Predecir cuánto costará una casa según su tamaño.
*   **Científico:** Estimar la expansión del universo midiendo la distancia y velocidad de galaxias.

#### C. Regresión Logística (Logistic Regression)

**¿Qué resuelve?**
Clasifica datos en dos opciones (Sí/No, 0/1) calculando la *probabilidad* de que pertenezcan a una de ellas.

**¿Por qué es importante?**
Fundamental para toma de decisiones binarias con incertidumbre (riesgo de crédito, diagnósticos).

**Definición Técnica:**
Modela la probabilidad $P(Y=1|X)$ usando la función sigmoide $\sigma(z) = \frac{1}{1+e^{-z}}$, ajustando parámetros por Máxima Verosimilitud.

**Definición Simple (Secundaria):**
Imagina que quieres separar manzanas rojas de manzanas verdes en una mesa. La regresión logística es como poner una vara (frontera) en la mesa. Todo lo que esté a un lado de la vara se etiqueta como "Posiblemente Rojo" y al otro como "Posiblemente Verde". Además, te dice qué tan seguro está (ej: "Estoy 90% seguro de que esto es rojo").

**Ejemplos:**
*   **Cotidiano:** Filtro de SPAM (¿Es correo basura o no?).
*   **Científico:** Predecir si un paciente tiene una enfermedad (Sí/No) según sus análisis.

#### F. Redes Neuronales (Deep Learning - MLP)

**¿Qué resuelve?**
Aprende patrones extremadamente complejos y no lineales (caras, voces, traducción).

**¿Por qué es importante?**
Permite a las computadoras "ver" y "escuchar", resolviendo problemas que no tienen reglas matemáticas simples.

**Definición Técnica:**
Composición de funciones no lineales en capas. $f(x) = \sigma(W_2 \sigma(W_1 x))$. Se entrena vía Backpropagation del gradiente del error.

**Definición Simple (Secundaria):**
Es como un equipo de personas pasándose un mensaje. La primera fila ve una foto y pasa detalles simples ("hay una línea curva") a la segunda fila. La segunda fila combina eso ("parece un ojo"). La tercera fila combina más ("es una cara"). Al final, deciden juntos qué hay en la foto. Aprenden corrigiéndose unos a otros cuando se equivocan.

**Ejemplos:**
*   **Cotidiano:** Desbloqueo facial de tu celular.
*   **Científico:** Detectar patrones genéticos ocultos en el ADN.

---

### 6.3 Aprendizaje No Supervisado

Aquí, la computadora trabaja sola, sin maestro. Le damos datos ($X$) pero *no* le damos respuestas ($Y$). Su tarea es encontrar estructuras, grupos o patrones ocultos por sí misma.

#### D. K-Means Clustering (Agrupamiento)

**¿Qué resuelve?**
Agrupa objetos similares en "clusters" o montones, sin saber qué son esos objetos de antemano.

**¿Por qué es importante?**
Ayuda a descubrir segmentos naturales en datos caóticos (clientes, especies biológicas).

**Definición Técnica:**
Particiona datos en $k$ conjuntos minimizando la varianza intra-cluster (distancia euclidiana al centroide $\mu$). Algoritmo iterativo Expectation-Maximization.

**Definición Simple (Secundaria):**
Imagina que tienes una bolsa de canicas de muchos colores mezclados y te pido que las separes en 3 montones. No te digo qué colores buscar, solo que pongas las que se parecen juntas. Al final tendrás un montón de "rojizas", otro de "azuladas", etc., sin que yo te dijera cómo hacerlo.

**Ejemplos:**
*   **Cotidiano:** Netflix creando grupos de usuarios con gustos similares ("Amantes de comedias").
*   **Científico:** Clasificar nuevas especies de plantas por su forma sin saber sus nombres.

#### E. Análisis de Componentes Principales (PCA)

**¿Qué resuelve?**
Simplifica datos complejos reduciendo su cantidad de variables, pero conservando la información importante.

**¿Por qué es importante?**
Permite visualizar datos de muchas dimensiones (imposibles de ver para humanos) y elimina el "ruido".

**Definición Técnica:**
Transformación ortogonal que proyecta datos a un nuevo sistema de coordenadas (componentes principales) donde la varianza se maximiza progresivamente. Utiliza valores propios de la matriz de covarianza.

**Definición Simple (Secundaria):**
Imagina la sombra de un objeto 3D (como una tetera) en la pared. El objeto es complejo, pero la sombra es plana (2D). Si giras la tetera hasta que la sombra muestre su forma más clara (donde se ve el mango y el pico), has hecho un PCA: has reducido un objeto 3D a una imagen 2D perdiendo la menor cantidad de detalle posible.

**Ejemplos:**
*   **Cotidiano:** Comprimir una imagen JPG (quitas datos pero la foto se ve casi igual).
*   **Científico:** Analizar miles de genes y encontrar los 2 o 3 "super-genes" responsables de una enfermedad.

---

# PARTE II: CIENCIA DE DATOS AVANZADA
*Temas especializados para modelado complejo, inferencia en alta dimensión y sistemas estocásticos.*

## 7. Estrategias Avanzadas de Aprendizaje Supervisado

### G. Máquinas de Soporte Vectorial (SVM)

**¿Qué resuelve?**
Clasifica datos que no son linealmente separables (ej. una nube de puntos rojos rodeada de puntos azules) mapeándolos a dimensiones superiores.

**¿Por qué es importante?**
Es extremadamente robusto en espacios de alta dimensión y cuando se tienen pocos datos de entrenamiento (ej. clasificación de genes o imágenes médicas).

**Definición Técnica:**
Busca el hiperplano óptimo que maximiza el *margen* (distancia a los puntos más cercanos de cada clase). Utiliza el "Kernel Trick" $K(x_i, x_j)$ para proyectar los datos a un espacio de características de mayor dimensión donde son linealmente separables sin calcular explícitamente las coordenadas.

**Definición Simple (Secundaria):**
Imagina puntos rojos y azules en una mesa que no puedes separar con una vara recta. SVM golpea la mesa por debajo para que los puntos salten al aire; mientras están en el aire, pasa una hoja de papel (hiperplano) que los separa perfectamente.

**Ejemplos:**
*   **Científico:** Clasificación de proteínas.
*   **Cotidiano:** Reconocimiento de escritura a mano.

### H. Métodos de Ensamble (Random Forest & Boosting)

**¿Qué resuelve?**
Mejora la precisión y reduce el error combinando la "opinión" de múltiples modelos simples (árboles de decisión) en lugar de confiar en uno solo muy complejo.

**¿Por qué es importante?**
Dominan las competencias de ciencia de datos (como Kaggle) para datos tabulares debido a su alto rendimiento y robustez.

**Definición Técnica:**
*   **Bagging (Random Forest):** Entrena múltiples árboles en paralelo con subconjuntos aleatorios de datos (Bootstrap) y promedia sus predicciones para reducir la varianza.
*   **Boosting (XGBoost, AdaBoost):** Entrena árboles secuencialmente, donde cada nuevo árbol se enfoca en corregir los errores cometidos por los anteriores, reduciendo el sesgo.

**Definición Simple (Secundaria):**
Es la "sabiduría de las multitudes". Si le preguntas a un solo experto, puede equivocarse. Pero si le preguntas a 100 personas promedio y tomas la decisión de la mayoría, es mucho más probable que aciertes. Random Forest es esa votación democrática; Boosting es un equipo donde cada experto se especializa en resolver lo que el anterior no pudo.

**Ejemplos:**
*   **Finanzas:** Detección de fraude en tarjetas de crédito.
*   **Medicina:** Diagnóstico basado en múltiples síntomas.

---

## 8. Regresión y Regularización (Alta Dimensión)

### I. Regresión Penalizada (Ridge, Lasso, Elastic Net)

**¿Qué resuelve?**
Permite entrenar modelos cuando hay demasiadas variables (incluso más variables que datos, $p > n$) o cuando las variables están muy correlacionadas (multicolinealidad), situaciones donde la regresión normal falla.

**¿Por qué es importante?**
Es fundamental en la era del Big Data, Genómica y Finanzas, donde tenemos miles de características posibles pero historias limitadas.

**Definición Técnica:**
Añade un término de penalización a la función de costo para restringir la magnitud de los coeficientes $\beta$.
*   **Ridge (L2):** Minimiza $Error + \lambda \sum \beta^2$. "Encoge" los coeficientes hacia cero pero no los elimina.
*   **Lasso (L1):** Minimiza $Error + \lambda \sum |\beta|$. Fuerza a que algunos coeficientes sean exactamente cero, realizando *selección de variables*.
*   **Elastic Net:** Combina L1 y L2.

**Definición Simple (Secundaria):**
Imagina que quieres explicar el éxito de una película y tienes 1000 posibles razones. La regresión normal se confundirá e inventará relaciones falsas. Lasso es un filtro estricto que dice: "Solo puedes elegir las 5 razones más importantes, el resto ignóralas". Ridge dice: "Puedes usar todas, pero no le des demasiada importancia a ninguna en particular".

**Ejemplos:**
*   **Genómica:** Encontrar genes causantes de cáncer entre 20,000 posibilidades con solo 100 pacientes.
*   **Economía:** Predicción de inflación con miles de indicadores macroeconómicos.

### J. Inferencia Post-Lasso

**¿Qué resuelve?**
Resuelve el problema de invalidez estadística que ocurre al usar los mismos datos para seleccionar variables y para testear hipótesis (Sesgo de Selección).

**¿Por qué es importante?**
Sin esto, los p-valores y los intervalos de confianza en modelos de alta dimensión son falsos. Es esencial para la inferencia causal moderna.

**Definición Técnica:**
Utiliza un proceso de "Doble Selección" u ortogonalización para separar el efecto de la variable de interés de las variables de confusión (confounders) seleccionadas por Lasso, permitiendo obtener estimadores con propiedades asintóticas normales válidas.

**Definición Simple (Secundaria):**
Si usas los datos para elegir a los "sospechosos" (variables) y luego usas los mismos datos para "juzgarlos", tu juicio está viciado. Post-Lasso es un método legal riguroso para separar la fase de investigación (selección) de la fase de juicio (inferencia), asegurando que el veredicto sea justo.

---

## 9. Validación y Métricas Rigurosas

### K. Evaluación de Predicción

**¿Qué resuelve?**
Cuantifica qué tan bueno es un modelo prediciendo la realidad y si es mejor que el azar o un promedio simple.

**Definición Técnica:**
*   **Regresión:**
    *   *Error Cuadrático Medio (MSE):* Promedio de los errores al cuadrado ($\frac{1}{n}\sum(y-\hat{y})^2$).
    *   *R² (Coeficiente de Determinación):* Proporción de la varianza explicada por el modelo.
*   **Clasificación:**
    *   *F-Score:* Media armónica entre Precisión ($P = \frac{TP}{TP+FP}$) y Exhaustividad ($R = \frac{TP}{TP+FN}$). Identifica el balance óptimo.
    *   *ANOVA:* Análisis de Varianza para comparar si las diferencias en predicciones entre grupos son significativas.

### L. Evaluación de Clusters (No Supervisado)

**¿Qué resuelve?**
Determina si los grupos encontrados por un algoritmo son reales o meras coincidencias, ya que no hay "respuestas correctas" (etiquetas) para comparar.

**Definición Técnica:**
*   **Coeficiente de Silhouette:** Mide qué tan parecido es un objeto a su propio cluster ($a$) comparado con el cluster vecino más cercano ($b$). $S = \frac{b-a}{\max(a,b)}$. Rango [-1, 1].
*   **Estadístico GAP:** Compara la dispersión intra-cluster del modelo contra la dispersión esperada de una distribución aleatoria de referencia. Si el Gap es grande, los clusters son reales.
*   **Índice de Rand Ajustado (ARI):** Mide la similitud entre dos agrupamientos (ej. uno real y uno predicho), corrigiendo por el azar. 0 es aleatorio, 1 es perfecto.

### M. Criterios de Selección de Modelos (AIC / BIC)

**¿Qué resuelve?**
Ayuda a elegir el mejor modelo buscando un equilibrio entre precisión (ajuste) y simplicidad (parsimonia).

**Definición Técnica:**
Penalizan la verosimilitud (Likelihood, $L$) según el número de parámetros ($k$).
*   **AIC (Akaike):** $2k - 2\ln(L)$. Mejor para predicción.
*   **BIC (Bayesiano):** $k \ln(n) - 2\ln(L)$. Penaliza más fuerte la complejidad a medida que crecen los datos ($n$); busca el modelo "verdadero".

**Definición Simple (Secundaria):**
Es la aplicación matemática del principio de la Navaja de Ockham: "La explicación más simple que se ajusta a los datos suele ser la mejor".

---

## 10. Aprendizaje No Supervisado Avanzado

### N. Clustering Jerárquico

**¿Qué resuelve?**
Organiza los datos en una estructura de árbol (dendrograma) de grupos anidados, mostrando relaciones de sub-grupos, sin necesidad de definir un número de clusters $k$ inicial.

**¿Por qué es importante?**
Útil en biología (taxonomía) y organización de documentos, donde las categorías tienen niveles (ej. Animal -> Mamífero -> Canino).

**Definición Técnica:**
*   *Aglomerativo:* Comienza con $N$ clusters (cada punto es uno) y fusiona iterativamente los más cercanos.
*   *Divisivo:* Comienza con 1 cluster gigante y lo divide recursivamente.

### O. Modelos Probabilísticos (GMM & EM)

**¿Qué resuelve?**
Permite el "Clustering Suave" (Soft Clustering), donde un punto puede pertenecer parcialmente a varios grupos con diferente probabilidad.

**Definición Técnica:**
*   **GMM (Gaussian Mixture Models):** Asume que los datos provienen de una mezcla de varias distribuciones normales (campanas de Gauss).
*   **Algoritmo EM (Esperanza-Maximización):** Método iterativo para encontrar los parámetros máximamente verosímiles de estos modelos cuando hay variables latentes (ocultas).

**Definición Simple (Secundaria):**
En lugar de decir "Este cliente es VIP" (etiqueta rígida), dice "Este cliente tiene un 70% de probabilidad de ser VIP y un 30% de ser Regular". Captura mejor la ambigüedad y matices de la realidad.

### P. Modelado de Tópicos (LDA)

**¿Qué resuelve?**
Descubre temas abstractos ocultos dentro de una colección masiva de documentos de texto.

**Definición Técnica:**
**Asignación Latente de Dirichlet (LDA):** Modelo generativo que asume que cada documento es una mezcla de tópicos y cada tópico es una mezcla de palabras. Utiliza inferencia bayesiana para revertir este proceso y descubrir los tópicos subyacentes.

**Definición Simple (Secundaria):**
Imagina que te dan mil licuados de frutas diferentes (documentos) y tienes que averiguar qué frutas (tópicos) se usaron para hacerlos, solo probándolos, sin ver la receta. LDA "desmezcla" los licuados para encontrar los ingredientes originales.

---

## 11. Sistemas Complejos y Estocásticos

### Q. Teoría de Grafos y Redes

**¿Qué resuelve?**
Analiza relaciones y conectividad entre entidades, no solo sus propiedades individuales.

**Conceptos Clave:**
*   **Matriz de Adyacencia/Laplaciana:** Representación matricial de la red y sus conexiones.
*   **Clustering Espectral:** Usa los eigenvectores de la matriz Laplaciana para particionar el grafo en comunidades óptimas (Min-Cut).
*   **Embeddings:** Algoritmos como DeepWalk o Node2Vec que aprenden representaciones vectoriales de los nodos basadas en sus vecinos.

**Ejemplo:**
Redes sociales (detectar comunidades de amigos), Rutas logísticas, Análisis de fraude financiero (redes de lavado de dinero).

### R. Cadenas de Markov

**¿Qué resuelve?**
Modela sistemas que cambian de estado aleatoriamente con el tiempo, donde el futuro depende únicamente del presente.

**Definición Técnica:**
Un proceso estocástico sin memoria (Propiedad de Markov): $P(X_{t+1}|X_t, X_{t-1},...) = P(X_{t+1}|X_t)$. Se define por una Matriz de Transición que contiene las probabilidades de pasar de un estado a otro.

**Definición Simple (Secundaria):**
Es como un juego de mesa donde tu próximo movimiento depende solo de en qué casilla estás ahora, no de cómo llegaste allí. Por ejemplo, predecir el clima de mañana basándose solo en el clima de hoy.

**Ejemplos:**
*   **Tecnología:** El algoritmo PageRank de Google original (un caminante aleatorio en la web).
*   **Texto:** Teclados predictivos ("Hola, ¿cómo...?" -> "estás").

---

## 12. Ingeniería de Características (Feature Engineering)

### S. Codificación (Encoding) e Imputación

**¿Qué resuelve?**
Transforma datos crudos incompatibles (texto, categorías, valores nulos) en un formato numérico limpio y completo que los algoritmos estandarizados pueden procesar matemáticamente.

**¿Por qué es importante?**
La mayoría de los algoritmos avanzados (SVM, Redes Neuronales, Regresión Lineal) no pueden operar sobre cadenas de texto (ej. "Rojo", "Azul") ni sobre huecos vacíos (NaN). La calidad de la entrada determina el límite superior de la calidad del modelo.

**Definición Técnica:**
*   **One-Hot Encoding:** Transforma una variable categórica de cardinalidad $k$ en $k$ variables binarias (dummys) ortogonales $\in \{0,1\}$, evitando asumir orden donde no existe.
*   **Imputación:** Estima $P(X_{missing} | X_{observed})$. Puede ser simple (media/mediana) o basada en modelos (K-NN Imputation, MICE - Multiple Imputation by Chained Equations).

**Definición Simple (Secundaria):**
Es como un traductor universal. Si le hablas en "Español" (palabras) a una calculadora, no te entenderá. Tienes que traducir "perro" a un código numérico. Y si al libro le faltan páginas (datos nulos), tratas de deducir qué decían leyendo el contexto de las páginas anteriores.

**Ejemplos:**
*   **Finanzas:** Convertir "Nivel de Riesgo: Alto/Medio/Bajo" en números puros.
*   **Salud:** Rellenar un dato de presión arterial faltante usando la edad y peso del paciente.

### T. Transformación de Variables (Box-Cox & Scaling)

**¿Qué resuelve?**
Modifica la escala, forma o distribución de los datos para que cumplan con las asunciones teóricas de los algoritmos (como la normalidad o la homocedasticidad).

**Definición Técnica:**
*   **Estandarización (Z-Score):** $z = \frac{x - \mu}{\sigma}$. Re-csala los datos para tener media 0 y desviación estándar 1. Vital para algoritmos basados en distancia (K-Means, SVM).
*   **Transformación Box-Cox:** Familia de transformaciones de potencia $y(\lambda)$ parametrizadas por $\lambda$ diseñadas para estabilizar la varianza y hacer que los datos se aproximen a una distribución Normal Gaussiana.

---

## 13. Bibliografía
1.  **Bishop, C. M.** (2006). *Pattern Recognition and Machine Learning*. Springer.
2.  **Hastie, T., Tibshirani, R., & Friedman, J.** (2009). *The Elements of Statistical Learning*. Springer.
3.  **Murphy, K. P.** (2012). *Machine Learning: A Probabilistic Perspective*. MIT Press.
4.  **Pearl, J.** (2009). *Causality*. Cambridge University Press.
5.  **Goodfellow, I., Bengio, Y., & Courville, A.** (2016). *Deep Learning*. MIT Press.
6.  **Kuhn, M., & Johnson, K.** (2013). *Applied Predictive Modeling*. Springer.
7.  **Chernozhukov, V.** (2015). *Post-Selection and Post-Regularization Inference*.

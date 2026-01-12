# Ciencia de Datos: Fundamentos Teóricos y Matemáticos

## 1. Introducción y Contexto

**Definición Técnica Rigurosa:**
Sea $D$ un conjunto de datos (dataset) que representa un fenómeno observable. La Ciencia de Datos se define como el estudio de funciones computables $f: D \to I$, donde $I$ representa información o conocimiento procesable. Este proceso implica la intersección de la **Estadística**, las **Matemáticas** y las **Ciencias de la Computación**.

A diferencia del análisis de datos tradicional, la Ciencia de Datos no solo busca describir el pasado, sino utilizar modelos para inferir $P(Y|X)$, la probabilidad de un resultado futuro $Y$ dado un conjunto de variables observadas $X$.

### 5.1 Naturaleza y Flujo de los Datos (DIKW)

Antes de modelar, los datos pasan por una jerarquía de valor:
1.  **Datos:** Símbolos brutos ("38", "Rojo").
2.  **Información:** Datos con contexto ("Temperatura: 38°C").
3.  **Conocimiento:** Información sintetizada ("Tiene fiebre").
4.  **Sabiduría:** Juicio aplicado ("Administrar antipirético").

**Estructuración:**
*   **Datos Estructurados:** Tablas relacionales (SQL).
*   **Datos No Estructurados:** Texto, imágenes, audio (requieren transformación a tensores/embeddings).

---

# PARTE I: FUNDAMENTOS Y MÉTODOS ESENCIALES
*Métodos estándar enseñados en cursos introductorios.*

## 6. Inferencia Estadística Básica

### A. Pruebas de Hipótesis (Hypothesis Testing)
*   **Conceptos Clave:**
    *   *Hipótesis Nula ($H_0$):* La suposición por defecto (ej. "no hay efecto", "es azar").
    *   *Nivel de Significancia ($\alpha$):* El umbral de error aceptable (usualmente 0.05).
    *   *Valor P:* Probabilidad de obtener los resultados observados asumiendo que $H_0$ es cierta.

**¿Qué resuelve?**
Determina si existe evidencia suficiente en una muestra de datos para inferir que una cierta condición es verdadera para toda la población. Resuelve el problema de distinguir entre un efecto real y el mero azar.

**¿Por qué es importante?**
Es la base del método científico cuantitativo. Sin ella, no podríamos validar si un nuevo medicamento funciona realmente o si es simple coincidencia.

**Definición Técnica:**
Sea $H_0$ la hipótesis nula y $H_1$ la alternativa. Un test calcula un estadístico $T$ a partir de los datos. El Valor P es $P(T \ge t_{obs} | H_0)$. Definimos una región crítica $C_\alpha$ tal que $P(T \in C_\alpha | H_0) = \alpha$. Rechazamos $H_0$ si el valor P $< \alpha$.

**Definición Simple:**
Imagina un juicio. La hipótesis nula es "Inocente". El Valor P es la probabilidad de que las pruebas en su contra hayan aparecido por pura casualidad. Si esa probabilidad es minúscula (ej. 0.001%), entonces es "demasiada casualidad" y decides que es culpable.

**Ejemplos:**
*   **Cotidiano:** Determinar si un dado está cargado. Si sacas un '6' veinte veces seguidas, la probabilidad (valor P) es tan baja que concluyes que está trucado.
*   **Científico:** Ensayo clínico. Comparar la tasa de curación del Grupo Medicamento vs Grupo Placebo para ver si la diferencia es significativa.

## 7. Aprendizaje Supervisado (Básico)
*Modelo $f(X) \to Y$ entrenado con ejemplos etiquetados.*

### B. Regresión Lineal (Linear Regression)
*   **Conceptos Clave:**
    *   *Variable Dependiente ($Y$):* Lo que quieres predecir.
    *   *Residuos:* Diferencia entre el valor real y el predicho ($y_i - \hat{y}_i$).
    *   *Mínimos Cuadrados:* Método para encontrar la mejor línea minimizando errores.

**¿Qué resuelve?**
Modela la relación entre una variable continua $Y$ y una o más variables $X$. Predice el valor numérico de $Y$ basándose en $X$ asumiendo una tendencia lineal.

**¿Por qué es importante?**
Permite cuantificar relaciones (ej. "por cada año extra de experiencia, el salario sube $X") y hacer predicciones simples e interpretables.

**Definición Técnica:**
Dado un conjunto $\{ (x_i, y_i) \}$, y el modelo $Y = X\beta + \epsilon$, buscamos el vector $\hat{\beta}$ que minimice la Suma de Errores Cuadráticos ($SSE$):
$$ J(\beta) = ||Y - X\beta||^2 $$
La solución cerrada es $\hat{\beta} = (X^T X)^{-1} X^T Y$.

**Definición Simple:**
Tienes puntos dispersos en un papel. Usas una regla para dibujar una sola línea recta que pase lo más cerca posible de todos los puntos a la vez (promediando las distancias). Esa línea predice dónde caerán los futuros puntos.

**Ejemplos:**
*   **Cotidiano:** Predecir el precio de una casa basándose en sus metros cuadrados.
*   **Científico:** Ley de Hubble. Estimar la velocidad de expansión del universo midiendo la distancia de las galaxias.

### C. Regresión Logística (Logistic Regression)
*   **Conceptos Clave:**
    *   *Función Sigmoide:* Curva en forma de 'S' que convierte cualquier número en una probabilidad (0 a 1).
    *   *Odds (Probabilidad):* Razón entre probabilidad de éxito y fracaso.
    *   *Frontera de Decisión:* Línea que separa las clases.

**¿Qué resuelve?**
Clasifica datos en categorías discretas (generalmente binarias: Sí/No) calculando la probabilidad de pertenencia a la clase positiva.

**¿Por qué es importante?**
Es el estándar mundial para calcular riesgos (médicos, financieros) donde la respuesta no es un número, sino una decisión binaria con incertidumbre.

**Definición Técnica:**
Modelamos la probabilidad $P(Y=1|X)$ usando la función logística:
$$ P(Y=1|X) = \sigma(\beta^T X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \dots)}} $$
Los parámetros $\beta$ se estiman maximizando la función de Verosimilitud (Likelihood) o minimizando la Entropía Cruzada.

**Definición Simple:**
Imagina querer separar manzanas rojas de verdes en una mesa usando una vara recta. La regresión logística pone esa vara y además te dice, para cada manzana, qué tan seguro está: "Estoy 95% seguro de que esta es roja" (está muy lejos de la vara) vs "Estoy 51% seguro" (está casi en la línea).

**Ejemplos:**
*   **Cotidiano:** Filtro de Spam. Calcula la probabilidad de que un email sea basura basándose en palabras clave.
*   **Científico:** Medicina. Calcular la probabilidad de que un paciente sufra un infarto basándose en su colesterol, edad y peso.

## 8. Aprendizaje No Supervisado (Básico)
*Buscar patrones en $X$ sin tener etiquetas $Y$.*

### D. K-Means Clustering
*   **Conceptos Clave:**
    *   *Centroide:* El punto central promedio de un grupo (cluster).
    *   *Varianza Intra-cluster:* Medida de qué tan compactos (similares) son los puntos de un grupo.
    *   *Distancia Euclidiana:* La "línea recta" entre dos puntos.

**¿Qué resuelve?**
Agrupa un conjunto de datos desordenado en $k$ grupos distintos basándose en su similitud geométrica, sin saber de antemano qué son.

**¿Por qué es importante?**
Permite descubrir estructuras ocultas, segmentar poblaciones y organizar información que nadie ha etiquetado manualmente.

**Definición Técnica:**
El objetivo es particionar $n$ observaciones en $k$ clusters $S$ para minimizar la suma de las distancias al cuadrado dentro de cada cluster (Inercia):
$$ \arg \min_S \sum_{i=1}^{k} \sum_{x \in S_i} ||x - \mu_i||^2 $$
Donde $\mu_i$ es el centroide. Se usa el algoritmo iterativo de Lloyd (Asignación -> Actualización).

**Definición Simple:**
Imagina una fiesta donde nadie se conoce. Le pides a la gente que se junte en 3 grupos con lso que se parezcan más. Primero se juntan al azar, luego se mueven de mesa en mesa buscando gente más afín, hasta que todos están en el grupo más parecido a ellos.

**Ejemplos:**
*   **Cotidiano:** Segmentación de Clientes. El supermercado descubre grupos como "Compradores de fin de semana" o "Familias numerosas" analizando tickets de compra.
*   **Científico:** Biología. Clasificar nuevas especies de plantas analizando el tamaño de sus hojas y tallos sin conocer su nombre taxonómico.

### E. Análisis de Componentes Principales (PCA)
*   **Conceptos Clave:**
    *   *Dimensionalidad:* Número de variables (columnas) en tus datos.
    *   *Varianza:* Cantidad de información o "diversidad" en los datos.
    *   *Ortogonalidad:* Variables independientes (perpendiculares) entre sí.

**¿Qué resuelve?**
Simplifica datos complejos reduciendo su número de variables, transformándolas en un conjunto menor de "super-variables" (Componentes Principales) que resumen la información.

**¿Por qué es importante?**
Permite visualizar datos imposibles de ver (más de 3 dimensiones), elimina ruido y acelera el procesamiento (combate la maldición de la dimensionalidad).

**Definición Técnica:**
Es una transformación lineal ortogonal que proyecta los datos a un nuevo sistema de coordenadas donde la mayor varianza se encuentra en la primera coordenada (Primer Componente). Matemáticamente, corresponde a la descomposición en valores propios (eigendecomposition) de la matriz de covarianza $\Sigma$:
$$ \Sigma v = \lambda v $$

**Definición Simple:**
Imagina la sombra de una tetera (objeto 3D) en la pared (2D). Si giras la tetera hasta encontrar la sombra que mejor muestra su forma (donde se ve el mango, el pico y el cuerpo), has hecho PCA: has reducido 3 dimensiones a 2 perdiendo la menor cantidad de detalles posible.

**Ejemplos:**
*   **Cotidiano:** Compresión de Imágenes. Reducir el peso de un archivo JPG eliminando los detalles que el ojo humano apenas percibe.
*   **Científico:** Genética. Analizar miles de genes y resumirlos en 2 o 3 componentes que explican la predisposición a una enfermedad.

### F. Redes Neuronales (Deep Learning - MLP)
*   **Conceptos Clave:**
    *   *Neurona Artificial:* Unidad que recibe entradas, las suma con pesos y aplica una función.
    *   *Función de Activación:* El "gatillo" no lineal (ej. ReLU) que decide si la neurona se activa.
    *   *Backpropagation:* Algoritmo para corregir los errores ajustando los pesos hacia atrás.

**¿Qué resuelve?**
Aprende relaciones extremadamente complejas y no lineales que los algoritmos tradicionales no pueden captar, como reconocer objetos en fotos o entender lenguaje.

**¿Por qué es importante?**
Es el motor de la Inteligencia Artificial moderna (Visión por Computadora, Chatbots, Conducción Autónoma).

**Definición Técnica:**
Un Perceptrón Multicapa (MLP) es una composición de funciones $f(x) = f^{(L)}(\dots f^{(1)}(x))$. Cada capa realiza una transformación afín seguida de una activación no lineal $\sigma$:
$$ h^{(l)} = \sigma(W^{(l)} h^{(l-1)} + b^{(l)}) $$
Se entrena minimizando una función de costo $J$ mediante Gradiente Descendente.

**Definición Simple:**
Es como un equipo gigante de personas pasándose un mensaje ("teléfono descompuesto" pero corregido). La primera fila ve píxeles y dice "veo bordes". La segunda junta bordes y dice "veo ojos". La tercera dice "es una cara". Aprenden corrigiéndose unos a otros cada vez que se equivocan.

**Ejemplos:**
*   **Cotidiano:** Desbloqueo Facial. Tu celular reconoce tu cara en distintos ángulos.
*   **Científico:** Plegamiento de Proteínas (AlphaFold). Predecir la forma 3D de una proteína a partir de su secuencia de ADN.

---

# PARTE II: CIENCIA DE DATOS AVANZADA
*Temas especializados para modelado complejo y validación rigurosa.*

## 9. Evaluación y Validación de Clusters

### G. Coeficiente de Silhouette
*   **Conceptos Clave:**
    *   *Cohesión ($a$):* Distancia media a puntos del mismo cluster.
    *   *Separación ($b$):* Distancia media al cluster vecino más cercano.

**¿Qué resuelve?**
Evalúa la calidad de un cluster individual sin tener etiquetas reales.

**¿Por qué es importante?**
Valida si la agrupación tiene sentido físico o es artificial.

**Definición Técnica:**
$S = \frac{b - a}{\max(a, b)}$. Varía de -1 (mal asignado) a +1 (perfectamente asignado).

### H. Estadístico GAP
*   **Conceptos Clave:**
    *   *Distribución Nula:* Datos aleatorios uniformes sin patrones.
    *   *Dispersión:* Medida de "desorden".

**¿Qué resuelve?**
Determina el número óptimo de clusters ($k$) comparando contra el azar.

**¿Por qué es importante?**
Evita ver patrones donde no los hay.

**Definición Técnica:**
Compara la dispersión del modelo ($W_k$) contra la dispersión esperada de una distribución aleatoria ($W_k^{ref}$). $\text{Gap}(k) = E[\log(W_k^{ref})] - \log(W_k)$.

### I. Criterios de Selección (AIC / BIC)
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

### J. Regularización (Ridge, Lasso, Elastic Net)
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

### K. Inferencia Post-Lasso
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

### L. Máquinas de Soporte Vectorial (SVM)
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

### M. Métodos de Ensamble (Trees & Forests)
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

### N. Clustering Probabilístico (GMM)
*   **Conceptos Clave:**
    *   *Variable Latente:* Pertenencia oculta a un grupo.
    *   *Algoritmo EM:* Esperanza-Maximización.

**¿Qué resuelve?**
Clustering "suave" donde un punto puede pertenecer parcialmente a varios grupos.

**¿Por qué es importante?**
Modela la incertidumbre en la asignación de grupos.

**Definición Técnica:**
Asume que los datos vienen de una mezcla de distribuciones Gaussianas y optimiza sus parámetros iterativamente con EM.

### O. Asignación Latente de Dirichlet (LDA)
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

### P. Teoría de Grafos
*   **Conceptos Clave:**
    *   *Matriz Laplaciana:* ($D - A$) Describe la conectividad.
    *   *Eigenvector:* Vector propio de la matriz.

**¿Qué resuelve?**
Encuentra comunidades en redes basándose en conexiones, no distancia.

**¿Por qué es importante?**
Fundamental para redes sociales y conexiones neuronales.

**Definición Técnica:**
Clustering Espectral: Usa los eigenvectores asociados a los valores propios más pequeños del Laplaciano para particionar el grafo (Min-Cut).

### Q. Cálculo Estocástico
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

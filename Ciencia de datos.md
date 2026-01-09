# Ciencia de Datos: Fundamentos Teóricos y Matemáticos

## 1. Introducción y Contexto

**Definición Técnica Rigurosa:**
Sea $D$ un conjunto de datos (dataset) que representa un fenómeno observable. La Ciencia de Datos se define como el estudio de funciones computables $f: D \to I$, donde $I$ representa información o conocimiento procesable. Este proceso implica la intersección de la **Estadística**, las **Matemáticas** y las **Ciencias de la Computación**.

A diferencia del análisis de datos tradicional, la Ciencia de Datos no solo busca describir el pasado, sino utilizar modelos para inferir $P(Y|X)$, la probabilidad de un resultado futuro $Y$ dado un conjunto de variables observadas $X$.

### 5.1 Naturaleza y Flujo de los Datos (DIKW)

Antes de modelar, los datos pasan por una jerarquía de valor:
1.  **Datos:** Símbolos brutos ("38").
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

**¿Qué resuelve?**
Determina si existe evidencia estadística suficiente para rechazar una conjetura sobre una población, distinguiendo efectos reales del azar.

**¿Por qué es importante?**
Es la base del método científico. Sin ella, no podríamos validar si un nuevo medicamento funciona realmente o es coincidencia.

**Definición Técnica:**
Dado un estadístico $T$, calculamos el **Valor P**: $P(T \ge t_{obs} | H_0)$. Si Valor P < $\alpha$, rechazamos $H_0$.

**Definición Simple:**
Eres un juez. $H_0$ es "Inocente". El Valor P es la probabilidad de que las pruebas en su contra sean casualidad. Si es bajísima, dictas "Culpable".

## 7. Aprendizaje Supervisado (Básico)
*Modelo $f(X) \to Y$ entrenado con ejemplos etiquetados.*

### B. Regresión Lineal (Linear Regression)
*   **Conceptos Clave:**
    *   *Residuos:* La diferencia entre el valor real y el predicho ($y - \hat{y}$).
    *   *Mínimos Cuadrados:* Método para minimizar la suma de los errores al cuadrado ($SSE$).

**¿Qué resuelve?**
Predice un valor numérico continuo basándose en variables relacionadas, asumiendo una relación de línea recta.

**¿Por qué es importante?**
Permite cuantificar relaciones y predecir valores numéricos futuros simples.

**Definición Técnica:**
Encuentra $\beta$ que minimiza $J(\beta) = ||Y - X\beta||^2$. Solución: $\hat{\beta} = (X^T X)^{-1} X^T Y$.

**Definición Simple:**
Dibujar una línea recta que pase lo más cerca posible de todos los puntos de una gráfica a la vez.

### C. Regresión Logística (Logistic Regression)
*   **Conceptos Clave:**
    *   *Sigmoide:* Función $1/(1+e^{-z})$ que aplasta cualquier número a un rango entre 0 y 1.
    *   *Probabilidad:* Certeza de que ocurra un evento.

**¿Qué resuelve?**
Clasifica datos en dos opciones (Sí/No) calculando la probabilidad de pertenencia.

**¿Por qué es importante?**
Es el estándar para predicción de riesgo binario en medicina y finanzas.

**Definición Técnica:**
Modela la probabilidad logarítmica (logit) de la clase positiva: $\ln(\frac{P}{1-P}) = \beta^T X$.

**Definición Simple:**
Poner una frontera en una mesa para separar dos grupos de objetos y decir qué tan seguro estás de la clasificación de cada uno.

## 8. Aprendizaje No Supervisado (Básico)
*Buscar patrones en $X$ sin etiquetas $Y$.*

### D. K-Means Clustering
*   **Conceptos Clave:**
    *   *Centroide:* El punto promedio central de un grupo.
    *   *Distancia Euclidiana:* La línea recta entre dos puntos.

**¿Qué resuelve?**
Agrupa datos en $k$ grupos distintos basándose en similitud geométrica (cercanía).

**¿Por qué es importante?**
Descubre segmentos naturales en datos sin etiquetas previas.

**Definición Técnica:**
Itera asignando puntos al centroide más cercano y recalculando centroides para minimizar la varianza intra-cluster.

**Definición Simple:**
Organizar invitados en mesas. Se mueven a la mesa donde la gente se parece más a ellos hasta que todos están cómodos.

---

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

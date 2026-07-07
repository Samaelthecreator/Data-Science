# Perfil Profesional: Especialista en Ciencia de Datos (Data Scientist)

Este documento define el perfil, requerimientos y competencias base esperadas para el rol de Data Scientist, fundamentado no solo en conocimientos técnicos, sino en una sólida capacidad analítica y matemática para abordar los datos.

## 1. Perfil Académico Prerrequisito
El candidato ideal debe poseer una sólida base cuantitativa y analítica, habiendo cursado exitosamente estudios superiores en alguna de las siguientes disciplinas:
*   Ciencias de la Computación
*   Matemáticas
*   Actuaría

Ó carreras afines vinculadas estrechamente a las ciencias exactas o ingeniería.

## 2. Herramientas y Habilidades de Programación
El profesional debe trascender el entorno puramente teórico y ser capaz de llevar las ideas a código productivo. Es necesario contar con:
*   **Dominio de lenguajes de programación clave:** Conocimiento profundo de **Python**, **R** y/o **Scala** para el manejo de datos, análisis y despliegue de modelos.
*   **Experiencia Demostrable:** Haber aplicado estos lenguajes y sus ecosistemas (frameworks y librerías especializadas) a proyectos y problemas reales.

## 3. Portafolio y Experiencia Práctica
Se requiere evidencia tangible del trabajo del candidato:
*   **Repositorio Público (GitHub):** El candidato debe contar con un repositorio en GitHub (o plataformas similares como GitLab/Bitbucket) activo, que documente proyectos reales vinculados a la Ciencia de Datos. El repositorio debe evidenciar buenas prácticas de programación, claridad en la documentación (`README`) y la aplicación metódica de los modelos de aprendizaje.

---

## 4. Conocimientos Técnicos Mínimos (Base del Perfil)

Tomando como base los requerimientos teóricos fundamentales y especializados, el Científico de Datos debe demostrar dominio teórico y práctico en las siguientes áreas de conocimiento:

### A. Fundamentos Matemáticos y Estadísticos
*   **Probabilidad e Inferencia:** Dominio del Teorema de Bayes, cálculo de probabilidades condicionales, Pruebas de Hipótesis empíricas (con entendimiento profundo de p-valores e hipótesis nulas) y generación de Intervalos de Confianza.
*   **Matemáticas Aplicadas:** Sólidas bases en **Álgebra Lineal** (manejo de matrices, tensores y transformaciones ortogonales) y **Cálculo Multivariable** (esencial para comprender el Gradiente Descendente y optimización de funciones de costo).
*   **Estadística Descriptiva:** Medidas de dispersión, tendencia central y distribuciones probabilísticas comunes.

### B. Análisis, Estructuración y Tratamiento de Datos
*   **Comprensión de la Jerarquía DIKW:** Capacidad de transmutar Datos crudos en Información, Conocimiento y finalmente, Sabiduría (para toma de decisiones pragmáticas y éticas).
*   **Ingeniería de Características (Feature Engineering):** 
    *   Técnicas de codificación como *One-Hot Encoding*.
    *   Estrategias sólidas de imputación de datos nulos o faltantes (MICE, K-NN Imputation).
    *   Transformación de variables mediante *Estandarización (Z-Score)* y conversiones para estabilizar varianzas (como la *Transformación Box-Cox*).
*   **Manipulación de Estructuras:** Destreza tanto con datos estructurados (Álgebra Relacional, bases de datos SQL) como comprensión del preprocesamiento de datos no estructurados (textos, tensores, embeddings).

### C. Modelado Predictivo e Inferencia (Aprendizaje Supervisado)
*   **Modelos Base:** Regresión Lineal Simple/Múltiple y Regresión Logística.
*   **Árboles de Decisión y Ensambles:** Capacidad para implementar métodos robustos en alta dimensión como **Random Forest (Bagging)** y algoritmos de **Boosting (XGBoost, AdaBoost)**.
*   **Modelado Avanzado y Regularización:** Comprensión y uso indispensable de técnicas de penalización para entornos de $p > n$ o alta multicolinealidad: **Regresión Ridge (L2)**, **Lasso (L1)** y **Elastic Net**. 
*   **Inferencia en Alta Dimensión:** Conocimiento de los principios de **Inferencia Post-Lasso** para controlar sesgos de selección.
*   **Límites de Decisión Complejos:** Aplicación e intuición detrás de las **Máquinas de Soporte Vectorial (SVM)** y el "Kernel Trick".
*   **Deep Learning (Introducción):** Arquitecturas bases de Redes Neuronales como el Perceptrón Multicapa (MLP) y el mecanismo de Backpropagation.

### D. Descubrimiento de Patrones (Aprendizaje No Supervisado)
*   **Agrupamiento (Clustering):** Algoritmos participativos como **K-Means**, acompañados de estrategias de **Clustering Jerárquico** (aglomerativo y divisivo).
*   **Reducción de Dimensionalidad:** Implementación e interpretación del **Análisis de Componentes Principales (PCA)**.
*   **Modelos Probabilísticos y de Tópicos:** Agrupamientos "suaves" a través de **GMM (Gaussian Mixture Models)** y el algoritmo EM. Descubrimiento de tópicos abstractos en texto puro mediante **LDA (Asignación Latente de Dirichlet)**.

### E. Validación Rigurosa y Métricas de Selección
El profesional no solo construye modelos, sino que valida asertivamente su robustez y previene el sobreajuste (overfitting):
*   **Predicción:** Selección de métricas correspondientes (MSE, RMSE, R² para regresión; F-Score, Precision, Recall y matriz de confusión para clasificación; pruebas ANOVA).
*   **Clustering:** Evaluación de cohesión sin etiquetas (Coeficiente de Silhouette, Estadístico GAP, Índice de Rand Ajustado).
*   **Criterios Comparativos:** Uso de penalizaciones logarítmicas por complejidad mediante los criterios **AIC (Akaike)** y **BIC (Bayesiano)**.

### F. Sistemas Estocásticos y Complejos (Deseable)
Capacidad de abstraer y modelar problemas dinámicos empleando:
*   **Teoría de Grafos y Redes:** Análisis de adyacencia, clustering espectral en nodos y embeddings relacionales.
*   **Procesos sin Memoria:** Matrices de transición en **Cadenas de Markov** para modelado de cambios de estado aleatorios sobre el tiempo.

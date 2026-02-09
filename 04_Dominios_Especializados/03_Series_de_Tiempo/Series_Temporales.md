# Análisis de Series Temporales

El análisis de series temporales es una disciplina fundamental en la Ciencia de Datos que se centra en estudiar datos ordenados cronológicamente. A diferencia de otros problemas de machine learning donde las observaciones se asumen independientes, en una serie temporal la dependencia temporal es la característica clave.

## 1. Conceptos Fundamentales

### ¿Qué es un Proceso Estocástico?
Es un modelo matemático que representa una colección de variables aleatorias ordenadas en el tiempo. Formalmente, es una sucesión de variables aleatorias $\{X_n, n \in N\}$, donde el índice $n$ representa el tiempo.

### Clasificación por Tiempo
- **Tiempo Discreto:** Las observaciones se toman en intervalos específicos (ej. cierre diario de bolsa, ventas mensuales).
  - Ejemplos: Cadenas de Markov, Martingalas.
- **Tiempo Continuo:** La variable se registra en cualquier instante de tiempo.
  - Ejemplos: Procesos de Poisson, Movimiento Browniano.

## 2. Componentes de una Serie Temporal

Una serie temporal suele descomponerse en cuatro componentes principales:

1.  **Tendencia ($T_t$):** La dirección general de los datos a largo plazo (creciente, decreciente o estable).
2.  **Ciclo ($C_t$):** Fluctuaciones de largo plazo (más de un año) alrededor de la tendencia, a menudo asociadas a ciclos económicos.
3.  **Estacionalidad ($S_t$):** Patrones repetitivos y predecibles en periodos cortos y fijos (ej. ventas navideñas, turismo en verano).
4.  **Componente Irregular / Ruido ($I_t$ o $\epsilon_t$):** Fluctuaciones aleatorias e impredecibles.

### Modelos de Descomposición
- **Aditivo:** $Y_t = T_t + C_t + S_t + \epsilon_t$ (Útil cuando la magnitud de las fluctuaciones es constante).
- **Multiplicativo:** $Y_t = T_t \times C_t \times S_t \times \epsilon_t$ (Útil cuando las fluctuaciones crecen proporcionalmente a la tendencia).

## 3. Estacionariedad y Transformaciones

Una serie es **Estacionaria** cuando sus propiedades estadísticas (media, varianza, covarianza) son constantes en el tiempo. La mayoría de los modelos predictivos asumen estacionariedad.

- **Ruido Blanco:** Serie con media 0, varianza constante y sin autocorrelación.
- **Caminata Aleatoria (Random Walk):** La serie evoluciona sin un patrón determinista predecible.

### Técnicas de Estabilización
Si una serie no es estacionaria, debemos transformarla:
1.  **Diferenciación:** Calcular la diferencia entre observaciones consecutivas ($Y_t - Y_{t-1}$) para eliminar tendencias.
2.  **Logaritmos:** Aplicar $log(Y_t)$ para estabilizar la varianza (heterocedasticidad).
3.  **Suavizado Exponencial:**
    - *Simple:* Para series sin tendencia ni estacionalidad.
    - *Doble (Holt):* Para series con tendencia.
    - *Triple (Holt-Winters):* Para series con tendencia y estacionalidad.

## 4. Métodos de Pronóstico (Forecasting)

### Modelos Univariados
Se basan únicamente en el pasado de la propia variable.

- **ARIMA (AutoRegressive Integrated Moving Average):**
    - **AR ($p$):** Autoregresivo. Depende de sus valores pasados.
    - **I ($d$):** Integrado. Número de diferenciaciones para hacerla estacionaria.
    - **MA ($q$):** Media Móvil. Depende de los errores pasados.
    - *Nota:* Se seleccionan $p$ y $q$ analizando correlogramas (ACF y PACF).

- **SARIMA:** Extensión de ARIMA para manejar estacionalidad explícita.

### Modelos Multivariados
Analizan la relación entre múltiples series temporales simultáneamente.

- **VAR (Vectores Autoregresivos):** Modela la interdependencia lineal entre múltiples series temporales. Cada variable es una función lineal de sus valores pasados y los de las otras variables.
- **VEC (Vector de Corrección de Errores):** Para series cointegradas (que comparten una tendencia de largo plazo).

### Modelos de Volatilidad
- **GARCH:** Modela la varianza condicional. Crucial en finanzas donde la volatilidad no es constante (se agrupa en clusters).

## 5. Validación y Métricas

Para evaluar un modelo, dividimos la serie en entrenamiento y prueba (respetando el orden temporal).

- **MAE (Error Absoluto Medio):** Promedio de los errores absolutos. Fácil de interpretar.
- **MSE (Error Cuadrático Medio):** Penaliza más los errores grandes.
- **RMSE (Raíz del Error Cuadrático Medio):** En las mismas unidades que la variable original.
- **MAPE (Error Porcentual Absoluto Medio):** Error en porcentaje. Útil para comparar series de diferentes escalas.

---
*Este documento sintetiza los conceptos clave para el análisis y modelado de series temporales.*

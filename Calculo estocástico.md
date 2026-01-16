# Fundamentos de Cálculo Estocástico y Series Temporales

> **Nota del Revisor (Albert):** Este documento ha sido reestructurado para cumplir con estándares de rigor académico. Se asume familiaridad con Teoría de la Medida y Análisis Real.

## 1. Definición Axiomática de Procesos Estocásticos

Un **proceso estocástico** no es simplemente una "colección de variables". Es un objeto matemático definido sobre un espacio de probabilidad.

### 1.1 Espacio de Probabilidad Filtrado
Sea $(\Omega, \mathcal{F}, \mathbb{P})$ un espacio de probabilidad, donde:
*   $\Omega$: Espacio muestral (conjunto de todos los posibles resultados).
*   $\mathcal{F}$: Una $\sigma$-álgebra sobre $\Omega$ (conjunto de eventos medibles).
*   $\mathbb{P}$: Una medida de probabilidad $\mathbb{P}: \mathcal{F} \to [0, 1]$.

Un proceso estocástico $X = \{X_t : t \in T\}$ es una colección de variables aleatorias definidas en $\Omega$ con valores en un espacio de estados $S$ (usualmente $\mathbb{R}^d$).

### 1.2 Filtración y Flujo de Información
Para modelar la "información disponible hasta el tiempo $t$", introducimos el concepto de **filtración** $\{\mathcal{F}_t\}_{t \in T}$.
*   Es una familia creciente de sub-$\sigma$-álgebras: $\mathcal{F}_s \subseteq \mathcal{F}_t \subseteq \mathcal{F}$ para todo $s \le t$.
*   Decimos que el proceso $X$ es **adaptado** a la filtración si $X_t$ es $\mathcal{F}_t$-medible para todo $t$.
*   Interpretación: En el tiempo $t$, conocemos el valor de $X_t$, pero el futuro $X_{t+h}$ es incierto (una variable aleatoria no constante respecto a $\mathcal{F}_t$).

---

## 2. Clasificación Temporal

### 2.1 Series de Tiempo (Tiempo Discreto)
Aquí $T = \mathbb{Z}$ o $T = \mathbb{N}$.
Una serie de tiempo se denota como $\{X_t\}_{t \in \mathbb{Z}}$.
*   **Ejemplos:** Cadenas de Markov en tiempo discreto, procesos ARMA, GARCH.
*   **Operador de Retardo (Lag Operator):** $L X_t = X_{t-1}$. Fundamental para representar ecuaciones en diferencias estocásticas:
    $$A(L)X_t = B(L)\varepsilon_t$$

### 2.2 Procesos en Tiempo Continuo
Aquí $T = [0, \infty)$ o $T = \mathbb{R}$.
*   **Ejemplos:** Movimiento Browniano (Proceso de Wiener), Procesos de Poisson, Difusiones de Itô.
*   **Regularidad de Trayectorias:** Conceptos como continuidad, diferenciabilidad y variación acotada son críticos.
    *   *Nota:* Las trayectorias del Movimiento Browniano son continuas en casi todas partes, pero no diferenciables en ninguna parte.

---

## 3. Estacionariedad y Dependencia

La noción intuitiva de "estabilidad" se formaliza mediante dos conceptos distintos.

### 3.1 Estacionariedad Fuerte (Strict-Sense Stationarity)
El proceso $\{X_t\}$ es estrictamente estacionario si la distribución conjunta de $(X_{t_1}, \dots, X_{t_k})$ es idéntica a la de $(X_{t_1+h}, \dots, X_{t_k+h})$ para cualquier $h$ y cualquier conjunto finito de índices.
*   Impacto: Toda la estructura probabilística es invariante ante traslaciones temporales.

### 3.2 Estacionariedad Débil (Covariance Stationarity)
Es la condición estándar en análisis de series temporales (e.g., Box-Jenkins). Requiere:
1.  Existencia de momentos de segundo orden: $\mathbb{E}[X_t^2] < \infty$.
2.  Media constante: $\mathbb{E}[X_t] = \mu$ para todo $t$.
3.  Autocovarianza dependiente solo del rezago (lag):
    $$Cov(X_t, X_{t+h}) = \gamma(h)$$

**Función de Autocorrelación (ACF):**
$$\rho(h) = \frac{\gamma(h)}{\gamma(0)}$$

> **¡Atención!** Un proceso puede ser débilmente estacionario pero no estrictamente estacionario (ej. procesos con momentos superiores cambiantes). Inversamente, un proceso estrictamente estacionario sin segundo momento finito (ej. distribución de Cauchy) no es débilmente estacionario.

---

## 4. Ruido Blanco y Martingalas

Es crucial distinguir entre tipos de independencia y "falta de memoria".

### 4.1 Ruido Blanco (White Noise)
Un proceso $\{\varepsilon_t\}$ es Ruido Blanco (WN) si:
1.  $\mathbb{E}[\varepsilon_t] = 0$.
2.  $Var(\varepsilon_t) = \sigma^2 < \infty$.
3.  $\gamma(h) = 0$ para todo $h \neq 0$ (incorrelación).

*   **Ruido Blanco Gaussiano:** Si además $\varepsilon_t \sim \mathcal{N}(0, \sigma^2)$.
*   **Ruido Blanco IID:** Si las variables son independientes e idénticamente distribuidas. (Condición más fuerte que la incorrelación).

### 4.2 Martingalas y Diferencias de Martingala
Una martingala es un proceso $\{M_t\}$ adaptado tal que $\mathbb{E}[|M_t|] < \infty$ y:
$$\mathbb{E}[M_{t+1} | \mathcal{F}_t] = M_t$$
Es el modelo matemático de un "juego justo". El mejor pronóstico de mañana es el valor de hoy.

Una **Diferencia de Martingala (MDS)** es un proceso $\{X_t\}$ tal que $\mathbb{E}[X_t | \mathcal{F}_{t-1}] = 0$.
*   Todo MDS no correlacionada es Ruido Blanco, pero esto permite heterocedasticidad condicional (volatilidad cambiante), base de los modelos **ARCH/GARCH**.

---

## 5. Transformaciones y Operadores

### 5.1 Diferenciación ($\Delta$)
Usada para liminar tendencias estocásticas (raíces unitarias).
$$\Delta X_t = (1-L)X_t = X_t - X_{t-1}$$
Si un proceso requiere $d$ diferenciaciones para volverse estacionario, decimos que es Integrado de orden $d$, denotado $I(d)$.

### 5.2 Suavizado Exponencial (Enfoque Espacio-Estado)
Más allá de fórmulas heurísticas, el suavizado exponencial simple corresponde a un modelo ARIMA(0,1,1) o a un modelo de Espacio de Estados de "Innovaciones Múltiples" con componentes no observables (Nivel local).

---

## 6. Modelos Lineales Clásicos (Enfoque Wold)

El **Teorema de Descomposición de Wold** establece que todo proceso estacionario de covarianza puramente no determinista puede escribirse como una suma infinita de ruidos blancos pasados:
$$X_t = \sum_{j=0}^{\infty} \psi_j \varepsilon_{t-j}$$
donde $\sum \psi_j^2 < \infty$.

### Modelos ARMA(p, q)
Aproximaciones racionales de parsimonia finita para la descomposición de Wold.
$$ \phi(L) X_t = \theta(L) \varepsilon_t $$
*   **Estacionariedad:** Requiere que las raíces del polinomio autorregresivo $\phi(z) = 0$ yazcan fuera del círculo unitario.
*   **Invertibilidad:** Requiere que las raíces de $\theta(z) = 0$ yazcan fuera del círculo unitario (permite expresar el ruido como función del pasado observado).

---

## 7. Métricas de Validación (Critique)

Evitar el uso ciego de métricas. Seleccionar según la función de pérdida del problema.

*   **MSE (Mean Squared Error):** Minimizado por la esperanza condicional $\mathbb{E}[X_{t+h}|\mathcal{F}_t]$. Penaliza fuertemente grandes errores.
*   **MAE (Mean Absolute Error):** Minimizado por la mediana condicional. Robustez ante outliers.
*   **Criterios de Información (AIC, BIC):**
    $$AIC = -2 \ln(\mathcal{L}) + 2k$$
    No son pruebas de hipótesis. Estiman la Divergencia de Kullback-Leibler entre el modelo y la verdad generadora de datos. El BIC es consistente (encuentra el modelo verdadero si $n \to \infty$), el AIC es eficiente (minimiza el error de predicción).

---

## Bibliografía Recomendada
1.  **Hamilton, J. D.** (1994). *Time Series Analysis*. Princeton University Press. (La referencia canónica).
2.  **Brockwell, P. J., & Davis, R. A.** (1991). *Time Series: Theory and Methods*. Springer. (Rigor matemático alto).
3.  **Øksendal, B.** (2003). *Stochastic Differential Equations*. Springer. (Introducción estándar a procesos continuos).

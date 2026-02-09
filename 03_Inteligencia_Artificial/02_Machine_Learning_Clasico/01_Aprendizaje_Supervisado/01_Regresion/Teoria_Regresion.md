# Algoritmos de Regresión

La regresión es una técnica de aprendizaje supervisado utilizada para predecir **valores continuos** (ej. precio de una casa, temperatura, ventas).

## 1. Regresión Lineal Simple
Modela la relación entre una variable independiente $X$ y una dependiente $Y$ mediante una línea recta:
$$Y = \beta_0 + \beta_1 X + \epsilon$$
Donde $\beta_0$ es la intersección, $\beta_1$ es la pendiente (cuánto cambia Y por unidad de X) y $\epsilon$ es el error irreducible.
El objetivo es encontrar la línea que minimice la suma de los errores cuadrados (RSS).

## 2. Regresión Logística
**¡Ojo!** A pesar de su nombre, se usa para **CLASIFICACIÓN**.
Estima la probabilidad de que una instancia pertenezca a una clase (ej. Sí/No, 0/1) usando la función sigmoide:
$$P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X)}}$$
La salida es un valor entre 0 y 1. Si es > 0.5, se clasifica como clase 1.

## 3. Modelos No Lineales
Cuando la relación no es una línea recta.
- **Regresión Polinomial:** Añade potencias de la variable original ($X^2, X^3$) para ajustar curvas.
- **Splines:** Ajusta polinomios suaves por tramos.
- **Funciones Escalonadas:** Divide el rango de X en intervalos y asigna una constante a cada uno.

## 4. Métricas de Evaluación
- **MSE (Mean Squared Error):** Promedio de los errores al cuadrado. Penaliza grandes fallos.
- **RMSE:** Raíz del MSE. Interpretable en las mismas unidades que Y.
- **$R^2$ (Coeficiente de Determinación):** Proporción de la varianza de Y explicada por el modelo (0 a 1). Cuanto más cerca de 1, mejor ajuste.

# Métodos de Ensamble (Ensemble Learning)

"La unión hace la fuerza". Los métodos de ensamble combinan múltiples modelos "débiles" para crear un modelo "fuerte" y robusto.

## 1. Bagging (Bootstrap Aggregating)
Reduce la varianza y evita el sobreajuste.
- **Funcionamiento:**
    1.  Crea múltiples subconjuntos de datos aleatorios con reemplazo (muestras Bootstrap).
    2.  Entrena un modelo independiente en cada muestra (generalmente árboles de decisión profundos).
    3.  Combina las predicciones (promedio para regresión, votación para clasificación).
- **Ejemplo Estrella:** **Random Forest**.
    - Es un Bagging de árboles, pero además, en cada división del árbol, selecciona un subconjunto aleatorio de características. Esto descorrelaciona los árboles y mejora el rendimiento.

## 2. Boosting
Reduce el sesgo y la varianza. Convierte aprendices débiles en fuertes secuencialmente.
- **Funcionamiento:**
    1.  Entrena un modelo simple.
    2.  Identifica los errores que cometió.
    3.  Entrena un segundo modelo enfocado en corregir esos errores (dando más peso a los datos mal clasificados).
    4.  Repite y suma los modelos ponderadamente.
- **Algoritmos Estelares:**
    - **AdaBoost:** El original. Ajusta pesos de las instancias.
    - **Gradient Boosting (GBM):** Optimiza una función de pérdida (loss function) usando descenso de gradiente.
    - **XGBoost / LightGBM:** Implementaciones optimizadas y ultra rápidas de Gradient Boosting. Estándar en competiciones de Kaggle.

## Resumen: Bagging vs Boosting
- **Bagging (Random Forest):** Modelos paralelos independientes. Reduce Varianza. Bueno para modelos que sobreajustan.
- **Boosting (XGBoost):** Modelos secuenciales dependientes. Reduce Sesgo y Varianza. Bueno para modelos muy simples.

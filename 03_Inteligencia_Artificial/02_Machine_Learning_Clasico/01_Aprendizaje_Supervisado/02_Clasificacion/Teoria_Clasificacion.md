# Algoritmos de Clasificación

La clasificación busca asignar una etiqueta o categoría discreta a una nueva observación basándose en datos pasados.

## 1. Árboles de Decisión
Modelos jerárquicos que toman decisiones mediante reglas "si-entonces".
- **Estructura:**
    - *Raíz:* El punto de partida.
    - *Nodos:* Puntos de decisión basados en atributos (ej. "¿Es mayor de edad?").
    - *Hojas:* La predicción final (clase).
- **Algoritmos populares:** ID3 (usa Entropía), C4.5 (mejora ID3), CART (usa Gini).
- **Ventaja:** Muy interpretables.
- **Desventaja:** Propensos al sobreajuste (overfitting).

## 2. Clasificación por Reglas
Similar a los árboles, pero genera un conjunto de reglas independientes (ej. "Si X, entonces Y").
- Algoritmos: CN2, FOIL, RIPPER.

## 3. K-Vecinos Más Cercanos (KNN)
Clasificador "perezoso" (no entrena un modelo, memoriza los datos).
Para clasificar un punto nuevo:
1.  Busca los **K** puntos más cercanos en el espacio de datos.
2.  Asigna la clase más común entre esos vecinos (voto mayoritario).
*Nota:* Sensible a la escala de los datos (requiere normalización).

## 4. Máquinas de Vectores de Soporte (SVM)
Busca el hiperplano óptimo que separa las clases con el mayor margen posible.
- Funciona bien en espacios de alta dimensión.
- Usa **Kernels** para transformar datos no lineales a espacios lineales.

## 5. Métricas de Evaluación
- **Precisión (Precision):** De los que el modelo dijo que eran positivos, ¿cuántos lo eran realmente?
- **Exhaustividad (Recall):** De todos los positivos reales, ¿cuántos encontró el modelo?
- **F1-Score:** Media armónica entre Precisión y Recall. Ideal cuando las clases están desbalanceadas.

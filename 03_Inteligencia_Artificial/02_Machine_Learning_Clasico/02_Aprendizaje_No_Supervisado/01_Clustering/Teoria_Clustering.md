# Algoritmos de Agrupamiento (Clustering)

El clustering es el aprendizaje no supervisado por excelencia. Su objetivo es encontrar estructuras ocultas en datos no etiquetados, agrupando elementos similares entre sí y separando los diferentes.

## 1. Tipos de Clustering
- **Exclusivo (Hard):** Cada dato pertenece a un único grupo.
- **Difuso (Soft):** Cada dato tiene un grado de pertenencia a varios grupos (ej. Fuzzy C-Means).
- **Jerárquico vs. Particional:** Estructura de árbol o división plana.

## 2. Clustering Jerárquico
Construye una jerarquía de clusters anidados (dendrograma).
- **Aglomerativo (Bottom-Up):** Empieza con cada punto como un cluster y los va fusionando.
    - *Enlace Simple (Single Linkage):* Distancia mínima entre puntos de clusters.
    - *Enlace Completo (Complete Linkage):* Distancia máxima.
    - *Promedio:* Distancia media.
- **Divisivo (Top-Down):** Empieza con un solo cluster gigante y lo va dividiendo.

## 3. K-Means (Particional)
El algoritmo más popular por su simplicidad.
1.  Elige $K$ centroides iniciales al azar.
2.  Asigna cada punto al centroide más cercano.
3.  Recalcula los centroides como el promedio de los puntos asignados.
4.  Repite hasta que los centroides no cambien.
*Desventaja:* Debes especificar $K$ de antemano y es sensible a outliers.

## 4. DBSCAN (Basado en Densidad)
Agrupa puntos que están muy juntos (alta densidad) y marca como ruido los que están en zonas de baja densidad.
- **Conceptos:**
    - *Epsilon ($\epsilon$):* Radio de vecindad.
    - *MinPts:* Número mínimo de puntos para considerar una zona "densa".
- **Ventaja:** No necesitas especificar el número de clusters y encuentra formas arbitrarias (no solo esferas como K-Means).

## 5. Validación
- **Coeficiente de Silueta (Silhouette):** Mide qué tan parecido es un objeto a su propio cluster (cohesión) comparado con otros clusters (separación).
    - Valor cercano a +1: Bien agrupado.
    - Valor cercano a -1: Mal agrupado.

# Transformación de Datos e Ingeniería de Características

Una vez limpios, los datos rara vez están listos para un modelo de Machine Learning. La fase de transformación busca representarlos de la forma más útil posible.

## 1. Reducción de Datos
En entornos de Big Data, reducir la dimensionalidad o el volumen sin perder información crítica es vital.

- **Selección de Características (Feature Selection):** Eliminar variables irrelevantes o redundantes (altamente correlacionadas). Reduce el sobreajuste y acelera el entrenamiento.
- **Selección de Instancias:** Usar técnicas de muestreo para reducir el número de filas.

## 2. Discretización y Binning
Convertir variables numéricas continuas en categóricas (intervalos).
- *Ejemplo:* Convertir "Edad" (18, 19, ..., 90) en "Grupos de Edad" (Joven, Adulto, Mayor).
- Ayuda a manejar relaciones no lineales y reduce el ruido.

## 3. Normalización y Escalado
Muchos algoritmos (como KNN, K-Means, Redes Neuronales) son sensibles a la escala de los datos. Si una variable varía entre 0-1 y otra entre 0-1000, la segunda dominará el cálculo de distancias.

### Métodos Comunes
- **Min-Max Scaling:** Transforma los datos a un rango [0, 1].
  $$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$
- **Z-Score (Estandarización):** Centra los datos en 0 con desviación estándar 1. Ideal si la distribución es Gaussiana (Normal).
  $$Z = \frac{X - \mu}{\sigma}$$
- **Escala Decimal:** Mueve el punto decimal según el valor absoluto máximo.

## 4. Ingeniería de Características (Feature Engineering)
Es el arte de crear nuevas variables a partir de las existentes para mejorar el rendimiento del modelo.
- *Ejemplo:* De una fecha "2023-12-25", extraer "Es_Navidad" (Binario) o "Dia_Semana".
- *Codificación (Encoding):* Transformar variables categóricas a numéricas.
    - **One-Hot Encoding:** Crea una columna binaria por categoría.
    - **Label Encoding:** Asigna un número entero a cada categoría.

---
*Una buena transformación de datos suele tener más impacto en el resultado final que la elección del algoritmo.*

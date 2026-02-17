# Redes Neuronales Convolucionales (CNN)

Las CNN son redes especializadas en procesar datos con una estructura de rejilla (como imágenes). Han revolucionado la Visión por Computadora.

## 1. Concepto Clave: Convolución
En lugar de conectar cada píxel a cada neurona (lo que sería computacionalmente imposible), las CNN usan **Filtros (Kernels)** pequeños que se deslizan sobre la imagen.
- Detectan patrones locales como bordes, texturas o formas.
- **Invarianza:** Pueden reconocer un objeto sin importar en qué parte de la imagen esté.

## 2. Arquitectura Típica

1.  **Capa Convolucional:** Aplica los filtros para crear "Mapas de Características".
2.  **Función de Activación (ReLU):** Introduce no linealidad.
3.  **Pooling (Submuestreo):** Reduce el tamaño espacial de la imagen para reducir parámetros y evitar sobreajuste.
    - *Max Pooling:* Toma el valor máximo de una ventana (ej. 2x2).
    - *Average Pooling:* Toma el promedio.
4.  **Capa Flatten:** "Aplana" los mapas 2D a un vector 1D.
5.  **Capa Densa (Fully Connected):** Una red neuronal clásica que clasifica el vector de características extraído.

## 3. Ventajas
- **Extracción Automática de Características:** A diferencia del ML clásico donde un humano diseñaba los filtros, la CNN *aprende* los filtros óptimos durante el entrenamiento.
- **Jerarquía:** Las primeras capas aprenden bordes simples; las intermedias, formas; y las últimas, objetos complejos (caras, coches).

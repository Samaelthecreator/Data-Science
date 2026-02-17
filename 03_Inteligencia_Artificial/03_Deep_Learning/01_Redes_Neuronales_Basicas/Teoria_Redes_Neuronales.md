# Redes Neuronales Artificiales

Las redes neuronales son modelos inspirados en el cerebro humano, diseñados para aprender límites de decisión complejos y no lineales. Son la base del Deep Learning.

## 1. El Perceptrón y el MLP

### Perceptrón Simple
La unidad más básica. Calcula una suma ponderada de las entradas, añade un sesgo (bias) y aplica una función de paso.
$$Salida = f(\sum (w_i \cdot x_i) + b)$$
*Limitación:* Solo puede resolver problemas **linealmente separables** (no puede resolver XOR).

### Perceptrón Multicapa (MLP)
Conecta múltiples perceptrones en capas.
- **Capa de Entrada:** Recibe los datos.
- **Capas Ocultas:** Procesan características intermedias. Gracias a ellas, la red puede aprender funciones **no lineales** complejas.
- **Capa de Salida:** Entrega la predicción final.

## 2. Entrenamiento: Backpropagation

¿Cómo aprende la red? Ajustando los pesos ($w$) para minimizar el error.
1.  **Feedforward:** Los datos pasan de la entrada a la salida.
2.  **Cálculo del Error:** Se compara la predicción con el valor real (Loss Function).
3.  **Backpropagation (Retropropagación):** El error se propaga hacia atrás desde la salida hasta la entrada. Usando la **Regla de la Cadena**, se calcula cuánto contribuyó cada peso al error (gradiente).
4.  **Descenso del Gradiente:** Se actualizan los pesos en dirección opuesta al gradiente para reducir el error.

## 3. Funciones de Activación
Introducen la NO linealidad en la red (sin ellas, una red profunda sería igual a una regresión lineal gigante).

- **Sigmoide:** $\frac{1}{1+e^{-x}}$. Salida (0, 1). Útil para probabilidad, pero sufre de "desvanecimiento del gradiente".
- **Tanh (Tangente Hiperbólica):** Salida (-1, 1). Centrada en cero, mejor que la sigmoide.
- **ReLU (Rectified Linear Unit):** $max(0, x)$. La más usada en capas ocultas. Eficiente y evita el desvanecimiento del gradiente.
- **Softmax:** Usada en la capa de salida para clasificación multiclase (convierte salidas en probabilidades que suman 1).

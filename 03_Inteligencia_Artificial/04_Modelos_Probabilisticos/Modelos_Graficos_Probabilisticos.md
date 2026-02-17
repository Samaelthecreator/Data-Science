# Modelos de Grafos Probabilísticos

Estos modelos combinan la **Teoria de Grafos** con la **Probabilidad** para representar sistemas complejos con incertidumbre. Son la base del razonamiento moderno en IA antes del auge del Deep Learning masivo para datos no estructurados.

## 1. Redes Bayesianas
Son grafos acíclicos dirigidos (DAGs) donde:
- **Nodos:** Representan variables aleatorias.
- **Aristas (Flechas):** Representan dependencias probabilísticas condicionales ($A \rightarrow B$ significa que B depende de A).

### Características
- Permiten razonar sobre causalidad y diagnóstico (ej. Síntoma $\rightarrow$ Enfermedad).
- Manejan datos faltantes marginalizando variables.
- **Inferencia:** Calcular la probabilidad de una variable no observada dada la evidencia ($P(Enfermedad | Fiebre = Alta)$).
    - *Exacta:* Costosa computacionalmente.
    - *Aproximada:* Métodos como **MCMC (Markov Chain Monte Carlo)**.

## 2. Modelos Ocultos de Markov (HMM)
Especializados en datos secuenciales (tiempo o texto) donde el estado verdadero del sistema es "oculto" y solo vemos observaciones ruidosas.
- *Ejemplo:* Reconocimiento de voz (el sonido es la observación, la palabra es el estado oculto).
- **Componentes:**
    - Estados ocultos ($S$).
    - Observaciones ($O$).
    - Probabilidades de Transición ($A_{ij}$): Probabilidad de pasar del estado $i$ al $j$.
    - Probabilidades de Emisión ($B_j(k)$): Probabilidad de generar la observación $k$ desde el estado $j$.

## Diferencia Clave
- Las Redes Bayesianas son generativas y pueden tener estructuras complejas.
- Los HMM son un caso específico de Red Bayesiana dinámica para secuencias lineales.

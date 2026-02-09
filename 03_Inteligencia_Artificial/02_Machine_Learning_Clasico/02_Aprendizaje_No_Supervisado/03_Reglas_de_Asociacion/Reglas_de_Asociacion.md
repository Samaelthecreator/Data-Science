# Reglas de Asociación

Técnica de aprendizaje no supervisado para descubrir relaciones ocultas entre variables en grandes bases de datos.
*Ejemplo clásico:* Análisis de la cesta de la compra ("Si compra pañales, probablemente compre cerveza").

## Conceptos Básicos
Una regla se define como $X \rightarrow Y$ (Si X, entonces Y).
- **Ítem:** Un elemento (ej. leche).
- **Transacción:** Un conjunto de ítems comprados juntos.
- **Itemset:** Un conjunto de uno o más ítems.

## Métricas de Interés
¿Cómo sabemos si una regla es buena?

1.  **Soporte (Support):** ¿Qué tan frecuente es el conjunto {X, Y} en toda la base de datos?
    $$Soporte(X \rightarrow Y) = \frac{\text{Transacciones con } X \cup Y}{\text{Total Transacciones}}$$
2.  **Confianza (Confidence):** Si alguien compró X, ¿qué tan probable es que compre Y?
    $$Confianza(X \rightarrow Y) = \frac{\text{Soporte}(X \cup Y)}{\text{Soporte}(X)}$$
3.  **Lift (Elevación):** ¿Cuánto más probable es Y dado X, comparado con si fueran independientes?
    - $Lift > 1$: Asociación positiva (se atraen).
    - $Lift = 1$: Independencia.
    - $Lift < 1$: Asociación negativa (se repelen).

## Algoritmos
1.  **Apriori:**
    - Usa un enfoque iterativo "nivel a nivel".
    - Principio Apriori: "Si un itemset es frecuente, todos sus subconjuntos también lo son".
    - *Desventaja:* Puede ser lento porque escanea la base de datos múltiples veces.
2.  **FP-Growth (Frequent Pattern Growth):**
    - Más eficiente. Construye una estructura de árbol (FP-Tree) comprimida.
    - Solo escanea la base de datos dos veces.

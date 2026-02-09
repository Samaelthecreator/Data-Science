# Aprendizaje por Refuerzo (Reinforcement Learning)

En el RL, un **agente** aprende a tomar decisiones interactuando con un **entorno** mediante un proceso de prueba y error.

## Conceptos Clave
1.  **Agente:** La entidad que toma decisiones (ej. un robot, un programa de ajedrez).
2.  **Entorno:** El mundo con el que interactúa.
3.  **Estado ($S$):** Situación actual del agente.
4.  **Acción ($A$):** Lo que el agente hace.
5.  **Recompensa ($R$):** Feedback inmediato del entorno (positivo o negativo) tras una acción.
6.  **Política ($\pi$):** La estrategia del agente (mapa de Estados -> Acciones).

## Dilema Exploración vs. Explotación
- **Exploración:** Probar acciones nuevas para descubrir mejores recompensas (riesgo de fallar).
- **Explotación:** Usar lo que ya se sabe que funciona para maximizar la recompensa inmediata.
*El agente debe equilibrar ambas.*

## Algoritmos Comunes
- **Q-Learning:** Aprende una función de valor (Q-Table) que estima la calidad de una acción en un estado.
- **Monte Carlo:** Aprende de episodios completos (juegos terminados).
- **SARSA:** Similar a Q-Learning pero "on-policy" (aprende de la política que está siguiendo).

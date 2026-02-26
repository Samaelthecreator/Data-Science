# Transacciones Distribuidas y Aislamiento

Una transacción es una agrupación lógica de lecturas y escrituras que deben triunfar o fallar juntas (Atomicidad: **Commit** o **Rollback**). En sistemas de un solo nodo, esto es trivial gracias al Write-Ahead Log. En un clúster de múltiples máquinas, el proceso es sumamente complejo por el problema del consenso.

## 1. El Problema del Consenso Atómico
Si una transacción afecta los datos del Nodo A y el Nodo B, ¿cómo nos aseguramos de que ambos hagan commit al mismo tiempo? ¿Qué pasa si el Nodo A hace commit pero el Nodo B falla a mitad del proceso? Para evitar inconsistencias se requieren protocolos de coordinación.

### A. Commit de Dos Fases (2 Phase Commit - 2PC)
El algoritmo estándar utilizado en la mayoría de bases de datos relacionales distribuidas. Requiere un nodo especial: el **Coordinador**.
1.  **Fase de Preparación (Prepare):** El Coordinador pregunta a todos los participantes si están listos para hacer commit de la transacción (bloqueando temporalmente esos recursos).
2.  **Fase de Consolidación (Commit/Abort):**
    - Si *TODOS* dicen que SÍ $\rightarrow$ El Coordinador envía una orden de **Commit** a todos.
    - Si *UNO SOLO* dice que NO, o se desconecta (timeout) $\rightarrow$ El Coordinador envía una orden de **Abort (Rollback)** a todos.

*El peligro de 2PC (Punto Único de Fallo):* Es un protocolo bloqueante. Si el Coordinador se cae *después* de que un participante respondió "SÍ" pero *antes* de que reciba el "Commit", el participante queda bloqueado (una "transacción en duda") hasta que el coordinador resucite consultando su log.

### B. Commit de Tres Fases (3PC)
Añade una fase de "Preparación para el Commit" y reglas de timeout más estrictas tanto para los nodos como para el coordinador. Es no-bloqueante ante los fallos del coordinador, PERO sufre de una sobrecarga enorme de mensajes (latencia) y es vulnerable a la inconsistencia "cerebro dividido" (split-brain) durante particiones de red. En la práctica real, casi no se usa a favor del 2PC.

## 2. Enfoques Modernos Deterministas
Para evitar el alto costo de coordinación de 2PC, algunas arquitecturas adoptan un **ordenamiento secuencial determinista** global:
- **Arquitectura Calvin:** Utiliza un "Secuenciador" que agrupa transacciones en milisegundos y define un orden de ejecución inmutable para todo el clúster. Si todos los nodos ejecutan la misma secuencia matemática al mismo tiempo partiendo del mismo estado inicial, tendrán el mismo final sin tener que coordinarse entre ellos (se elimina el 2PC).
- **El Enfoque Spanner (Google):** Usa *TrueTime*, un reloj distribuido hiperpreciso (mantenido con relojes atómicos y GPS) que asigna un "timestamp" riguroso a cada transacción. Permite lecturas distribuidas rapidísimas de snapshots pasados sin necesidad de utilizar bloqueos (bloqueo mutuo).

## 3. Aislamiento y Concurrencia (Bloqueo de 2 Fases)

Cuando dos transacciones interactúan concurrentemente, necesitamos aislarlas (la "I" en ACID).
- **Serializabilidad:** Es el nivel máximo de aislamiento. Garantiza que el resultado final de ejecutar transacciones al mismo tiempo sea idéntico a ejecutarlas una tras otra (en serie).
- **Bloqueo de Dos Fases (2PL):** Una de las técnicas clásicas para lograr serializabilidad en bases de datos. 
  - Fase 1: Se adquieren *Cerrojos* (Locks).
    - *Cerrojo Compartido (Shared Lock):* Para lectura. Varias transacciones pueden leer a la vez.
    - *Cerrojo Exclusivo (Exclusive Lock):* Para escritura. Bloquea todo, impidiendo lecturas y escrituras de otros.
  - Fase 2: Al terminar toda la transacción, se liberan TODOS los cerrojos simultáneamente.

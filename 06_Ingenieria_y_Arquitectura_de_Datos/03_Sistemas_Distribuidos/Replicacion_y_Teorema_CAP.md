# Replicación y Modelos de Consistencia

La replicación consiste en mantener una copia (réplica) de los mismos datos en múltiples nodos (servidores) distribuidos geográficamente. Esto reduce la latencia acercando los datos al usuario y añade tolerancia a fallos.

## 1. El Teorema CAP (Conjetura de Brewer)

En sistemas distribuidos, es imposible garantizar tres propiedades simultáneamente cuando hay un fallo en la red:
- **C**onsistencia (Consistency): Todos los nodos ven la misma información al mismo tiempo.
- **A**lta Disponibilidad (Availability): Cada petición recibe una respuesta de éxito o fallo (el sistema no se cuelga).
- Tolerancia a **P**articiones (Partition Tolerance): El sistema sigue operando incluso si algunos nodos pierden comunicación entre sí.

Dado que las particiones de red (P) son inevitables (cables se rompen, switches fallan), en la práctica un sistema distribuido debe elegir entre:
- **Sistemas CP:** Priorizan la Consistencia. Si un nodo no puede comunicarse con el resto, se bloqueará o dará un error antes que devolver un dato obsoleto (Ej: MongoDB, HBase).
- **Sistemas AP:** Priorizan la Disponibilidad. Si un nodo queda aislado, seguirá respondiendo consultas con los datos que tenga, aunque estén obsoletos (Ej: Cassandra, DynamoDB).

### El Teorema PACELC (Extensión)
CAP solo aplica durante una partición. PACELC añade: "Else (E), cuando el sistema funciona normalmente, debes elegir entre Latency (L) o Consistency (C)".
- **Harvest y Yield:** Métricas para la degradación elegante. 
  - *Yield:* Porcentaje de peticiones respondidas con éxito (clásicos "nueves" de disponibilidad, ej. 99.99%).
  - *Harvest:* Qué tan completa es la respuesta. Es mejor devolver 99 de 100 resultados rápido (baja Harvest, alto Yield) que fallar la consulta completa.

## 2. Modelos de Consistencia

- **Consistencia Estricta (Linealizabilidad / Atomicidad):** El más exigente. Cada operación de escritura parece ocurrir instantáneamente, y cualquier lectura posterior a ese punto temporal (Punto de Linealización) verá ese dato. Es determinista.
- **Consistencia Secuencial:** Mantiene el orden de las operaciones para un mismo cliente/proceso (como si se ejecutaran en serie), pero no garantiza el orden global en tiempo real respecto a otros clientes.
- **Consistencia Eventual:** (Típico en sistemas AP). Si no hay nuevas escrituras, eventualmente todos los nodos sincronizarán y tendrán los mismos datos, pero mientras tanto, clientes distintos pueden ver valores temporales distintos.

## 3. Modelos de Replicación (Líder / Seguidor)

### Replicación Líder (Maestro-Esclavo)
1.  Un nodo es el **Líder**. Todas las escrituras DEBEN ir a él.
2.  El Líder anota el cambio en su disco y lo despacha a los **Seguidores** mediante un log de replicación.
3.  Las lecturas pueden hacerse desde el Líder o cualquier Seguidor.
- **Problema:** Si el Líder se cae, nadie puede escribir hasta que uno de los Seguidores sea promovido a nuevo Líder. (Cuello de botella).

### Multilíder (Maestro-Maestro)
Permite que varios nodos compartan la carga de escrituras.
- Cada Líder procesa escrituras locales y las reenvía asíncronamente a los demás.
- **Ventaja:** Mitiga la dependencia de un solo nodo central (ideal para sistemas con múltiples datacenters globales).

# Procesamiento de Datos en Tiempo Real (Streaming)

A diferencia del procesamiento Batch (donde los datos son estáticos y finitos), en el **Stream Processing** los datos no tienen fin ("Unbounded data"); llegan continuamente, como clics en una web, logs de sensores o transacciones financieras. El objetivo es reaccionar al evento tan pronto como ocurre (baja latencia).

## 1. Patrón Productor / Consumidor Asíncrono
Para evitar que un sistema se colapse si entran más datos de los que puede procesar, no se conectan directamente. En su lugar, se usa un **intermediario (Message Broker)** que actúa como un búfer o amortiguador.
- **Productor (Publisher):** Dispara un evento y se olvida. No espera confirmación del destino. Funciona en modo "Fire-and-forget".
- **Consumidor (Subscriber):** Lee los mensajes del intermediario a su propio ritmo. Si el consumidor cae y revive, retoma desde donde se quedó.

## 2. Brokers basados en Logs (El Estilo Kafka)

Existen colas de mensajes clásicas (AMQP como RabbitMQ) que borran el mensaje de la memoria inmediatamente después de que el consumidor avisa que lo leyó. Esto es riesgoso si el consumidor guarda mal el dato (no hay forma de recuperarlo).

Los **Logs de Mensajería Distribuida (Apache Kafka)** adoptaron la filosofía de las bases de datos:
1.  **Append-only Log:** El intermediario guarda los mensajes en disco anexándolos al final de un archivo inmutable dividido en servidores y en **Tópicos**.
2.  **Persistencia y Repetición:** El mensaje *NO se borra* tras ser leído. Diferentes consumidores pueden leer el mismo mensaje a velocidades distintas usando un **Offset Mínimo** (el índice por donde van). Si descubres un bug en tu algoritmo de hoy, solucionas el bug, rebobinas el offset a ayer, y reprocesas exitosamente toda la historia.

## 3. Sincronización de Sistemas y CDC

Un problema enorme en arquitecturas modernas es la **Escritura Dual (Dual Write) / Condición de Carrera**. 
- *Ejemplo:* Una empresa quiere guardar el nuevo usuario en MySQL y a la vez indexarlo en un motor de búsqueda (Elasticsearch) y limpiar cache en (Redis). Si escribe en los 3 desde el código, MySQL puede guardar rápido, pero si Redis y Elastic escriben en un orden invertido o uno se cae en medio segundo, los tres sistemas dicen tener datos distintos (Inconsistencia silenciosa).

### Change Data Capture (CDC)
Es la solución elegante. En lugar de forzar a la aplicación a sincronizar 3 sistemas, la app SOLO escribe en la **Base de Datos Líder (MySQL)**.
- Un conector especializado (Ej. **Debezium**, Kafka Connect) *lee el archivo WAL (log secreto)* de MySQL en tiempo real, extrae cualquier fila que cambió, y emite ese cambio como un "Evento" hacia Kafka.
- Los sistemas derivados (Seguidores: Redis, Elasticsearch) escuchan ese evento desde Kafka de forma asíncrona y aplican el cambio *exactamente en el mismo orden de ejecución total* logrando una perfecta consistencia eventual descentralizada.

## 4. Complex Event Processing (CEP)
Sistemas especializados (como Flink o Kafka Streams) en analizar patrones dentro del flujo en movimiento, en vez de almacenar datos para consultarlos. 
- La Base de Datos guarda DATA y tú metes QUERYS para preguntar.
- El CEP guarda tu QUERY permanentemente, y le echas el río de DATA sin parar. Cuando un patrón coincide en vivo (Ej. "Si recibe 3 tarjetas rechazadas de IPs rusas en menos de 5 segundos con el mismo nombre"), el CEP emite un "Alerta Compleja de Fraude" en microsegundos.

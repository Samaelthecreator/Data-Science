# Formatos de Codificación y Flujos de Datos

Cuando un programa tiene datos en memoria (objetos, listas, árboles), ese formato está optimizado para la CPU local. Sin embargo, para enviar esos datos por la red a otro servidor o guardarlos en una base de datos, deben transformarse a una secuencia de bytes universal. Este proceso se llama **Codificación** (Encoding, Serialización o Marshaling).

El diseño del esquema de codificación dicta cuán mantenible y evolucionable será el sistema. Deben mantener:
- **Compatibilidad hacia atrás:** Código nuevo puede leer datos escritos por código antiguo.
- **Compatibilidad hacia adelante:** Código antiguo puede leer datos escritos por código nuevo.

---

## 1. Formatos de Codificación

### A. Específicos del Lenguaje (Mala Práctica)
Lenguajes de programación traen serializadores nativos (ej. `pickle` en Python, `Serializable` en Java).
- **Problemas:** Son ineficientes, carecen de versionamiento por lo que rompen la compatibilidad y, críticamente, **presentan agujeros de seguridad severos** (pueden inyectar código malicioso en la deserialización).

### B. Formatos Estandarizados (Legibles)
- **JSON / XML:** Son ubicuos, pero tienen problemas de tipado (ej. XML no distingue un número de un string; JSON no distingue un `int` de un `float`). Carecen de soporte para matrices de bytes binarios directas.
- **BSON (Binary JSON):** Resuelve limitaciones de JSON añadiendo tipos binarios. Nativo de MongoDB.

### C. Formatos Binarios basados en Esquemas
Altamente eficientes, ocupan menos red y disco porque no repiten el nombre de los campos continuamente. Usan "IDs de campos".
- **Protocol Buffers (Protobuf - Google):** Excelente rendimiento. Usa un archivo de definición (esquema) estricto.
- **Thrift (Facebook):** Similar a Protobuf, soporta varios protocolos en capas.
- **Apache Avro:** Diferente a Protobuf/Thrift porque el esquema va embebido con los datos o se negocia en tiempo de escritura/lectura. Es excelente para Big Data distribuido (Hadoop, Kafka) porque soporta la **resolución de esquemas** (el escritor puede tener una versión del esquema y el lector tener otra, y Avro los mapea dinámicamente).

---

## 2. Flujo de Datos (Cómo viaja la información)

¿Cómo interactúan procesos distintos en un sistema?

### A. Bases de Datos
Un proceso escribe en la base de datos (codifica) y otro proceso, o el mismo en el futuro, lee de ella (descodifica). El almacenamiento debe soportar compatibilidad entre el viejo estado guardado y el nuevo código intentando leerlo.

### B. Llamadas Cliente-Servidor (APIs)
La comunicación directa (Síncrona) sobre red.
- **Servicios Web (REST):** Basados en los verbos HTTP (`GET`, `POST`, `PUT`, `DELETE`). Tratan a las entidades como recursos identificables por URIs. Muy estándar en la red externa.
- **RPC (Remote Procedure Call):** Intenta hacer que llamar a una función en un servidor remoto parezca una llamada a una función local. Evolucionó desde sistemas viejos (CORBA, RMI) a sistemas binarios de alto rendimiento (ej. **gRPC** sobre Protobuf). Se usa principalmente para comunicación *interna* entre **Microservicios**.

### C. Flujo de Mensajes Asíncronos (Brokers)
El "Productor" envía mensajes pero NO espera respuesta ("dispara y olvida") y el "Consumidor" los lee.
- **Ventajas:**
    - El Productor no se bloquea esperando a que el Consumidor termine de procesar.
    - El Broker actúa como una memoria intermedia (**Queue/Buffer**). Si el sistema receptor cae, los mensajes no se pierden, el Broker los retiene y aplica *Backpressure* o memoria en disco.
- **Tópicos y Suscripción (Pub/Sub):** Los mensajes relacionados se agrupan en **Tópicos** (Topics), permitiendo que un evento dispare múltiples procesos a la vez.
- **Logs vs. Colas clásicas:** 
    - Las colas clásicas (ej. RabbitMQ) destruyen el mensaje en cuanto el consumidor confirma que lo procesó.
    - Los **Brokers basados en Logs** (ej. **Apache Kafka**) actúan casi como bases de datos. Anexan los mensajes al final de un log persistente con un índice (offset). Muchos consumidores pueden leer el mismo flujo a diferentes velocidades o reprocesar datos del pasado sin borrarlos.

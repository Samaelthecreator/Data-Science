# Casos de Estudio en Empresas Tecnológicas

La teoría de los sistemas distribuidos y el procesamiento masivo de datos se desarrolló para resolver problemas reales en empresas que crecían a un ritmo sin precedentes. A continuación, se analiza cómo tres gigantes resolvieron sus retos de arquitectura de datos.

## 1. Twitter: Caché y Predictibilidad (Twemcache)
Twitter es un sistema de *microblogging* donde el desafío principal no son las escrituras (tweets), sino la inmensa cantidad de *lecturas* (mostrar el *timeline* a millones de usuarios).

- **El Reto:** El cuello de botella era acceder a la base de datos principal constantemente para leer.
- **La Solución:** Una capa gigantesca de caché basada en **Redis** y **Memcached**. La caché en Twitter está diseñada para servir más de 120 GB de datos por segundo.
- **Twemproxy y Twemcache:** Para escalar la caché horizontalmente sin saturar de conexiones la red, crearon un proxy ligero (*Twemproxy*). Además, desarrollaron su propio *fork* de Memcached, llamado **Twemcache**, optimizado específicamente para las necesidades de adaptabilidad, alta disponibilidad y **predictibilidad** (tiempos de respuesta consistentes sin picos de latencia).
- **Arquitectura Híbrida:** Usan *Scalding* para el procesamiento por lotes (batch) y *Heron* para el procesamiento en tiempo real (streaming), formando una Arquitectura Lambda.

## 2. Uber: Visión Holística del Ecosistema Kafka
El sistema de Uber debe unir el mundo físico con el digital en tiempo real: desde la geolocalización de un conductor hasta el procesamiento del pago y la asignación dinámica de precios (surge pricing).

- **El Reto:** Miles de microservicios generando eventos desconectados que necesitan ser cruzados al instante (ej. unir clics en la app con viajes completados con valoraciones de choferes para calcular la ganancia).
- **La Solución Estructural:** Uber tiene una de las implementaciones más grandes del mundo de **Apache Kafka**, utilizándolo como la "columna vertebral" central o bus de eventos de toda la empresa. Todas las aplicaciones escriben allí.
- **El Ecosistema (Stack):**
    - **Kafka:** Actúa como el bróker central inmutable.
    - **Apache Flink:** Realiza el procesamiento en stream (tiempo real), consumiendo de Kafka y generando alertas inmediatas.
    - **Apache Hive:** Para almacenamiento histórico pesado y analítica por lotes (Data Lake).
    - **Apache Pinot:** Data store tipo OLAP distribuido. Se conecta a Kafka para ingerir datos y permitir consultas analíticas *ad-hoc* con latencia sub-milisegundo, usadas para los dashboards internos operativos.

## 3. Facebook: De Bases Relacionales a Grafos (TAO)
En los inicios de Facebook, la red social intentó escalar utilizando las herramientas abiertas más comunes del momento: MySQL (Base de datos relacional) y Memcached.

- **El Reto Inicial:** Construyeron los perfiles como grafos lógicos (usuarios, relaciones de amistad, "me gusta", grupos) pero los guardaron en MySQL.
- **Sharding Relacional (El Parche):** Cuando MySQL no dio abasto, hicieron particionado (*sharding*) manual, guardando un índice de en qué servidor vivía cada usuario. El problema fue que perdieron el poder del SQL: no podían hacer un `JOIN` para unir amigos si vivían en servidores diferentes.
- **El Problema de Caché:** Tenían bases esclavo geográficamente distribuidas y cachés. La replicación asíncrona provocaba inconsistencias: un usuario subía una foto, la página recargaba leyendo de la caché vieja, y la foto "desaparecía" temporalmente.
- **La Solución: TAO:** En 2009 construyeron **TAO** (The Associations and Objects). TAO no es una base de datos nueva desde cero, sino una *API de Grafos NoSQL increíblemente inteligente construida por encima de MySQL*. 
    - Desde la perspectiva del desarrollador, ya no interactuaban con SQL ni se preocupaban de invalidar la caché. Solo leían "Nodos" y "Arcos" (Edges).
    - TAO se encargaba de interceptar las peticiones, gestionar el ruteo a Memcached o bajar hasta el MySQL correcto resolviendo la consistencia y la replicación por debajo de forma transparente.

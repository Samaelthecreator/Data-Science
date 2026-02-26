# Procesamiento de Datos por Lotes (Batch Processing)

El procesamiento por lotes (offline) toma un gran conjunto de datos estáticos (del pasado), ejecuta un trabajo pesado (que puede tardar minutos, horas o días) y produce un nuevo conjunto de datos de salida sin afectar el rendimiento de los sistemas online orientados al usuario final.

## 1. La Filosofía UNIX: La Base del Batch
UNIX estableció principios de diseño fundamentales que inspiraron sistemas modernos como Hadoop:
1.  **Hacer una cosa y hacerla bien:** Herramientas pequeñas como `awk`, `grep`, `sort`, unidas para tareas complejas.
2.  **Inmutabilidad:** Los programas leen un archivo y arrojan resultados en un archivo nuevo o en pantalla, *nunca* modifican el archivo original de entrada.
3.  **Encadenamiento (Pipes):** La salida de un programa es directamente la entrada de otro (`|`). Esto permite componer transformaciones sin necesidad de almacenar el estado intermedio en el disco duro constantemente.

## 2. MapReduce y HDFS (El salto a lo Distribuido)
MapReduce (popularizado por Google y llevado al open source por Hadoop) es como "UNIX distribuido en miles de máquinas".
No usa una supercomputadora, sino miles de discos duros de computadoras normales ("Commodity Hardware") conectados en red creando un único Sistema de Ficheros Distribuido (Google File System o **HDFS**).

### El Flujo MapReduce
1.  **Leer y Dividir:** Se lee el archivo grande de HDFS y se divide en bloques pequeños.
2.  **Mapeo (Map):** Hadoop busca en qué máquina física está guardado cada bloque y envía el *código de la función Map* a esa máquina (es más barato mover código que mover Terabytes de datos). El "Mapper" extrae pares `Clave-Valor`.
3.  **Shuffle y Sort:** Es el corazón del algoritmo. La red agrupa todos los pares con la misma clave (ej. todas las compras del usuario "Juan") y las ordena. Los resultados intermedios se envían a los nodos "Reducers" basándose en el hash de la clave.
4.  **Reducción (Reduce):** El "Reducer" recibe la lista de valores para una clave y los procesa (ej. sumando el total de compras de "Juan") para guardar el archivo final en HDFS.

## 3. Motores de Flujos de Datos (Dataflow)
*Ej: Apache Spark, Tez, Flink (en modo batch)*

MapReduce es robusto pero tiene un gran problema de lentitud: la **Materialización**. Exige guardar el resultado de cada pequeño paso intermedio en los discos duros replicados de HDFS antes de continuar con el siguiente trabajo MapReduce.
- **La Solución Dataflow:** Trata todo el flujo de trabajo como un grafo (ej. Hive o Pig). En lugar de parar y guardar a disco, mantiene los datos intermediarios en la memoria RAM y los pasa directamente al siguiente operador.
- **Tolerancia a fallos iterativa:** Si un nodo falla, Spark prefiere *recalcular* ese pedazo perdido usando la pista de linaje (las transformaciones previas) en vez de haber respaldado todo en disco como hace MapReduce, siendo exponencialmente más rápido.

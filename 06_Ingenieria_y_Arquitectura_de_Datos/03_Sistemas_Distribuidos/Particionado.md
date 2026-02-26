# Particionado de Datos (Sharding)

A medida que el volumen de datos o el tráfico supera la capacidad de escritura de un solo nodo potente (escalado vertical "Scale Up" topado), la única solución es el **Particionado** (escalado horizontal "Scale Out"): romper los datos en subconjuntos y repartirlos entre múltiples servidores. (Ej. vNodes en Cassandra o Shards en MongoDB).

El santo grial del particionado es lograr que si tenemos P particiones/nodos, podamos procesar P veces más carga. Pero rara vez la distribución es perfecta.

## 1. Problemas de la Distribución
Si un volumen se particiona mal, tendremos:
- **Particiones Sesgadas (Data Skew):** Algunos nodos asumen casi toda la carga y almacenamiento.
- **Hot Spots:** El caso extremo donde el %99 del tráfico se dirige a un solo nodo porque todos están buscando/escribiendo la misma clave (ej. si partimos por fecha y hoy todo el mundo escribe el evento "Navidad", solo un nodo recibe la carga y colapsará).

## 2. Estrategias de Asignación (Routing)

### A. Asignación Aleatoria Simple
- **Pros:** Distribución estadísticamente perfecta. No hay *Hot Spots*.
- **Contras:** A la hora de las lecturas es terrible. Como no sabemos dónde quedó el dato (clave), debemos enviar la consulta SQL a todas las máquinas (*Scatter-Gather*) y esperar que alguna responda.

### B. Particionado por Rango (Range Partitioning)
Si un diccionario A-Z se parte, Nodo 1 maneja A-H, Nodo 2 I-Q, etc.
- **Pros:** Búsquedas por rango son tremendamente rápidas si los datos están ordenados (ej. "nombres de A a C" ocurre en una sola máquina y los datos están juntos). Ideal si definimos bien los rangos lógicos (ej. en HBase).
- **Contras:** Susceptible a Hot Spots si las claves incrementan secuencialmente (como marcas de tiempo - timestamps).
- *Solución:* Usar prefijos diferenciadores combinados con el timestamp.

### C. Particionado por Hash Complejo
En lugar de mirar el valor crudo, se le aplica una función Matemática (Hash MD5 o MurmurHash). Los valores cambian drásticamente borrando el sesgo, entonces la clave que daba *Hash X* va al Nodo 1.
- **Pros:** Garantiza una distribución increíblemente uniforme mitigando el Data Skew y los Hot Spots vinculados a rangos secuenciales.
- **Contras:** Adiós a la lectura óptima por rango (*Sweep range scans*), ya que los hashes correspondientes a claves en secuencia acabarán desperdigados en nodos diferentes aleatoriamente. (Cassandra usa este enfoque principalmente).

## 3. Índices Secundarios en Nodos Particionados

Si además de la "llave" particionadora quieres buscar por un campo extra (Búsqueda textual como Elasticsearch), ¿dónde guardas ese índice?
1. **Índice Local (Document Partitioning):** Cada nodo mantiene un índice independiente *solo para su pedazo* de base de datos.
    - *Ventaja:* Escritura en O(1), no hay dependencias.
    - *Desventaja:* Lentitud en la lectura por dispersión (famoso **Scatter-Gather** + Latencia de Cola). Todos deben buscar en sus índices y devolver la data antes de que el Master decida el resultado final.
2. **Índice Global (Term Partitioning):** Se construye un super-índice de toda la base de datos, y ESTE índice también se particiona y distribuye. Las rutas a cualquier documento apuntan a su Clave general.
    - *Ventaja:* Lectura súper veloz (no scatter).
    - *Desventaja:* Actualizar un documento requiere doble penalización de red: escribir el dato en el Servidor A y cruzar red para actualizar el Índice Global que vive alojado en el Servidor B. Puede romper fácilmente el balance.

## 4. Rebalanceo

Cuando añades un servidor nuevo o se quema uno, los nodos deben "Rebalancearse" para compartir su carga con el "chico nuevo" sin tumbar al servicio.

- La mala idea: **Hash Módulo N:** (N = nº de nodos). Si $13 \% 4$ = Nodo 1, pero metes un nodo nuevo (N=5), la función cambia de comportamiento radical, $13 \% 5$ = Nodo 3. Esto causa un movimiento sísmico gigante donde el %99 de las keys deben migrar a nuevos vecinos consumiendo TODO tu canal de red (Saturación).
- La buena idea: **Pre-splitting & Hashing Consistente:** En lugar de tener $N=4$ Nodos con 4 particiones, se crean $N=4$ Nodos albergando 1024 *Microparticiones Virtuales*. Cuando un nuevo Nodo X es agregado, simplemente "secuestra" unas pocas sub-particiones directamente de cada vecino preexistente. Así la mudanza de gigabytes transcurre rápida y granularmente sin matar tu ancho de banda general.

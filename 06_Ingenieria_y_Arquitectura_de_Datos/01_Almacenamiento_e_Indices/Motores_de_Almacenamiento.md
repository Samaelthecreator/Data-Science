# Motores de Almacenamiento e Índices

Las bases de datos utilizan diferentes estructuras subyacentes para organizar, guardar y recuperar la información del disco duro. Elegir el motor de almacenamiento correcto es crítico para el rendimiento (lectura vs escritura).

## 1. Almacenamiento en LOG (Append-Only)
La forma más sencilla de almacenar datos es un archivo tipo "Log" (bitácora).
- **Funcionamiento:** Cada nueva escritura simplemente se concatena (append) al final del archivo en formato "clave-valor". Nunca se sobrescribe.
- **Ventaja (Escritura):** Rendimiento altísimo porque añadir al final de un archivo secuencial es la operación más rápida en un disco.
- **Desventaja (Lectura):** Pésimo rendimiento. Para encontrar un valor, hay que leer todo el archivo de principio a fin ($O(N)$). 

### Solución: Índices Hash
Para evitar leer todo el archivo, se guarda en memoria RAM un **Índice Hash** (un diccionario de metadatos) que mapea cada "clave" a la "dirección en bytes" dentro del disco donde está esa clave.
- **Riesgo:** El índice **DEBE** caber completo en la memoria RAM. Si hay muchas claves distintas, el sistema colapsará.
- **Compactación y Segmentación:** Como el log crece infinitamente (incluso si actualizamos el valor de una clave, se crea una nueva entrada al final), los sistemas modernos dividen el log en "segmentos". Periódicamente realizan **Compactación** en segundo plano: combinan segmentos viejos, se quedan solo con la clave más reciente y borran las obsoletas, liberando espacio.

## 2. SSTables y Árboles LSM
(Sorted String Tables / Log-Structured Merge-Tree)

Las **SSTables** son una mejora directa al almacenamiento en log. 
- **La gran diferencia:** Los pares de clave-valor dentro del segmento están **ordenados por la clave**.
- **Beneficios:**
    - Al fusionar (compactar) segmentos, el proceso es rapidísimo (como el algoritmo Merge Sort).
    - No es necesario tener TODAS las claves en memoria RAM. Solo necesitas tener un índice parcial (disperso) porque, como los datos están ordenados, puedes buscar el rango entre dos claves conocidas y saltar al disco.
    - Soporta búsqueda eficiente por rangos (ej. "dame las claves entre 'a' y 'c'").

### Árbol LSM (Log-Structured Merge-Tree)
Es el motor que usa SSTables (usado en Cassandra, RocksDB, LevelDB).
1. Cuando llega una escritura, se añade primero a un pequeño árbol en memoria (**Memtable**, usualmente un Árbol AVL o Rojo-Negro).
2. Cuando la Memtable se llena, se escribe al disco como un nuevo segmento SSTable ordenado.
3. **Punto fuerte:** Tienen una "amplificación de escritura" baja (escriben rápido). Consiguen un alto nivel de compactación (no desperdician espacio).

## 3. Árboles B (B-Trees)
El estándar de facto en casi todas las bases de datos relacionales tradicionales (MySQL, PostgreSQL).

- **Estructura conceptual:** A diferencia de los logs que añaden datos al final, los Árboles B dividen el disco en bloques o **Páginas** de tamaño fijo (ej. 4KB o 8KB).
- **Sobrescritura:** Este motor **SÍ** sobrescribe las páginas directamente en el disco duro.
- **Estructura del Árbol:** Una página "padre" contiene rangos de claves y referencias (punteros) a páginas "hijas". Navigas desde la raíz bajando por el árbol hasta llegar a la página "hoja" que tiene tu dato.

### Resiliencia ante fallos: WAL
¿Qué pasa si al sobrescribir una página se va la luz (falla la base de datos) y la página queda corrupta ("huérfana")?
Para prevenir esto, los B-Trees utilizan un **Write-Ahead Log (WAL)**. Es un archivo log donde se anota cada modificación *antes* de aplicarla al propio árbol. En caso de fallo, la base de datos usa el WAL para reconstruir la estructura al reiniciarse.

### B-Trees vs LSM-Trees
- **LSM-Trees:** Son más rápidos para **escribir** datos masivos (escriben secuencialmente, baja amplificación de escritura).
- **B-Trees:** Son más rápidos para **leer** (especialmente valores individuales) e ideales para cargas transaccionales porque estructuran bien los datos, aunque dejan "fragmentación" (espacio libre sin usar dentro de las páginas).

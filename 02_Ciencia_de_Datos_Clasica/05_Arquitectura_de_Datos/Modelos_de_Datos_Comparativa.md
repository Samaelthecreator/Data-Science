# Modelos de Datos: Comparativa y Guía de Uso

Este documento analiza los principales paradigmas de modelado de datos, desde los históricos hasta los modernos NoSQL, con un enfoque práctico para la toma de decisiones arquitectónicas.

---

## 1. Modelo Jerárquico (Hierarchical Model)
Histórico (ej. IBM IMS).

- **Base Teórica:** Estructura de **Árbol**. Un nodo padre puede tener múltiples hijos, pero un hijo solo un padre.
- **Condiciones de Uso:** Datos con una estructura estrictamente arbórea y estática (ej. organigrama simple, sistema de archivos).
- **Limitaciones Teóricas:** No puede representar relaciones N a M de forma natural (requiere duplicación de datos). Inflexible ante cambios en la estructura.
- **Limitaciones Computacionales:**
    - *Óptimo:* Lecturas muy rápidas si se conoce la ruta de acceso (jerarquía).
    - *Deficiente:* Alta complejidad para reorganizar el árbol. Navegación obligatoria desde la raíz.
- **Comentarios:** El ancestro de las bases de datos modernas. Su rigidez lo hizo obsoleto para aplicaciones generales, pero el concepto vive en formatos como XML.

---

## 2. Modelo de Red (Network Model / CODASYL)
Evolución del jerárquico.

- **Base Teórica:** Estructura de **Grafo Dirigido** (restringido). Un hijo puede tener múltiples padres. Utiliza punteros físicos.
- **Condiciones de Uso:** Datos altamente interconectados con esquemas fijos y relaciones conocidas de antemano.
- **Limitaciones Teóricas:** Complejidad conceptual muy alta. El programador debe conocer la estructura física de navegación ("navegar por los punteros").
- **Limitaciones Computacionales:**
    - *Óptimo:* Rendimiento extremo en transacciones conocidas.
    - *Deficiente:* Ad-hoc queries (consultas no planificadas) son casi imposibles o muy lentas. Modificar el esquema (Schema Evolution) es traumático.
- **Comentarios:** Intentó resolver la rigidez del árbol, pero creó un "infierno de punteros". Fue desplazado totalmente por el modelo relacional debido a su complejidad.

---

## 3. Modelo Relacional (SQL)
El estándar dominante (Oracle, PostgreSQL, MySQL).

- **Base Teórica:** **Álgebra Relacional** y Teoría de Conjuntos. Los datos se organizan en tuplas (filas) agrupadas en relaciones (tablas).
- **Condiciones de Uso:**
    - Datos estructurados con esquema claro.
    - Relaciones **N a M** y **N a 1** complejas.
    - Necesidad de integridad transaccional fuerte (ACID).
    - Reportes y consultas complejas (JOINs).
- **Limitaciones Teóricas:** Impedancia Objeto-Relacional (diferencia entre cómo programa la aplicación y cómo se guardan los datos). Dificultad para escalar horizontalmente (distribuido).
- **Limitaciones Computacionales:**
    - *Óptimo:* Consultas complejas, agregaciones, consistencia de datos.
    - *Deficiente:* Transacciones masivas concurrentes (bloqueos). Esquema rígido (Schema-on-Write) que requiere migraciones para cambios ("Alter Table"). JOINs costosos en grandes volúmenes.
- **Comentarios:** La opción por defecto segura. "Si no sabes qué usar, usa Relacional". Normalización reduce redundancia pero aumenta complejidad de lectura (Joins).

---

## 4. Modelo Documental (NoSQL - Document Store)
El moderno flexible (MongoDB, Couchbase).

- **Base Teórica:** Estructura de **Árbol/Diccionario** (JSON, BSON). Agregados autocontenidos.
- **Condiciones de Uso:**
    - Relaciones **1 a N** donde los hijos se acceden casi siempre con el padre (ej. Post + Comentarios).
    - Esquemas cambiantes o evolutivos (polimorfismo).
    - Desarrollo ágil (Schema-on-Read).
- **Limitaciones Teóricas:** No soporta JOINs nativos eficientes (se hacen en aplicación). Consistencia eventual en muchos casos (BASE vs ACID).
- **Limitaciones Computacionales:**
    - *Óptimo:* **Localidad Espacial**. Leer un objeto complejo entero es una sola operación de disco (sin Joins). Alta escalabilidad horizontal (Sharding).
    - *Deficiente:* Actualizaciones puntuales dentro de documentos grandes (puede requerir reescribir todo el documento). Consultas que cruzan múltiples colecciones.
- **Comentarios:** Ideal para OLTP web y móvil. "Desnormalizar es la norma": se prefiere redundancia a cambio de velocidad de lectura.

---

## 5. Modelo de Grafos (Graph Database)
El especialista en conexiones (Neo4j, Amazon Neptune).

- **Base Teórica:** **Teoría de Grafos**. Nodos (entidades) y Aristas (relaciones) son ciudadanos de primera clase.
- **Condiciones de Uso:**
    - Relaciones complejas, profundas y transitivas (ej. Redes sociales, detección de fraude, recomendadores, "amigo del amigo del amigo").
    - Relaciones **N a M** densas.
- **Limitaciones Teóricas:** No es ideal para agregaciones masivas o recorridos de tabla completa (ej. "promedio de edad de todos los usuarios").
- **Limitaciones Computacionales:**
    - *Óptimo:* "Index-free adjacency". Navegar de un nodo a sus vecinos es costo constante O(1), no depende del tamaño de la base de datos (a diferencia de los JOINs relacionales que son costosos).
    - *Deficiente:* Sharding (distribuir el grafo en varios servidores) es un problema matemático complejo no resuelto eficientemente (Graph Partitioning).
- **Comentarios:** Usar SOLO si las relaciones son tan importantes como los datos mismos.

---

## Tabla Comparativa de Selección

| Escenario de Datos | Jerárquico | Red | Relacional (SQL) | Documental (NoSQL) | Grafos | Justificación |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Catálogo de Productos E-commerce** | Insuficiente | No Recomendable | Suficiente | **Óptimo** | Insuficiente | Los productos varían en atributos (ropa vs electrónica). El modelo documental permite esquemas flexibles (JSON) por producto. |
| **Sistema Contable / Bancario** | Suficiente | Suficiente | **Óptimo** | Insuficiente | No Recomendable | Requiere ACID estricto, precisión decimal y consistencia absoluta. El relacional es el rey de la integridad. |
| **Red Social (Quién sigue a quién)** | No Recomendable | Suficiente | Suficiente | Insuficiente | **Óptimo** | Las consultas de "amigos de mis amigos" requieren múltiples JOINs en SQL (lento). En grafos es navegación directa y natural. |
| **Blog (Posts y Comentarios)** | No Recomendable | No Recomendable | Suficiente | **Óptimo** | Suficiente | Un post y sus comentarios se leen juntos. Guardarlos en un solo documento JSON aprovecha la localidad espacial. |
| **Análisis de Fraude (Anillos)** | No Recomendable | No Recomendable | Insuficiente | Insuficiente | **Óptimo** | Detectar patrones complejos de relaciones (anillos, conexiones indirectas) es trivial en grafos e imposible en otros. |
| **Reportes BI / Warehousing** | No Recomendable | No Recomendable | **Óptimo** (Columnar) | Suficiente | No Recomendable | SQL estándar es imbatible para agregaciones, sumas, promedios y cruces de grandes volúmenes de datos estructurados. |

**Leyenda:**
- **Óptimo:** La arquitectura nativa favorece este caso de uso.
- **Suficiente:** Se puede hacer, pero requiere esfuerzo extra o no es lo más eficiente.
- **Insuficiente:** Rendimiento pobre o complejidad de desarrollo muy alta.
- **No Recomendable:** Anti-patrón. No usar bajo ninguna circunstancia moderna.

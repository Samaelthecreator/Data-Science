# Clase 2 — Herramientas Analíticas (Pandas Fundamentals)

> **Documento de desarrollo académico.** Redactado desde el rol de un profesional con maestría en cálculo estadístico y estocástico, enfoque en cómputo estadístico. Aquí Pandas **no es el objetivo**: es la implementación computacional de los conceptos estadísticos de la Clase 1. Cada método se justifica por su función estadística, y cada decisión (sobre todo la imputación) se toma a partir de la forma de la distribución.
>
> **Estructura:** (1) Glosario; (2) Desarrollo con casos idóneos y no idóneos; (3) Ejemplos con el mejor y el peor caso.

---

## 1. Glosario de conceptos

| # | Concepto | Definición operativa |
|---|---|---|
| 1 | **`Series`** | Arreglo unidimensional etiquetado (un vector con índice). Es una columna. |
| 2 | **`DataFrame`** | Tabla bidimensional de columnas `Series` que comparten un índice de filas. |
| 3 | **Índice (`Index`)** | Etiquetas de las filas (o columnas). Permite alineación por etiqueta, no por posición. |
| 4 | **`dtype`** | Tipo de dato de una columna (`int64`, `float64`, `object`, `category`, `datetime64`). Determina qué estadística es válida. |
| 5 | **`read_csv`** | Importa datos tabulares desde texto delimitado a un `DataFrame`. |
| 6 | **`pd.DataFrame(...)`** | Construye un `DataFrame` desde diccionarios, listas o arreglos. |
| 7 | **Generación sintética** | Crear datos con `numpy.random` y una **semilla** fija para reproducibilidad. |
| 8 | **Semilla (`seed`)** | Estado inicial del generador pseudoaleatorio; garantiza resultados repetibles. |
| 9 | **`head` / `tail`** | Primeras / últimas filas. Inspección rápida de estructura. |
| 10 | **`shape`** | Tupla `(n_filas, n_columnas)`. Tamaño muestral y dimensionalidad. |
| 11 | **`columns`** | Etiquetas de columnas (las variables del estudio). |
| 12 | **`info`** | Resumen de tipos, no-nulos y memoria. Diagnóstico de calidad. |
| 13 | **`describe`** | Resumen estadístico por columna: `count`, media, `std`, min, cuartiles, max. Es la Clase 1 condensada. |
| 14 | **`loc`** | Selección por **etiqueta** de filas/columnas. |
| 15 | **`iloc`** | Selección por **posición** entera. |
| 16 | **Máscara booleana** | Serie de `True/False` que filtra filas según una condición (submuestreo). |
| 17 | **`isna` / `notna`** | Detección de valores nulos (`NaN`). |
| 18 | **`fillna`** | Imputación: sustituye nulos por un valor (media, mediana, moda, constante). |
| 19 | **`dropna`** | Elimina filas o columnas con nulos. |
| 20 | **Imputación** | Reemplazo de datos faltantes por un valor estimado según el mecanismo de nulidad. |
| 21 | **MCAR / MAR / MNAR** | Mecanismos de nulidad: completamente al azar / al azar condicionado / no al azar. Determinan si imputar sesga. |
| 22 | **`axis`** | Eje de la operación: `axis=0` recorre filas (opera por columna); `axis=1` recorre columnas (opera por fila). |
| 23 | **`inplace`** | Argumento que modifica el objeto en sitio y devuelve `None`. En desuso por sus efectos secundarios. |
| 24 | **`SettingWithCopyWarning`** | Aviso de que se intenta escribir sobre una posible copia (vista ambigua). |
| 25 | **Indexación encadenada** | `df[...][...] = ...`: patrón que dispara el warning anterior y puede no modificar el original. |
| 26 | **Vista vs. copia** | Una vista comparte memoria con el original; una copia no. La ambigüedad es fuente de errores silenciosos. |
| 27 | **`groupby`** | Divide en grupos, aplica una función y combina (split-apply-combine). |
| 28 | **`astype` / coerción de tipos** | Conversión explícita de `dtype`; evita que números lleguen como texto. |

---

## 2. Desarrollo de cada concepto: cuándo es idóneo y cuándo no

### 2.1 `Series` y `DataFrame`: el porqué del índice

Un `DataFrame` **no es una hoja de cálculo**: alinea por etiqueta del índice, no por posición física. Esto evita el error clásico de "sumar dos columnas desalineadas", pero sorprende a quien viene de Excel: si dos `Series` tienen índices distintos, la operación produce `NaN` donde no coinciden.

- *Idóneo cuando:* cada fila es una unidad muestral y cada columna una variable; se necesita alineación segura al combinar tablas.
- *No sirve / cuidado cuando:* el índice tiene duplicados (la alineación se vuelve ambigua y las uniones explotan en producto cartesiano); se depende del orden posicional sin fijar el índice.

### 2.2 `dtype`: el tipo decide la estadística

El `dtype` gobierna qué operación es legítima. Una columna numérica leída como `object` (texto) permite "sumar" por concatenación pero no calcular una media. Una variable categórica codificada como enteros (1, 2, 3 para ciudades) invita a calcular una "media de ciudad" que no tiene sentido.

- *Idóneo:* fijar `category` para nominales (ahorra memoria y previene aritmética inválida); `datetime64` para fechas (habilita remuestreo temporal).
- *No sirve:* tratar códigos categóricos como números; dejar fechas como texto (imposibilita ordenar y agrupar por tiempo).

### 2.3 Creación e importación; datos sintéticos con semilla

Los datos sintéticos son didáctica y metodológicamente valiosos: **conocemos la verdad** (la $\mu$, la $\sigma$, la correlación reales), lo que permite verificar si un método la recupera. La semilla fija convierte "aleatorio" en "reproducible", requisito de cualquier resultado científico.

- *Idóneo:* prototipar y enseñar; construir *tests* de un pipeline con propiedades conocidas; estudiar el comportamiento de un estimador por simulación.
- *No sirve:* como sustituto de datos reales para concluir sobre el mundo (los sintéticos solo contienen la estructura que uno mismo inyectó).

### 2.4 Métodos de exploración; `describe` como diagnóstico

`describe()` condensa la Clase 1. Leerlo bien evita graficar a ciegas: si `mean` ≫ `50%` (mediana), hay asimetría a la derecha **antes** de dibujar nada; si `std` es enorme frente a la media, sospecha atípicos; si `max` está lejísimos del `75%`, hay cola larga.

- *Idóneo:* primer diagnóstico de cualquier dataset numérico.
- *No sirve:* para variables categóricas (usar `value_counts`); `describe` sobre ellas da métricas engañosas o vacías. Tampoco detecta relaciones entre columnas (es univariado).

### 2.5 Selección y filtrado: `loc`, `iloc`, máscaras

Filtrar es **submuestrear**: cambia la población de referencia y puede introducir sesgo de selección. Distinguir `loc` (etiqueta) de `iloc` (posición) es crítico: tras ordenar o filtrar, la posición 0 ya no es la etiqueta 0.

- *Idóneo `loc`:* seleccionar por condición o por nombre de columna (legible y estable).
- *Idóneo `iloc`:* recorrer por posición (primeras $k$ filas) sin importar etiquetas.
- *No sirve:* mezclar ambos mentalmente (fuente de errores off-by-one); filtrar y luego olvidar que el índice tiene huecos.

### 2.6 Valores nulos e imputación (núcleo de la clase)

La decisión de imputación depende de **dos preguntas**: (a) ¿qué forma tiene la distribución? y (b) ¿por qué faltan los datos?

**(a) Forma → estadístico de imputación.**
- Distribución **simétrica** sin atípicos → imputar con la **media** es razonable.
- Distribución **asimétrica** o con atípicos → imputar con la **mediana**: la media arrastra el sesgo de la cola hacia el valor imputado, deformando la distribución y desplazando su centro. La mediana preserva la forma.
- Variable **categórica** → imputar con la **moda** (o una categoría "Desconocido" explícita).

**(b) Mecanismo de nulidad → si imputar es legítimo.**
- **MCAR** (faltan al azar): imputar o `dropna` no sesga; solo se pierde eficiencia.
- **MAR** (faltan según otra variable observada): imputación condicional (por grupo) es válida.
- **MNAR** (faltan según su propio valor, p. ej. los ingresos altos se ocultan): **cualquier** imputación simple sesga; hay que modelar la nulidad o, al menos, documentarla.

- *Idóneo:* imputar cuando la fracción de nulos es baja y el mecanismo es MCAR/MAR; usar mediana en colas pesadas.
- *No sirve:* imputar a ciegas con la media en MNAR (amplifica el sesgo); `dropna` cuando los nulos no son aleatorios (elimina justamente el subgrupo informativo).

### 2.7 `axis` e `inplace`

`axis=0` significa "a lo largo de las filas" → el resultado es **por columna** (`df.mean(axis=0)` da la media de cada columna). Es contraintuitivo y causa la mayoría de los errores de principiante. `inplace=True` está cayendo en desuso: rompe el encadenamiento de métodos, no ahorra memoria de forma garantizada y oscurece si se trabaja sobre una copia.

- *Idóneo:* preferir el estilo funcional `df = df.operacion(...)` (explícito, encadenable, sin ambigüedad de copia).
- *No sirve:* confiar en `inplace` para "ahorrar memoria" (a menudo copia igual); razonar `axis` de memoria en vez de verificar.

### 2.8 Errores más comunes

| Error | Síntoma | Corrección |
|---|---|---|
| Indexación encadenada | `SettingWithCopyWarning`; el cambio no persiste | Usar un solo `.loc[filas, columna] = valor` |
| Confundir `axis` | Se promedia en la dirección equivocada | Recordar: `axis=0` opera por columna |
| Números como texto | `describe` no da estadísticas; sumas concatenan | `pd.to_numeric` / `astype(float)` |
| Índice duplicado | Uniones que multiplican filas | `reset_index` / verificar `index.is_unique` |
| Mutar el original sin querer | Efectos secundarios silenciosos | Trabajar sobre `.copy()` explícita |

---

## 3. Ejemplos: el mejor y el peor caso de uso

### Ejemplo A — Elección del estadístico de imputación

Columna `ingreso_mensual`, asimétrica a la derecha (media 3.443, mediana 2.429), con nulos concentrados en ingresos altos (MNAR).

**✅ Mejor caso.**
```python
col = df["ingreso_mensual"]
# La forma manda: distribución asimétrica -> mediana
df["ingreso_imputado"] = col.fillna(col.median())
```
La mediana no se deja arrastrar por la cola; la distribución imputada conserva su forma y su centro. Además, se documenta que el mecanismo es MNAR, de modo que el lector sabe que la imputación es un mínimo defendible, no una verdad.

**❌ Peor caso.**
```python
df["ingreso_imputado"] = col.fillna(col.mean())   # media en cola pesada + MNAR
```
Doble error: (1) la media ya está inflada por la cola; (2) los nulos correspondían justo a ingresos altos, así que rellenar con un valor demasiado bajo **subestima** sistemáticamente a ese subgrupo. El histograma resultante muestra un pico artificial en la media. La conclusión sobre "ingreso típico" queda sesgada.

### Ejemplo B — `loc` vs. indexación encadenada

**✅ Mejor caso.**
```python
# Un único .loc: inequívoco, modifica el original
df.loc[df["edad"] < 0, "edad"] = np.nan
```

**❌ Peor caso.**
```python
# Encadenado: dispara SettingWithCopyWarning y puede NO modificar df
df[df["edad"] < 0]["edad"] = np.nan
```
El primer `df[...]` puede devolver una copia; la asignación se aplica a esa copia efímera y se descarta. El bug es silencioso: el código "corre" pero los datos no cambian. Es el error más frecuente —y más difícil de detectar— en Pandas.

### Ejemplo C — `dtype` correcto

**✅ Mejor caso.**
```python
df["ciudad"] = df["ciudad"].astype("category")   # nominal
df["fecha"]  = pd.to_datetime(df["fecha"])        # habilita resample/groupby temporal
```
Tipar bien previene aritmética inválida sobre categóricas y habilita el análisis temporal de la Clase 4.

**❌ Peor caso.**
```python
df["ciudad_id"].mean()   # 'ciudad' codificada 1,2,3 -> "media de ciudad" = sin sentido
```
El código devuelve un número (p. ej. 2.4) que parece un resultado, pero no significa nada: promediar etiquetas nominales es un error conceptual que la máquina no detecta.

### Ejemplo D — `describe` como diagnóstico previo

**✅ Mejor caso.** Antes de graficar, se lee `df.describe()` y se observa `mean = 3.443` frente a `50% = 2.429`. Conclusión inmediata y correcta: **asimetría a la derecha**; se planifica usar mediana e histograma con foco en la cola. La estadística guía la visualización, no al revés.

**❌ Peor caso.** Se corre `df.describe()` sobre un `DataFrame` con la columna `codigo_postal` numérica y se reporta su "media" y "std" como si fueran informativas. Un código postal es un identificador nominal; sus estadísticos de posición y dispersión son ruido con apariencia de dato.

### Ejemplo E — `dropna` y el mecanismo de nulidad

**✅ Mejor caso.** En un experimento controlado, unas mediciones se pierden por un corte eléctrico aleatorio (MCAR). `df.dropna()` reduce $n$ pero no sesga: la submuestra sigue siendo representativa.

**❌ Peor caso.** En una encuesta de salud, los pacientes más graves no completan el seguimiento y sus filas quedan con nulos (MNAR). `df.dropna()` elimina justo a los más graves; el análisis resultante subestima la severidad y la mortalidad. Aquí borrar es peor que imputar con cuidado, y ambos requieren declarar el sesgo.

---

## 4. Síntesis de la clase

Pandas es el brazo ejecutor de la Clase 1. La competencia no está en memorizar métodos, sino en que **cada llamada tenga una justificación estadística**: `describe` diagnostica forma; el filtrado redefine la muestra; la imputación elige su estadístico según la asimetría y su legitimidad según el mecanismo de nulidad. Los errores clásicos (indexación encadenada, `axis`, tipos mal asignados, `dropna` en MNAR) no son fallos de sintaxis sino de razonamiento sobre qué representa el dato. Con esta base, la Clase 3 pasa a **ver** —histogramas, cajas y dispersión— lo que aquí se calculó.

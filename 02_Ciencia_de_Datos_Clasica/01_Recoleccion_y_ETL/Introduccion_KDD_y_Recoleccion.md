# Descubrimiento de Conocimiento en Bases de Datos (KDD) y Recolección

El proceso **KDD (Knowledge Discovery in Databases)** es la metodología clásica para extraer conocimiento útil, válido, novedoso y comprensible a partir de grandes volúmenes de datos. Aunque a menudo se usa como sinónimo de "Minería de Datos", el KDD es el proceso completo, donde la minería es solo una fase.

## 1. El Proceso KDD

Este proceso se compone de varias etapas secuenciales e iterativas:
1.  **Selección:** Identificar y extraer los datos relevantes para el análisis.
2.  **Preprocesamiento:** Limpiar los datos (ruido, valores perdidos).
3.  **Transformación:** Adecuar los datos al formato necesario para los algoritmos.
4.  **Minería de Datos (Data Mining):** Aplicar algoritmos inteligentes para encontrar patrones.
5.  **Interpretación/Evaluación:** Analizar los resultados para convertirlos en conocimiento.

*Nota:* Otros marcos de trabajo populares son **CRISP-DM** (Cross Industry Standard Process for Data Mining) y **SEMMA**.

## 2. Selección de Datos

Antes de recolectar, debemos definir el objetivo del negocio.
Preguntas clave:
- ¿Necesitamos todos los datos o una muestra?
- ¿Qué variables (columnas) son relevantes?

### Técnicas de Muestreo (Sampling)
Cuando el volumen de datos es masivo, trabajamos con muestras representativas para reducir costos computacionales.
- **Aleatorio Simple:** Cada instancia tiene la misma probabilidad de ser elegida.
- **Estratificado:** Asegura que subgrupos minoritarios estén representados proporcionalmente.
- **Por Agrupación (Cluster):** Se seleccionan grupos completos al azar.
- **Balanceado:** Crucial en problemas de clasificación con clases desequilibradas (ej. fraude).

## 3. Limpieza de Datos (Data Cleaning)

Los datos del mundo real suelen ser "sucios": incompletos, ruidosos o inconsistentes.

### Tratamiento de Valores Perdidos (Missing Values)
Estrategias comunes:
1.  **Eliminación:** Borrar filas con datos faltantes (solo si son pocas y no introduce sesgo).
2.  **Imputación Simple:** Rellenar con la media, mediana o moda.
3.  **Imputación Avanzada:** Usar algoritmos (KNN, Regresión) para predecir el valor faltante basándose en otras variables.

### Tratamiento de Ruido (Noise)
El ruido es un error aleatorio o varianza no explicada en una variable.
- **Nivel de Clase:** Etiquetas incorrectas (ej. un correo spam marcado como no-spam).
- **Nivel de Atributo:** Valores erróneos (ej. edad = 200).

*Técnicas de suavizado:*
- **Binning (Discretización):** Agrupar valores continuos en intervalos reduce el impacto de pequeñas fluctuaciones.
- **Regresión:** Ajustar una línea o curva para suavizar la tendencia.
- **Outliers (Valores Atípicos):** Detección y tratamiento de valores extremos (pueden ser errores o fraudes).

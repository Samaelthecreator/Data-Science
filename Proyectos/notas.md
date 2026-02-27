La clasificación tiene un conjunto limitado de salidas (por ejemplo, «spam» o «no spam»). La regresión busca predecir una salida que puede tomar cualquier valor dentro de un rango continuo.

### Sobre las limitantes en la visualización de datos.

Los diagramas de dispersión son excelentes para ver tendencias, pero hay fallas de calidad en ellos, ejemplos:

- Valores Nulos ($NaN$): Las librerías de visualización (como Seaborn) suelen ignorar los valores nulos automáticamente para poder graficar. Esto es peligroso porque podrías creer que tienes 1,460 datos, cuando en realidad solo estás graficando 500 porque el resto están vacíos.

- Datos "Dummy" o Centinelas: A veces, quien capturó los datos pone un 999 o un 0 cuando no sabe la respuesta. En una gráfica, esto se ve como un punto más, pero matemáticamente destruye la pendiente de tu recta.

- Duplicados: Si tienes una fila repetida 50 veces, en el scatter plot verás un solo punto, pero el modelo le dará 50 veces más importancia a esa observación (sobreajuste).

- Precisión vs. Exactitud: Un dato puede verse "bien" en la gráfica (dentro del rango), pero ser erróneo (ej. una casa de 10 m² que cuesta $1,000,000). La gráfica no te dirá si el dato es mentira, solo si es coherente con los demás.
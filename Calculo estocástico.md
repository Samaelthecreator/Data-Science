# Calculo Estocástico

Un proceso etocástico es un proceso aleatorio que evoluciona con el tiempo. Estos procesos se modelan a partir de sucesiones o colecciones matemáticas.
Cada una de las variables aleatorias del proceso tienen su propia funcion de distribución de probabilidad y pueden o no estar correlacionadas entre si.

Cada variable o conjunto de variables sometidas a influencias o efectos aleatorios constituye un proceso estocástico.


## Series en tiempo.
Las series en tiempo son una forma de modelar un proceso estocástico a través de sucesiones matemáticas {y}_t, donde t es el tiempo. 

Existen  dos tipos de series de tiempo:

Por el tipo de variable aleatoria:
    - Continua: Son series de tiempo que contienen variables aleatorias continuas.
    Ejemplos: procesos de Poisson, procesos de renovación, cadenas de markov a tiempo continuo, Procesos de nacimiento y muerte, modelos de colas, movimiento browniano.
    - Discreta: Son series de tiempo que contienen variables aleatorias discretas.
    Ejemplos: Cadenas de markov a tiempo discreto, Martingalas a tiempo discreto
Por la dimensión de la variable aleatoria:
    - Univariadas: Son series de tiempo que solo contienen una variable aleatoria.
    - Multivariadas: Son series de tiempo que contienen varias variables aleatorias.

Hint: Las mediciones en las series tienen que ser independientes de procesos de medición
Generalmente se usan tasas o indices (comprobar y extender)

### Carácteristicas de las series en tiempo.
Con base en la construcción matemática de las series en tiempo, estas tienen las siguientes características:

1.- Longitud de la serie o intervalo de válidez/tiempo:Esto representa el intervalo de tiempo que representa la serie.

2.- Partición o numero de elementos: representa el valor de las observaciones en el intervalo de tiempo (evento aleatorio) y tambien se denomina como resolución de la serie.

Tambien se consideran las siguientes carácteristicas

3.- Nivel o media de la serie: representa el valor promedio de todas las variables aleatorias del proceso.

4.- Varianza de la serie: representa la dispersión de las variables aleatorias del proceso con respecto a su media.

5.- Desviación estándar de la serie: representa la raiz cuadrada de la varianza de las variables aleatorias del proceso con respecto a su media.

6.- frecuencia de la serie: representa la cantidad de mediciones en un intervalo de tiempo.


COMENTARIOS: ¿Existen más caracteristicas importantes de las series? las mas importantes en este momento son las que determinan los componentes de la serie (ej: estacionalidad, tendencia, estacionariedad) como condiciones necesarias para la aplicación de modelos predictivos.

revisar si el punto 6 no es el mismo que el dos.


### Componentes de la series en tiempo.

Los componentes de la series en tiempo son los siguientes:

1.- Estacionalidad: Determina la presencia de crestas y valles periodicos en la serie en un tiempo relativamente corto (a veces en semanas o meses - promedio de un ciclo de un año).

2.- Tendencia: es la dirección general que toma la serie a lo largo del tiempo, esta puede ser:
- Ascendente: cuando la serie crece a lo largo del tiempo.
- Descendente: cuando la serie decrece a lo largo del tiempo.
- Estacionaria: cuando la serie no tiene tendencia. (revisar)

Si el nivel o la media de la serie cambia con respecto al tiempo, implica que existe una tendencia en la serie. Su desviación estandar es constante:

| Variable | estado | consideraciones |
|-------|---------------------|
| Media | variable | ""|
| Desviación estándar | constante |"" |

3.-  Ciclo: Presencia de crecimiento y decrecimeinto en la serie de forma periodíca. A diferencia de la estacionalidad la variación ciclica o ciclo no presenta crestas y valles de la misma magnitud (generalmente varia)

| Variable | estado | consideraciones |
|-------|---------------------|
| Media | variable | ""|
| Desviación estándar | variable |""|

4.- Valores aberrantes o residuos: .

Tipos de esquemas de series en tiempo:

    - Aditivo: Yt= Tt + Ct + St + e. 
    - Multiplicativo: Yt= Tt * Ct * St * e.
    - Mixto: Yt= Tt * (Ct + St) * e.


Estos son los componentes principales de una serie en tiempo.

COMENTARIOS: se tendría que validar las definiciones de los componentes. En general se enseñan a determinar estos componentes a partir de su representación gráfica. Pero es importante poderlo determinar a partir de cantidades matemáticas (por ejemplo las variables en las tablas posteriores a la definición) y como podriamos calcular algunos otros parámetros para asegurarnos (sin uso gráfico) si existen estos componentes o no.

Para los tipos de esquema, desarrollarlos mas a profundidad escribiendo por que son importantes definirlos a partir de estos esquemas y ejemplos de.

### Estacionariedad
Es importante diferenciar entre estacionariedad y estacionalidad. 
Son aquellas series en las cuales
tanto la media como la variabilidad de los valores en
el tiempo es nula o casi nula. Sus medidas fundamentales son La media, la varianza y la covarianza (La heterocedasticidad es el concepto que define la alteración de la varianza)
La serie estacionaria mantiene su media y varianza en el tiempo.
De igual forma una serie no estacionaria es la que su varianza y media SI varían en el tiempo.


### Ruido blanco: 
Series temporales que presentan valores aleatorios que siguen una distribución normal con media cero y varianza constante. (revisar y ampliar) 


### Transformaciones

Las series temporales tienen un conjunto de transformaciones con el objetivo de que, o bien sean descritas de mejor manera (que esta sucediendo) o bien se puedan predecir en un intervalo futuro.

Estas transformaciones son:

1.- Diferenciación: hacen que la media sea cero y esta definida por:
        y(t) = y(t) -y(t-1)

2.- Ajuste logaritmico: esto nos ayuda a hacer que la varianza sea constante.
        y(t) = log(y(t))

3.- Suavizado exponencial: 
en general existen los diferentes tipos de suavizado exponencial:
    - Simple:Estos son para series sin tendencia ni estacionalidad.
    - Doble:Estos son para series con tendencia y sin estacionalidad.
    - Triple:Estos son para series con tendencia y con estacionalidad.

Si se desea realizar intervalos de predicción para pronósticos realizados mediante métodos de suavizado exponencial. Los intervalos de predicción requieren que los errores de pronóstico no esten correlacionados y estén distribuidos normalmente con media cero y varianza constante


4.- Método ETS:


5.- Método Naive (ingenuo): este método unicamente predice los valores futuros extendiendo el ultimo valor observado.

6.- Método Naive estacionario: este método utiliza las variaciones ciclicas con la tendencia para predecir los valores futuros.



### Métodos predictivos (forecasting)

Los siguientes modelos se definen para series estacionarias.

Modelo ARMA (media movil autoregresiva): un modelo ARMA (promedio móvil) se
usa generalmente para modelar una serie de tiempo
que muestra dependencias a corto plazo entre
observaciones sucesivas


Modelo ARIMA (media movil autoregresiva integrada): Un modelo ARIMA (p,d,q) , p representa el orden del proceso autoregresivo, d el numero de diferencias que son necesarias para que el proceso sea estacionario y q representa el orden del proceso de medias móviles.

Las recomendaciones generales a la hora de realizar modelos predictivos en series temporales son:


Modelo SARMA:



• El pronóstico se debe realizar por un período o un
horizonte h, que debe ser como máximo igual al
periodo observado, pues, en términos generales,
los modelos predictivos, en la medida en la que se
alejan del último dato recogido, se van haciendo
más laxos y por lo tanto menos fiables.
• Se debe seleccionar aquel modelo que muestre un
menor valor en su medida depresión de pronóstico
para conseguir pronósticos menos amplios.



COMENTARIOS: que son los ordenes en estos modelos?, por que es importante el AIC,BIC, ALcc. ¿Que es el periodo de horizonte h y cuales son sus demarcaciones?

¿Que son los retardos y los rezagos?

### Parámetros de validación.

-Error absoluto medio (MAE): 
- Error cuadratico medio (MSE): 
- Raiz del error cuadrático medio (RMSE):
- Error absoluto medio normalizado (NMAE): 
-Error porcentual Medio (MPE):
- Error porcentual Medio Absoluto (MAPE):
- Coeficiente de U de theil


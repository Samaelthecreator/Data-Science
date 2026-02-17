Modulo 7 : series en tiempo

Proceso estocástico: Es un modelo matemático que permite representar una colección de variables aleatorias en el tiempo 

La teoría de los procesos estocásticos se centra en el
estudio y modelización de sistemas que evolucionan a
lo largo del tiempo. La forma habitual de describir la evolución del sistema
es mediante sucesiones o colecciones de variables
aleatorias (v.a.). De esta manera, se puede estudiar cómo
evoluciona una variable aleatoria a lo largo del tiempo.

Una sucesión de v.a. {Xn, n Є N} donde
el subíndice indica el instante de tiempo (o espacio)


Se tenía que una v.a. X(s) es una función que va desde un
espacio muestral S a la recta real, de manera que a cada
punto s Є S del espacio muestral se le puede asociar un
número de la recta real

 evolución azarosa a lo largo del tiempo -> (estos pueden ser a tiempo discreto o continuo)

Ejemplos:

• La evolución del mercado de valores: Bachelier.
• La descripción con de los movimientos de
partículas: Thiele, Einstein, Smoluchowski.
• Otras contribuciones importantes se debieron a
Ville, Doob, Bernstein, Íto, y Kolmogorov, entre otros


Procesos a tiempo discreto:
• Cadenas de Markov a tiempo discreto
• Martingalas a tiempo discreto

Procesos a tiempo continuo:
• Procesos de Poisson
• Procesos de renovación
• Cadenas de Markov a tiempo continuo
• Procesos de nacimiento y muerte
• Modelos de colas
• El movimiento browniano

Hay dos tipos de series en tiempo:
Continuas: Cualquier valor del tiempo
Discretas: Intervalos de tiempo
Las series temporales tienen además otra
característica, que hace muy difícil su tratamiento
mediante los métodos estadísticos habituales, pues
en la mayoría de estos se exige el cumplimiento del
supuesto de independencia de las observaciones,
mientras que las series generalmente se caracterizan
por la dependencia existente entre observaciones
sucesivas. Dicho de otro modo, puede existir una
correlación entre las diferentes observaciones de una
variable en periodos consecutivos de tiempo

Consistencia:La
metodología de recolección debe ser invariablemente
la misma, esta es la base fundamental para dar
consistencia al dato. El método empleado sea capaz de
medir las fluctuaciones del evento en el tiempo y no
tanto la verdadera magnitud del fenómeno. Variaciones tambien en la recolección y procesamiento de datos, calidad, consistencia, veracidad.

estas mediciones en las series tienen que ser independientes del proceso de medición Generalmente se usan tasas o indices.

	Estabilidad: una serie es inestable cuando son eventos poco frecuentes o su magnitud es despreciable con relación a la población en la cual ocurren.

Cuando hay datos erroneos o aberrantes, se recomienda definirlos nulos. Las técnicas que se utilizan para tratarlos son las siguientes:

Sustitución por la semisuma de los valores
vecinos. Esta es la forma más sencilla y habitual
de sustituir un valor aberrante, sobre todo cuando
se trata de casos aislados.
2. Sustitución por la media aritmética general de
la serie. Este método puede ser la mejor manera
de estimar un dato, siempre y cuando la serie no
tenga grandes fluctuaciones.
3. Sustitución por el valor resultante de la interpolación
de valores adyacentes. Este método asume en cierta
forma que existe una correlación entre los valores
consecutivos de la serie y que cada observación
está relacionada con las observaciones previas, pues
consiste en ajustar los valores adyacentes al perdido
mediante una línea y después sustituirlo por el valor
de la expresión matemática correspondiente a ese
momento de tiempo.
4. Sustitución por el valor esperado según la
tendencia. En esta forma se obtiene primero
la tendencia de la serie con el resto de los
valores (puede opcionalmente realizarse algún
suavizamiento previo). El dato perdido se estima
entonces a partir de esta.

la longitud de las series (intervalos temporales) dependerá de los casos y sus longitudes de existencia.

Tipos de gráficos de series:

Gráfico arimético simple (GAS)
(hint: escalas semilogarítmicas)

Los tres componentes principales de una serie de
tiempo son su momento de inicio, su frecuencia y
su momento de terminado


		Tema 2: La serie temporal

Las series tienen los siguientes componentes:

• Tendencia (T): representa la evolución de la serie
en el largo plazo, mostrando la orientación de valor
que posee la serie en el tiempo, para la obtención
de la tendencia es necesario disponer de una
serie relativamente larga y de un número de ciclos
completo, para que esta no se vea influida por la
fase del ciclo en que finaliza la serie, por lo que, a
veces, resulta difícil separar ambos componentes.
En estos casos resulta útil englobar ambos
componentes en uno solo, denominado ciclo-
tendencia o tendencia generalizada.

La tendencia se puede ver como la pendiente a partir de la estimación de la media de los valores de una serie a lo largo del tiempo. Tipos:
Positiva: crecen los valores a través del tiempo
Negativa: decrementan conforma al tiempo
nula: media relativamente uniforme


• Fluctuación cíclica (C): refleja las fluctuaciones
de carácter periódico pero no necesariamente
regular a medio plazo, en torno a la tendencia. Este
componente es frecuente hallarlo en las series
económicas, puesto a que se debe a los cambios
en la actividad económica.

Son aquellos registros repetitivos y rítmicos que tienen lugar en lapsos más prolongados (ej: series económicas).

• Variación estacional (S): recoge aquellos
comportamientos de tipo regular y repetitivo que se
dan a lo largo de un periodo de tiempo -generalmente
igual o inferior a un año- y que son producidos por
factores tales como las variaciones climatológicas,
las vacaciones, las fiestas, entre otras. Es decir,
estas variaciones están relacionadas generalmente
con las estaciones meteorológicas, dado que a
estas deben su nombre.

La estacionalidad se asocia a la
variación usual de hábitos a lo largo de estos períodos (estaciones del año)

• Movimientos irregulares (I): pueden ser
aleatorios, además recogen los pequeños efectos
accidentales o erráticos, como resultado de hechos
no previsibles pero identificables a posteriori
(huelgas, catástrofes, etc.)

Valores aberrantes: valores que se desvían significativamente
de la media y que, adicionalmente, parecieran estar
completamente disociados del comportamiento general
de los datos

Estos se asocian generalmente a metodología específica de recopilación
y recolección del dato, a un registro erróneo accidental,
o efectivamente a un valor debidamente recogido
pero que, en efecto, se disocia del comportamiento
general de la serie.





La detección de los componentes generalmente se hace a través de su graficación




HINTS: 
La función R “Decompose”, obtiene las series
de tendencia, estacionalidad e irregular de una serie
temporal a través de medias móviles, además permite
obtener los componentes en base a un esquema aditivo
o multiplicativo




Tema 3: Tipologias

Frecuencia de las series:
• Series de baja frecuencia: son series que tienen
medidas mensuales, trimestrales, anuales o
incluso, de periodos anuales agrupados, como
décadas o quinquenios.
En este tipo de series, es posible observar
eventualmente el comportamiento cíclico o
estacional de la serie.
• Serie de alta frecuencia: hacen referencia
a aquellas series cuyos datos son diarios o,
incluso, en lapsos menores al día, como pueden
ser por hora o lapsos específicos establecidos
con rangos bajos. Estos permitirán realizar una
analogía sobre el ciclo, aunque no se considerará
como un comportamiento propiamente cíclico
o estacional, debido a que el lapso entre una
medida y la siguiente no atiende a las estaciones,
así como tampoco permite construir unos
ciclos constantes, los cuales están asociados a
periodos anuales.


Definición de estacionariedad : Son aquellas series en las cuales
tanto la media como la variabilidad de los valores en
el tiempo es nula o casi nula. Sus medidas fundamentales son La media, la varianza y la covarianza (La heterocedasticidad es el concepto que define la alteración de la varianza)
La serie estacionaria mantiene su media y varianza en el tiempo.
De igual forma una serie no estacionaria es la que su varianza y media SI varían en el tiempo.

Los beneficios de las series estacionarias es la posibilidad de aplicarle modelos predictivos, la mayoria de los modelos estan diseños para hacer predicciones sobre series estacionarias.

RUIDO BLANCO: series temporales con media igual a cero y varianza constante

Random Walk: define un comportamiento azaroso


Transformaciones

Diferenciación: este proceso transforma una serie no estacionaria a estacionaria y se calculan las diferencias del valor con su antecesor.

Ajuste logarítmico: se aplica el logaritmo natural a la serie de datos,. especificamente, una serie de datos univariantes (vector) , esto reduce la alteración de la varianza -> estabilidad en terminos de la amplitud de varianza.

Suavizado exponencial : Se encuentran los siguientes tipos de suavizado
exponencial :
• Suavizado exponencial simple (para series sin
tendencia ni estacionalidad)
• Suavizado exponencial doble (para series con
tendencia, pero sin estacionalidad)
• Suavizado exponencial triple (para series con
tendencia y estacionalidad)


Tema 4: Esquemas para series temporales

se asume que los datos Y pueden expresarse como
una función de una componente de tendencia Tt , la
componente cíclica, cuando está presente Ct , una
componente estacional St y de un error et que está
formado por el efecto de diversos factores

t= Representa la tendencia
Ct= Representa el componente cíclico
St= Representa la estacionalidad de la serie

Esquema aditivo:
El esquema aditivo toma la siguiente forma: 
			
Yt= Tt + Ct + St + e

Se considera que sus componentes son independientes entre si

Esquema multiplicativo:

Yt= Tt * Ct * St * et

Estos modelos son apropiados cuando la magnitud
de las fluctuaciones estacionales de la serie crece y
decrece proporcionalmente con los crecimientos y
decrecimientos de la tendencia, Los componentes dependen entre si




Esquema mixto:

O bien ser una combinación de ambos, por ejemplo:
Yt= T t + C t + St * et
Yt= T t * C t * St + et

Este modelo es en el supuesto de que uno o varios componentes se comporten de forma independiente. Los componentes independientes se suman y los que tienen comportamiento dependiente se multiplican

En este curso solo se estudiará el método gráfico que
consiste en:
1. Calcular las medias y desviaciones típicas de cada
año.
2. Representar estos estadísticos en unos ejes de
coordenadas (media, desviación típica).
3. Si la nube de puntos es creciente, esquema
multiplicativo; y, en caso contrario, aditivo.

Lo importante es identificar ante que tipo de modelo se esta trabajando

Formas de identificar:

Visualmente: Gráfico simple de los datos:
Recurso plot.ts()
Recurso ggseansonpllot(): dibujará de forma superpuesta, a través de gráficos de lineas, todos los periodos estudiados (identificar el avance en el tiempo)
solicitud plot() , autoplot() de la función decompose(): separará los datos originales, la tendencia, la estacionalidad y sus rezagos

Metodología estadística de la descomposición.

la serie temporal se puede dividir en tres
componentes. En el modelo aditivo, se comienza
calculando la tendencia. Puede estimarse de varias
formas mediante un método paramétrico (escriba
cálculo de mínimos cuadrados). La línea de tendencia
puede ser, según el modelo [4]:
lineal: y = a t + b
cuadrático / orden 2: y = a t² + bt + c
exponencial: y = a exp (wt)
Para la estacionalidad, el objetivo es encontrar un patrón
que se repita en una frecuencia temporal. Se debe
eliminar el componente tendencial y distinguir el período
de la temporada y su motivo

El ruido donde el residuo es lo que queda después de
la eliminación de los componentes de tendencia y
estacionales. En general, se estima que es ruido blanco
Gaussiano [4].
Para un modelo multiplicativo, se puede reducir a un
modelo aditivo tomando el logaritmo natural de la serie
de tiempo y, por lo tanto, a su descomposición anterior


Cuanto mayor sea
la proporción de la varianza de un componente, más
explicará el fenómeno. Así, un mercado con una fuerte
estacionalidad tendrá su componente estacional con
una alta varianza

La funcion seasonplot(), a diferencia de un gráfico de serie temporal estándar, seasonplot() superpone los datos de cada período estacional (por ejemplo, cada año) en un mismo eje horizontal. 
Visualización: Permite observar patrones estacionales repetitivos y detectar desviaciones o cambios en el comportamiento a lo largo de los años de forma más clara.
Estructura: El eje X muestra las "temporadas" (meses o trimestres) y cada línea representa un ciclo completo (un año
Método ETS (estacionariedad, tendencia, save ->)
Metodo naive


Tema 5: Métodos básicos de forecast

Se desarrollará el tema para determinar la predicción para Series estacionales y no estacionales 


Suavizado exponencial Simple:
Se utiliza para la predicción o proyección de datos futuros de una serie temporal. Este método funciona con muy pocos registros de períodos
anteriores destacando los hechos más recientes sobre
los más antiguos.

Ventajas  

Este es el método más utilizado por su versatilidad
y facilidad, algunas de las características o ventajas
principales de dicho método son las siguientes:
• La formulación es sencilla, solo requiere el
pronóstico anterior, la demanda real del periodo de
pronóstico y la constante de suavización.
• Funciona bien en conjuntos de datos pequeños
• Es suficientemente preciso.
• Establece una importancia mayor para los periodos
más recientes y una menor para los más antiguos.

El método de suavización exponencial simple trabaja
a través de una constante de suavización alfa (α) que
tiene un valor comprendido entre 0 y 1, aunque en la
práctica su valor suele variar entre 0,05 y 0,50; esta
constante constituye un valor de ponderación, el cual es
mayor para los datos más recientes y va disminuyendo
conforme se aleja en el tiempo.
La fórmula de suavizamiento exponencial es la siguiente:

F t = F t - 1 + α (At - 1 - F t - 1 )

• Ft = nuevo pronóstico

• Ft-1 = pronóstico del periodo anterior

• α = constante de suavización

• At-1 = demanda real del periodo anterior
La casuística específica para la aplicación del suavizado
exponencial en términos del nivel o grado de suavizado
es el siguiente:

• Suavizado exponencial simple (para series sin
tendencia ni estacionalidad).
• Suavizado exponencial doble (para series con
tendencia, pero no estacionalidad)
• Suavizado exponencial triple (para series con
tendencia y estacionalidad)

 
Herramientas:

Función ses (): pronósticos de suavizado exponencial, esta
función devuelve el pronóstico de una serie temporal y
para una cantidad h=períodos a estimar

En la función que se usa en R para realizar un suavizado exponencial, en el parámetro level se establece el nivel de confianza para los intervalos de predicción y el parámetro beta fija en el valor de parpametro de suavizado de la tendencia



Métodos de pronóstico ingenuos (pronóstico naive):



ME, RMSE, MAE, MPE, MAPE y MASE



Tema 6: Análisis de residuos.

Si se desea realizar intervalos de predicción para pronósticos realizados mediante métodos de suavizado exponencial. Los intervalos de predicción requieren que los errores de pronóstico no esten correlacionados y estén distribuidos normalmente con media cero y varianza constante.



Modelos ARIMA (media movil integrada autoregresitva):

Estos modelos se definen para series de tiempo estacionarias
estadístico George Edward Pelham Box y el estadístico
e ingeniero Gwilym Meirion Jenkins en 1970 en el libro
Análisis de series temporales. Predicción y control (Time
Series Análisis: Forecasting and Control).

Un modelo ARIMA (p,d,q) , p representa el orden del proceso autoregresivo, d el numero de diferencias que son necesarias para que el proceso sea estacionario y q representa el orden del proceso de medias móviles.

Si se parte de una serie no estacionaria, se tiene que aplicar diferenciación hasta hacerla Estacionaria (d veces).
la diferenciación se hace con la función diff()

Lo siguiente es encontrar los valores apropiados de p y q
con el uso del correlograma (acf()) y el correlograma parcial (pacf() )


Modelo ARMA (Media móvil autoregresivo):

un modelo ARMA (promedio móvil) se
usa generalmente para modelar una serie de tiempo
que muestra dependencias a corto plazo entre
observaciones sucesivas


Por otra parte, un modelo ARMA (0,1) es un modelo


de promedio móvil de orden 1. Este modelo se puede
escribir como:
X t - μ = Zt - (θ * Zt - 1 )
Xt = Serie de tiempo que se estudia
μ= Media de la serie
Zt = Ruido blanco con media 0 y varianza constante
θ = Parametro estimado


hint: AIC,BIC,AIcc

Suavizado exponencial:

El método de suavización exponencial utiliza los
promedios históricos de una variable en un período para
intentar predecir su comportamiento futuro

La fórmula, que se enseñó con detalle en el ejemplo,
incluye una demanda real (Do) y un pronóstico (Po).
Por otro lado, también se tiene en cuenta el factor de
suavización (alfa) expresado en tantos por uno. La
fórmula sería la siguiente:
P1
= P0 + α(D0 - P 0
)
El proceso que se realiza es el suavizado de la serie,
donde:
• P0 = Pronóstico del período anterior (Po)
• D0 = Demanda
• α = factor de suavización

Modelos de suavizado más complejos: Box-Jenkins , Holt Winter.

Ventajas de los métodos de
suavización exponencial
Las ventajas son sobre todo la sencillez y la facilidad
de aplicación, pero hay algunas más. A continuación, se
enseñan las más relevantes:
• No necesita de muchos datos históricos, a
diferencia de otros métodos como el ARIMA.
• Tiene una mayor precisión que otros al utilizar
técnicas de modelado exponencial.
• Es un método que goza de gran flexibilidad, al
utilizar datos de demanda que pueden ser elegidos
por el investigador.
• El llamado alisado exponencial doble permite
reducir los problemas de pronóstico cuando el
factor de suavización es mayor a 0.5. Uno de sus
pocos inconvenientes.

El paquete forecast incluye la función “auto.
arima()” que realiza un ajuste automático de un
modelo ARIMA a una serie temporal dada.






Tema 7: Regresión en el contexto de series temporales.

Las recomendaciones generales a la hora de realizar modelos predictivos en series temporales son:

• El pronóstico se debe realizar por un período o un
horizonte h, que debe ser como máximo igual al
periodo observado, pues, en términos generales,
los modelos predictivos, en la medida en la que se
alejan del último dato recogido, se van haciendo
más laxos y por lo tanto menos fiables.
• Se debe seleccionar aquel modelo que muestre un
menor valor en su medida depresión de pronóstico
para conseguir pronósticos menos amplios.

Error: es la distancia que hay entre el valor predicho y el valor real.
Error absoluto = valor observado - valor esperado error










Error medio: promedio de todos los errores de un conjunto de observaciones

1 n
ME= 1/n SIGMA(y i - f i )
n i= 1
Esta es una métrica muy simple. Desafortunadamente
está sesgada, debido al efecto de compensación
de errores de predicción positivos y negativos

Este puede mostrar rapidamente la simetria de la distribución de errores.


Error absoluto medio (MAE): Utiliza los valores absolutos de los errores en los calculos.

 		n
MAE= 1/n SIGMA |y i - f i|
n =1


Error cuadrático medio(MSE):

Otorga mayor penalización en los errores de predicción grandes que el MAE


Raiz del error cuadratico medio (RMSE) : Es sacar la raiz del MSE.
tiene las mismas unidades que la variable predicha, por lo que es mejor su interpretabilidad.


Error porcentual Medio (MPE): Es el promedio de errores porcentuales por los que cada previsión difere de sus correspondientes va

lores reales observados






Proporciona el error en terminos de porcentajes
Esta métrica no es adecuada para conjunto de datos que contienen valores ceros (indeterminación)

Error Porcentual Absoluto Medio (MAPE). es similar al MAE y al MPE solo que en terminos de porcentajes. con todo y sus limitaciones.


Coeficiente de U de theil:

Tenemos el primer coeficiente de thail:


Para valores entre [0,1]
Cuanto mayor sea la precisión de la predicción. menor será el valor del coeficiente.

El segundo coeficiente U2 se indica cuánto más (o menos) preciso es un modelo en relación con una predicción trivial.


Al igual que U1, U2 tiene un limite inferior de 0 (predicción perfecta). cuando el valor supera 1, significa que la predicción es incluso peor que la predicción trivial.

Estos Residuos nos ayudan a determinar los valores de p y q para el modelo




















Elección del mejor modelo
R utiliza la Estimación de Máxima Verosimilitud
(MLE) para estimar el modelo ARIMA. Intenta
maximizar la probabilidad logarítmica para valores
dados de p, d y q al encontrar estimaciones de
parámetros para maximizar la probabilidad de
obtener los datos que se han observado, además:
- Usa el criterio de información de Akaike (AIC) para
un conjunto de modelos e investigar los modelos
con los valores AIC más bajos.
- Prueba el criterio de información bayesiano (BIC)
de Schwarz e investiga los modelos con los
valores BIC más bajos




Tema 8: Modelos predictivos de series temporales

Los pasos para poder trabajar con un problema que involucre series temporales es, primeramente:

Graficar: cargando los datos y transformandolos a tipo time series (ts)
Descomponer la serie= Tendencia + Efecto estacional + Residuos (se usa decompose -> tendencia, patron aleatorio y stl - > estacionalidad, retardos o rezagos)
Transformar la serie a estacionaria (generalmente) para posteriormente aplicar los métodos predictivos. Una serie estacionaria es una serie temporal cuyas propiedades estadísticas (media, varianza y covarianza) no cambian con el tiempo, oscilando alrededor de un valor medio constante sin tendencias alcistas o bajistas claras, y con una variabilidad que permanece estable
Definir el modelo: aditivo o multiplicativo
verificación: determinar si es idóneo el modelo prouesto 
estimación de parámetros: podemos determinar parámetros que se ajusten mas a la forma del comportamiento de los datos.
Predicción de datos: se determina el horizonte h 

Estabilización de la varianza

Se suelen utilizar logaritmos. Se utiliza cuando la variabilidad sea aproximadamente proporcional al nivel de la serie.

Estabilización de la tendencia:

La forma mas simple y directa de estabilizar una serie es através de diferenciación -> hacer tendencia estable.

Eliminar estacionalidad: se deben tomar diferencias estacionales de orden 12, dado que el 12 obedece a la cantidad de periodos dentro de cada ciclo estacional


Retardos o rezagos:
*El correlograma es una representación gráfica de las autocorrelaciones 

Los gráficos acf y pacf, representan los rezagos que describen el comportamiento de los valores de la serie.


Paquetes importantes para datos:

Tidyverse: exploración, ordenación y analizar datos.

Ggplot2: paquete de visualización de datos

Proporciona una serie de funciones para la
manipulación de datos. Algunas de sus funciones más
usadas son las mencionadas a continuación:

• “filter ()” elige filas en función de los valores de las
columnas.
• “slice ()” elige filas en función de la ubicación.
• “arrange ()” cambia el orden de las filas.
• “select ()” cambia si se incluye o no una columna.
• “rename ()” cambia el nombre de las columnas.
• “mutate ()” cambia los valores de las columnas y
crea nuevas columnas.
• “relocate ()” cambia el orden de las columnas.
• “summarise ()” contrae un grupo en una sola fila


Librerias para análisis de series temporales:

FORECAST: Paquete R proporciona métodos y herramientas para
mostrar y analizar pronósticos de series temporales
invariadas, incluido el suavizado exponencial a través
de modelos de espacio de estado y el modelado
automático ARIMA

La siguiente lista muestra todas las funciones que
produce Forecast objetos.
• “meanf ()”
• “naive ()”, “snaive ()”
• “rwf ()”
• “croston ()”
• “stlf ()”
• “ses ()”
• “holt ()”, “hw ()”
• “splinef ()”
• “thetaf ()”
• “Forecast ()”
• “Forecast ()”

fpp2
Carga varios paquetes necesarios para realizar el análisis
descrito en el libro.

Tseries
Este paquete ofrece una serie de funciones específicas
para el análisis de la serie temporal, que a su vez
permiten describir la serie, por ejemplo, conocer esos
movimientos irregulares, realizar pruebas específicas
como la Dickey Fuller y separar la estacionariedad de la
serie. Este paquete a su vez contiene algunos modelos
de ajuste entre otros modelos GARCH y ARMA.





## Guía de Modelos Multivariados y Especializados en Series Temporales

Estos modelos y pruebas responden a limitaciones de los métodos univariados (como ARIMA o suavizado exponencial) que no pueden manejar relaciones entre múltiples series, volatilidad cambiante o la necesidad de verificar estacionariedad.

### 1. Modelos VAR (Vector Autoregresivo)
**¿Qué es?** Un sistema de ecuaciones donde **cada variable** se explica por sus propios valores pasados y los valores pasados de **todas las demás variables** del sistema. Es una generalización multivariante del AR univariante[reference:0].

**¿Para qué y por qué es necesario?**
*   **Propósito**: Modelar la **dinámica conjunta** y las interacciones de retroalimentación entre series temporales múltiples (ej: PIB, inflación, tasa de interés).
*   **Caso de uso típico**: Análisis de **shocks** y sus propagaciones (usando Funciones de Impulso-Respuesta), y pronóstico de un sistema de variables.
*   **¿Por qué otros métodos no sirven?**:
    *   Un **ARIMA univariante** modela cada serie por separado, ignorando la información de las demás.
    *   Los **modelos de ecuaciones simultáneas estructurales** requieren supuestos teóricos muy fuertes (ej: definir qué variables son exógenas). El VAR evita esto al tratar a todas las variables como **potencialmente endógenas**[reference:1].

### 2. Modelos VEC (Vector de Corrección de Error)
**¿Qué es?** Es un **VAR restringido** aplicado a series que están **cointegradas**. Incluye un término que "corrige" los desequilibrios de corto plazo, guiando al sistema hacia su **relación de equilibrio de largo plazo**[reference:2].

**¿Para qué y por qué es necesario?**
*   **Propósito**: Modelar tanto la **dinámica de corto plazo** como las **relaciones de equilibrio de largo plazo** entre series no estacionarias.
*   **Caso de uso típico**: Analizar pares de acciones para *pairs trading*, o relaciones macroeconómicas como consumo-ingreso, donde las variables "no se separan demasiado" en el largo plazo[reference:3].
*   **¿Por qué otros métodos no sirven?**:
    *   Aplicar un **VAR estándar** a series no estacionarias (I(1)) sin cointegración lleva a **regresiones espurias**[reference:4].
    *   **Diferenciar** las series para hacerlas estacionarias y luego aplicar un VAR (VAR en diferencias) **elimina la información de largo plazo**. El VEC la preserva a través del término de corrección.

### 3. Prueba de Dickey-Fuller (Aumentada)
**¿Qué es?** Una prueba estadística (y su versión ampliada, ADF) para detectar **raíces unitarias**. Su hipótesis nula es que **la serie no es estacionaria** (tiene una raíz unitaria)[reference:5].

**¿Para qué y por qué es necesario?**
*   **Propósito**: Verificar formalmente el supuesto de **estacionariedad** antes de aplicar modelos como ARIMA, que lo requieren.
*   **Caso de uso típico**: Paso previo **obligatorio** en el modelado ARIMA. Determina si y cuántas veces se necesita **diferenciar** la serie.
*   **¿Por qué otros métodos no sirven?**:
    *   Evaluar la estacionariedad "a ojo" en un gráfico es subjetivo y poco confiable.
    *   Los **correlogramas (ACF/PACF)** pueden sugerir no estacionariedad (decaimiento lento), pero no ofrecen una prueba formal. La ADF es el estándar.

### 4. Modelo GARCH (Generalized Autoregressive Conditional Heteroskedasticity)
**¿Qué es?** Un modelo que describe cómo la **varianza condicional** (volatilidad) de una serie evoluciona en el tiempo, dependiendo de shocks pasados y de la volatilidad pasada[reference:6].

**¿Para qué y por qué es necesario?**
*   **Propósito**: Modelar y predecir la **volatilidad cambiante** (*clusters* de volatilidad), común en datos financieros.
*   **Caso de uso típico**: Valoración de opciones, cálculo de **Value at Risk (VaR)** dinámico, y modelado de rendimientos de activos[reference:7].
*   **¿Por qué otros métodos no sirven?**:
    *   **ARIMA/SUAVIZADO** asumen **varianza constante** (homocedasticidad). Si la volatilidad es cambiante, sus intervalos de predicción serán incorrectos.
    *   Permite cuantificar fenómenos como la **persistencia** (α+β cerca de 1) y la **asimetría** (con extensiones como EGARCH)[reference:8][reference:9].

### Resumen Comparativo y Diagrama de Decisión

| Modelo/Prueba | Problema que resuelve | ¿Qué lo hace único? | Método anterior inadecuado |
| :--- | :--- | :--- | :--- |
| **VAR** | Dinámica conjunta de múltiples series. | Modela interdependencias sin teoría estructural rígida. | ARIMA univariante (ignora relaciones). |
| **VEC** | Relación de largo plazo entre series no estacionarias. | Incorpora un "mecanismo de corrección" hacia el equilibrio. | VAR en diferencias (pierde info de largo plazo). |
| **Dickey-Fuller** | Verificar estacionariedad. | Prueba formal para raíz unitaria (base para diferenciar). | Inspección visual o ACF (subjetivo/no formal). |
| **GARCH** | Volatilidad que cambia en el tiempo (clusters). | Modela la varianza condicional de forma dinámica. | Cualquier modelo que asuma varianza constante. |

```mermaid
flowchart TD
    A[Problema de Análisis] --> B{Variables involucradas?}
    B -->|Una sola serie| C[Análisis Univariante]
    B -->|Múltiples series| D{¿Series estacionarias?<br>Prueba Dickey-Fuller}
    
    C --> C1{¿Volatilidad constante?<br>Inspeccionar residuos}
    C1 -->|Sí| C2[Usar ARIMA/Suavizado]
    C1 -->|No, hay clusters| C3[Usar GARCH]

    D -->|Sí, I(0)| E[Usar VAR]
    D -->|No, I(1)| F{¿Existe cointegración?<br>Prueba de Johansen}
    F -->|Sí| G[Usar VEC]
    F -->|No| H[Usar VAR en diferencias]
```

### Conclusión

Estas herramientas expanden tu caja de herramientas más allá del mundo univariante. Los **modelos VAR y VEC** te permiten analizar sistemas de variables, crucial en economía y finanzas. La **prueba de Dickey-Fuller** es un paso diagnóstico esencial para evitar modelar incorrectamente series no estacionarias. Finalmente, **GARCH** es indispensable cuando la incertidumbre (volatilidad) no es constante, sino que se agrupa en el tiempo, como ocurre en casi todos los mercados financieros. La elección depende enteramente de la naturaleza de tus datos y la pregunta de investigación.





MODULO 8
Diseño y desarrollo de sistemas inteligentes

Una de las técnicas más empleadas para
la extracción del conocimiento es lo que se conoce
como «descubrimiento de conocimiento en bases
de datos» o knowledge discovery in databases (KDD)

El proceso KDD está compuesto por los siguientes
pasos:
• Selección de datos a partir de un conjunto mayor
• Preprocesamiento de los datos
• Transformación de los datos a un formato distinto
• Minería de datos, que consiste en la aplicación
de diferentes algoritmos para la extracción de
patrones en los datos
• Evaluación e interpretación de los patrones
extraídos que dará lugar al conocimiento

Existen otros
marcos para la extracción de conocimiento a partir de
datos como el cross industry standard process for data
mining (CRISP-DM) o el sample, explore, modify, model,
and assess (SEMMA), pero ambos son variaciones en la
implementación del proceso

identificar el objetivo
desde el punto de vista del cliente antes de comenzar
el proceso KDD

Las tres primeras fases del proceso KDD
(selección, preprocesamiento y transformación

Selección de datos:

Sera necesario hacer las siguientes preguntas:

¿Qué cantidad de datos se necesitan? Se puede
encontrar en el caso de disponer de un conjunto de
datos masivo que sea imposible de abordar entero,
o que las necesidades del problema solo requieran
de una pequeña muestra.
• En el caso de seleccionar un subconjunto de datos,
¿qué técnica de selección de datos emplearía?
• ¿Consideramos los datos cuantitativos, categóricos,
o ambos?
• En el caso de que los datos sean numéricos,
¿empleamos las variables discretas, las continuas,
o ambas?
• ¿El conjunto de datos contiene texto libre? ¿Será útil
para el análisis?

Por ello es importante determinar el muestreo de los datos. 4Preprocesamiento de datos |
El muestreo se emplea principalmente para facilitar
el análisis de grandes volúmenes de datos. Para ello,
se puede reducir el número de instancias, particionar
conjuntos de datos para emplearlos en diferentes
objetivos, ayudar al balanceo de los datos, crear los
conjuntos de entrenamiento, test y validación, etcétera.
Algunas técnicas para seleccionar un subconjunto de
datos del conjunto de datos original son las siguientes:
• Muestreo aleatorio
• Muestreo con reemplazo
• Muestreo balanceado
• Muestreo por agrupación
• Muestreo estratificado

Datos sucios: campos vacíos, erróneos y/o
inconsistentes con el resto.

Tratamientos y transformaciones:
Tratamiento de valores perdidos. Por lo general
existen dos enfoques encargados de tratar con
estos valores [5]:
- El primero de ellos es eliminar las instancias o
ejemplos que incluyen estos valores perdidos e
incluso aquellos atributos que contengan gran
cantidad de valores perdidos.
- Y el segundo es «rellenar» o imputar los
valores perdidos. Existen métodos básicos de
imputación basados en la estadística como
la imputación por la media, los métodos hot-
deck, el uso de procedimientos de máxima
verosimilitud para la imputación de valores,
métodos de regresión, etcétera. Y otros más
avanzados basados en aprendizaje automático
como por ejemplo, imputación mediante
K-Nearest Neighbor (KNN), Support Vector
Machines (SVM), K-means, entre otros.

Tratamiento del ruido. El ruido puede definirse como
un error aleatorio en una variable registrada dentro
de un conjunto de datos. Los datos ruidosos pueden
darse a nivel de clase y a nivel de atributos [3]:
- Ruido a nivel de clase (o etiqueta): se da cuando
un ejemplo está etiquetado de forma incorrecta,
dándose dos tipos: ejemplos contradictorios, es
decir, ejemplos duplicados con distinta etiqueta,
y ejemplos mal etiquetados.
- Ruido a nivel de atributo: valores erróneos dentro
de los atributos, perdidos, desconocidos, o
incompletos.


 Los filtros empleados para detectar y eliminar el ruido
suelen emplearse en el caso de ruido a nivel de clase,
ya que la eliminación de instancias con ruido a nivel de
atributo puede ser contraproducente porque dichas
instancias pueden seguir teniendo información valiosa
para la construcción del clasificador.

Algoritmos para el tratamiento de ruido a nivel de atributo:
Suavizado (metodos de binning)
- regresión

Algoritmos tolerantes al ruido:
C4.5	


A veces el ruido es nuestro objetivo. por ejemplo los tipos de ruidos serian:

raude bancario, buscando
transacciones anómalas o poco comunes, y
la deteccíon de cáncer de mama detectando
regiones anómalas en mamografías, entre otros.

Para ello 

Transformación:
• Reducción de los datos (paso opcional -> dependerá el tiempo de procesamiento del algoritmo para determinar si es necesario o no)
Comprende una serie de técnicas para la
obtención de una representación reducida de los
datos originales. Cabe destacar que los datos ya
se encuentran listos para su análisis (proceso de
minería de datos), por lo que se considera un paso
opcional siempre que el tiempo de ejecución del
algoritmo de minería de datos no sea prohibitivo.
En entornos big data este paso es imprescindible.
También resulta de gran utilidad para reducir la
complejidad de los datos mejorando así la calidad
de los modelos. Existen diferentes técnicas para la
reducción de los datos según las necesidades del
problema, a saber.

Procesos de reducción de datos:
Selección de características: identificar caracteristicas importantes y eliminar las irrelevantes o las redundantes
Selección de instancias: un ejemplo de selección de instancias es el muestreo aleatorio
Discretización: transformación  de datos cuantitativos en atributos discretos con un número finito de intervalos.
Normalización de datos: es especialmente util para aquellos algoritmos que emplean medidas de distancia como el de los vecinos mas cercanos KNN. y los algoritmos de clustering. Ejemplos de métodos de normalización:
Normalización min-max
Z-score
Escala decimal



Mineria de datos: Proceso de busqueda y descubrimiento de patrones y conocimiento útil a partir de datos se le conoce como mineria de datos.
Mineria de datos -> KDD (análisis de estos para la busqueda de patrones y conocimiento útil)

Tipos de análisis:
Análisis predictivo: predicidir el valor de un atributo concreto basado en los valores del resto de atributos, existen dos tipos: Clasificación y regresión
Análisis descriptivo: Patrones que resumen las relaciones de los datos: análisis de asociación o reglas de asociación. Detección de anomalias.

Algunas formas de representación de la salida de un proceso de minería de datos son las siguientes:
tablas
Modelos lineales
Arboles
Reglas:las reglas son una representación
alternativa a los árboles de decisión, siendo el
antecedente de las reglas las precondiciones que
se deben cumplir para que esa regla se active,
y el consecuente, la clase o clases que cubre el
antecedente.
Representación basada en instancias
Clusters

Por ultimo vamos a determinar métricas para evaluar el rendimiento de los modelos.



					Tema 2
			Aprendizaje supervisado

El aprendizaje supervisado es el desarrollo de algoritmos capaces de aprender a partir de un conjunto de datos.

Dentro del aprendizaje automático se puede distinguir tres tipos principales:
Aprendizaje supervisado: A partir de datos previamente etiquetados, poder etiquetar nuevos datos de entrada
Aprendizaje no supervisado: a partir de cierto conjunto de datos, determinar si estos se agrupan en ciertas etiquetas y cuales son estas
Aprendizaje por refuerzo

Los atributos que forman parte del conjunto de
entrenamiento normalmente suelen ser de dos tipos:
nominales (o categóricos) o numéricos. Los atributos
nominales tienen una cardinalidad finita (discretos)
mientras que el dominio de los atributos numéricos
está delimitado por límites superiores e inferiores
(continuos) [2


Aprendizaje supervisado -> clasificación, regresión







El aprendizaje no supervisado es sinónimo de clustering (agrupación).A menudo se utilizan medidas de distancia o de densidad para calcular las similitudes.

Otro problema dentro del aprendizaje no supervisado son las reglas de asociación: son un conjunto de técnicas cuyo objetivo es encontrar reglas de asociación en los datos: Ej: Analizar la probabilidad de que cuando un cliente compre un producto X tambien compre un producto Y



Aprendizaje por refuerzo

Aprende mediante la interacción de un agente con su entorno (aprendizaje iterativo). El agente realiza acciones (basadas en ensayo y error) dentro de un entorno recibiendo recompensas si sus acciones le conducen a estados deseables. -> maximización de dicha recompensa.

Existe el dilema entre *explotación y exploración* .Para la obtención de una gran recompensa,
el agente debe preferir realizar las acciones que en
el pasado le han resultado eficaces para obtener la
recompensa (explotación). Pero para descubrir esas
acciones el agente tiene que probar aquellas que no ha
seleccionado antes, explotando lo que ya conoce para
obtener una recompensa, pero también explorando
nuevas acciones para obtener una mejor selección
para el futuro. El dilema es que ni la exploración ni la
explotación pueden llevarse a cabo exclusivamente
sin fracasar en la tarea. El agente debe probar una
variedad de acciones y favorecer progresivamente las
que parecen ser mejores 

Este aprendizaje nace a finales del siglo 80

En el aprendizaje por refuerzo, el agente aprende a partir de su propia experiencia

Los elementos básicos que componen un sistema de
aprendizaje por refuerzo son los siguientes:
• El agente que aprende a partir de las iteraciones
con el entorno y persigue un determinado objetivo.
• El entorno que en la práctica es la parte del universo
cuyo estado interesa al diseñar el agente, lo que él
percibe y es afectado por las acciones del agente.
• Una política que define el comportamiento del agente
en un momento dado. También se puede entender
como un mapa que relaciona los estados percibidos
por el agente dentro del entorno con las acciones que
el agente debe realizar en esos estados.
• Una función de recompensa que define el objetivo
en un problema de aprendizaje por refuerzo. Se
trata de un valor numérico que define como es de
buena una acción o estado para el agente.
• Una función de valor que especifica lo que es
«bueno» a largo plazo a diferencia de la función
de recompensa que indica lo que es «bueno» en
un sentido inmediato. A grandes rasgos, el valor
de un estado es la cantidad total de recompensa
que un agente puede esperar acumular en el futuro
partiendo de ese estado.
• Un modelo del entorno que imita el
comportamiento del entorno. Es algo opcional
dentro de los sistemas de aprendizaje por
refuerzo. Dado un estado y una acción, el
modelo puede predecir el siguiente estado y la
recompensa resultante.

Ejemplos de algoritmos clásicos de aprendizaje por refuerzo:
Algoritmos monte carlo
El aprendizaje por diferencia temporal 
SARSA
Q-learning

En la medida que la complejidad en los entornos crece. estos métodos de aprendizaje por refuerzo comienzan a ser iniviables.

Otros paradigmas de aprendizaje:

• Aprendizaje semi-supervisado: es un tipo de
aprendizaje que se encuentra a medio camino entre
el aprendizaje supervisado y el no supervisado. El
aprendizaje semi-supervisado tiene un gran valor
práctico, ya que en muchas ocasiones es difícil
extraer datos que estén etiquetados. Algunos
ejemplos de aplicación son los siguientes: en el
reconocimiento del habla, ya que se necesitaría
mucho tiempo para etiquetar cada enunciado
con su fonema; en el procesamiento del lenguaje
natural como por ejemplo para la construcción de
árboles sintácticos (treebank); en la detección de
spam, ya que conseguir un gran número de correos
etiquetados es tedioso; en sistemas de video
vigilancia a la hora de identificar diferentes objetos
en los frames del video; etcétera. La mayoría de
las estrategias de aprendizaje semi-supervisado
se basan en la inclusión adicional de información
a otro paradigma de aprendizaje. Los principales
escenarios que se dan en el aprendizaje semi-
supervisado son los siguientes [8]:
• Clasificación semi-supervisada: consisten en
el entrenamiento de un clasificador con datos
etiquetados y no etiquetados con el objetivo de
que este nuevo clasificador sea mejor que un
clasificador entrenado solo con datos etiquetados.
• Clustering con restricciones: es una extensión
de los algoritmos de clustering (aprendizaje no
supervisado) en el que los datos de entrenamiento
consisten en instancias no etiquetadas, sin
embargo, existe cierta información sobre los
grupos como, por ejemplo, que ciertas instancias
no pueden estar en el mismo clúster o viceversa con
el objetivo de obtener una mejor agrupación que si
únicamente se emplean los datos no etiquetados.

6Aprendizaje automático |
• Aprendizaje multi-instancia: en el que cada
ejemplo consiste en una bolsa de instancias, en
lugar de una sola instancia.
• Clasificación multi-etiqueta: en la que cada
instancia procesada se asocia no a una clase sino
a un subconjunto de clases.
• Minería de patrones emergentes o descubrimiento
de subgrupos: es una hibridación de aprendizaje
supervisado y no supervisado, concretamente entre
clasificación y minería de asociación, cuyo objetivo
es extraer reglas de interés con respecto a un
atributo objetivo.
• Aprendizaje desbalanceado: es una extensión del
aprendizaje supervisado en el que alguna de las
clases objetivo tiene un número de ejemplos mucho
menor que el resto de las clases.
• Aprendizaje por transferencia: consiste en la
creación de un modelo para una o más tareas de
origen y aplicar este modelo a un problema diferente
pero que guarde cierta relación con el problema o
los problemas de origen.
• Aprendizaje profundo: es un tipo particular de
aprendizaje automático que se basa en gran medida
en los conocimientos sobre el cerebro humano,
la estadística y las matemáticas. El aprendizaje
profundo está inspirado en una evolución de los
sistemas de redes neuronales, que son algoritmos
que imitan el comportamiento de las neuronas y que
permiten aprender a partir de datos. El aprendizaje
profundo va más allá permitiendo representar los
datos como una jerarquía anidada de conceptos de
más complejos a más simples [9].
• Minería de flujo de datos: está relacionado con el
aprendizaje supervisado y con el no supervisado y
consiste en un paradigma de aprendizaje en el que
la entrada es un flujo de datos continuo


				Tema 3

Algoritmos de clasificación para el aprendizaje supervisado.

Aprendizaje automático inductivo:

Arboles de decisión: Trabajan por inducción (de casos particulares llegar al concepto general). Predice el valor de la clase objetivo.

Componentes de un arbol:

Nodo raíz, el cual no tiene enlaces entrantes y tiene
cero o más enlaces salientes.
Nodos intermedios, que tienen exactamente un
enlace entrante y dos o más enlaces salientes.
Cualquier nodo intermedio puede ser un nodo
raíz de un sub-árbol. Cada uno de los nodos no
terminales, el nodo raíz y los nodos intermedios,
contienen las condiciones definidas por los
atributos del conjunto de datos. Estas condiciones
actúan como separadores sobre la existencia o
no de alguna de las características, lo que permite
clasificar los ejemplos y determinar cuáles serán
los nodos sucesores.
 Nodos hoja, o nodos terminales, que tienen un
enlace entrante y ninguno saliente. Cada nodo hoja
está asociado a una etiqueta de clase y representan
los conceptos extraídos de forma automática.


La construcción de un árbol de decisión se puede abordar
de forma recursiva:
1. Partir de un conjunto de ejemplos o de
entrenamiento etiquetado.
2. Seleccionar un atributo o separador del conjunto
de ejemplos capaz de dividir el conjunto de
ejemplos como nodo raíz y crear ramas por cada
valor posible de ese atributo.
3. Repetir el proceso de forma recursiva para cada
rama empleando únicamente las instancias que
llegan a cada rama.
4. Seguir desarrollando el árbol hasta que se llegue a
la clase (o etiqueta), lo que hará que ese nodo se
convierta en nodo hoja.

a la
hora de construir un árbol de decisión, es necesario
tener alguna forma de seleccionar los atributos más
importantes para el proceso de clasificación y el orden
de uso de esos atributos, lo que se denomina criterio
de selección de esos separadores.

Ejemplos de separadores:

Entropia o cantidad de información
Criterio de gini/Indice de Gini

Ejemplos algoritmos para arboles de decisión:
ID3: el separador principal es la entropia, problema: sobreaprendizaje
C4.5: mejoramiento del ID3, incluye un mecanismo de poda que elimina o no desarrolla algunas ramas del arbol de decisión siguiendo algun criterio.
CART (Clasification and Regression Trees): puede utilizarse para problemas de clasificación y de regresión. Este solo introduce particiones binarias. El algoritmo de CART emplea el índice de Gini para seleccionar la mejor partición y un método de poda llamado coste-complejidad


Aprendizaje basado en reglas:

Estos métodos son una extensión de la lógica de primer orden para manejar representaciones relacionales.

Un modelo de clasificación basado en reglas consiste
en un conjunto de reglas si-entonces (if-then). Cada
regla está compuesta por la conjunción de los valores
de los atributos (características) que forman el
antecedente y una etiqueta de clase en el consecuente
de la regla.

Los conjuntos de reglas suelen ser mas sencillos que los árboles de decisión.

El hecho de que en el aprendizaje
basado en reglas permita las reglas superpuestas –
reglas que no tienen por qué abarcar todo el espacio de
instancias– puede dar lugar a conjuntos de reglas más
pequeños. Sin embargo, en este caso se necesitarán
mecanismos de desempate para elegir una regla cuando
más de una cubre el ejemplo por clasificar, y también
clasificaciones por defecto (qué etiqueta elegir cuando
ninguna regla cubre el ejemplo dado.

En la construcción de las reglas solo se amplía un único
nodo sucesor a la vez (a diferencia de los árboles de
decisión), aprendiendo así una regla que cubre parte
de los ejemplos del conjunto de entrenamiento. Una
vez aprendida la regla, se eliminan del conjunto de
entrenamiento todos los ejemplos cubiertos por esa
regla y se repite el procedimiento con los ejemplos
restantes.

Las reglas para validar la calidad de una regla de clasificación son:
• Cobertura de una regla: fracción de instancias que
satisfacen el antecedente de una regla.
• Precisión de una regla: fracción de instancias
que satisfacen tanto el antecedente como el
consecuente de una regla

La extracción de reglas se puede abordar desde dos
perspectivas, métodos directos y métodos indirectos [7]:
• Métodos directos: que consisten en extraer reglas
directamente de los datos. Algunos algoritmos para
la extracción de reglas son:
- CN2: desarrollado por Clark y Niblett en 1989
fue el primer algoritmo de reglas en reconocer
el problema de sobreaprendizaje y ponerle
remedio. Algunas características relevantes de
este algoritmo es su método de pre-poda para
filtrar reglas no significativas o el hecho de poder
manejar múltiples clases para clasificar.
- First-Order Inductive Learner (FOIL): propuesto por
Quinlan en 1990 funciona básicamente como CN2
con la diferencia de que FOIL no evalúa la calidad de
la regla individual, sino que su heurística evalúa la
mejora de una regla con respecto a su antecesora.
Otra innovación de FOIL es que puede emplear
pruebas que calculen relaciones entre múltiples
atributos e incluso introducir nuevas variables en el
cuerpo de la regla.

- Repeated Incremental Pruning to Produce Error
Reduction (RIPPER): desarrollado por Cohen en
1995 fue el primer algoritmo que contrarrestó
eficazmente el sobreaprendizaje. A pesar de que
los algoritmos anteriores poseían mecanismos
para tratar el sobreaprendizaje, se demostraron
ineficaces. La idea subyacente para evitar este
sobreaprendizaje es una fase de postprocesamiento
para la optimización del conjunto de reglas en
el contexto de otras reglas, tanto las aprendidas
previamente como en las posteriores.
• Métodos indirectos: consiste en la extracción de
reglas a partir de otros modelos de clasificación,
como por ejemplo a partir del algoritmo C4.5 de
árboles de decisión o incluso de redes neuronales


SVM y KNN: Es uno de los mejores clasificadores de caja negra (no explicables),
este es un generalizador de un clasificador mas simple llamado clasificador de margen máximo.

MMC
SVC
SVM
Kernel polinomial
Kernel de base radial

Algoritmos de vecinos mas cercanos (KNN).
Estos modelos forman la categoria de aprendizaje basado en instancias.
Este modelo emplea los propios datos de entrenamiento para prededicr una nueva instancia

 n es el número de
atributos y el funcionamiento es el siguiente:
• Se selecciona un valor de k, que será el número de
vecinos más cercanos a una instancia de prueba.
• La nueva instancia se clasifica en función de los k
vecinos más cercanos, calculando la distancia de la
nueva instancia con cada uno de los ejemplos del
conjunto de entrenamiento.
• La nueva instancia se clasifica en función de la
clase mayoritaria de sus vecinos más cercanos.
• En caso de que haya empate en las clases se elige
al azar una de ellas para clasificar el nuevo ejemplo.

Para variables nominales: distancia de Hamming
Para variables numéricas: distancias de minkovsky

Si k es pequeño -> el clasificador es susceptible de sobreaprendizaje

KNN es susceptible al ruido

Si k es grande -> la clasificación de las nuevas instancias pueden ser erroneas

es sensible a valores perdidos.
Métricas y puntuaciones para clasificación:

Precisión: capacidad del clasificador de etiquetar como positiva la instancia negativa
exhaustividad (recall) : mide la capacidad del clasificador de encontrar todas las instancias positivas.
Valor F-1 score: establece un equilibrio entre la precisión y la exhaustividad.




Tema 4
Algoritmos de regresión

Regresión lineal, regresión logística y modelos no lineales.

Regresión lineal: predice valores cuantitativos

Regresión lineal simple: Partimos de una observación X, para predecir una respuesta cuantitativa Y, suponemos que existe una relación lineal entre X y Y, esta se expresa de la siguiente forma:
y = b + b_1 * x_1
	b y b_1 son los coeficientes/ parámetros del modelo. Para calcular su error se utiliza el RSS (Residual sum of squares)





También se le puede agregar un parámetro de error, en dado caso de que exista variaciones en Y

Regresión logística: La diferencia es que, la regresión logistica a diferencia de la regresión lineal, predice si algo pertenece a una clase en lugar de valores continuos.
Este método trabaja con valores discretos como continuos.
La probabilidad esta comprendida entre 0 y 1, siendo 0 la clase negativa y 1 la clase positiva.
Para esto se usa la función sigmoide o logística.

Tanto en la regresión lineal como logistica, los parámetros beta 0 y beta 1 se calculan de los datos de entrenamiento

Para calcular estos parámetros se utiliza el enfoque de máxima verosimilitud

Hints positivos de la regresión logística:

- Pueden extenderse fácilmente a clasificación
multiclase. Esto se conoce como regresión
logística multinomial.
- Los parámetros (coeficientes) aprendidos en
la regresión logística pueden emplearse para
entender las relaciones entre los atributos y la
clase.
- La regresión logística es robusta frente a
espacios de alta dimensionalidad, ya que, no
implica cálculo de densidades o distancias que
son muy costosos.
- La regresión logística es robusta frente a
atributos irrelevantes y frente a atributos
redundantes. Sin embargo, la presencia de estos
atributos en entornos de alta dimensionalidad
puede llevar al sobre aprendizaje.
- Por último, la regresión logística no puede manejar
instancias con valores perdidos, pues como se ha
visto, las probabilidades se calculan mediante la
suma ponderada de todos los atributos.


Modelos no lineales:  Para conseguir una mejora sustancial en los modelos
lineales hay que relajar el supuesto de linealidad
Ejemplos:

Regresión polinomial: Amplía el modelo de regresión lineal añadiendo predictores adicionales elevando los existentes a una potencia, consiguiendo así un ajuste no lineal de los datos:




Epsilon es de igual forma el termino de error, los coeficientes tambien se encuentran con el método de minimos cuadrados.
Comentario: para valores de n muy grandes, la curva toma formas ineficientes para generalización del problema, por lo que se recomienda que sean valores no superiores a 4.
	

 Funciones escalonadas o funciones a trozos: a
diferencia de la regresión polinomial que impone
una estructura global en un modelo no lineal, las
funciones escalonadas dividen el rango de X en
intervalos al que se le ajusta una constante a
cada intervalo. Esto es transformar una variable
continua en una variable categórica ordenada.
Para ello se definen una serie de puntos de corte
con la que, a partir del rango de X, se construyen
K + 1 variables nuevas, donde K es el número de
cortes, estas variables también son conocidas
como variables dummy.
En ese sentido, una vez aplicada la transformación
a los predictores, se emplean los mínimos
cuadrados para ajustar un modelo lineal:




Es válido señalar que, el principal problema de las funciones escalonadas es seleccionar los puntos de corte


Splines de regresión.

Series temporales

Formas de analizarlas:

Representar la serie a analizar en un gráfico temporal
Dividir los datos en entrenamiento y test
Descomponer la serie temporal
Si tiene tendencia: esta s etiene que eliminar, Si tiene estacionalidad, esta se elimina. -> necesarios para el empleo de modelos paramétricos de análisis y predicción de series temporales.
Hacer a la serie no estacionaria estacionaria.
Aplicación de modelos paramétricos.


Metricas y puntuaciones para regresión

MSE(minimun square error)
RSE (Standar residual error): Es una estimación de la desviación estandar del error inherente a los modelos de regresión.
R cuadrada: toma valores entre 0 y 1, mide la proporcion de variabilidad en Y que puede explicarse utilizando X, por lo que los valores cercanos a unos serán mejores que los cercanos a 0



Tema 5
Algoritmos de agrupación


Técnicas de agrupamiento jerárquico.

Clustering o agrupamiento: encontrar grupos en datos -> Organización de un conjunto de instancias en un conjunto de grupos homogeneos

Tipos de clustering:
Exclusivos, no exclusivos y difusos: Parte de la hipotesis de no solapamiento, cada instancia pertenece a un unico cluster (lo cual en general puede que no se cumpla esto) . Para el tipo de agrupaciones en las que una instancia puede pertenecer a mas de un grupo se llaman agrupaciones no exclusivas.
Ejemplos:
agrupamiento borroso (fuzzy clustering): Cada punto pertenece a cada grupo con un grado de pertenencia entre 0 y 1

      -  Completo y parcial: en un clustering completo se
asigna cada punto a un cluster, mientras que en
clustering parcial puede haber instancias que no
pertenezcan a un grupo.


Aglomarativo y divisivo: El clustering aglomerativo parte de la idéa de que cada item (ejemplo) es un grupo y se va contrayendo nuevos soluciones uniendo esos grupos en grupos cada vez más amplios.

Clustering jerarquico:
Es un tipo de agrupamiento formado por una sucesión de clusters anidados, donde cada grupo está incluido en algún grupo de la siguiente partición.
La representación más común de este tipo de clustering se conoce como dendograma.

En el clustering jerárquico la mayoría de los algoritmos
que lo conforman son de tipo aglomerativo, empezando
con los ejemplos de partida como clusters y en cada paso
se fusionan el par de clusters más cercano. El algoritmo
de clustering jerárquico que se emplee debe dictar cómo
ha de interpretarse la matriz de proximidad (es una
matriz de nxn donde el valor de la celda ik representa una
medida de distancia entre el item i y el k) para fusionar
dos o más clusters

Algoritmo de agrupamiento de enlace simple (single-link
algorithm)
• Paso 1: Para construir el algoritmo, el primer paso
consiste en empezar con la agrupación disjunta
implícita, es decir, una agrupación que no contiene
aristas y que coloca cada objeto en un único
cluster. El grafo umbral (un grafo umbral es un
grafo no dirigido y no ponderado de n nodos y sin
bucles) es G (0).
- Paso 1.1: establecemos el valor de k = 1.
• Paso 2: si el número de componentes (subgrafos
conexos) en G(k) es menor que en número
de clusters en esa iteración, entonces cada
componente de G(k) se redefine como cluster.
• Paso 3: si G(k) es un único grafo conexo, se para. Si
no, se aumenta el valor de k y se vuelve al paso 2.


Algoritmo de Jhonson es la siguiente: 
• Se empieza con el clustering disjunto (debe
recordarse que es un enfoque aglomerativo), en
el nivel L(m) = 0, donde m = 0 (m es el número de
secuencia asignado al cluster).
• Se busca la distancia mínima entre dos pares de
clusters empleando la matriz de proximidad:
d[(a), (b)]=minf(){d[(i), (j)]}
donde (a) y (b) son clusters y d[(i), (j)] es la proximidad
entre esos dos clusters. El mínimo se hace sobre
todos los pares de clusters de la agrupación actual.
• Se incrementa el número de secuencia m en 1 y
se combinan los dos clusters (a) y (b) en un único
cluster. Se ajusta el nivel a L(m) = d[(a), (b)]


Técnicas de agrupamiento particional.

El clustering particional es una división del conjunto de datos en grupos no superpuestos, de manera que cada conjunto de datos está exactamente en un subconjunto.

A diferencia del clustering jerárquico, que busca una
jerarquía de grupos anidados, el clustering particional
es una división del conjunto de datos en grupos no
superpuestos, de manera que cada conjunto de datos
está exactamente en un subconjunto.
Formalmente el agrupamiento particional se define
como sigue: dados n patrones representados en un
espacio d-dimensional, determinar una partición de los
patrones en K grupos o clusters tal que los patrones
de un cluster sean más similares entre sí que los
patrones de un cluster diferente. El valor de K puede ser
especificado o no


Para definir siempre un algoritmo de agrupación o de clustering es necesario de definir el “parecido” de un grupo y un criterio de agrupamiento.

Agrupación K-medias:
Define un prototipo en términos de un centroide, que normalmente es la media de un grupo de puntos y suele aplicarse a datos en un espacio continuo de d-dimensiones.
hint: el centroide casi nunca corresponde a un punto de datos real.

La técnica de K-medias es la siguiente (3):
• Se elige los primeros K centroides iniciales, que se
corresponderá con el número de clusters deseados.
El parámetro K viene especificado por el usuario. La
colocación inicial de los centroides en el espacio
suele ser aleatoria.
• A continuación, cada punto se asigna al centroide
más cercano, y cada conjunto de puntos asignados
a un centroide forman un cluster. Para asignar un
punto al centroide más cercano se emplean medidas
de proximidad, como por ejemplo la distancia
euclídea o la similitud del coseno. Si se emplea la
medida de proximidad como la distancia euclídea,
es empleada como función objetivo la suma del
error cuadrático o dispersión. Es decir, se calcula la
distancia euclídea de cada punto al centroide más
cercano y después se calcula la suma de los errores
al cuadrado. El objetivo es minimizar ese error para
seleccionar la ejecución del k-medias adecuada.
Matemáticamente la dispersión se calcula de la
siguiente forma:
SSE= —----
donde ‘dist’ es la distancia euclídea, c_i es el
centroide y x el punto.
• El centroide de cada grupo se va actualizando en
función de los puntos asignados al cluster, es decir,
se vuelven a calcular de nuevo los centroides para
minimizar más el SSE.
• Este proceso se repite hasta que ningún punto
se mueva de cluster. También ocurrirá que los
centroides permanecerán fijos.

grupamiento basado en criterios locales. DBSCAN (5)
Los métodos de clustering basados en densidad
analizan regiones del espacio de alta densidad
separadas por otras de baja densidad. El DBSCAN es
un algoritmo de clustering basado en densidad.
DBSCAN es un enfoque basado en el centro, donde
la densidad se estima para un punto particular en el
conjunto de datos, contando el número de puntos
dentro de un radio específico. Esto lo hace un método
dependiente del radio ya que, si el radio es demasiado
grande, se formará un cluster muy grande, pero si es
muy pequeño, puede que en la densidad solo quepa un
punto. En DBSCAN, se asigna una etiqueta especial a
cada punto:
• Puntos núcleo: son los puntos que se encuentran
en el interior del cluster. Se considera un punto
como punto núcleo si hay al menos un número
mínimo de puntos dentro de una distancia definida
por el radio. El número mínimo de puntos y el radio
son predefinidos por el usuario.
• Puntos límite o frontera: son puntos que se
encuentran dentro del radio de un punto núcleo,
pero su radio de acción no contiene el mínimo
número de puntos definido.
• Puntos de ruido: cualquier punto que no sea ni
punto núcleo ni punto límite.

• Se colocan en el mismo cluster los puntos núcleo
que distan entre sí menos del radio predefinido.
• Del mismo modo también se asignan al cluster
aquellos puntos frontera asociados a cada punto
núcleo. En esta situación será necesario emplear
alguna heurística para resolver empates, ya que
se puede dar el caso de que un punto frontera
pertenezca al entorno de dos núcleos que no estén
en el mismo grupo.
• Los puntos ruido son descartados y quedan fuera
de los clusters.

DBSCAN es tolerante al ruido y permite manejar clusters de formas y tamaños arbitrarios.
Depende fuertemente los valores prefijados del número mínimo de puntos y del radio (casos de alto volumen o dimensionalidad)

Métricas y puntuaciones:

Generalmente se conoce al proceso de clustering como parte del análisis exploratorio de datos.

Las medidas de evaluación de los clusters se dividen en medidas de cohesión que determinan el grado de relación entre los elementos de un cluster y medidas de separación, que determinan lo bien separado que está un cluster de otro. 

Una de las
métricas más populares que combinan la cohesión y
la separación es el coeficiente de silueta (silhouette
coefficient). El coeficiente de silueta se calcula de la
siguiente forma para un punto:
• Se calcula la distancia media del punto i a todos los
demás puntos del cluster. A ese valor se le llama
a_i.
• Se calcula la distancia media de i a todos los puntos
de cada cluster al que no pertenece y se busca la
distancia media mínima con respecto a todos los
clusters indicados. A ese valor se le llama b_i.
• Por lo que el coeficiente de silueta para i viene dado
por la siguiente fórmula:
s_i= ((b_i-a_i)) /(max▒(a_i,b_i))
El valor del coeficiente de silueta varía entre -1 y 1, y es
deseable un coeficiente de silueta lo más cercano a 1.
El coeficiente de silueta global se obtiene calculando la
media de todos los coeficientes de silueta de los puntos.




Tema 6
Técnicas de reglas de asociación.


Las reglas de asociación se emplean en la busqueda de patrones frecuentes en base de datos. Esto sigue correspondiendo al aprendizaje no supervisado

Definición:

Dado un conjunto de ejemplos o transacciones sin etiquetar, donde cada transacción es un conjunto de items, una regla de asociación es una
expresión de la forma X Y, donde X e Y son un conjunto
de ítems (itemset). X Y se interpreta como “si X, entonces
Y”, lo que significa que las transacciones que contienen X
tienden a contener también Y 

Cada artículo del supermercado son los ítems y el
conjunto de la cesta de la compra son las transacciones
(se puede definir una transacción como un subconjunto
de ítems). Un ejemplo de regla sería:
Si queso y nata Galletas

El primer paso para aplicar las reglas de asociación
es determinar en la base de datos qué son los ítems y
cuáles son las transacciones:
• Item: es una tupla atributo valor, ya que una base
de datos está compuesta de atributos (columnas) y
cada registro de la base de datos contiene un valor
para cada atributo. Un ítem también puede tratarse
como una variable binaria, cuyo valor sería 1 si ese
ítem se encuentra en la transacción, o 0 en caso
contrario.
• Itemset: es una colección de 0 o más ítems. Si un
itemset contiene k ítems, es denominado k-itemset.
Un itemset puede estar vacío. La frecuencia
de aparición de un itemset es el número de
transacciones que lo contienen. Esto es también se
conoce como frecuencia o conteo del soporte.
• Transacción: definen casos particulares de
relaciones entre ítems, es decir, una transacción
ti es un subconjunto de ítems seleccionados del
conjunto total de ítems.



Las reglas de asociación son una expresión de
implicación (X Y) donde X e Y son conjuntos
disjuntos, es decir, X Y= Φ.La solidez de una regla
de asociación se puede medir en términos de
su soporte y confianza. El soporte (medida de
importancia) determina la frecuencia con la que una
regla es aplicable al conjunto de datos y la confianza
determina la frecuencia con la que los elementos de
Y aparecen en transacciones que contienen X

El soporte toma valores entre el rango [0.0,1.0], donde un
soporte igual a 1 significa que la regla aparece en todas
las transacciones de la base de datos, y 0 que no aparece
en ninguna de las transacciones.

 La confianza mide la fiabilidad de la inferencia
realizada por una regla, pero en reglas de asociación
esta inferencia no implica necesariamente causalidad.


Métodos para la extracción de reglas:

1. Encontrar todos los conjuntos de itemsets
frecuentes.
2. Generar reglas de asociación fuertes a partir de
itemsets frecuentes. Por definición tienen que
satisfacer un soporte y una confianza mínimos. El
umbral para el soporte y confianza está predefinido
por el usuario.

lgunos
métodos para la extracción de itemsets frecuentes.
• Algoritmo Apriori [3]
El algoritmo Apriori es un algoritmo propuesto por
R. Agrawal y R. Srikant en 1994 para la minería
de itemsets frecuentes para reglas de asociación
booleanas [4].
El algoritmo Apriori emplea un enfoque iterativo
conocido como búsqueda por niveles (level-
wise) donde se emplea k-itemsets para explorar
(K+1)-itemsets. El funcionamiento de Apriori es el
siguiente:
1. Para k=1 se generan un conjunto de itemsets
frecuentes que satisfacen el soporte mínimo.
A ese conjunto resultante se le denomina L1
(itemsets frecuentes de longitud 1).
2. A continuación, se emplea L1 para encontrar
L2 (conjunto de itemsets de longitud 2) y así
sucesivamente, recorriendo toda la base de
datos.
3. Se calcula el soporte de cada candidato.
4. Se eliminan los candidatos infrecuentes

El hecho de que se necesite recorrer la base de
datos entera en búsqueda de itemsets frecuentes
es tremendamente ineficiente. Para reducir el
espacio de búsqueda se emplea la propiedad
Apriori que quiere decir que todos los subconjuntos
no vacíos de un itemset frecuente son también
frecuentes.

Aplicando la propiedad anti-monotona en el algoritmo Apriori
sufre la siguiente modificación:
- Generar un nuevo conjunto de itemsets
candidatos C(k + 1) a partir de Lk combinando los
itemsets que solo se diferencian en el último ítem,
siguiendo la propiedad anti-monótona.
- Se calcula el soporte de cada candidato.
- Se eliminan los candidatos infrecuentes y los
frecuentes se añaden a L(k+1).
- Se incrementa k + 1.

El algoritmo Apriori es dependiente del umbral de
mínimo conteo del soport.
También se ve afectado por el número
de ítems; cuantos más ítems, mayor será el coste
computacional, porque el algoritmo Apriori recorre
varias veces la base de datos.

Método FP-Tree:
Han Pei u Yin han propuesto un modelo
de generación de itemsets frecuentes basado
en árbol de patrones frecuentes (FP-Tree).
El patron es el siguiente:

Se parte de una base de datos de transacciones.
2. Se recorre la base de datos una vez y se
obtienen los ítems frecuentes y sus soportes.
Se ordenan los ítems en orden descendente en
función de su soporte (L).
3. Se crea el nodo raíz del FP-Tree T y se etiqueta
como “nulo”. Para cada transacción de la base
de datos de transacciones se hace lo siguiente:
A. Se seleccionan y se ordenan en función de
L los ítems frecuentes de las transacciones.
Se define la lista ordenada como [p|P] donde
p es el primer elemento y P la lista restante.
Hay que recordar que cada transacción es un
subconjunto de ítems.
B. Para insertar un nodo en el árbol se procede
de la siguiente forma: si T tiene un hijo N tal
que el ítem de N = p, entonces se incrementa
N en 1, si no, se crea el nodo N con el primer
elemento de P, es decir, p, y se le asigna el
valor 1 y se pasa al siguiente elemento de la
lista P. Si P no está vacío se repite el mismo
proceso recursivamente.







Una vez construido el FP-tree se emplea el algoritmo
FP-growth [6] para la extracción de patrones frecuentes
empleando el FP-tree. El FP-growth emplea la técnica
divide y vencerás para extraer los itemsets frecuentes. El
proceso es el siguiente:
1. Se recorre el FP-tree y para cada ítem se genera
una pequeña base de patrones que contiene la
etiqueta de todos los nodos que llevan a ese ítem
junto con sus frecuencias.
2. A continuación, por cada base de patrones se
construye un FP-tree condicional y se hace tomando
el conjunto de items que es común en todos los
caminos de la base de patrones de cada ítem
calculando el soporte de los caminos en común.
3. Para finalizar, a partir de la tabla de patrones
condicionales y los FP-tree condicionales de
cada ítem se construyen los itemsets frecuentes
combinando los elementos del FP-tree condicional
con el ítem correspondiente a partir del cual se han
construido esos árboles condicionales.


Piatesky-Shapiro [8] propuso tres propiedades que toda
medida M debería tener para considerarse una buena
medida:
• Propiedad 1: M = 0 si X e Y son estadísticamente
independientes, esto es, P(XY) = P(X)P(Y).
• Propiedad 2: M es monótonamente creciente con
P(XY) cuando P(X) y P(Y) son iguales.
• Propiedad 3: M es monótonamente decreciente
con P(X) (o P(Y)) cuando P(XY) y P(Y) (o P(X)) son
iguale

7Técnicas de reglas de asociación |
La propiedad 1 quiere decir que una regla de asociación
que se da por casualidad, es decir, no tiene interés. La
propiedad 2 establece que cuanto mayor sea el soporte
de XY, mayor será el interés cuando el soporte de X y el
de Y sean fijos. Y, por último, el principio 3 establece que
si los soportes de XY e Y (o X) son fijos, cuanto menor
sea el soporte de X (o Y), más interesante será la regla.

En el caso del soporte y la confianza solo cumplen la
segunda propiedad. Existen otras medidas que cumplen
más propiedades como es el caso de la medida lift o
interés que se define como: I= (s(XY))/(S(X)S(Y)), al
tener en cuenta el soporte del consecuente es capaz
de comprobar la dependencia estadística. En el caso
de la medida de lift, cumple la propiedad 2 y 3, y la 1
la cumple si se normaliza, ya que en el caso de lift la
independencia estadística se alcanza con el valor 1 en
lugar del 0. Otras medidas de interés son Yule’s Q, que
cumple las tres propiedades, la convicción (solo cumple
la propiedad 2), Yule’s Y (cumple las tres propiedades) y
un largo etcétera


Tema 7
Técnicas de clasificación avanzada

Métodos de aprendizaje automático conocidos como ensambles
Especialmente el bagging/bootstrap agregation, el random forest y el boosting y su variación llamada AdaBoost.

Estas técnicas consisten en la agregación de clasificadores en un único modelo que se conocen como ensambles.
Los ensambles construyen un conjunto de clasificadores básicos a partir de datos de entrenamiento y la predicción se lleva a cabo mediante votación de las predicciones hechas por cada clasificador que compone el ensamble.

Para los arboles de decisión y el tema de la mucha variabilidad de la varianza. para reducir la varianza y aumentar la precisión del conjunto de test de un método de aprendizaje es a partir de muchos conjuntos de entrenamiento de una misma población.

El problema de este enfoque es que en la práctica
no se dispone de una población lo suficientemente
grande para la obtención de múltiples conjuntos de
entrenamiento.

Algoritmo de Bagging.

fue propuesto por Breiman en 1996 [3] y es un
procedimiento de propósito general para reducir la
varianza de un método de aprendizaje.

El bagging es especialmente útil en los árboles de decisión. En concreto, el proceso descrito en el anterior párrafo es para los árboles de regresión, en el que cada árbol individual se modela con cada una de las muestras bootstraps.

El bagging se puede extender a problemas de clasificación. En lugar de promediar los resultados de los distintos modelos, se realiza una votación, y la clase predicha será la mayoritaria.

Uno de los problemas del baggin es la interpretabilidad
Ya que al aplicar una cantidad grande de ellos es complicado determinar el procedimiento



Clasificador Random Forest

Construye un conjunto de árboles de decisión decorrelados.
Emplea tambien muestras bootstrap para entrenar árboles de decisión a diferencia de una cosa: en cada muestra se selecciona al azar un subconjunto de características o atributos.
 El número
de atributos que se suele emplear es la raíz cuadrada del
total de características de entrada

Dado un conjunto de entrenamiento D que constan de i
instancias y n atributos, el proceso de construcción de un
Random Forest se puede resumir de la siguiente forma [2]:
1. Construir la muestra boostrap D i del conjunto de
forma aleatoria mediante muestreo con reemplazo.
2. Usar Di para entrenar un árbol de decisión T i de la
siguiente forma: En cada nodo interno del árbol
T i seleccionar aleatoriamente un conjunto de n
atributos y elegir de esos n atributos el que muestre
la máxima reducción de la medida de impureza
empleada para la división. Repetir el proceso hasta
completar el árbol.

Una de las caracteristicas más importantes de los random forest es la baja correlación entre el modelo y las predicciones, gracias a la selección aleatoria de los atributos.

Los Random Forest son capaces de reducir la varianza
de los árboles sin perjurio alguno de su bajo sesgo
gracias al muestreo boostrap y al conjunto de árboles
no correlacionados. Esto lo hace robusto frente al
sobreaprendizaje.

 un
número muy grande de n dará lugar a modelos similares
a los de bagging. Como se ha visto, las sugerencias
más comunes en la literatura es emplear √n atributos
o incluso log 2 n + 1


Boosting para arboles de decisión


lgunas
características diferenciadoras de boosting son las
siguientes [1]:
• Boosting funciona de forma similar al bagging con
la diferencia de que los modelos se generan de
forma secuencial, ya que cada modelo emplea la
información de los anteriores e intenta corregir los
errores del modelo previo.
• En boosting, a diferencia del bagging, los árboles
crecen de forma secuencial. Cada árbol se
desarrolla empleando la información de los árboles
desarrollados anteriormente.
• La técnica de boosting no implica un muestreo
bootstrap, sino que cada árbol se ajusta a una
versión modificada del conjunto de datos original

• El enfoque boosting empleado para regresión
ajusta los árboles de decisión empleando los
residuos (diferencia entre lo observado y lo
predicho) en lugar del resultado Y. Estos residuos
se van actualizando, lo que hace que se vaya
mejorando el modelo lentamente en las áreas que
funciona peor.
• En el caso de clasificación el enfoque es distinto.
En el muestreo se ponderan las muestras para
que el aprendizaje se focalice en los ejemplos
más difíciles de clasificar, y a la hora de tomar la
decisión consensuada, en lugar de combinar los
clasificadores con el mismo peso en el voto, se
emplea también el voto ponderado

Las técnicas de boosting han ido mejorando a lo largo
de los años y se han añadido diversas variaciones a la
principal de boosting. Alguna de las variaciones más
populares son Adaptative Boosting (AdaBoost), Gradient
Boosting y Extreme Gradient Boosting (XGBoost). A
continuación, se profundizará en el método AdaBoost

- Como apunte adicional, si alguna ronda
intermedia produce un porcentaje de error
superior al 50 %, los pesos vuelven a sus
valores originales y se repite el procedimiento
de muestreo.











Tema 8
Modelos gráficos probabilístico

El razonamiento probabilístico es otro tipo de inteligencia artificial. Este permite modelar entornos con incertidumbre

Modelos probabilísticos.

Es un enfoque de tipo declarativo. La propiedad clave de este tipo de modelos es la separación entre razonamiento y conocimiento.
Para obtener conclusiones significativas, hay que razonar no solo sobre lo que es posible, si no también sobre lo que es probable.
Judea Pearl sentó las bases del razonamiento probabilístico.

existen modelos que proporcionan
mecanismos para tratar con estructuras complejas
y describirlas de forma compacta, lo que permite
construirlas y utilizarlas eficazmente. Estos modelos se
denominan modelos gráficos probabilísticos.

Los modelos gráficos probabilisticos utilizan una representación basada en gráfos como base para codificar de forma compacta una distribución compleja en un espacio de alta dimension. Existen dos familias de representaciones basadas en grafos de distribución:
Redes bayesianas
- Redes de Markov

Redes bayesianas
Estos modelos emplean representaciones gráficas en las que los nodos del grado corresponden a variables aleatorias y las aristas entre los nodos expresan relaciones probabilísticas.

Las redes bayesianas son grafos aciclicos dirigidos (DAG)

Se modelan las relaciones por nodos padres e hijos, para nodos “de nietos hacia adelante o abuelos” se les llama por ancestros y descendientes segun a quien se haga referencia.

Propiedad local de Markov:
un nodo de una red bayesiana es condicionalmente
independiente de sus no descendientes si sus padres
son conocidos. 








Variables ocultas:

En las redes bayesianas típicamente hay dos tipos
de variables: las observadas y las no observadas (que
son las que se infieren). Si se aborda en el contexto de
clasificación, las variables observadas harían referencia
al conjunto de atributos, y las no observadas a la salida
que debe inferirse.
En las redes bayesianas existen otro tipo de variables
no observadas a parte de la que hay que inferir,
estas variables se llaman ocultas y afectan a las
probabilidades de los atributos y las etiquetas de clase.
El uso de estas variables mejora la capacidad de la red
para representar las relaciones de probabilidad entre
las características y las clases


Existen algunas técnicas computacionales para realizar
eficientemente inferencias en redes bayesianas: (plantilla
multimedia 12)
• Eliminación de variables: que consiste en la
descomposición de la probabilidad, que depende
de las variables ocultas en el producto de varios
factores de solo un número pequeño de variables
ocultas. Con esto se consigue una reducción de la
complejidad, únicamente manipulando de forma
algebraica la operación.
• Modelos de inferencia aproximada como
el Markov Chain Monte Carlo (MCMC): que
proporcionan estimaciones de la probabilidad en
lugar de la inferencia exacta

Características de las redes bayesianas:
• Las redes bayesianas (3) proporcionan un
potente marco de razonamiento probabilístico,
ya que además de ser capaces de representar
las relaciones de probabilidad entre los atributos
y la etiqueta, también son capaces de manejar
variables ocultas.
• Las redes bayesianas son robustas frente a
atributos fuertemente correlados o incluso
redundantes.
• Las redes bayesianas también son robustas
ante la presencia de ruido en los datos ya que
puede tratar esos nodos como no observados y
marginarlos.
• La estructura de la red bayesiana suele requerir
para su construcción el conocimiento de expertos
en el dominio del problema.
• Debido a la capacidad de representar relaciones
complejas, las redes bayesianas son susceptibles
al sobreaprendizaje.
• Como se ha en el apartado anterior, cuando la
complejidad computacional de inferencia exacta
mediante redes bayesianas es muy alta, se suelen
emplear técnicas aproximadas como el MCMC.


Otros modelos gráficos probabilísticos.
Los modelos ocultos de markov se definen como la base formal para elaborar modelos probabilisticos de problemas de etiquetado de secuencias lineales.

Modelos ocultos de markov:

Se caracteriza por lo
siguiente:
• El número de estados del modelo N, denotando
cada estado individual como S = (S_1, S_n), y el
estado en el instante t como q_t.
• Los símbolos de observación M, que son la salida
del sistema que se está modelando. Cada símbolo
individual se denota como V = (V_1, V_M)
• La distribución de probabilidad para la transición
entre los estados.
a_ij=P[q_(t+1) =S_j -| q_t=S_i], donde 1≤i, j≤N
• La distribución de probabilidad del símbolo de
observación en el estado j.
b_j (k)=P [v_k en t-| q_t=S_j], donde 1≤i, j≤N y 1≤k≤M
• La distribución del estado inicial:
    π_i=P [q_1=S_i], donde 1≤i≤N

    Las características anteriores se pueden emplear como
    generador para obtener una secuencia de observaciones
    O = O_1, … O_t de la siguiente forma:
    1. Seleccionar un estado inicial q_1 = S_i de acuerdo
    con la distribución del estado inicial π.
    2. Marcar el instante t = 1.
    3. Elegir la observación O_t = V_k según la distribución
    de probabilidad de los símbolos en el estado S_i.
    4. Pasar a un nuevo estado q_(t+1) = S_j empleando la
    distribución de probabilidad para la transición entre
    los estados.
    5. Aumentar el valor de t y volver al paso 3, en el caso
    de que t no sea menor que T, en caso contrario
    terminar el proceso.



    -------------16/02/2026-----------------------//////////////////////////////////////////////////////////////////


    Tema 9:
    Redes neuronales



    Aprendizaje automático con redes neuronales artificiales.

    Perceptrón multicapa:

    Las redes neuronales son potentes modelos de clasificación capaces de aprender límites de decisión complejos y no lineales a partir de los datos.

    Historia:
    El neuropsicólogo Donald O. Hebb en 1948
    estableció las bases del aprendizaje mediante
    neuronas con la famosa regla de Hebb.

Perceptron:
Es un tipo básico de red neuronal que está formado por nodos de entrada, empleados para representar los atributos de entrada, y un nodo de salida, para representar la salida del modelo.

El nodo de salida es una función matemática
que calcula la suma ponderada de las entradas,
añade un factor de sesgo a la suma y para
finalizar, examina el signo del resultado para
producir la salida. Esta función que examina el
signo se denomina función de activación.

El perceptrón multicapa o red neuronal multicapa
generaliza el concepto básico de perceptrón con
una arquitectura más complejas de nodos que son
capaces de aprender límites de decisión no lineales

El perceptrón multicapa está formado por una capa
de entrada, empleada para representar los atributos
de entrada. Los atributos numéricos o binarios se
suelen representar mediante un único nodo, mientras
que los categóricos son representados por un nodo
diferente para cada valor.

Las entradas se introducen en las capas
intermedias denominadas capas ocultas, que
están formadas por unidades de procesamiento
llamadas nodos ocultos. Cada uno de los nodos
ocultos opera sobre los valores recibidos de la
capa de entrada o de los nodos ocultos de la capa
anterior, y produce un valor de activación que se
pasa a la capa siguiente.
La última capa, corresponde a la capa de salida y
procesa los valores de la capa oculta anterior para
producir las predicciones. En clasificación binaria la
capa de salida tiene un único nodo que representa
la etiqueta de clase.
Este tipo de redes también se denomina
feedforward






























Donde w k es el peso asociado al i-ésimo enlace
después de la k-esima iteración. El valor α es
la tasa de aprendizaje cuyo valor está entre 0
y 1, y se emplea para controlar la cantidad de
ajuste que se hace en cada iteración. Si el valor
de λ es muy bajo aprende muy lentamente y
si es muy alto no es capaz de generalizar. Y x ij
es el valor del j-ésimo atributo del ejemplo de
entrenamiento xi.

6. Se actualiza el valor de k. k = k +1
7. Se vuelve al paso cuatro o se finaliza si la media
entre la diferencia del valor de la salida real y el
predicho es menor que un umbral.
El principal problema del perceptrón es que no
puede encontrar una solución si las clases no
son linealmente separables.
Una de las diferencias principales entre el
perceptrón simple y el multicapa es que este
último puede resolver problemas que no son
linealmente separables, y esto es gracias
a las capas ocultas. Estos nodos ocultos
pueden considerarse como el aprendizaje de
características para distinguir entre las clases
de salida. Los perceptrones multicapa aprenden
una jerarquía de características a diferentes
niveles de abstracción que finalmente se
combinan en los nodos de salida para hacer las
predicciones [3].
A lo largo de esta sección se ha descrito el
proceso de aprendizaje de un perceptrón para
problemas de clasificación, pero las redes
neuronales también se pueden emplear para
problemas de regresión.

El principal problema del perceptrón es que no
puede encontrar una solución si las clases no
son linealmente separables.


Una de las diferencias principales entre el
perceptrón simple y el multicapa es que este
último puede resolver problemas que no son
linealmente separables, y esto es gracias
a las capas ocultas.














Para abordar esta problemática en el
año 1986 se desarrolló una técnica conocida como
backpropagation [2] que propaga las derivadas
parciales hacía atrás, es decir, desde la capa de
salida hasta las capas ocultas.

• Backpropagation
La técnica de backpropagation pretende
minimizar la función de coste ajustando los pesos
y los sesgos de la red. Y ese nivel de ajuste viene
determinado por el descenso del gradiente que
involucra el coste con respecto a los parámetros.
El funcionamiento de una red neuronal de
tipo feedforward empleando la técnica de
retropropagación se puede describir de la siguiente
forma [4]:
1. Se inicializan los pesos y el sesgo de forma
aleatoria, normalmente siguiendo una
distribución normal.
2. El segundo paso consiste en propagar hacia
adelante. Primero cada atributo de entrada
pasa por la capa de entrada sin sufrir alteración
alguna. A continuación, se calcula la entrada de
la capa oculta empleando la siguiente ecuación:

z i ,k= wT xij + b


Backpropagation: el error se propaga hacia
atrás actualizando los pesos y los sesgos
para reflejar el error de la predicción de la red.
Para la capa de salida el error se calcula con la
función de coste y se retropropaga hacia atrás
empleando el descenso del gradiente. Mediante
la regla de la cadena se pueden representar las
derivadas parciales con respecto a w I
ij de la
siguiente forma [3]:
La ecuación puede simplificarse de la siguiente
manera:
Por tanto, para calcular las derivadas parciales
solo se necesita determinar δi
l. La resolución
de esta fórmula cambiará dependiendo de la
función de pérdida empleada. Por lo que yendo
hacia atrás desde la capa de salida L hasta
las capas ocultas aplicando recursivamente la
ecuación anterior para cada nodo oculto para
calcular las derivadas parciales de la función de
pérdida con respecto a los pesos wI
ij y el sesgo
b i , se consigue minimizar el error.
4. Condición de finalización: existen varias
condiciones de finalización:
A. Que los parámetros converjan.
B. Que se alcance el número máximo de épocas
(número de ciclos de ejecución de la red
neuronal).
C. Que el porcentaje de ejemplos mal
clasificados esté por debajo de un umbral.




• Funciones de activación
La función de activación es una de las partes más
importantes de las redes neuronales ya que define
la salida de la red neuronal. Y no solo de la neurona
de la última capa, sino también de las neuronas
de las capas ocultas. El objetivo de la función de
activación es asignar valores entre 0 y 1, o -1 y 1,
etcétera, dependiendo del tipo de función.
La salida de la función de activación hacia la
siguiente capa de la red se denomina propagación
hacia adelante.


6Redes neuronales |
Existen diferentes tipos de funciones de activación
y básicamente se dividen en dos tipos:
- Funciones de activación lineales: cuya salida es
una línea recta lo que implica que el resultado no
estará acotado a ningún rango. La fórmula es la
siguiente:
Donde b es el sesgo.
- Funciones de activación no lineales: son las más
usadas. La no linealidad de estas funciones facilita
que el modelo se adapte a una gran variedad
de datos. Algunas funciones de activación no
lineales son las siguientes:
» Función sigmoidal:
Funcion de tangente hiperbólica
Función de ReLu (Rectified Linear Unit)

Redes Feedforward
Tema 10:
Aprendizaje profundo


Redes feedforward profundas:
El uso de capas ocultas en las redes neuronales se basa en la afirmación de que las características mas complejas de alto nivel pueden constituirse combinando caracteristicas más simples de nivel inferior.
Generalmente, cuanto mayor sea el número de capas ocultas, mayor será la jerarquía de características aprendidas por la red.

Las redes profundas de tipo feedforward, o
perceptrones multicapa, son los modelos de
aprendizaje profundo por excelencia.


Y cuando las redes de tipo feedforward se amplían para incluir conexión de retroalimentación se denominan redes neuronales recurrentes.

El hecho de que
se denominen capas ocultas es porque la salida de
esta no es la solución deseada. La dimensión de
las capas ocultas determina el tamaño del modelo.

se han experimentado pequeños
cambios a nivel de algoritmo que han mejorado el
rendimiento de las redes tipo feedforward, como,
por ejemplo:
- El cambio de la función de coste del error
cuadrático medio a la familia de funciones de
pérdida de entropía cruzada mejoró el rendimiento
de los modelos con funciones sigmoidales o de
tipo softmax en la capa de salida.
- El empleo en las capas ocultas de la función de
activación Rectified Linear Unit (ReLU) en lugar
de la función sigmoidal mejoró en gran medida el
rendimiento de la red.

Redes neuronales convolucionales y modelos de secuencia
Estas son un
tipo especializado de red neuronal para procesar datos
con una topología conocida, como las imágenes. El
nombre de red convolucional viene dado porque implica
una operación matemática llamada convolución


Estas son un
tipo especializado de red neuronal para procesar datos
con una topología conocida, como las imágenes. El
nombre de red convolucional viene dado porque implica
una operación matemática llamada convolución


• Pooling
La función de pooling o agrupación modifica la
salida de la capa. Esta función sustituye la salida
de la red en un lugar determinado por un resumen
estadístico de las salidas cercanas, es decir,
reduce el tamaño de los mapas de características
utilizando alguna función para resumir las
subregiones.

Existen varias funciones de pooling,
como el max pooling, que extrae la salida máxima
de una región del mapa de características. Otras
funciones de pooling famosas son average of
a rectangular neighborhood, la norma L2 de un
vecino rectangular, o la media ponderada basada
en la distancia desde el píxel central 


Capa de clasificación:
El funcionamiento es el siguiente: se aplana el
mapa de salida en un vector que se emplea para
alimentar a estas capas totalmente conectadas,
se propaga el resultado hacia adelante y se
aplica el backpropagation en cada iteración de
entrenamiento.


		Modulo 9
Arquitecturas y sistemas para uso intensivo de datos

Los requisitos principales para los sistemas serán fiabilidad, adaptabilidad (escabilidad) y mantenibilidad.

Gartner (2000) señaló una necesidad de crecimiento en volumen y variedad y velocidad

Las herramientas que se fueron creando fueron como por ejemplo: sistemas de log como kafka - Gestión de colas de mensajes con garantias de durabilidad similar a las bases de datos.
Las tres caracteristicas son:

• Fiabilidad/confiablilidad: capacidad de un sistema para continuar
funcionando correctamente a pesar de posibles
defectos.
incluye que la aplicación realice la acción que espera el usuario en un tiempo determinado bajo unas condiciones de Carga determinadas¨
El sistema debe de tener un mecanismo de autorización o seguridad para que determinadas acciones no puedan ser llevadas a cabo por personal sin autorización.
Se suele esperar que el sistema siga funcionando correctamente
incluso cuando el usuario no sigue el camino diseñado
No comete errores. Estos sistemas se etiquetan como
resilientes o tolerantes a fallos.


• Adaptabilidad / Escalabilidad: capacidad de un
sistema de hacer frente a una mayor demanda, bien
en términos de tráfico, de volumen de datos o de
complejidad.
cada sistema deberá describir sus parámetros de carga, es decir, aquellos aspectos relevantes para su sistema. Una vez elegidos los parámetros de carga del sistema es
necesario conocer los valores de los mismos: número de
peticiones atendidas por segundo, tiempo de respuesta
ante una petición, tiempo de procesamiento, etc. Estos
valores constituyen el rendimiento del sistema y es
interesante conocer la respuesta de la aplicación ante
aumentos de carga, así como las necesidades de recursos
para mantener el rendimiento ante esos aumentos.
Generalmente los parámetros de carga se utilizan distribución de valores.
Estos suelen recogerse en gráficos de dispersión o en histogramas con indicadores de percentil.
Estos indicadores son especialmente útiles porque
muestran los valores representativos del rendimiento
del sistema (valor más frecuente) o casos extremos
(percentiles altos, 95, 99, 99.9 %)

Tipos de escalabilidades:
• Escalado vertical (aumentar el potencial de las
máquinas existentes).
• Escalado horizontal (distribuir la carga entre más
máquinas)



• Mantenibilidad: capacidad de un sistema para
continuar evolucionando por aquellos que
empezaron el desarrollo o por personas diferentes
de manera productiva.

 la adaptación del sistema a nuevos entornos, existen tres principios de mantenibilidad:

1. Operabilidad: cualidad de que un sistema pueda
ser mantenido en ejecución sin problemas.
2. Simplicidad: cualidad de que un sistema sea
fácilmente comprensible por nuevos ingenieros.
3. Evolucionabilidad: cualidad de que un sistema sea
fácilmente extensible o que su comportamiento
pueda ser modificado.

Es común en la gestión de sistemas que exista un
equipo dedicado a que el software siga en ejecución
de forma adecuada en producción. 

la configurabilidad
del sistema, facilitando un comportamiento por defecto,
pero dando la posibilidad que éste sea sobreescrito
cuando sea necesario. Eliminar dependencias con
valores estáticos o acciones pensando en una máquina
concreta.

el 75 % del coste total de propiedad del
software está relacionado con el mantenimiento






HINTS: Ingenieria de caos, la verificación de nueva funcionalidad de
forma acotada como blue-green deployment o canary
release, amplificación de latencia de cola, Behaviour Driven Development (BDD), refactoring.

Tipos de fallos:
Software
Hardware
Humanos

**Simplicity is a prerequisite for reliability. - Edsger W. Dijkstra** -> La sencillez de un sistema no implica que el conjunto de funcionalidades que ofrezca el mismo sea pobre, sino que el sistema solo tenga la complejidad inherente al problema y no sea la implementación de la solución la que añada complejidad al sistema


PARAMETROS DE RENDIMIENTO.







Tema 2: Modelado de datos


Modelos de datos:
Las abstracciones son una de las herramientas más importantes a la hora de luchar contra la complejidad de un sistema.

Modelo relacional:

Bases de datos jerarquicas: La información se almacena en una estructura de árbol, donde un nodo padre puede tener varios hijos. Posiblemente, la versión mas conocida es la IMS (1968), El IMS utiliza el lenguaje de consultas DL/1 y es posible
gracias al modelo jerárquico.
cada registro tiene una clave de secuencia jerárquica (HSK, por sus
siglas en inglés). Esta clave se calcula concatenando
las claves de los ancestros a la clave del registro actual,
permitiendo que estén ordenados en profundidad.

El IMS ofrecía soporte para cuatro formatos de
almacenamiento diferentes. Los registros raíz pueden
ser almacenados secuencialmente, indexados
mediante un árbol B usando la clave del registro, o
en una tabla hash mediante la clave del registro. Los
registros descendientes pueden ser encontrados
bien colocados físicamente en secuencia o utilizando
diferentes formas de punteros.



1. Obliga a que el modelado de una solución incurra
en redundancia de datos. Las relaciones obligan a
que la información en los hijos deba ser repetida
para permitir representar esa misma información
con otro nodo padre. Esta circunstancia abre la
puerta a problemas de inconsistencia de datos, por
ejemplo, si solo se actualizan ciertos registros de
los registros duplicados.

2. Un nodo hijo solo puede existir si existe el padre.
En una estructura de árbol se está obligado a que
una entidad esté relacionada con otra para existir.



Bases de datos de red

En 1969 el comité committee on data systems
languages (CODASYL) liberó una especificación
para un nuevo modelo de datos de red. Este modelo
organizaba los registros utilizando claves en forma de
red, en lugar de en árbol.


Un registro de tipo propietario tiene una relación con
registro de tipo hijo mediante un arco con nombre
que en Codasyl se llamaba set. En Codasyl, existe una
relación 1-n entre las instancias de tipo propietario y las
instancias de tipo hijo. Una base de datos Codasyl es
aquella que tiene instancias set e instancias registro
con al menos un punto de entrada (un registro que no
es hijo de ninguno de los otros registros).
Esta nueva base de datos resolvía muchas de las
restricciones de un modelo jerárquico, pero seguía
siendo difícil modelar ciertas situaciones. Por ejemplo,
una de las limitaciones de este tipo de bases de datos
es que los arcos o sets, solo podían establecerse entre
dos registros por lo que representar relaciones entre tres
elementos obligaba a modelos poco naturales.

el modelo es
considerablemente más complejo que uno jerárquico,


Modelo relacional:

En 1970, Ted Codd propuso el modelo relacional. Su
motivación radicaba en el gran tiempo de dedicación
que se empleaban en tareas de mantenimiento al utilizar
sistemas IMS cuando había cambios físicos o lógicos.
Su propuesta se basaba en tres aspectos:
1. Almacenar la información en estructuras de datos
sencillas (tablas).
2. Acceso a un conjunto de datos mediante un
lenguaje de modelado de alto nivel.
3. No debe ser necesario una propuesta de
almacenamiento físico.

A mitad de los 70, nacieron dos lenguajes
de consulta para el modelo relacional, SQL y QUEL
como versiones mucho más sencillas y amigables de la
propuesta inicial de Ted Codd. A raíz del éxito de DB/2
IBM acabó declarando ganador al modelo relacional y
estableciendo SQL como el lenguaje estándar.

ambién durante la década de los 70 surgió el modelo
entidad-relación y a finales el semántico. Durante la
década de los 80 se realizaron ampliaciones al modelo
relacional y a finales y principios de los 90 nuevos
modelos como el orientado a objetos y objeto-relacional
fueron creados.


Modelo documental (NoSQL).

tienen que ser pequeñas las estructuras.

Patron subconjunto


Una de las ventajas que proporcionan aquellas bases de
datos con un modelo de documentos (especificado en
JSON) es la reducción de la adaptación de impedancias
objeto-relacional [2]. Este concepto hace referencia a la
necesidad de adaptar, traducir o unir el lenguaje de la
aplicación al lenguaje de la base de datos y viceversa
(eliminar esta problemática fue el principal motivo de la
aparición de las bases de datos orientadas a objetos [3]
a mediados de 1980).


• Relaciones 1 a N
En el modelo tradicional SQL, la representación
más común de una relación 1 a n, es la
representación normalizada, que consiste en que
aquella entidad que pueda aparecer n veces está
en una tabla separada y utiliza una referencia
de clave externa (foreign key) a la otra tabla que
representa la entidad con cardinalidad 1.
Las soluciones de documentos pueden
representar esta relación en un único documento
JSON, añadiendo un array para cada relación
1 a N entre la entidad que se está definiendo
(cardinalidad 1) y los elementos del array
(cardinalidad N). Esta representación se
aprovecha de la localidad espacial. Cuando la
información a obtener requiere tanto la entidad
como las entidades relacionadas, en un modelo
relacional es necesario bien utilizar múltiples
consultas o utilizar operaciones join entre la tabla
tratada y las subordinadas.
• Relaciones N a 1 y N a M
Cuando la relación es inversa, es decir N
elementos apuntan a otra entidad, se tiene una
relación N a 1 (por ejemplo, N entidades empleado
apuntarán a una entidad empleador actual).
En esta ocasión, utilizar un identificador a otra
tabla en lugar de directamente el nombre del
empleador permite una serie de ventajas, tales
como, la consistencia (eliminando la posibilidad
de errores ortográficos o diferencias de estilo),
facilidad de actualizar información del empleador
(modificando los datos de esa tabla, en lugar de
modificar la información de cada empleado),
búsquedas más sencillas, facilidad para traducir
la información en otros idiomas, etc. Eliminar con
la duplicación o redundancia de datos es la idea
de la normalización. Este concepto no encaja con
el modelo de documentos, pero sí con el modelo
relacional, donde es común relacionar tablas
mediante un identificador y luego utilizar joins
para recabar la información deseada.


Actualmente, los mayores argumentos para el
uso del modelo de documentos son la flexibilidad
del esquema de la base de datos y el mejor
rendimiento (principio de localidad espacial). A
favor del modelo relacional está el soporte para
representar y obtener información mediante joins
de relaciones N a 1 y N a M

En una base de datos
de documentos, simplemente se escribiría con el
nuevo formato, en una base de datos relacional
sería necesario modificar el esquema y actualizar
la información de las tablas, pudiendo incurrir en
tiempo de inactividad de la base de datos.
En este aspecto, es necesario entender la
estructura y los diferentes tipos de objetos que
tendrá la base de datos. En situaciones donde
se necesiten numerosos tipos de objetos o la
estructura de los datos venga determinada por un
servicio o sistema externo la opción del esquema
en tiempo de lectura será superior a la de tiempo
de escritura. Sin embargo, la estructura de los
datos debe tener la misma estructura y se tiene
que asegurar que se cumpla, se obtendrá beneficio
al tener un esquema en tiempo de escritura.
Otro de los factores a tener en cuenta, es el acceso
y la actualización de la información. Dado que las
bases de datos de documentos aprovechan el
principio de cercanía de referencias, el rendimiento
será superior cuando la aplicación utilice gran parte
de la información del documento, ya que este tipo
de gestores suelen cargar el documento entero
independientemente de la porción a utilizar por la
aplicación.
De este modo, se evitarían las diferentes
búsquedas necesarias en un modelo relacional
con varias tablas. En el caso de la actualización de
información, se serán penalizados al tener mucha
información agrupada en un documento, a menos
que el tamaño del documento codificado sea el
mismo. Por este motivo, se recomiendan crear
documentos pequeños y aumentar el tamaño de
los mismos en las escrituras, reduciendo el número
de casos en el que estas bases de datos son útiles.
En los últimos años, las bases de datos relacionales
han añadido soporte para interactuar con XML o
JSON y las bases de datos de documentos facilitan,
de diferentes maneras, operaciones joins, haciendo
que los caminos de ambas se crucen ofreciendo las
ventajas de un modelo híbrido

Modelo de grafos

Existen diferentes formas de crear o estructurar
un grafo, así como diferentes maneras de realizar
consultas. Los dos modelos más relevantes son el
modelo de grafo de propiedades (property graph) y
el triple store (también llamado almacén de RDF). El
gestor de base de datos más conocidos del modelo
de propiedades es Neo4J y, MarkLogic o AllegroGraph
son algunas de las que utilizan el modelo triple store.
También hay gestores que soportan ambos modelos
como es el caso de Amazon Neptune. Asimismo,
existen diferentes lenguajes de consulta tales como
Cypher (lenguaje utilizado en Neo4J), Gremlim (Amazon
Neptune), SPARQL (GraphDB).

El modelo de grafo de propiedades consiste en que
cada vértice tiene un identificador único, un conjunto
de arcos salientes, otro de arcos entrantes y una
colección de propiedades de tipo clave-valor. Cada
arco tiene un identificador único, el vértice donde
comienza el arco, el vértice donde acaba, una etiqueta
que define el tipo de relación entre dos vértices y una
colección de propiedades clave-valor.
En este modelo, cada vértice puede conectarse con
cualquier otro vértice sin ninguna restricción en cuanto a
tipos o limitaciones de un esquema (no es necesario la
homogeneidad de datos de los diferentes vértices). Para
cada vértice, están disponibles tanto los arcos de entrada
como de salida por lo que se puede recorrer el grafo en
cualquier sentido. Además, dado que los arcos tienen
una etiqueta el modelo es claro y limpio aun teniendo
diferentes tipos de relaciones entre los vértices. Estas
propiedades hacen que este modelo sea fácilmente
extensible, añadiendo relaciones y vértices con información
de diferente índole a la que ya se tiene. Este es uno de
los principios, la evolucionabilidad, que se busca para
conseguir aplicaciones de alta mantenibilidad.
El modelo triple-store permite representar un grafo al
igual que el modelo anterior, pero utilizando un modo
muy particular. En este modelo la información se
almacena en un triplete, que está compuesto por sujeto-
predicado-objeto, como «Juan sabe inglés».
El sujeto de un triplete es equivalente a un vértice en un
grafo, pudiendo el objeto adoptar dos formas:
1. Un valor con un tipo de datos primitivo, como un
número, «Juan pesa 75 kg».
2. Otro vértice en el grafo. En este caso, el sujeto y el
objeto son dos vértices y el predicado es un arco del
grafo. «Juan conoce a María», donde Juan y María
serían dos vértices y conoce es la etiqueta del arco.

 Modelos de datos |
El modelo de bases de datos de grafo puede hacer
recordar al modelo de red (Codasyl) aunque difieren
significativamente. El modelo Codasyl tenía un
esquema que indicaba qué tipo de registro podía ser
asociado con otros tipos, se debía acceder por el punto
de entrada y los hijos de un registro eran un conjunto
ordenado (las aplicaciones debían preocuparse por
mantener ese orden al escribir nuevos registros).
Como se ha visto, el modelo de grafos no tiene esas
restricciones permitiendo la conexión de vértices con
diferente información, pudiendo recorrer el grafo desde
cualquier vértice. Además, los modelos de grafos
facilitan lenguajes de consulta declarativos de alto
nivel, mucho más sencillos que el lenguaje imperativo
y con dependencia física de Codasyl.




HINTS: bases
de datos de tipo schema-on-write (aquí estarían
las relacionales) y schema-on-read (y aquí las
de documentos), poliglota. 



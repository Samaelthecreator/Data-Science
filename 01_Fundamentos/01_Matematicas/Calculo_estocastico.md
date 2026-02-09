# Fundamentos de Procesos Estocásticos y Series Temporales

> **Autor:** Albert (PhD)
> **Enfoque:** Rigor Matemático con Intuición Física
> **Objetivo:** Explicar la mecánica interna de los fenómenos aleatorios temporales para una audiencia general.

---

## 1. El Quiebre con la Estadística Clásica: ¿Por qué necesitamos una nueva teoría?

La estadística clásica (como calcular el promedio de altura de un grupo) asume que cada dato es una isla independiente. En el mundo real, los datos son una cadena.

**El Problema del Tiempo:**
Imagina que mides la temperatura cada hora. El dato de las 10:00 AM ($X_t$) está fuertemente "amarrado" al de las 9:00 AM ($X_{t-1}$).
*   **Estadística Clásica:** Asume que el orden no importa (barajar los datos no cambia el promedio).
*   **Procesos Estocásticos:** El orden *es* la información. Si barajas una canción (serie de tiempo de audio), se convierte en ruido. La estructura está en la secuencia.

---

## 2. Definición Formal y Caracterización

### 2.1 El Escenario Matemático (Espacio de Probabilidad)

Para modelar la incertidumbre, necesitamos un escenario bien definido: $(\Omega, \mathcal{F}, \mathbb{P})$.

1.  **Espacio Muestral ($\Omega$ - El Multiverso):** Es el conjunto de *todas* las historias posibles que podrían haber ocurrido desde el inicio de los tiempos.
2.  **Eventos ($\mathcal{F}$):** Las preguntas de Sí/No que podemos responder (ej. "¿Subió la bolsa hoy?").
3.  **Medida de Probabilidad ($\mathbb{P}$):** Es una función que asigna un peso a cada evento, $\mathbb{P}: \mathcal{F} \to [0, 1]$. Nos dice qué tan probable es que ocurra un escenario.
    *   *Debe cumplir:* $\mathbb{P}(\Omega)=1$ (algo tiene que pasar) y ser aditiva para eventos disjuntos.

**¿Qué es una Realización?**
Un proceso estocástico es un abanico de infinitos futuros posibles. Pero nosotros solo vivimos en *uno*. La **Realización** es ese único camino histórico que observamos (los datos que tienes en tu Excel).
*   *Importancia:* La dificultad de la estadística radica en intentar entender el funcionamiento de todo el "abanico" (el proceso generador) viendo solo "una varilla" de él (la realización).

### 2.2 Anatomía de la Serie (Componentes)

Al igual que un prisma descompone la luz, la matemática descompone una serie temporal ($X_t$).

$$X_t = \text{Estructura Predecible} (T_t, S_t, C_t) + \text{Incertidumbre} (\varepsilon_t)$$

1.  **Tendencia ($T_t$):** La dirección a largo plazo.
2.  **Estacionalidad ($S_t$):** Patrones fijos (reloj).
3.  **Ciclo ($C_t$):** Olas de fondo (economía).
4.  **Ruido / Componente Irregular ($\varepsilon_t$):**
    *   **¿Cómo se detecta?** Es el residuo. Si restas la tendencia y la estacionalidad a tus datos, lo que queda debería ser "basura aleatoria" sin patrón. Si ves patrones en el residuo, tu modelo está incompleto.

**La Descomposición de Wold (El Teorema Fundamental):**
Este teorema nos dice que *cualquier* proceso estacionario (sin tendencia explosiva) se puede ver como ecos de choques pasados.
*   *Ejemplo Matemático:* Imagina un proceso AR(1) donde hoy es la mitad de ayer más un choque: $X_t = 0.5 X_{t-1} + \varepsilon_t$.
*   *Descomposición:* Si sustituimos hacia atrás recursivamente:
    $$ X_t = \varepsilon_t + 0.5 \varepsilon_{t-1} + 0.25 \varepsilon_{t-2} + 0.125 \varepsilon_{t-3} + \dots $$
    **Interpretación Física:** El valor de hoy es la suma del choque de hoy, más el eco del choque de ayer (atenuado a la mitad), más el eco de antier (un cuarto)... El presente es la suma ponderada de toda la historia de "sorpresas".

---

## 3. Transformaciones: Herramientas de Modelado

Antes de predecir, necesitamos "limpiar" la serie para que se comporte bien matemáticamente.

### 3.1 Estabilización de Varianza (Homocedasticidad)

**Homocedasticidad** significa "igual dispersión". Queremos que el error de nuestra predicción sea igual de grande hoy que dentro de 10 años.
Si la serie es volátil (se mueve poco cuando $X$ es pequeño, y muchísimo cuando $X$ es grande), no es homocedástica.

*   **Transformaciones:**
    *   **Logaritmo ($\ln X_t$):** La más común. Comprime los valores altos. Útil cuando la volatilidad es proporcional al nivel (crecimiento porcentual).
    *   **Box-Cox:** Una familia de transformaciones (raíz cuadrada, inverso, log) que busca automáticamente la mejor función para estabilizar la varianza.

### 3.2 Estabilización de la Media (Diferenciación)

Si la serie crece siempre (tiene tendencia), la media no es constante.
*   **Diferenciación ($\Delta X_t = X_t - X_{t-1}$):** En lugar de modelar el *precio* del dólar (que cambia siempre), modelamos el *cambio* en el precio (que oscila alrededor de cero).
    *   *¿Es el único método?* No. Puedes usar regresión para restar la tendencia ("Detrending"), pero la diferenciación es más robusta para tendencias estocásticas.
    *   *¿Se pierde información?* **Sí, se pierde el "Nivel".** Al diferenciar, sabes que subió $1 peso, pero olvidas si subió de $10 a $11 o de $1000 a $1001. Para recuperar el pronóstico original, debes "deshacer" la resta (integrar) sumando acumulativamente.

---

## 4. Modelos Predictivos e Intuición Física

### 4.1 Ruido Blanco (La Materia Prima)
Físicamente, el **Ruido Blanco** es **Información Pura** o "Sorpresa".
*   Si pudieras predecir el ruido, ya no sería ruido, sería un patrón.
*   Se llama "Blanco" por analogía con la luz blanca: contiene "todas las frecuencias" con igual intensidad. No suena agudo ni grave, suena a estática.
*   En modelos, es la fuente de energía que mantiene vivo al sistema. Sin ruido, el sistema se detendría en un punto fijo.

### 4.2 Modelos AR (Inercia) y Parámetro $p$
$$ AR(p): X_t = \phi_1 X_{t-1} + \dots + \phi_p X_{t-p} + \varepsilon_t $$
*   **Intuición:** Inercia o Memoria.
*   **Parámetro $p$ (Orden):** Nos dice **"¿Qué tan profunda es la memoria?"**.
    *   $p=1$: Solo me importa ayer.
    *   $p=12$: Me importa lo que pasó hace un año (mensual).
*   **Importancia:** Modelan sistemas que se resisten al cambio rápido (como la temperatura de un horno).
*   **Condición:** Deben ser estables. Si $\phi > 1$, el sistema explota (efecto bola de nieve).

### 4.3 Modelos MA (Impacto) y Parámetro $q$
$$ MA(q): X_t = \varepsilon_t + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q} $$
*   **Choque ($\varepsilon_t$):** Es un evento externo repentino. Una noticia de última hora, un terremoto, una orden de compra grande.
*   **Interpretación:** El valor de hoy depende del choque de hoy y de los "ecos" de los choques pasados.
*   **Parámetro $q$ (Orden):** Nos dice **"¿Cuánto tiempo resuena el eco?"**.
    *   $q=0$: El choque desaparece instantáneamente (Mercado ultra-eficiente).
    *   $q=3$: Una noticia afecta el mercado hoy, y sigue teniendo réplicas por 3 periodos más.

### 4.4 ARIMA
Une ambos mundos:
1.  **I(d):** Primero estabilizamos el nivel (diferenciando $d$ veces).
2.  **AR(p):** Modelamos la inercia interna del sistema.
3.  **MA(q):** Modelamos cómo el sistema absorbe los golpes externos.

---

## 5. Glosario de Términos

*   **Estacionariedad:** Equilibrio estadístico. Las reglas del juego (media, varianza) no cambian con el tiempo, aunque la pelota se mueva.
*   **Proceso Estocástico:** Una colección de variables aleatorias ordenadas en el tiempo. Una partitura musical donde las notas se eligen tirando dados.
*   **Raíz Unitaria:** Cuando un proceso tiene memoria perfecta. Un choque ocurrido hace 100 años sigue afectando el nivel de hoy. (Requiere diferenciación).

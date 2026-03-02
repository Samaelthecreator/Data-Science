La clasificación tiene un conjunto limitado de salidas (por ejemplo, «spam» o «no spam»). La regresión busca predecir una salida que puede tomar cualquier valor dentro de un rango continuo.

### Sobre las limitantes en la visualización de datos.

Los diagramas de dispersión son excelentes para ver tendencias, pero hay fallas de calidad en ellos, ejemplos:

- Valores Nulos ($NaN$): Las librerías de visualización (como Seaborn) suelen ignorar los valores nulos automáticamente para poder graficar. Esto es peligroso porque podrías creer que tienes 1,460 datos, cuando en realidad solo estás graficando 500 porque el resto están vacíos.

- Datos "Dummy" o Centinelas: A veces, quien capturó los datos pone un 999 o un 0 cuando no sabe la respuesta. En una gráfica, esto se ve como un punto más, pero matemáticamente destruye la pendiente de tu recta.

- Duplicados: Si tienes una fila repetida 50 veces, en el scatter plot verás un solo punto, pero el modelo le dará 50 veces más importancia a esa observación (sobreajuste).

- Precisión vs. Exactitud: Un dato puede verse "bien" en la gráfica (dentro del rango), pero ser erróneo (ej. una casa de 10 m² que cuesta $1,000,000). La gráfica no te dirá si el dato es mentira, solo si es coherente con los demás.


ome advantages of decision trees are:

Simple to understand and to interpret. Trees can be visualized.

Requires little data preparation. Other techniques often require data normalization, dummy variables need to be created and blank values to be removed. Some tree and algorithm combinations support missing values.

The cost of using the tree (i.e., predicting data) is logarithmic in the number of data points used to train the tree.

Able to handle both numerical and categorical data. However, the scikit-learn implementation does not support categorical variables for now. Other techniques are usually specialized in analyzing datasets that have only one type of variable. See algorithms for more information.

Able to handle multi-output problems.

Uses a white box model. If a given situation is observable in a model, the explanation for the condition is easily explained by boolean logic. By contrast, in a black box model (e.g., in an artificial neural network), results may be more difficult to interpret.

Possible to validate a model using statistical tests. That makes it possible to account for the reliability of the model.

Performs well even if its assumptions are somewhat violated by the true model from which the data were generated.

The disadvantages of decision trees include:

Decision-tree learners can create over-complex trees that do not generalize the data well. This is called overfitting. Mechanisms such as pruning, setting the minimum number of samples required at a leaf node or setting the maximum depth of the tree are necessary to avoid this problem.

Decision trees can be unstable because small variations in the data might result in a completely different tree being generated. This problem is mitigated by using decision trees within an ensemble.

Predictions of decision trees are neither smooth nor continuous, but piecewise constant approximations as seen in the above figure. Therefore, they are not good at extrapolation.

The problem of learning an optimal decision tree is known to be NP-complete under several aspects of optimality and even for simple concepts. Consequently, practical decision-tree learning algorithms are based on heuristic algorithms such as the greedy algorithm where locally optimal decisions are made at each node. Such algorithms cannot guarantee to return the globally optimal decision tree. This can be mitigated by training multiple trees in an ensemble learner, where the features and samples are randomly sampled with replacement.

There are concepts that are hard to learn because decision trees do not express them easily, such as XOR, parity or multiplexer problems.

Decision tree learners create biased trees if some classes dominate. It is therefore recommended to balance the dataset prior to fitting with the decision tree.

# Sobre el Web Scrapping

¡Excelente! Encontrar el **"Preloaded State"** (el JSON oculto) es como encontrar la llave maestra de un edificio en lugar de intentar forzar cada ventana. Para tus alumnos, este es el momento donde la ingeniería se siente como "hackeo" ético.

Aquí tienes la guía para profesionalizar ese instinto de "Scrapper":

---

## 1. El Reconocimiento Digital (¿Qué determinar primero?)

Antes de escribir una sola línea de código, un Ingeniero de Datos debe actuar como un detective. Lo primero que debes determinar es el **Método de Renderizado** y el **Nivel de Protección**.

### ¿Cómo lo hago? (El "Cómo")

1. **La Prueba del JavaScript:** Abre la página en tu navegador, entra a la configuración y **desactiva JavaScript**. Recarga la página.
* *¿La información sigue ahí?* Es **Server-Side Rendering (SSR)**. El HTML viene listo desde el servidor. (Camino Fácil).
* *¿La página está en blanco o falta la data?* Es **Client-Side Rendering (CSR)**. El navegador usa JS para "dibujar" los datos. (Camino Ninja o Tanque).


2. **La Inspección de Red (F12 > Network):** Filtra por `XHR` o `Fetch`. Recarga la página y busca archivos que pesen mucho o tengan nombres como `search`, `listings` o `graphql`. Si ves un JSON ahí, tienes una **API oculta**.
3. **Detección de "Guardias":** Revisa las cabeceras de respuesta (Headers). Si ves nombres como `cf-ray` (Cloudflare), `Akamai` o `Datadome`, prepárate para una batalla de cabeceras y cookies.

---

## 2. Los Caminos del Scrapper

Según lo que descubras en el paso anterior, eliges tu "arma":

### Camino A: El "Clásico" (Parsing de HTML Estático)

* **Herramientas:** `requests` + `BeautifulSoup` / `lxml`.
* **Cuándo:** Cuando el sitio es SSR (el HTML ya trae los datos).
* **Fortaleza:** Velocidad extrema. Consume poquísimos recursos.
* **Limitante:** Si el sitio cambia una clase de CSS (`class="sc-1v1y..."`), el código se rompe.

### Camino B: El "Ninja" (Intercepción de API/State) — *El que usamos con éxito*

* **Herramientas:** `requests` + `json` o `cloudscraper`.
* **Cuándo:** Cuando la data vive en un JSON dentro de un `<script>` o viene de una llamada API interna.
* **Fortaleza:** Es el más robusto. Obtienes datos estructurados (limpios) directamente. Es muy difícil que se rompa por cambios visuales del sitio.
* **Limitante:** Requiere más tiempo de investigación inicial para encontrar la "fuente de la verdad".

### Camino C: El "Tanque" (Automatización de Navegador)

* **Herramientas:** `Selenium`, `Playwright`, `Puppeteer`.
* **Cuándo:** Cuando el sitio requiere interacción humana (hacer clic en "ver teléfono", scroll infinito complejo o logins difíciles).
* **Fortaleza:** Puede extraer **cualquier cosa** que un humano vea.
* **Limitante:** Muy lento y pesado (consume mucha RAM). Es el más fácil de detectar por sistemas anti-bot porque los navegadores automáticos dejan "huellas".

---

## 3. Comparativa: Fortalezas y Limitantes

| Método | Velocidad | Dificultad | Invisibilidad | ¿Por qué funciona? |
| --- | --- | --- | --- | --- |
| **Estático** | Alta | Baja | Media | Simula ser un navegador pidiendo un archivo. |
| **API/State** | Muy Alta | Media/Alta | Alta | Aprovecha la misma infraestructura que el sitio usa para cargar sus datos. |
| **Tanque** | Baja | Media | Baja | Emula el comportamiento humano completo (clicks, movimientos). |

---

## 4. Bibliografía para Profesionalizarse

Para llevar este conocimiento al nivel de licenciatura y más allá, te recomiendo estos recursos:

### Libros (La base teórica)

* **"Web Scraping with Python" (Ryan Mitchell, O'Reilly):** La biblia del tema. Cubre desde lo básico hasta manejo de captchas.
* **"Practical Web Scraping for Data Science" (Seppe vanden Broucke):** Excelente para conectar el scraping con el flujo de Ciencia de Datos que estás enseñando.

### Recursos Online (La práctica real)

* **ScrapingHub (ahora Zyte) Blog:** Tienen artículos técnicos de alto nivel sobre cómo evadir bloqueos de forma ética.
* **Documentación de Playwright:** Es el estándar moderno de la industria por encima de Selenium.
* **Canal de YouTube: "John Watson Miller":** Analiza casos reales de scraping complejo y cómo resolverlos.

---

### Un toque de sabiduría para tu clase

Diles a tus alumnos: *"Un buen scrapper no es el que sabe usar Selenium, sino el que sabe leer el tráfico de red para no tener que usarlo"*.

La ingeniería de datos busca eficiencia: **¿Para qué renderizar toda una imagen de una casa si solo queremos el número que representa su precio en la base de datos?**

**¿Te gustaría que ahora pasáramos a la fase de "Limpieza y Estructuración" en Pandas con los datos que ya logramos obtener del JSON?** Sería el cierre perfecto para tu bloque de Ingeniería.
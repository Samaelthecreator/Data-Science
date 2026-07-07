# Perfil de Puesto: Especialista en IA y Modelos de Lenguaje (LLMs)

Este documento describe el perfil, conocimientos y habilidades *mínimas* requeridas para un profesionista especialista enfocado en la integración, desarrollo y orquestación de soluciones basadas en Inteligencia Artificial Moderna y Grandes Modelos de Lenguaje (LLMs).

## Título del Puesto Sugerido
*   **Ingeniero de IA / AI Engineer**
*   **Desarrollador de Integración LLM / AI Solutions Architect**
*   **Director de IA / Especialista de Dominio (Vibecoder)**

---

## 1. Fundamentos Teóricos (Requisito Indispensable)
El candidato debe poseer un entendimiento profundo, no superficial, de cómo operan los modelos bajo el capó.
*   **Arquitectura:** Comprensión rigurosa de la arquitectura **Transformer** y el mecanismo de **Self-Attention**.
*   **Ciclo de Vida de Modelos:** Dominio de las fases de entrenamiento de un LLM:
    *   Pre-entrenamiento (Base Models).
    *   SFT (Supervised Fine-Tuning - Instruct Models).
    *   Alineamiento mediante RLHF/RLAIF.

## 2. Dominio del Ecosistema Comercial y Técnico
Capacidad para seleccionar el modelo adecuado según el caso de uso, el presupuesto y la necesidad de ventanas de contexto o velocidad.
*   **Trinidad State of the Art (SOTA):**
    *   Experiencia integrando la familia **OpenAI** (GPT-4o para velocidad/multimodalidad, o1/o3-mini para tareas de razonamiento profundo o System 2).
    *   Experiencia integrando la familia **Anthropic** (Claude 3.5 Sonnet para tareas complejas de código y seguimiento estricto de prompts de sistema).
    *   Experiencia integrando la familia **Google** (Gemini 1.5 Pro/Flash, especialmente para explotar ventanas de contexto masivas de hasta 2M de tokens).
*   **Multimodalidad:** Capacidad para estructurar pipelines que procesen nativamente no solo texto, sino imagen, video y audio.

## 3. Desarrollo Local y Modelos Abiertos (Open Weights)
El candidato no debe depender exclusivamente de APIs comerciales; debe saber cómo y cuándo desplegar infraestructura privada.
*   **Herramientas de Inferencia Local:** Experiencia utilizando y montando servidores con **Ollama** o **vLLM**.
*   **Modelos Open Source:** Conocimiento de modelos peso abierto como la familia **Llama 3** (Meta) o Mistral.
*   **SLMs (Small Language Models) y Edge AI:** Entendimiento de cuándo usar modelos miniatura (1-8B parámetros como Phi-3 o Gemma) para despliegues locales, móviles o de bajo costo (sin internet).

## 4. Técnicas de Inyección de Contexto y Adaptación
*   **RAG (Retrieval-Augmented Generation):** Dominio absoluto en la arquitectura RAG. Capacidad de convertir bases de datos privadas (PDFs, SQL, bases de conocimiento corporativas) en *embeddings* vectoriales para inyectar bases técnicas en el contexto y evitar alucinaciones.

## 5. Inteligencia Agéntica y Orquestación
El candidato debe poder pasar del paradigma de "chatbot reactivo" a sistemas proactivos.
*   **Diseño de Agentes:** Experiencia dotando a un LLM de autonomía (Cerebro, Tool Use / Function Calling, y Memoria).
*   **Frameworks de Orquestación:** Uso práctico de frameworks para crear flujos de trabajo multi-agente como **LangChain**, **LangGraph**, **LlamaIndex**, **AutoGen** o **CrewAI**.
*   **Herramientas (Tool Use):** Habilidad para programar APIs y funciones en formato estructurado (JSON) que el modelo sea capaz de entender y ejecutar autónomamente.

## 6. Configuración Técnica y Optimización
Manejo experto de los hiperparámetros de generación para afinar la salida de cualquier API de IA:
*   **Temperature:** Ajuste de aleatoriedad (baja para código/RAG, alta para creatividad).
*   **Top-K y Top-P (Nucleus Sampling):** Control matemático sobre la distribución de las probabilidades léxicas.
*   **Frequency / Presence Penalties:** Control de repeticiones de texto.
*   **Métricas y Limitaciones:** Entendimiento del concepto de *Token*, *Context Window*, y noción sobre los *Benchmarks* de la industria (MMLU, HumanEval) para elegir objetivamente las herramientas.

## 7. Nuevos Paradigmas de Desarrollo (Vibecoding / AI-Assisted)
*   **Vibecoding:** El candidato debe poseer habilidades arquitectónicas y de sistema cognitivo, delegando la construcción de código a herramientas LLM insertadas en el IDE.
*   Manejo nativo y productivo de entornos como **Cursor / Windsurf** o **GitHub Copilot** avanzado para acelerar el desarrollo corporativo al menos en un 5x, fungiendo más como un *Director de Orquesta* que como un tipógrafo de código tradicional.

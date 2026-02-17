# Principios de Arquitectura de Datos

El diseño de sistemas para uso intensivo de datos debe garantizar tres pilares fundamentales: Fiabilidad, Escalabilidad y Mantenibilidad.

## 1. Fiabilidad (Reliability)
La capacidad del sistema para continuar funcionando correctamente (hacer lo que el usuario espera) incluso ante la adversidad (fallos de hardware, software o humanos).
- **Tolerancia a Fallos:** El sistema no se detiene si un componente falla (ej. redundancia de servidores).
- **Resiliencia:** Capacidad de recuperación automática.

*"La simplicidad es un requisito previo para la fiabilidad." - Edsger W. Dijkstra*

## 2. Escalabilidad (Scalability)
La capacidad de afrontar un aumento en la carga (tráfico, volumen de datos o complejidad) manteniendo el rendimiento.
- **Escalado Vertical (Scale Up):** Más potencia a una sola máquina (CPU, RAM). Límite físico y costoso.
- **Escalado Horizontal (Scale Out):** Distribuir la carga entre muchas máquinas (Cluster). Más complejo de administrar pero teóricamente ilimitado.

### Parámetros de Carga
Para medir la escalabilidad, primero debemos medir la carga:
- Peticiones por segundo (RPS).
- Latencia (tiempo de respuesta).
*Nota:* Usar percentiles (p95, p99) es mejor que la media para detectar problemas que afectan a los usuarios más lentos.

## 3. Mantenibilidad (Maintainability)
La facilidad con la que el sistema puede ser modificado y adaptado en el futuro. El mayor costo del software no es su desarrollo inicial, sino su mantenimiento.
- **Operabilidad:** Fácil de monitorear y gestionar en producción.
- **Simplicidad:** Código limpio y arquitecturas comprensibles para nuevos ingenieros.
- **Evolucionabilidad:** Fácil de extender con nuevas funcionalidades sin romper lo existente.

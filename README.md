# examen_Final_Frank

1. Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar 
brevemente
Análisis de datos (Data Analysis):
Python es ampliamente utilizado para analizar grandes volúmenes de datos y obtener insights. Bibliotecas como Pandas y NumPy facilitan la manipulación de datos, limpieza y cálculo de estadísticas descriptivas.
Ciencia de datos (Data Science):
Python se emplea en la ciencia de datos para construir modelos predictivos, aplicar técnicas de machine learning y realizar análisis exploratorios con herramientas como Scikit-learn y TensorFlow.
Visualización de datos (Data Visualization):
Con librerías como Matplotlib, Seaborn y Plotly, Python permite crear gráficos interactivos y estáticos para comprender mejor los datos y comunicar los resultados de manera visual.
Procesamiento de datos masivos (Big Data):
Python se usa en entornos de procesamiento de grandes volúmenes de datos, integrándose con sistemas como Hadoop o Spark. Librerías como PySpark permiten trabajar con datos distribuidos a gran escala.
Automatización de flujos de trabajo de datos:
Python es ideal para la automatización de tareas relacionadas con datos, como la recolección, transformación y almacenamiento de información, con librerías como Airflow para gestionar flujos de trabajo complejos.

2. ¿Cómo se diferencian Flask de Django? Argumentar.
Flask:
Flask es ligero y minimalista. Proporciona solo lo básico para desarrollar aplicaciones web, lo que lo hace más flexible y fácil de personalizar.
Flask es un framework minimalista y flexible, lo que significa que permite a los desarrolladores construir aplicaciones de manera rápida y personalizable. Proporciona la base necesaria para comenzar, pero deja muchas decisiones de diseño y arquitectura en manos del desarrollador. Esto lo convierte en una excelente opción para proyectos más pequeños o cuando se busca un control total sobre cada aspecto de la aplicación.


Framework completo: 
Django es más grande y viene con muchas características "out of the box", como un ORM (Object-Relational Mapping), autenticación y administración de usuarios, entre otros.
Django es un framework más completo que sigue el principio de "baterías incluidas". Ofrece muchas funcionalidades listas para usar, como autenticación, administración de bases de datos y herramientas para gestionar formularios, lo que permite a los desarrolladores concentrarse más en la lógica de negocio en lugar de preocuparse por la configuración inicial. Su estructura predefinida puede hacer que el desarrollo de aplicaciones más grandes sea más eficiente


3. ¿Qué es un API? Explicar en sus propias palabras
un conjunto de reglas que permite a diferentes app o sistemas a comunicarse entre si, facilita el intercambio de información, datos o servicios. como por ejemplo cuando creas un app y nesecita información o datos de un servidor sin tener que interactuar con la base de datos.
4. ¿Cuál es la principal diferencia entre REST y WebSockets?
En REST, el cliente hace solicitudes (por ejemplo, usando HTTP) al servidor, y este responde con los datos necesarios. Es adecuado para aplicaciones donde las actualizaciones no necesitan ser en tiempo real.
Se utiliza principalmente para aplicaciones CRUD (crear, leer, actualizar, eliminar), donde el intercambio de datos no es constante.

WebSockets permite una conexión persistente entre cliente y servidor, donde ambos pueden enviar mensajes entre sí en tiempo real.
Es ideal para aplicaciones en tiempo real como chats, actualizaciones en vivo, o videojuegos multijugador.

5. Describir un ejemplo de API comercial y como funciona – usar otros ejemplos no vistos 
en el curso

PayPal API

facilita la integración de sistemas de pago para procesar pagos y reembolsos mediante cuentas PayPal o tarjetas de crédito.

La PayPal API funciona como un intermediario entre los comerciantes y los clientes, permitiendo a las plataformas de comercio electrónico integrar un sistema de pagos seguro y eficiente. Cuando un cliente decide realizar una compra, la API se encarga de procesar el pago mediante la recopilación de la información de la tarjeta de crédito o los detalles de la cuenta PayPal del cliente. Después de verificar la autenticidad y disponibilidad de fondos, la API envía una solicitud de autorización a PayPal. Si el pago es aprobado, los fondos son transferidos del cliente al comerciante, y este último recibe una notificación confirmando la transacción exitosa. Además, la API ofrece funciones para gestionar reembolsos, realizar seguimientos de transacciones y acceder a informes detallados, lo que simplifica el proceso de venta y mejora la experiencia del cliente.

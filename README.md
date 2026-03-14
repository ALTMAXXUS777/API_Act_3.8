# API REST para Administración de Tareas Personales con Python y Flask

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

## 📌 Descripción del Proyecto

Este proyecto es una **API RESTful** diseñada específicamente para la administración de un sistema básico de tareas personales. Ha sido construido utilizando **Python**, el micro-framework **Flask** y **SQLAlchemy** como ORM (Object Relational Mapper) para interactuar de forma sencilla con una base de datos **SQLite**.

El objetivo principal detrás del desarrollo de esta API es comprender y consolidar los conocimientos prácticos sobre la arquitectura cliente-servidor, la creación e implementación de un modelo de datos robusto y la ejecución completa de operaciones **Actividades CRUD** (Create, Read, Update, Delete) a través de peticiones HTTP.

---

## 🎯 Objetivos de Aprendizaje

Durante la planificación, el desarrollo y las pruebas de este proyecto, se han abarcado múltiples conceptos esenciales en la creación de aplicaciones Backend modernas. 

Entre las habilidades y conceptos reforzados se encuentran:

1. **Estructura de Micro-servicios Restful:** 
   - Entender profundamente la diferencia entre los métodos HTTP (`GET`, `POST`, `PUT`, `DELETE`) y cómo cada uno mapea conceptualmente con una acción específica dentro del sistema de datos.
   - Aprender sobre la entrega correcta de códigos de estado HTTP (Ej. `200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`) para asegurar que todo cliente que interactúe con la API sepa con precisión qué ocurrió con su petición.

2. **Modelado de Bases de Datos con SQLAlchemy:**
   - Dejar de escribir consultas SQL puras para aprovechar el poder de los ORMs, lo que permite interactuar con la base de datos de manera más segura y orientada a objetos puro en Python.
   - Definir y crear correctamente esquemas de bases de datos relacionales asegurando integridad (por ejemplo, previniendo guardar tareas vacías donde el título es nulo).
   
3. **Manejo Correcto de Formatos JSON:**
   - La API fue codificada para recibir instrucciones sólamente en formato JSON desde el `Body` de la petición.
   - Igualmente, fue diseñada para serializar automáticamente los objetos complejos de Python provenientes de la base de datos (Entidad _Tarea_) en diccionarios comprensibles y finalmente parsearlos a JSON estructurado como salidas.

4. **Entornos Virtuales:**
   - Aislar el entorno del proyecto usando `.venv`, previendo conflictos y garantizando que se pueden instalar libremente librerías en versiones específicas sin alterar el comportamiento global del sistema de Python.

---

## 🏗️ Estructura y Arquitectura del Proyecto

El proyecto está autocontenido y diseñado para ser un bloque monolítico y minimalista, optimizado para entender a las primeras el flujo de datos. Su estructura es la siguiente:

```bash
API_3.8/
│
├── .venv/                  # Entorno virtual de Python
├── app.py                  # Código principal de la API y rutas CRUD
├── requirements.txt        # Control de versiones para dependencias (Flask, SQLAlchemy)
├── instance/
│   └── tareas.db           # Base de Datos SQLite (Auto-generada)
└── img/                    # Carpeta con las evidencias (Capturas de Postman)
```

### El Modelo de la Base de Datos

El diseño de la tabla `Tarea` en SQLAlchemy contiene cuatro campos indispensables acordados en los requisitos técnicos:

- `id`: Identificador principal (Integer, Primary Key).
- `titulo`: Texto obligatorio descriptivo corto.
- `descripcion`: Detalles opcionales más extensos.
- `estado`: Refleja el estado actual. Por defecto se asigna a "Pendiente". Otras opciones sugeridas son "En progreso" o "Completada".

---

## 🚀 Guía de Instalación y Puesta en Marcha

Para iniciar rápidamente la copia local del servidor en tu máquina y empezar a interactuar con la API, sigue estos pasos:

### 1. Clonar el repositorio
Descarga este código en tu entorno de trabajo:
```bash
git clone https://github.com/JOSTHONS/API_3.8.git
cd API_3.8
```

### 2. Preparar el Entorno (Windows)
Es vital utilizar el entorno virtual adjunto o crear uno nuevo para instalar correctamente Flask y la librería SQLAlchemy sin problemas de compatibilidad global.
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Instalar Dependencias
Instala los paquetes estipulados en el archivo estricto de requerimientos.
```powershell
pip install -r requirements.txt
```

### 4. Lanzar el Servidor de Pruebas
Flask levantará el entorno local, creará al vuelo la base de datos si esta no existe previamente en la carpeta e inicializará el puerto `5000`.
```powershell
python app.py
```

---

## 📚 Documentación de Endpoints y Uso Práctico

La API arranca en el servidor local de Flask: `http://127.0.0.1:5000`. 
A continuación se explica al detalle cómo ejecutar los cuatro métodos requeridos, acompañados de evidencia funcional utilizando la plataforma **Postman**.

### 1. 🟢 Crear una Tarea Nueva (POST)
**Endpoint**: `POST /tareas`

Permite inyectar un nuevo registro de una tarea en el sistema. El campo `titulo` es estrictamente requerido. `descripcion` y `estado` son opcionales.

**Ejemplo del Body de la Petición:**
```json
{
    "titulo": "Terminar evidencia",
    "descripcion": "Subir las capturas de Postman al reporte"
}
```

**Resultado esperado:**
La API verifica los datos de entrada, los inyecta validando contra el modelo, crea el evento SQLAlchemy, le asigna un estado "Pendiente", lo guarda físicamente y retorna los parámetros con un código estado **201**.

#### 📸 Evidencia - Creación de Tarea (POST)
Se puede apreciar exitosamente el `Status: 201 Created` además de la asignación automática por defecto del estado pendiente y la enumeración incremental del `ID`.

![Operación POST - Crear](img/Captura%201.png)


---


### 2. 🔵 Consultar Múltiples Tareas (GET)
**Endpoint**: `GET /tareas`

Este método recolecta y lista todos los registros existes persistentes grabados hasta el momento actual en el sistema, devolviendo una estructura en Array JSON de todas las tareas.

**Ejemplo de Petición:**
No es necesario enviar JSON en el body, simplemente hacer la llamada hacia la URL.

**Resultado esperado:**
La API le solicitará al ORM de la Base de Datos leer absolutamente cada fila contenida en la tabla Tarea, instanciarla, mapearla en un arreglo plano de Python usando la propiedad helper `to_dict` y finalmente serializarla como vector devolviendo el grupo entero bajo un código de estado **200 OK**.

#### 📸 Evidencia - Lectura General (GET)
A continuación, podemos ver una consulta GET donde se aprecian registros múltiples que fueron inyectados exitosamente con anterioridad. 

![Operación GET - Consultar](img/Captura%202.png)


---


### 3. 🟡 Actualizar una Tarea (PUT)
**Endpoint**: `PUT /tareas/<id>`

Modifica parcial o totalmente un elemento registrado en base a su ID. Todos los valores del modelo son actualizables. Comúnmente usado para cambiar la propiedad "estado" hacia un progreso real.

**Ejemplo del Body de la Petición a `/tareas/3`:**
```json
{
    "estado": "Completada"
}
```

**Resultado esperado:**
El servidor localiza el registro buscando su clave primaria. Si existe, reemplaza únicamente los atributos dictados en la petición (que fueron procesados como JSON y validados) y los sobreescribe en base de datos. Se retorna la tarea final resultante bajo un código **200 OK**.

#### 📸 Evidencia - Actualización Controlada (PUT)
Observamos cómo la tarea seleccionada ha cambiado existosamente el valor de su campo `estado` gracias a la petición enviada vía cliente de pruebas, demostrando la maleabilidad del registro.

![Operación PUT - Actualizar](img/Captura%203.png)


---


### 4. 🔴 Eliminar permanentemente una Tarea (DELETE)
**Endpoint**: `DELETE /tareas/<id>`

Borra por de tu tabla el registro asociado con el número de identificador primario otorgado explícitamente dentro de la misma URL (Ruteo estricto de Flask).

**Ejemplo de Petición:**
Enviar el método HTTP Delete directo al endpoint correspondiente: `http://127.0.0.1:5000/tareas/2` para borrar la segunda tarea de todo el listado global.

**Resultado esperado:**
Flask identifica que se solicita una eliminación con identificador `2`. Interroga usando SQLAlchemy si esa entidad vive físicamente en la memoria de la SQL Local. Al encontrarla, ejecuta un `db.session.delete()` garantizando el borrado y reescribiendo el cambio masivo al final. Devuelve confirmación json en formato amigable **200 OK**.

#### 📸 Evidencia - Eliminación (DELETE)
Como se puede notar, Postman corrobora que la acción ha ocurrido con gran certeza y nos devuelve el mensaje explícito indicando la correcta supresión del campo requerido.

![Operación DELETE - Eliminar](img/Captura%204.png)


---

## 📋 Conclusiones

Este proyecto consolida a un alto grado qué significan las operaciones transaccionales para las aplicaciones web hoy día. 

1. **Eficiencia en Ruteo**: Gracias al decorador `@app.route()` se probó de manera factible lo rápido que es enlazar de ida y vuelta rutas REST con funciones puras utilizando Flask.
2. **Serializador Interno**: Crear el método instanciado helper `to_dict()` para el Modelo es una de las grandes lecciones aprendidas para lograr transformaciones limpias de objetos-base-de-datos que a Python le son extraños a arreglos y JSON que todo software frontal necesita procesar.  
3. **Escalabilidad**: Se preparó el entorno para continuar su crecimiento usando estándares fuertes, ya sea adaptarlo a PostreSQL, enlazarle un ORM distinto o aplicarle contenedores Docker. El modelado básico CRUD es el cerebro medular de los sistemas interactivos. 

> *Nota del Desarrollador: Cuidar que se pase correctamente el content-type como application/json en cada nueva query desde el frontend garantizará siempre una respuesta segura por el API.*

`Hecho con amor y mucho Python 🐍 by Josthyn.`

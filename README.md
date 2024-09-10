# actividad_diagnostica_soa
Actividad Diagnostica API

# Florist API

Este proyecto es una API RESTful para un negocio de floristería que permite la gestión de un **catálogo** de productos y el procesamiento de **pedidos**. Utiliza **FastAPI** como framework del lado del servidor, con una base de datos **MongoDB** alojada en MongoDB Atlas. La API sigue una arquitectura hexagonal (también conocida como "puertos y adaptadores") para garantizar una separación clara entre la lógica de negocio y las capas externas, como las interfaces o bases de datos.

## Tecnologías utilizadas

- **Python** (FastAPI)
- **MongoDB** (MongoDB Atlas)
- **Swagger UI** (Documentación interactiva automática)
- **Uvicorn** (Servidor ASGI para ejecutar FastAPI)

## Funcionalidades

- Gestión del catálogo de productos de la floristería.
- Gestión de pedidos por parte de los clientes.
- Documentación de la API generada automáticamente usando Swagger UI.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu máquina:

1. **Python 3.7 o superior**.
2. **pip** (el administrador de paquetes de Python).
3. Una cuenta de **MongoDB Atlas** con las credenciales de acceso y una base de datos creada.

### Variables de entorno

El archivo de conexión a la base de datos espera que definas una variable de entorno para la URI de MongoDB Atlas:

- **MONGODB_URI**: La URI para conectar con tu base de datos de MongoDB Atlas. Debería tener el formato:

mongodb+srv://<usuario>:<contraseña>@floristadb.et9vl.mongodb.net/?retryWrites=true&w=majority&appName=floristadb

bash
Copy code

## Instalación

Sigue los pasos a continuación para clonar el repositorio, instalar dependencias y ejecutar los servicios.

### 1. Clona el repositorio

```bash
git clone <url-del-repositorio>
cd florist-api
2. Crea un entorno virtual (opcional pero recomendado)
bash
Copy code
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
3. Instala las dependencias
bash
Copy code
pip install -r requirements.txt
4. Configura la URI de MongoDB Atlas
Establece la URI de MongoDB como una variable de entorno antes de iniciar el servidor:

En Linux/macOS:

bash
Copy code
export MONGODB_URI="mongodb+srv://<usuario>:<contraseña>@floristadb.et9vl.mongodb.net/?retryWrites=true&w=majority&appName=floristadb"
En Windows (Powershell):

bash
Copy code
$env:MONGODB_URI="mongodb+srv://<usuario>:<contraseña>@floristadb.et9vl.mongodb.net/?retryWrites=true&w=majority&appName=floristadb"
5. Ejecuta el servidor FastAPI
Usa Uvicorn para levantar el servidor:

bash
Copy code
uvicorn app.main:app --reload
Esto iniciará el servidor en modo de recarga automática. Puedes acceder a la API en http://127.0.0.1:8000/.

6. Documentación Swagger
La documentación interactiva de la API estará disponible automáticamente en el siguiente enlace:

arduino
Copy code
http://127.0.0.1:8000/docs
Estructura del proyecto
bash
Copy code
/florist-api
│
├── /app
│   ├── /catalog        # Módulo para gestionar el catálogo de productos
│   ├── /orders         # Módulo para gestionar los pedidos
│   ├── /config         # Configuración de la base de datos
│   └── main.py         # Punto de entrada de la aplicación FastAPI
│
├── /tests              # Pruebas unitarias y de integración
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación del proyecto
Cómo contribuir
Haz un fork de este repositorio.
Crea una nueva rama con tu funcionalidad: git checkout -b feature/nueva-funcionalidad.
Realiza los cambios y haz commit: git commit -m 'Añadida nueva funcionalidad'.
Haz push a tu rama: git push origin feature/nueva-funcionalidad.
Abre un pull request.
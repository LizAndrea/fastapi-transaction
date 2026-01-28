# AppTransactionFastAPI

API de un Sistema de transacción, desarrollado usando FastAPI con Python.

Este proyecto es una API REST que permite gestionar Clientes (Customers), Planes (Plans) y Transacciones (Transactions), así como establecer relaciones entre ellos.

## Tecnologías Utilizadas

El proyecto utiliza las siguientes tecnologías y librerías clave:

-   **[Python 3.10+](https://www.python.org/)**: Lenguaje de programación principal.
-   **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno y rápido para construir APIs.
-   **[SQLAlchemy](https://www.sqlalchemy.org/)**: Toolkit SQL y ORM (Object Relational Mapper).
-   **[Alembic](https://alembic.sqlalchemy.org/en/latest/)**: Herramienta de migración de base de datos para usar con SQLAlchemy.
-   **[Pydantic](https://docs.pydantic.dev/)**: Validación de datos y gestión de configuraciones usando anotaciones de tipo de Python.
-   **[Uvicorn](https://www.uvicorn.org/)**: Servidor ASGI "Lightning-fast".
-   **[PostgreSQL](https://www.postgresql.org/)**: Sistema de gestión de bases de datos relacional.

## Requisitos Previos

Antes de comenzar, asegúrate de tener las siguientes herramientas instaladas. Si es tu primera vez configurando un entorno de desarrollo, sigue la sección de **Preparación del Entorno (Desde Cero)** más abajo.

-   **Python 3.10+** (incluye pip y venv)
-   **PostgreSQL 13+**
-   **Git**

### Verificación

Para confirmar que tienes las herramientas instaladas y comprobar sus versiones, ejecuta los siguientes comandos en tu terminal:

```bash
# Verificar versión de Python (Debe ser 3.10 o superior)
python3 --version
# Nota: En Windows puede ser 'python --version'

# Verificar versión de Git
git --version

# Verificar versión de PostgreSQL (si tienes el cliente instalado)
psql --version
```

## Preparación del Entorno (Desde Cero)

Si no tienes instaladas las herramientas mencionadas, sigue estos pasos según tu sistema operativo:

### Linux / WSL (Ubuntu/Debian)

1.  **Actualizar lista de paquetes**
    ```bash
    sudo apt update
    ```
2.  **Instalar Git, Python y herramientas de entorno virtual**
    Es crucial instalar `python3-venv` y `python3-pip` ya que a menudo no vienen preinstalados en algunas distribuciones.
    ```bash
    sudo apt install git python3 python3-pip python3-venv -y
    ```
3.  **Instalar PostgreSQL**
    ```bash
    sudo apt install postgresql postgresql-contrib -y
    ```

### Windows

1.  **Instalar Python**
    *   Descarga el instalador desde [python.org](https://www.python.org/downloads/).
    *   **IMPORTANTE**: Al iniciar el instalador, marca la casilla **"Add Python to PATH"** antes de dar clic en "Install Now".
2.  **Instalar Git**
    *   Descarga e instala Git desde [git-scm.com](https://git-scm.com/download/win).
    *   Usa las opciones predeterminadas del instalador.

---

## Instalación del Proyecto

Una vez preparadas las herramientas, sigue estos pasos para levantar el proyecto:

### 1. Clonar el repositorio
Descarga el código fuente a tu máquina.
```bash
git clone <URL_DEL_REPOSITORIO>
cd fastapi-transaction
```

### 2. Crear un Entorno Virtual
El entorno virtual aísla las librerías del proyecto para no afectar tu sistema global.

*   **Linux / macOS**:
    ```bash
    python3 -m venv env
    ```
*   **Windows**:
    ```powershell
    python -m venv env
    ```

### 3. Activar el Entorno Virtual
Debes activarlo cada vez que trabajes en el proyecto. Verás que tu terminal muestra `(env)` al inicio.

*   **Linux / macOS**:
    ```bash
    source env/bin/activate
    ```
*   **Windows**:
    ```powershell
    .\env\Scripts\activate
    ```

### 4. Instalar Dependencias
Instala todas las librerías necesarias listadas en `requirements.txt`.

> [!WARNING]
> **Usuarios de Windows**: Antes de ejecutar el comando, debéis editar el archivo `requirements.txt` y **borrar la línea `uvloop==0.21.0`**.
>
> **¿Por qué?**: `uvloop` es un reemplazo de alto rendimiento para el bucle de eventos asyncio, pero está construido sobre `libuv` y diseñado específicamente para sistemas **Unix** (Linux y macOS). **No es compatible con Windows**, por lo que la instalación fallará si no se elimina.

```bash
pip install -r requirements.txt
```

### 5. Configuración de Base de Datos y Variables
1.  Copia el archivo de ejemplo:
    *   **Linux/Mac**: `cp .env.example .env`
    *   **Windows**: `copy .env.example .env`
2.  Abre el archivo `.env` y configura tus credenciales de PostgreSQL (`DATABASE_URL`).
3.  Crea la base de datos en PostgreSQL si aún no existe.

### 6. Ejecutar Migraciones (Solo PostgreSQL)
Crea las tablas en la base de datos usando Alembic.
```bash
alembic upgrade head
```

## Uso con SQLite (Opcional)

Si prefieres usar **SQLite** para desarrollo local (sin instalar PostgreSQL), sigue estos pasos:

1.  Abre el archivo `.env`.
2.  Comenta la línea de `DATABASE_URL` de PostgreSQL y descomenta la de SQLite:
    ```ini
    # DATABASE_URL = "postgresql://..."
    DATABASE_URL = "sqlite:///./database.db"
    ```
3.  **No es necesario ejecutar migraciones**. La aplicación creará automáticamente el archivo `database.db` y las tablas al iniciarse (gracias a la función `lifespan` en `main.py`).

> [!NOTE]
> Si deseas usar **Alembic** con SQLite, necesitarás instalar el driver asíncrono `aiosqlite` (`pip install aiosqlite`) y cambiar la URL a `sqlite+aiosqlite:///./database.db`, ya que la configuración de migraciones actual espera un entorno asíncrono. Para uso básico, la configuración por defecto es suficiente.

---

**Nota sobre Base de Datos**: Asegúrate de crear la base de datos definida en tu `DATABASE_URL` (en el archivo `.env`) antes de ejecutar `alembic upgrade head`.

## Ejecución

Tienes dos opciones principales para levantar el servidor de desarrollo:

### Opción 1: FastAPI CLI (Recomendado para desarrollo)

Esta es la forma moderna y recomendada para desarrollar. Incluye recarga automática y una interfaz de consola amigable.

```bash
fastapi dev app/main.py
```

### Opción 2: Uvicorn (Servidor ASGI estándar)

Puedes ejecutar el servidor directamente con Uvicorn. Es útil si necesitas configuraciones específicas del servidor o un entorno más similar a producción (sin el modo dev).

```bash
uvicorn app.main:app --reload
```
*El flag `--reload` habilita el reinicio automático al detectar cambios en el código.*

---

El servidor se iniciará generalmente en `http://127.0.0.1:8000`.

## Documentación API (Swagger UI)

FastAPI genera automáticamente documentación interactiva para la API. Una vez que el servidor esté en ejecución, puedes acceder a ella en:

-   **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - Permite probar los endpoints directamente desde el navegador.
-   **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) - Documentación alternativa más limpia y estructurada.
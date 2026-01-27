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

Antes de comenzar, asegúrate de tener instalado:

-   Python 3.10 o superior
-   PostgreSQL instalado y ejecutándose
-   Git

## Instalación y Configuración

Sigue los pasos correspondientes a tu sistema operativo.

### Linux / WSL

1.  **Clonar el repositorio**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd fastapi-transaction
    ```

2.  **Crear y activar un entorno virtual**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3.  **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar variables de entorno**
    ```bash
    cp .env.example .env
    ```
    Edita el archivo `.env` con tus credenciales de PostgreSQL.

5.  **Ejecutar migraciones**
    ```bash
    alembic upgrade head
    ```

### Windows

1.  **Clonar el repositorio**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd fastapi-transaction
    ```

2.  **Crear y activar un entorno virtual**
    ```powershell
    python -m venv env
    .\env\Scripts\activate
    ```

3.  **Instalar dependencias**
    ```powershell
    pip install -r requirements.txt
    ```

4.  **Configurar variables de entorno**
    ```powershell
    copy .env.example .env
    ```
    Edita el archivo `.env` con tus credenciales de PostgreSQL.

5.  **Ejecutar migraciones**
    ```powershell
    alembic upgrade head
    ```

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
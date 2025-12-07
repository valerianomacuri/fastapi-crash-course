# FastAPI Crash Course

[![Python](https://img.shields.io/badge/python->=3.13-blue)]()

Proyecto de ejemplo para manejar productos usando **FastAPI** y **uv** como gestor de dependencias.

---

## 🔧 Requisitos

- Python >= 3.13
- uv (para manejo de dependencias y tareas)
- fastapi >= 0.123.10
- pydantic >= 2.12.5
- uvicorn >= 0.38.0 (para correr el servidor)

---

## ⚡ Instalación

1. Clonar el repositorio:

```bash
git clone <url-del-repo>
cd fastapi-crash-course
````

2. Instalar dependencias con **uv**:

```bash
uv sync
```

3. Instalar dependencias de desarrollo (opcional):

```bash
uv sync --group dev
```

---

## 🚀 Ejecutar el proyecto

Para desarrollo (auto-recarga de cambios):

```bash
uv run uvicorn app.main:app --reload
```

Para producción:

```bash
python -m gunicorn app.main:app -k uvicorn.workers.UvicornWorker
```

El servidor correrá en [http://localhost:8000](http://localhost:8000)

---

## 🐳 Crear la imagen de Docker

```bash
docker-compose up --build
```

---

## 📝 Formateo de Código

Se utiliza **Black** para formateo:

```bash
uv run black .
```

---

## 📄 Licencia

Agregar tu licencia aquí.

# Usar imagen oficial de Python
FROM python:3.12-slim

# Instalar UV (método oficial más rápido)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY pyproject.toml uv.lock* ./

# Instalar dependencias con UV
RUN uv sync --frozen --no-cache

# Copiar el código de la aplicación
COPY . .

# Exponer puerto
EXPOSE 8000

# Ejecutar con Gunicorn + UvicornWorker
CMD ["uv", "run", "gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--workers", "2"]

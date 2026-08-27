# Dockerfile del backend FastAPI.
# Usa la imagen oficial de Python y `uv` para instalar dependencias de forma replicable.
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Instala `uv` para sincronizar el entorno desde pyproject.toml / uv.lock.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copia los archivos de dependencias primero para aprovechar el caché de capas.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Copia el código de la aplicación.
COPY app ./app
COPY alembic ./alembic

# Expone el puerto de Uvicorn (configurable mediante PORT, default 8000).
EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

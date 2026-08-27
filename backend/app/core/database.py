"""Conexión a la base de datos usando SQLModel / SQLAlchemy.

Se utiliza una sesión asincrónica para no bloquear el event loop
de FastAPI. La configuración de la URL proviene de `config.py`.
"""

from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

# `pool_pre_ping` evita errores con conexiones caídas (ej. reinicio de Postgres).
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)


def init_db() -> None:
    """Crea las tablas definidas por los modelos (solo para desarrollo)."""
    from app import models  # noqa: F401  # Importa modelos para registrarlos en el metadata.

    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session]:
    """Dependency que provee una sesión de base de datos por request."""
    with Session(engine) as session:
        yield session

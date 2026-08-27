"""Endpoint de salud.

Permite verificar rápidamente que la aplicación está levantada y
que puede conectarse a la base de datos.
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlmodel import Session

from app.core.database import get_session

router = APIRouter(tags=["health"])

SessionDep = Annotated[Session, Depends(get_session)]


@router.get("/healthcheck")
def healthcheck(db: SessionDep) -> dict[str, str]:
    """Devuelve el estado de la API y la conectividad con la base de datos."""
    db_status = "ok"
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        db_status = "error"

    return {"status": "ok", "database": db_status}

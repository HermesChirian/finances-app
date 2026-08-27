"""Punto de entrada de la aplicación FastAPI.

Levanta la instancia de la API, configura CORS, incluye los routers
de la API v1 y expone el healthcheck raíz.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings


def create_app() -> FastAPI:
    """Fábrica de la aplicación FastAPI."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version="0.1.0",
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # --- CORS ---
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # --- Routers ---
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)

    @app.get("/", tags=["root"])
    def root() -> dict[str, str]:
        return {
            "app": settings.PROJECT_NAME,
            "docs": "/docs",
            "healthcheck": f"{settings.API_V1_PREFIX}/healthcheck",
        }

    return app


app = create_app()

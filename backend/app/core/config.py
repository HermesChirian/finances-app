"""Configuración global de la aplicación.

Lee las variables de entorno mediante Pydantic Settings y provee
una instancia única y tipada de configuración para todo el backend.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuración tipada del backend."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --- General ---
    PROJECT_NAME: str = "Finances API"
    API_V1_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = "development"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # --- Base de datos ---
    DATABASE_URL: str = (
        "postgresql+psycopg://finances:finances_dev_password@localhost:5432/finances"
    )

    # --- CORS ---
    # Orígenes permitidos separados por coma.
    BACKEND_CORS_ORIGINS: str = "http://localhost:5173,http://localhost:3000"

    # --- Autenticación (Clerk) ---
    CLERK_JWKS_URL: str = ""
    CLERK_ISSUER: str = ""
    CLERK_AUDIENCE: str = ""

    @property
    def cors_origins(self) -> list[str]:
        """Devuelve la lista de orígenes CORS permitidos."""
        return [origin.strip() for origin in self.BACKEND_CORS_ORIGINS.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    """Devuelve una instancia cacheada de la configuración."""
    return Settings()


settings = get_settings()

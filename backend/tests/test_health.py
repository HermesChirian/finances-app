"""Pruebas del endpoint de salud."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthcheck_forwards_database_status() -> None:
    """El endpoint /api/v1/healthcheck responde con status ok."""
    response = client.get("/api/v1/healthcheck")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "database" in payload


def test_root_endpoint() -> None:
    """El endpoint raíz responde e informa la ubicación de la documentación."""
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["docs"] == "/docs"
    assert "healthcheck" in payload

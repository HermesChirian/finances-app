# 💰 Personal Finance App — Fullstack Web Application

Aplicación web Fullstack para la gestión eficiente de finanzas personales. Diseñada bajo una arquitectura **monorepo desacoplada**, permite llevar el control de ingresos, gastos operacionales, liquidez total acumulada y administración avanzada de tarjetas de crédito en cuotas.

Mapeada originalmente desde un prototipo funcional en hojas de cálculo y migrada a una pila tecnológica moderna con **FastAPI** y **React (Vite)**.

---

## 🚀 Características Principales

* **Diferenciación de Flujo de Caja y Liquidez:**
  * **Balance Mensual:** Resultado del mes seleccionado (`Ingresos - Gastos`).
  * **Liquidez Total:** Acumulado histórico no afectado por filtros temporales.
  * **% de Ahorro:** Cálculo dinámico sobre ingresos operativos.
* **Gestión de Tarjetas de Crédito y Cuotas:**
  * Registro neutral de consumos a crédito para no alterar el flujo de caja del mes.
  * Cálculo de **Deuda Pendiente** derivado entre consumos acumulados y pagos de resumen efectuados.
  * Proyección automática de compras diferidas en cuotas.
* **Visualización Dinámica:**
  * Métricas principales (KPIs) y gráficos interactivos por categorías de gastos.
* **Arquitectura Multiusuario:**
  * Seguridad y aislamiento de datos con autenticación basada en **Clerk** y verificación de JWT en el backend.

---

## 🛠️ Tech Stack

### Backend
* **Lenguaje:** Python 3.13+
* **Framework:** FastAPI (Uvicorn)
* **ORM:** SQLModel / SQLAlchemy
* **Base de Datos:** PostgreSQL
* **Migraciones:** Alembic
* **Autenticación:** Clerk Auth (verificación de JWT en el backend)

### Frontend
* **Framework:** React + TypeScript (Vite)
* **Estilos:** Tailwind CSS
* **Componentes UI:** Tremor
* **Utilidades:** Day.js, React Hook Form, Zod
* **Autenticación:** Clerk Auth (UI en el frontend)

### Infraestructura & Herramientas
* **Contenedores:** Docker & Docker Compose
* **Control de Versiones:** Git & GitHub (Conventional Commits)

---

## 📁 Estructura del Proyecto (Monorepo)

```text
finanzas-app/
├── backend/                  # API REST construida con FastAPI
│   ├── app/
│   │   ├── api/              # Endpoints y controladores REST
│   │   │   └── v1/           # Router de la API v1
│   │   ├── core/             # Configuración global y seguridad (Clerk)
│   │   ├── models/           # Modelos de base de datos (SQLModel)
│   │   ├── schemas/          # Validadores de entrada/salida (Pydantic)
│   │   ├── services/         # Lógica de negocio y cálculos financieros
│   │   └── main.py           # Punto de entrada de FastAPI
│   ├── alembic/              # Control de versiones de la BD
│   ├── tests/                # Pruebas unitarias e integración (Pytest)
│   └── Dockerfile
├── frontend/                 # Cliente Web en React (Vite)
│   ├── src/
│   │   ├── components/       # Componentes de UI reusables y gráficos
│   │   ├── hooks/            # Custom Hooks de React
│   │   ├── services/         # Cliente de llamadas a la API REST
│   │   ├── store/            # Estado global
│   │   ├── types/            # Definiciones TypeScript
│   │   └── lib/              # Utilidades y formateadores
├── docker-compose.yml        # Infraestructura de desarrollo (PostgreSQL, pgAdmin)
└── docs/                     # Documentación de arquitectura y decisiones
```

---

## 🚀 Guía de Instalación y Ejecución

### Prerrequisitos
* Python 3.13+ y [uv](https://docs.astral.sh/uv/)
* Node.js 20+ y npm
* Docker & Docker Compose (para PostgreSQL en desarrollo)

### 1. Levantar la base de datos

```bash
docker compose up -d
```

Esto levanta **PostgreSQL 16** (puerto `5432`) y **pgAdmin 4** (puerto `5050`).

### 2. Backend

```bash
cd backend
cp .env.example .env        # Completá las variables según corresponda
uv sync                     # Instala las dependencias
uv run uvicorn app.main:app --reload
```

La API queda disponible en `http://localhost:8000`. La documentación interactiva
(Swagger) está en `http://localhost:8000/docs` y el healthcheck en
`http://localhost:8000/api/v1/healthcheck`.

### 3. Frontend

```bash
cd frontend
cp .env.example .env.local  # Completá las variables según corresponda
npm install
npm run dev
```

### Tests y Lint (Backend)

```bash
cd backend
uv run pytest               # Ejecuta la suite de pruebas
uv run ruff check .         # Ejecuta el linter
uv run ruff format --check .  # Verifica el formato
```

---

## 🔐 Variables de Entorno

El detalle completo de variables se encuentra en `backend/.env.example` y
`frontend/.env.example`. Apuntes clave:

* **Backend:** `DATABASE_URL`, `BACKEND_CORS_ORIGINS`, `CLERK_JWKS_URL`, `CLERK_ISSUER`, `CLERK_AUDIENCE`.
* **Frontend:** `VITE_API_URL`, `VITE_CLERK_PUBLISHABLE_KEY`.
* **Nunca** se debe committear un archivo `.env` real con secretos.

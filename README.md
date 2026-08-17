# 💰 Personal Finance App — Fullstack Web Application

Aplicación web Fullstack para la gestión eficiente de finanzas personales. Diseñada bajo una arquitectura **monorepo desacoplada**, permite llevar el control de ingresos, gastos operacionales, liquidez total acumulada y administración avanzada de tarjetas de crédito en cuotas[cite: 1, 2].

Mapeada originalmente desde un prototipo funcional en hojas de cálculo y migrada a una pila tecnológica moderna con **FastAPI** y **Next.js**[cite: 1].

---

## 🚀 Características Principales

* **Diferenciación de Flujo de Caja y Liquidez:**
  * **Balance Mensual:** Resultado del mes seleccionado (`Ingresos - Gastos`)[cite: 1].
  * **Liquidez Total:** Acumulado histórico no afectado por filtros temporales[cite: 1].
  * **% de Ahorro:** Cálculo dinámico sobre ingresos operativos[cite: 1].
* **Gestión de Tarjetas de Crédito y Cuotas:**
  * Registro neutral de consumos a crédito para no alterar el flujo de caja del mes[cite: 1].
  * Cálculo de **Deuda Pendiente** derivado entre consumos acumulados y pagos de resumen efectuados[cite: 1].
  * Proyección automática de compras diferidas en cuotas[cite: 1].
* **Visualización Dinámica:**
  * Métricas principales (KPIs) y gráficos interactivos por categorías de gastos[cite: 1].
* **Arquitectura Multiusuario:**
  * Seguridad y aislamiento de datos con autenticación basada en JWT[cite: 2].

---

## 🛠️ Tech Stack

### Backend
* **Lenguaje:** Python 3.11+
* **Framework:** FastAPI
* **ORM:** SQLModel / SQLAlchemy
* **Base de Datos:** PostgreSQL
* **Migraciones:** Alembic
* **Autenticación:** OAuth2 + JWT (JSON Web Tokens)

### Frontend
* **Framework:** Next.js (App Router) + TypeScript
* **Estilos:** Tailwind CSS
* **Componentes UI:** Shadcn UI
* **Visualización:** Recharts / Tremor

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
│   │   ├── core/             # Configuración global y seguridad JWT
│   │   ├── models/           # Modelos de base de datos (SQLModel)
│   │   ├── schemas/          # Validadores de entrada/salida (Pydantic)
│   │   └── services/         # Lógica de negocio y cálculos financieros
│   ├── alembic/              # Control de versiones de la BD
│   └── main.py               # Punto de entrada de FastAPI
├── frontend/                 # Cliente Web en Next.js
│   ├── src/
│   │   ├── app/              # Rutas e interfaces (App Router)
│   │   ├── components/       # Componentes de UI reusables y gráficos
│   │   ├── hooks/            # Custom Hooks de React
│   │   └── services/         # Cliente de llamadas a la API REST
└── docs/                     # Documentación de arquitectura y 

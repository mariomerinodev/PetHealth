# PetHealth 🐾📱

**PetHealth** es una aplicación móvil inteligente diseñada para simplificar la gestión de la salud y el historial clínico de las mascotas. Utilizando Inteligencia Artificial de alta velocidad, permite escanear cartillas de vacunación, recetas y documentos médicos para digitalizarlos y organizarlos automáticamente, además de gestionar recordatorios de citas y tratamientos.

---

## 🚀 Stack Tecnológico

El proyecto está construido con un enfoque moderno, escalable y optimizado para un alto rendimiento:

- **Frontend (App Móvil):** React Native + Expo + TypeScript (Cross-platform iOS y Android).
- **Backend (API Server):** Python 3.11+ con FastAPI (Validación estricta con Pydantic y alto rendimiento).
- **Inteligencia Artificial:** Groq API (Modelos de visión por computadora de ultra baja latencia).
- **Base de Datos & Almacenamiento:** Supabase (PostgreSQL relacional + Supabase Storage para documentos y fotos).
- **Pagos y Suscripciones:** RevenueCat (Gestión de pasarela de pagos para App Store y Google Play).

---

## 🗺️ Arquitectura del Modelo Entidad-Relación

El sistema se estructura en torno a cuatro entidades principales protegidas por seguridad a nivel de filas (RLS):

1. **`users`**: Propietarios de las cuentas y gestión de roles (`free`/`premium`).
2. **`pets`**: Perfiles de las mascotas asociadas a cada usuario.
3. **`medical_records`**: Historiales médicos estructurados y respaldados por los análisis de la IA (`ai_raw_json`).
4. **`reminders`**: Sistema de alertas automatizadas para vacunas, medicamentos y revisiones.

---

## 🛠️ Estructura del Repositorio

```text
pethealth/
├── backend/          # Servidor FastAPI y modelos de conexión (SQLAlchemy)
├── mobile/           # Aplicación React Native con Expo
├── database/         # Esquemas SQL y migraciones
└── README.md
```

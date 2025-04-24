# Sistema de Gestión de Motos

Sistema integral para la gestión de ventas, inventario y clientes de una concesionaria de motos.

## Características Principales

- **Dashboard Interactivo**: Visualización en tiempo real de KPIs, gráficos y estadísticas
  - Gráfico de estado de motos
  - Análisis de gastos por tipo
  - Seguimiento de ventas mensuales
  - Control de inventario por marca
  - Tabla de ventas recientes
  - Feed de actividades

- **Gestión de Clientes**: Registro y seguimiento de clientes
  - Información de contacto
  - Historial de compras
  - Preferencias y notas

- **Control de Inventario**: Gestión completa de motos
  - Registro de motos nuevas
  - Seguimiento de estado
  - Control de stock
  - Historial de mantenimiento

- **Ventas y Transacciones**: Sistema completo de ventas
  - Registro de ventas
  - Facturación
  - Seguimiento de pagos
  - Reportes financieros

- **Gastos y Mantenimiento**: Control de costos operativos
  - Registro de gastos
  - Categorización de gastos
  - Control de mantenimiento
  - Presupuestos

## Tecnologías Utilizadas

### Frontend
- React 18
- TypeScript
- Material-UI (MUI)
- Recharts para visualización de datos
- React Router para navegación
- Axios para llamadas API
- Framer Motion para animaciones

### Backend
- Node.js
- Express
- TypeScript
- PostgreSQL
- TypeORM
- JWT para autenticación

## Requisitos del Sistema

- Node.js 18 o superior
- PostgreSQL 14 o superior
- NPM 9 o superior

## Instalación

Para una guía detallada de instalación, consulta [INSTALL.md](INSTALL.md).

## Uso

1. Inicia el servidor backend:
```bash
cd backend
npm run dev
```

2. Inicia el frontend:
```bash
cd frontend
npm run dev
```

3. Accede a la aplicación:
- Frontend: http://localhost:3001
- Backend API: http://localhost:3000

## Estructura del Proyecto

```
.
├── backend/           # Servidor Node.js/Express
├── frontend/          # Aplicación React
├── INSTALL.md         # Guía de instalación
├── KNOWLEDGE_BASE.md  # Base de conocimiento
└── README.md          # Este archivo
```

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para soporte o consultas, contacta al equipo de desarrollo. 
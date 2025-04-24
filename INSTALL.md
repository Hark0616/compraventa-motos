# Guía de Instalación

Esta guía te ayudará a configurar y ejecutar el Sistema de Gestión de Motos en tu entorno local.

## Requisitos Previos

- Node.js 18 o superior
- PostgreSQL 14 o superior
- NPM 9 o superior
- Git

## 1. Clonar el Repositorio

```bash
git clone [URL_DEL_REPOSITORIO]
cd Motos
```

## 2. Configuración del Backend

### 2.1 Instalar Dependencias
```bash
cd backend
npm install
```

### 2.2 Configurar Variables de Entorno
Crear un archivo `.env` en la carpeta `backend` con el siguiente contenido:

```env
# Configuración de la Base de Datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=motos_db
DB_HOST=localhost
DB_PORT=5432

# Configuración del Servidor
PORT=3000
NODE_ENV=development

# Configuración de JWT
JWT_SECRET=tu_secreto_jwt
JWT_EXPIRES_IN=24h

# Configuración de CORS
CORS_ORIGIN=http://localhost:3001
```

### 2.3 Configurar la Base de Datos
1. Crear una base de datos PostgreSQL:
```sql
CREATE DATABASE motos_db;
```

2. Ejecutar las migraciones:
```bash
npm run migration:run
```

## 3. Configuración del Frontend

### 3.1 Instalar Dependencias
```bash
cd frontend
npm install
```

### 3.2 Configurar Variables de Entorno
Crear un archivo `.env` en la carpeta `frontend` con el siguiente contenido:

```env
REACT_APP_API_URL=http://localhost:3000/api
REACT_APP_WS_URL=ws://localhost:3000
```

## 4. Iniciar la Aplicación

### 4.1 Iniciar el Backend
```bash
cd backend
npm run dev
```

### 4.2 Iniciar el Frontend
```bash
cd frontend
npm run dev
```

## 5. Acceder a la Aplicación

- Frontend: http://localhost:3001
- Backend API: http://localhost:3000

## 6. Credenciales por Defecto

- Usuario: admin
- Contraseña: admin123

## 7. Solución de Problemas Comunes

### 7.1 Error de Conexión a la Base de Datos
- Verificar que PostgreSQL esté corriendo
- Confirmar credenciales en `.env`
- Verificar permisos de usuario
- Asegurar que la base de datos existe

### 7.2 Errores de CORS
- Verificar configuración en `backend/src/app.ts`
- Confirmar que las URLs en `.env` son correctas
- Asegurar que el frontend está usando el puerto correcto

### 7.3 Problemas de Autenticación
- Verificar token JWT
- Limpiar caché del navegador
- Confirmar que el token no ha expirado

### 7.4 Problemas de Compilación
- Asegurar que todas las dependencias están instaladas
- Verificar versiones de Node.js y NPM
- Limpiar caché de NPM si es necesario:
  ```bash
  npm cache clean --force
  ```

## 8. Estructura de Directorios

```
Motos/
├── backend/
│   ├── src/
│   │   ├── controllers/    # Controladores de la API
│   │   ├── entities/       # Entidades de TypeORM
│   │   ├── middlewares/    # Middlewares de Express
│   │   ├── routes/         # Rutas de la API
│   │   ├── services/       # Lógica de negocio
│   │   └── utils/          # Utilidades
│   ├── .env                # Variables de entorno
│   └── package.json        # Dependencias y scripts
│
├── frontend/
│   ├── src/
│   │   ├── components/     # Componentes React
│   │   ├── pages/         # Páginas de la aplicación
│   │   ├── services/      # Servicios API
│   │   ├── styles/        # Estilos globales
│   │   └── utils/         # Utilidades
│   ├── .env               # Variables de entorno
│   └── package.json       # Dependencias y scripts
│
└── docs/                  # Documentación
```

## 9. Actualizaciones

Para actualizar el sistema a la última versión:

```bash
git pull origin main
cd backend && npm install
cd ../frontend && npm install
```

## 10. Soporte

Para reportar problemas o solicitar ayuda:
1. Revisar la [Base de Conocimiento](KNOWLEDGE_BASE.md)
2. Abrir un issue en el repositorio
3. Contactar al equipo de soporte 
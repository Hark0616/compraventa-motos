# Base de Conocimiento del Sistema

## Arquitectura del Sistema

### Backend
- **Node.js con Express**
  - API RESTful
  - Middleware para autenticación y validación
  - Conexión a PostgreSQL mediante Sequelize

### Frontend
- **React con TypeScript**
  - Componentes funcionales con Hooks
  - Material-UI para la interfaz
  - React Router para navegación
  - React Query para gestión de estado y caché

## Componentes Principales

### Dashboard
- **KPICard**
  - Muestra métricas clave
  - Actualización en tiempo real
  - Diseño responsivo

- **MotoEstadoChart**
  - Gráfico circular de estados
  - Actualización automática
  - Tooltips interactivos

- **GastoTipoChart**
  - Gráfico de barras de gastos
  - Agrupación por categoría
  - Filtros por período

- **RecentSalesTable**
  - Tabla de últimas ventas
  - Formato de moneda local
  - Paginación y ordenamiento

### Gestión de Motos
- **MotoList**
  - Lista paginada
  - Filtros por estado y precio
  - Acciones rápidas

- **MotoForm**
  - Validación de campos
  - Manejo de estados
  - Subida de imágenes

- **MotoDetail**
  - Vista detallada
  - Historial de cambios
  - Acciones contextuales

### Gestión de Clientes
- **ClienteList**
  - Búsqueda avanzada
  - Filtros por estado
  - Exportación a CSV

- **ClienteForm**
  - Validación de datos
  - Autocompletado
  - Historial de compras

### Gestión de Ventas
- **VentaList**
  - Filtros por fecha
  - Cálculo de comisiones
  - Estado de pago

- **VentaForm**
  - Selección de moto
  - Selección de cliente
  - Cálculo automático

### Gestión de Gastos
- **GastoList**
  - Categorización
  - Filtros por tipo
  - Estado de pago

- **GastoForm**
  - Asignación a moto
  - Documentación adjunta
  - Aprobación de gastos

## Tipos de Datos

### Moto
```typescript
interface Moto {
  id: number;
  marca: string;
  modelo: string;
  anio: number;
  kilometraje: number;
  estado: 'DISPONIBLE' | 'RESERVADA' | 'VENDIDA';
  precio: number;
  color: string;
  cilindrada: number;
  observaciones: string;
  fechaVenta?: Date;
}
```

### Cliente
```typescript
interface Cliente {
  id: number;
  nombre: string;
  apellido: string;
  email: string;
  telefono: string;
  direccion: string;
  activo: boolean;
}
```

### Venta
```typescript
interface Venta {
  id: number;
  motoId: number;
  clienteId: number;
  fecha: Date;
  precio: number;
  comision: number;
  estado: 'PENDIENTE' | 'COMPLETADA' | 'CANCELADA';
}
```

### Gasto
```typescript
interface Gasto {
  id: number;
  motoId: number;
  tipo: string;
  monto: number;
  fecha: Date;
  descripcion: string;
  estado: 'PENDIENTE' | 'PAGADO';
}
```

## Servicios API

### MotoService
```typescript
class MotoService {
  obtenerTodas(): Promise<Moto[]>;
  obtenerPorId(id: number): Promise<Moto>;
  crear(moto: Omit<Moto, 'id'>): Promise<Moto>;
  actualizar(id: number, moto: Partial<Moto>): Promise<Moto>;
  eliminar(id: number): Promise<void>;
  obtenerPorEstado(estado: string): Promise<Moto[]>;
  obtenerPorRangoPrecio(minPrecio: number, maxPrecio: number): Promise<Moto[]>;
}
```

### ClienteService
```typescript
class ClienteService {
  obtenerTodos(): Promise<Cliente[]>;
  obtenerPorId(id: number): Promise<Cliente>;
  crear(cliente: Omit<Cliente, 'id'>): Promise<Cliente>;
  actualizar(id: number, cliente: Partial<Cliente>): Promise<Cliente>;
  eliminar(id: number): Promise<void>;
  obtenerHistorialCompras(id: number): Promise<Venta[]>;
}
```

### VentaService
```typescript
class VentaService {
  obtenerTodas(): Promise<Venta[]>;
  obtenerPorId(id: number): Promise<Venta>;
  crear(venta: Omit<Venta, 'id'>): Promise<Venta>;
  actualizar(id: number, venta: Partial<Venta>): Promise<Venta>;
  eliminar(id: number): Promise<void>;
  calcularComision(precio: number): number;
}
```

### GastoService
```typescript
class GastoService {
  obtenerTodos(): Promise<Gasto[]>;
  obtenerPorId(id: number): Promise<Gasto>;
  crear(gasto: Omit<Gasto, 'id'>): Promise<Gasto>;
  actualizar(id: number, gasto: Partial<Gasto>): Promise<Gasto>;
  eliminar(id: number): Promise<void>;
  obtenerPorMoto(motoId: number): Promise<Gasto[]>;
  obtenerPorTipo(tipo: string): Promise<Gasto[]>;
}
```

## Mejores Prácticas

### Desarrollo Frontend
1. **Componentes**
   - Usar componentes funcionales
   - Implementar TypeScript
   - Seguir convenciones de nombrado
   - Mantener componentes pequeños

2. **Estado**
   - Usar React Query para datos remotos
   - Minimizar estado local
   - Implementar memoización cuando sea necesario

3. **Estilos**
   - Usar Material-UI theme
   - Implementar diseño responsivo
   - Mantener consistencia visual

4. **Rendimiento**
   - Implementar lazy loading
   - Optimizar re-renders
   - Usar memo y useCallback

### Desarrollo Backend
1. **API**
   - Seguir convenciones REST
   - Implementar validación
   - Manejar errores apropiadamente

2. **Base de Datos**
   - Usar migraciones
   - Implementar índices
   - Optimizar consultas

3. **Seguridad**
   - Validar inputs
   - Implementar autenticación JWT
   - Usar HTTPS

## Flujos de Trabajo

### Alta de Moto
1. Ingresar datos básicos
2. Subir imágenes
3. Validar información
4. Guardar en sistema
5. Actualizar dashboard

### Proceso de Venta
1. Seleccionar moto
2. Seleccionar cliente
3. Calcular precio y comisión
4. Generar documentación
5. Actualizar estados

### Gestión de Gastos
1. Registrar gasto
2. Asignar a moto
3. Adjuntar documentación
4. Aprobar gasto
5. Actualizar estados

## Mantenimiento

### Backups
- Realizar backup diario de base de datos
- Mantener copias de seguridad por 30 días
- Verificar integridad de backups

### Actualizaciones
- Mantener dependencias actualizadas
- Probar actualizaciones en ambiente de desarrollo
- Documentar cambios

### Monitoreo
- Implementar logs
- Monitorear rendimiento
- Alertas de errores

## Solución de Problemas

### Errores Comunes
1. **Conexión a Base de Datos**
   - Verificar credenciales
   - Comprobar estado del servidor
   - Revisar logs

2. **Problemas de Rendimiento**
   - Optimizar consultas
   - Revisar índices
   - Monitorear recursos

3. **Errores de UI**
   - Verificar consola del navegador
   - Comprobar estado de componentes
   - Revisar props

### Debugging
1. **Frontend**
   - Usar React DevTools
   - Implementar logging
   - Revisar Network tab

2. **Backend**
   - Usar Postman
   - Revisar logs del servidor
   - Implementar tracing

## Recursos Adicionales

### Documentación
- [Material-UI](https://mui.com/)
- [React Query](https://tanstack.com/query/latest)
- [Sequelize](https://sequelize.org/)
- [Express](https://expressjs.com/)

### Herramientas
- VS Code
- Postman
- pgAdmin
- React DevTools

### Comunidad
- Stack Overflow
- GitHub Issues
- Discord Channel

## 1. Dashboard y Visualización de Datos

### 1.1 Componentes del Dashboard
- **KPICard**: Componente reutilizable para mostrar métricas clave
  - Soporta diferentes tipos de datos (números, porcentajes, moneda)
  - Incluye iconos y colores personalizables
  - Animaciones suaves al cargar

- **Gráficos Interactivos**:
  - **MotoEstadoChart**: Gráfico circular que muestra la distribución de motos por estado
    - Actualización en tiempo real
    - Tooltips informativos
    - Leyenda interactiva
  
  - **GastoTipoChart**: Gráfico de barras para análisis de gastos
    - Agrupación por categorías
    - Comparación temporal
    - Exportación de datos
  
  - **VentasMensualesChart**: Gráfico de área para tendencias de ventas
    - Filtrado por períodos
    - Zoom interactivo
    - Líneas de tendencia
  
  - **InventarioChart**: Gráfico de barras para control de inventario
    - Agrupación por marca
    - Filtros dinámicos
    - Indicadores de stock crítico

### 1.2 Tabla de Ventas Recientes
- Ordenamiento por columnas
- Paginación
- Filtros rápidos
- Acciones directas (ver detalles, editar)
- Exportación a CSV

### 1.3 Feed de Actividades
- Notificaciones en tiempo real
- Historial de acciones
- Filtrado por tipo de actividad
- Enlaces directos a registros relacionados

## 2. Gestión de Clientes

### 2.1 Registro de Clientes
- Información básica (nombre, contacto, dirección)
- Documentos de identidad
- Historial de compras
- Preferencias y notas

### 2.2 Seguimiento de Clientes
- Recordatorios de mantenimiento
- Notificaciones de promociones
- Historial de interacciones
- Sistema de fidelización

## 3. Control de Inventario

### 3.1 Registro de Motos
- Información técnica
- Documentación legal
- Fotos y especificaciones
- Historial de mantenimiento

### 3.2 Gestión de Stock
- Alertas de stock bajo
- Control de ubicación
- Registro de movimientos
- Valoración de inventario

## 4. Ventas y Transacciones

### 4.1 Proceso de Venta
- Selección de moto
- Cálculo de financiamiento
- Documentación requerida
- Generación de contrato

### 4.2 Seguimiento de Pagos
- Estado de cuentas
- Recordatorios automáticos
- Historial de pagos
- Reportes de morosidad

## 5. Gastos y Mantenimiento

### 5.1 Control de Gastos
- Categorización automática
- Presupuestos por área
- Análisis de tendencias
- Alertas de sobrepresupuesto

### 5.2 Mantenimiento
- Programación de servicios
- Registro de repuestos
- Historial de reparaciones
- Garantías y seguros

## 6. Configuración y Personalización

### 6.1 Ajustes del Sistema
- Parámetros generales
- Configuración de usuarios
- Roles y permisos
- Personalización de interfaz

### 6.2 Integraciones
- Sistema de facturación
- Plataformas de pago
- Servicios de mensajería
- Herramientas de análisis

## 7. Seguridad y Acceso

### 7.1 Autenticación
- Login seguro
- Recuperación de contraseña
- Verificación en dos pasos
- Sesiones concurrentes

### 7.2 Control de Acceso
- Roles predefinidos
- Permisos personalizados
- Registro de actividades
- Auditoría de cambios

## 8. Reportes y Análisis

### 8.1 Reportes Predefinidos
- Ventas por período
- Inventario actual
- Estado de cuentas
- Análisis de gastos

### 8.2 Reportes Personalizados
- Constructor de reportes
- Exportación en múltiples formatos
- Programación de envíos
- Dashboards personalizados

## 9. Soporte y Mantenimiento

### 9.1 Actualizaciones
- Proceso de actualización
- Backup de datos
- Migración de información
- Rollback de cambios

### 9.2 Solución de Problemas
- Diagnóstico de errores
- Logs del sistema
- Recuperación de datos
- Procedimientos de contingencia

## 10. Mejores Prácticas

### 10.1 Uso del Sistema
- Flujos de trabajo recomendados
- Optimización de procesos
- Tips de productividad
- Atajos de teclado

### 10.2 Administración
- Mantenimiento preventivo
- Monitoreo de rendimiento
- Optimización de recursos
- Planificación de capacidad 
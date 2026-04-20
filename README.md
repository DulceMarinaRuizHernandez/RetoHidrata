# HydroBoost - Aplicación Flet

Aplicación web construida con Flet para gestión de hidratación y operaciones matemáticas.

## 🚀 Despliegue en Render - SOLUCIÓN DEFINITIVA

### Problema resuelto:
Si estabas viendo el error "No se pudo abrir el archivo de requisitos", era porque Render detectaba múltiples proyectos Python en subcarpetas.

### ✅ Solución aplicada:
- Eliminado repositorio Git conflictivo en `mi_proyecto_flet/`
- Creado `.renderignore` para que Render ignore subcarpetas
- Configurado punto de entrada único en `app.py`

## 📋 Pasos para desplegar:

### 1. Inicializar Git (automático)
```bash
# Ejecuta el script incluido:
init_git.bat
```
O manualmente:
```bash
git init
git add .
git commit -m "Initial commit: HydroBoost"
```

### 2. Subir a GitHub/GitLab
```bash
# Crea un repositorio en GitHub y ejecuta:
git remote add origin <URL_DE_TU_REPOSITORIO>
git push -u origin main
```

### 3. Conectar con Render
1. Ve a [Render.com](https://render.com)
2. Conecta tu repositorio Git
3. Render detectará automáticamente:
   - `render.yaml` (configuración principal)
   - `app.py` (punto de entrada)
   - `requirements.txt` (dependencias)

### ⚙️ Configuración automática:
- **Runtime**: Python 3.11.9
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`
- **Puerto**: Automático (variable $PORT)

## 🔧 Desarrollo local

```bash
# Activar entorno virtual
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

## 📁 Estructura del proyecto

```
HydroBoost/
├── app.py              # 🚀 Punto de entrada principal
├── MainReto.py         # Lógica principal
├── requirements.txt    # 📦 Dependencias
├── render.yaml         # ⚙️ Configuración Render
├── Procfile           # 🔄 Alternativa Heroku-style
├── Dockerfile         # 🐳 Docker alternativo
├── runtime.txt        # 🐍 Versión Python
├── .renderignore      # 🚫 Archivos ignorados
├── Views/             # 🖥️ Vistas de UI
├── view/              # 📱 Vistas adicionales
├── controller/        # 🎮 Controladores
└── README.md          # 📖 Esta documentación
```

## 🐛 Solución de problemas

### Error: "No se pudo abrir requirements.txt"
✅ **RESUELTO** - Eliminamos repositorios Git conflictivos en subcarpetas

### Error: "ModuleNotFoundError"
✅ **RESUELTO** - Configurado PYTHONPATH correcto en `app.py`

### Error: "AttributeError: module 'flet' has no attribute..."
✅ **RESUELTO** - Actualizado a sintaxis moderna `ft.run()`

## 🎯 Características

- ✅ Interfaz web moderna con Flet
- ✅ Sistema de navegación por rutas
- ✅ Operaciones matemáticas
- ✅ Gestión de hidratación
- ✅ Despliegue automático en Render
- ✅ Compatible con Docker
@echo off
echo Inicializando repositorio Git para HydroBoost...
cd /d "%~dp0"
git init
git add .
git commit -m "Initial commit: HydroBoost Flet application"
echo.
echo Repositorio Git inicializado correctamente.
echo Ahora puedes hacer push a tu repositorio remoto en GitHub/GitLab/etc.
echo.
echo Para conectar con Render:
echo 1. Crea un repositorio en GitHub
echo 2. Ejecuta: git remote add origin <URL_DEL_REPOSITORIO>
echo 3. Ejecuta: git push -u origin main
echo 4. Conecta el repositorio en Render.com
pause
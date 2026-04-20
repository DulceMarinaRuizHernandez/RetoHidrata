#!/usr/bin/env python3
import os
import sys

# Cambiar al directorio raíz del proyecto
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Agregar el directorio raíz al PYTHONPATH para que los imports funcionen
sys.path.insert(0, script_dir)

# Ejecutar la aplicación principal
exec(open('MainReto.py').read())
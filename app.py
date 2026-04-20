#!/usr/bin/env python3
"""
Aplicación principal de HydroBoost - Punto de entrada para Render
"""
import os
import sys

# Agregar el directorio raíz al PYTHONPATH
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

# Ejecutar MainReto.py directamente
exec(open('MainReto.py').read())
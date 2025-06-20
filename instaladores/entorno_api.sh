#!/bin/bash

cd ../

# Nombre del entorno virtual
VENV_NAME="entorno_api"

# Eliminar carpeta del entorno si existe
if [ -d "$VENV_NAME" ]; then
  echo "Eliminando entorno virtual existente: $VENV_NAME"
  rm -rf "$VENV_NAME"
fi

echo "Creando entorno virtual: $VENV_NAME"
python3 -m venv $VENV_NAME

echo "Activando entorno virtual"
source $VENV_NAME/bin/activate

echo "Instalando librería Docker para Python"
pip install --upgrade pip
pip install docker

chmod -R 777 entorno_api/

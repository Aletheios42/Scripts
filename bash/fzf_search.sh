#!/bin/bash

# Busca directorios no ocultos
DIR=$(find "$HOME" -type d -not -path '*/.*' | fzf -m)

# Verifica si se ha seleccionado un directorio
if [ -n "$DIR" ]; then
  echo "Cambiando al directorio: $DIR"
  cd "$DIR" || {
    echo "Error al cambiar al directorio $DIR."
    return 1
  }
else
  echo "Ruta no válida."
fi

#!/bin/bash

# Función para eliminar archivos/directorios
confirm_delete() {
  for item in "$@"; do
    # Verificar si el archivo o directorio existe
    if [ -e "$item" ]; then
      # Preguntar al usuario si desea eliminar el archivo/directorio
      read -p "¿Deseas eliminar '$item'? [y/N]: " confirm
      if [[ "$confirm" =~ ^[Yy]$ ]]; then
        rm -rf "$item"
        echo "'$item' eliminado."
      else
        echo "'$item' no fue eliminado."
      fi
    else
      echo "'$item' no existe."
    fi
  done
}

# Llamada a la función confirm_delete con todos los argumentos pasados al script
confirm_delete "$@"

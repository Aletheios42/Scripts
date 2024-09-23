#!/bin/bash

DIR=$(find . -type d -not -path '*/\.*' | fzf -m)

if [-n "$DIR"]; then
  echo "cambiando al directorio: $DIR"
  cd "$DIR || return
else
  echo "Invalid Route."

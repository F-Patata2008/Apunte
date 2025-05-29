#!/bin/zsh

cd "$(dirname "$0")"  # Asegura que se ejecute en el directorio del script

# Añadir todos los cambios
git add .

# Verificar si hay cambios para commitear
if git diff --cached --quiet; then
  echo "No hay cambios para commitear."
  exit 0
fi

# Pedir mensaje de commit
echo -n "Mensaje de commit (dejar vacío para 'Auto-commit'): "
read commit_message

# Usar mensaje por defecto si está vacío
if [[ -z "$commit_message" ]]; then
  commit_message="Auto-commit: $(date '+%Y-%m-%d %H:%M:%S')"
fi

# Hacer commit
git commit -m "$commit_message"

# Intentar hacer push
if ! git push -u origin main; then
  echo "❌ Error: No se pudo hacer push. Revisa la conexión o el repositorio remoto."
  exit 1
else
  echo "✅ Push realizado con éxito."
fi


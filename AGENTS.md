# AGENTS.md — Apunte

Colección personal de apuntes y trabajos en LaTeX. No hay build system, tests, linters, ni CI.

## Estructura

- `balti/` — Guías Kumon: LaTeX + generadores Python (`gen.py`, `gen-kumon.py`). Los `.py` producen `.tex` de ejercicios/respuestas.
- `Herramientas/Informes/Informe_0{1,2,3}/` — Informes CC-1000. Cada uno tiene `main.tex` (entrada), `template.tex` (9174 líneas, Pablo Pizarro), `template_config.tex`, `library.bib`.
- `Herramientas/Labs/Lab_*` — Labs CC-1000 (Python, Excel). Algunos subdirectorios son venvs de Python (tienen `.gitignore` con solo `*`).
- `Desafios/` — Reportes CD1100 con bibliografía APA (`Reporte.tex`, `Tarea_3-1/Main.tex`).
- `In/` — Apuntes de enseñanza media (Instituto Nacional). Cada subdirectorio es una asignatura.
- `Prog-Comp/`, `Prog-Cpp/` — Apuntes de programación competitiva (C++/STL, OCI, IOI).
- `Fisica/` — Solo PDFs de referencia (no tocar).
- `Bio/`, `Lukas/` — Documentos independientes.

## Comandos

- **Compilar LaTeX:** Cada `.tex` es independiente. Usar `pdflatex` o `latexmk` sobre el archivo correspondiente.
  ```bash
  cd Herramientas/Informes/Informe_03 && latexmk -pdf main.tex
  ```
- **Regenerar guías Kumon:** Ejecutar `python3 gen.py` dentro del subdirectorio correspondiente (`balti/`, `balti/patas/`, `balti/avanzado/`, `balti/Fracs/`, etc.).
- **Push a GitHub:**
  ```bash
  ./push.sh
  ```
  Pide mensaje de commit (default: timestamp). Hace `git add . && commit && push origin main`.

## Convenciones

- README.md está desactualizado (describe una estructura que no coincide con la actual).
- La licencia es CC BY-NC-ND 4.0 (no modificar).
- No hay CI, tests, linters, formateadores, ni typecheckers.
- No hay `opencode.json` ni otras configs de herramientas.
- Git remote: `git@github.com:F-Patata2008/Apunte.git` — single branch `main`.
- Los commits están en español chileno informal.

# AGENTS.md — Apunte

Colección personal de apuntes y trabajos en LaTeX. No hay build system, tests, linters, ni CI.

## Estructura

- `Algebra/` — Apuntes, controles, pautas y resúmenes de Introducción al Álgebra (MA1101).
- `Calculo/` — Auxiliares, problemas propuestos, resoluciones de problemas (RP) y controles de Cálculo Avanzado (MA1002).
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
- **Push a GitHub:**
  ```bash
  ./push.sh
  ```
  Pide mensaje de commit (default: timestamp). Hace `git add . && commit && push origin main`.

## Convenciones

- README.md está actualizado y documenta todos los módulos con índices locales.
- Cada módulo principal (`Algebra/`, `Calculo/`, `Herramientas/`, `Desafios/`, `Bio/`, `In/`, `Prog-Comp/`, `Lukas/`) cuenta con su propio `README.md` de navegación.
- La licencia es CC BY-NC-ND 4.0 (no modificar).
- No hay CI, tests, linters, formateadores, ni typecheckers.
- No hay `opencode.json` ni otras configs de herramientas.
- Git remote: `git@github.com:F-Patata2008/Apunte.git` — single branch `main`.
- Los commits están en español chileno informal.

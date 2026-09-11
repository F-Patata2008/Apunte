# CD1100 — Desafíos de Innovación en Ingeniería

Material correspondiente al curso **CD1100** de la Facultad de Ciencias Físicas y Matemáticas (**FCFM**) de la **Universidad de Chile**.

El curso se enfoca en el desarrollo de proyectos de ingeniería mediante metodologías de innovación, diseño centrado en el usuario, investigación bibliográfica bajo estándares académicos (citas y referencias en formato APA con BibLaTeX/Biber), entrevistas de validación y prototipado.

---

## 📂 Contenido del Directorio

```
Desafios/
├── Reporte/                  # Informe principal de innovación con bibliografía APA
├── Tarea_3-1/                # Entrega de hito intermedio del proyecto
├── Tarea_4/                  # Informe y transcripción de entrevistas a usuarios
├── Fuentes/                  # Compilación bibliográfica y análisis de fuentes
├── info.pdf                  # Instrucciones y rúbricas del curso
└── Reporte_Formato_Base.pdf  # Pauta y formato base de entrega
```

---

## 📑 Entregas y Documentos

| Carpeta | Descripción | Archivos Clave |
| :--- | :--- | :--- |
| [`Reporte/`](./Reporte/) | Reporte final de proyecto en LaTeX (formato FCFM y APA) | [`Reporte.tex`](./Reporte/Reporte.tex) · [`Reporte.pdf`](./Reporte/Reporte.pdf) · [`library.bib`](./Reporte/library.bib) |
| [`Tarea_3-1/`](./Tarea_3-1/) | Reporte de avance y fundamentación técnica | [`Main.tex`](./Tarea_3-1/Main.tex) · [`tarea 3.pdf`](./Tarea_3-1/tarea%203.pdf) |
| [`Tarea_4/`](./Tarea_4/) | Guía de entrevistas y validación empírica | [`entreivusta.tex`](./Tarea_4/entreivusta.tex) · [`entreivusta.pdf`](./Tarea_4/entreivusta.pdf) |
| [`Fuentes/`](./Fuentes/) | Resumen de fuentes bibliográficas consultadas | [`Fuentes.tex`](./Fuentes/Fuentes.tex) · [`Fuentes.pdf`](./Fuentes/Fuentes.pdf) |

### Compilación con Biber / BibLaTeX
Dado que estos documentos utilizan citas y referencias bibliográficas avanzadas:
```bash
cd Desafios/Reporte
pdflatex Reporte.tex
biber Reporte
pdflatex Reporte.tex
# o alternativamente con latexmk:
latexmk -pdf Reporte.tex
```

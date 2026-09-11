# Biología — Cheat-Sheets y Resúmenes Condensados

Fichas de estudio y hojas de resumen de alta densidad para cursos de biología celular y molecular, diagramadas en **LaTeX** con cajas estilizadas mediante `tcolorbox` y esquemas `tikz`.

---

## 📂 Contenido

```
Bio/
├── EP1/   # Evaluación Periódica 1: Biología Celular y Bioenergética
├── EP2/   # Evaluación Periódica 2: Biología Molecular y Expresión Génica
└── EP3/   # Evaluación Periódica 3: Resumen Integral del Curso
```

---

## 📑 Detalle por Unidad

| Unidad | Temáticas Principales | Documentos |
| :--- | :--- | :--- |
| [`EP1/`](./EP1/) | Teoría celular, organelos eucariontes y procariontes, transporte transmembrana, metabolismo celular, respiración celular y fotosíntesis. | [`Cheat-Sheet.tex`](./EP1/Cheat-Sheet.tex) · [`Cheat-Sheet.pdf`](./EP1/Cheat-Sheet.pdf) |
| [`EP2/`](./EP2/) | Estructura del ADN y ARN, replicación, transcripción, traducción proteica, código genético y regulación de la expresión génica. | [`cheat2.tex`](./EP2/cheat2.tex) · [`cheat2.pdf`](./EP2/cheat2.pdf) |
| [`EP3/`](./EP3/) | Resumen global condensado para examen: integración metabólica, señalización celular, genética y fisiología celular. | [`Cheat-Full.tex`](./EP3/Cheat-Full.tex) · [`Cheat-Full.pdf`](./EP3/Cheat-Full.pdf) |

### Compilación
```bash
cd Bio/EP1
pdflatex Cheat-Sheet.tex
```

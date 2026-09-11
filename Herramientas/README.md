# CC1000 — Herramientas Computacionales para Ingeniería y Ciencias

Material del curso **CC1000** impartido en la Facultad de Ciencias Físicas y Matemáticas (**FCFM**) de la **Universidad de Chile**.

El curso abarca el uso avanzado de herramientas computacionales para la resolución de problemas en ingeniería y ciencias: composición tipográfica científica con **LaTeX**, análisis numérico y manipulación de datos con **Python** (Pandas, Matplotlib, NumPy, Jupyter), modelamiento en **planillas de cálculo** (Excel), y fundamentos de **inteligencia artificial y ética**.

---

## 📂 Estructura del Directorio

El contenido está dividido en 4 secciones principales:

```
Herramientas/
├── Informes/     # Informes temáticos formales en LaTeX (plantilla Pablo Pizarro)
├── Labs/         # Laboratorios prácticos (Python, Excel, Jupyter, datasets)
├── TP/           # Trabajos Previos (cuestionarios, código preliminar y reportes)
├── TPL/          # Tareas Post-Laboratorio (reportes técnicos finales en LaTeX)
└── images -> ../images  # Enlace relativo a imágenes y recursos gráficos comunes
```

---

## 📑 1. Informes (`Informes/`)

Informes extensos elaborados en LaTeX utilizando la plantilla oficial de Pablo Pizarro.

| Directorio | Título / Tema | Archivo Principal |
| :--- | :--- | :--- |
| [`Informe_01/`](./Informes/Informe_01/) | Informe Temático 1 | [`main.tex`](./Informes/Informe_01/main.tex) · [`main.pdf`](./Informes/Informe_01/main.pdf) |
| [`Informe_02/`](./Informes/Informe_02/) | Informe Temático 2 | [`main.tex`](./Informes/Informe_02/main.tex) · [`main.pdf`](./Informes/Informe_02/main.pdf) |
| [`Informe_03/`](./Informes/Informe_03/) | Informe Temático 3 | [`main.tex`](./Informes/Informe_03/main.tex) · [`main.pdf`](./Informes/Informe_03/main.pdf) |
| [`Informe_04/`](./Informes/Informe_04/) | Informe Temático 4 | [`main.tex`](./Informes/Informe_04/main.tex) · [`main.pdf`](./Informes/Informe_04/main.pdf) |
| [`TemplateInformeTematico/`](./Informes/TemplateInformeTematico/) | Plantilla base configurable | [`main.tex`](./Informes/TemplateInformeTematico/main.tex) |

### Compilación de Informes
Cada informe es autónomo. Para compilar cualquiera de ellos:
```bash
cd Herramientas/Informes/Informe_03
latexmk -pdf main.tex
```

---

## 🧪 2. Laboratorios Prácticos (`Labs/`)

Sesiones prácticas de desarrollo computacional:

- **`Lab_01` a `Lab_03`**: Fundamentos de LaTeX, tablas, ecuaciones y gráficos.
- **`Lab_04` a `Lab_06`**: Planillas de cálculo avanzadas (funciones lógicas, búsqueda, tablas dinámicas).
- **`Lab_07` a `Lab_10`**: Programación científica en Python (estructuras de datos, funciones, algoritmos, regresión lineal, Pandas y visualización con Matplotlib).
- **`Lab_11`**: Introducción a herramientas de Inteligencia Artificial aplicada.

---

## 📝 3. Trabajos Previos (`TP/`)

Guías y ejercicios preparatorios previos a cada sesión de laboratorio (`TP_LAB_01` a `TP_LAB_12`), con enunciados oficiales, soluciones en código y documentos complementarios sobre ética e IA.

---

## 📊 4. Reportes Post-Laboratorio (`TPL/`)

Informes de resultados de laboratorio (`TPL_01` a `TPL_09`) elaborados en LaTeX:

- [`TPL_01`](./TPL/TPL_01/): Primer reporte experimental ([`post.pdf`](./TPL/TPL_01/post.pdf))
- [`TPL_03`](./TPL/TPL_03/): Modelamiento de datos ([`Main.pdf`](./TPL/TPL_03/Main.pdf))
- [`TPL_04`](./TPL/TPL_04/): Planillas de cálculo I ([`TP_04.pdf`](./TPL/TPL_04/TP_04.pdf))
- [`TPL_05`](./TPL/TPL_05/): Planillas de cálculo II ([`Main.pdf`](./TPL/TPL_05/Main.pdf))
- [`TPL_06`](./TPL/TPL_06/): Planillas de cálculo III ([`Main.pdf`](./TPL/TPL_06/Main.pdf))
- [`TPL_07`](./TPL/TPL_07/): Introducción a Python ([`TPL_07.pdf`](./TPL/TPL_07/TPL_07.pdf))
- [`TPL_08`](./TPL/TPL_08/): Estructuras de control y funciones ([`TPL_08.pdf`](./TPL/TPL_08/TPL_08.pdf))
- [`TPL_09`](./TPL/TPL_09/): Regresión y análisis de datos en Python ([`TPL_09.pdf`](./TPL/TPL_09/TPL_09.pdf))

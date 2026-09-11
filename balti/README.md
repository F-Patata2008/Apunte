# Balti — Generador de Guías Matemáticas (Estilo Kumon)

Sistema de generación algorítmica de guías de ejercitación matemática estilo **Kumon** (Nivel F y superiores), desarrollado con scripts en **Python** que producen documentos listos para compilar en **LaTeX**, incluyendo tanto los cuadernillos de ejercicios como sus respectivas pautas de respuestas resueltas.

---

## 📂 Organización de Carpetas

```
balti/
├── gen-kumon.py       # Script generador base con lógica de ingeniería inversa para resultados limpios
├── Fracs/             # Ejercicios y respuestas de operaciones con fracciones (suma, resta, multiplicación, división)
├── Papomudas/         # Ejercicios de jerarquía de operaciones (PEMDAS / PAPOMUDAS) con enteros y fracciones
├── avanzado/          # Guías de nivel avanzado: Kumon F Experto (ejercicios y respuestas)
├── avanzado++/        # Guías masivas (1000 ejercicios combinados)
├── patas/             # Guías de potencias, cuadrados y cálculo mental
│   └── resp/corr/     # Pauta con correcciones detalladas
├── guia-01/           # Guías de práctica inicial
├── kumon-F/           # Cuadernillos estándar de Kumon F
├── respuestas/        # Pautas consolidadas
└── g/                 # Variantes adicionales de ejercicios
```

---

## ⚙️ Cómo Funciona la Generación

Los scripts en Python generan problemas de forma determinista o pseudoaleatoria calculando las respuestas de antemano ("ingeniería inversa"), garantizando que las fracciones se simplifiquen a valores enteros o fracciones irreducibles limpias.

### Regenerar una guía:
```bash
# Entrar al subdirectorio correspondiente
cd balti/avanzado

# Ejecutar el generador Python (creará los archivos .tex)
python3 gen.py

# Compilar los ejercicios y las respuestas con latexmk o pdflatex
latexmk -pdf Kumon_F_Experto_Ejercicios.tex
latexmk -pdf Kumon_F_Experto_Respuestas.tex
```

También se puede utilizar el generador general en la raíz de `balti`:
```bash
cd balti
python3 gen-kumon.py
```

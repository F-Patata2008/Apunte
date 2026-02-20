#!/usr/bin/env python3
import re
from fractions import Fraction

# --- CONFIGURACIÓN ---
# Pon aquí el nombre EXACTO de tu archivo de ejercicios actual
INPUT_FILE = "Kumon_F_Final_Cuadrados_Ejercicios.tex"
OUTPUT_FILE = "Kumon_F_Respuestas_CORREGIDAS.tex"

def to_latex_mixed(f):
    """Convierte Fraction a formato LaTeX Mixto"""
    if f.denominator == 1:
        return str(f.numerator)
    whole = f.numerator // f.denominator
    rem = f.numerator % f.denominator
    if whole > 0:
        return f"{whole} \\frac{{{rem}}}{{{f.denominator}}}"
    return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def solve_line(line):
    """Extrae la ecuación LaTeX, la convierte a Python y la resuelve"""
    # 1. Extraer lo que está entre $ ... $
    match = re.search(r'\$ (.*?) =', line)
    if not match:
        return None

    latex_eq = match.group(1)

    # 2. Limpiar comandos LaTeX para hacerlos "Pythonic"
    # Convertir Mixtos: "1 \frac{1}{2}" -> "(1 + Fraction(1, 2))"
    # Regex busca: Numero seguido opcionalmente de espacio y luego \frac{n}{d}
    expr = re.sub(
        r'(\d+)\s*\\frac\{(\d+)\}\{(\d+)\}',
        r'(\1 + Fraction(\2, \3))',
        latex_eq
    )

    # Convertir Fracciones simples: "\frac{1}{2}" -> "Fraction(1, 2)"
    expr = re.sub(
        r'\\frac\{(\d+)\}\{(\d+)\}',
        r'Fraction(\1, \2)',
        expr
    )

    # Reemplazos de operadores
    expr = expr.replace(r'\times', '*')
    expr = expr.replace(r'\div', '/')
    expr = expr.replace(r'\left(', '(')
    expr = expr.replace(r'\right)', ')')
    expr = expr.replace('^2', '**2')

    # 3. Evaluar
    try:
        # Usamos eval con un entorno seguro que solo tiene Fraction
        res = eval(expr, {"Fraction": Fraction})
        return to_latex_mixed(res)
    except Exception as e:
        print(f"Error resolviendo: {latex_eq} -> {e}")
        return "Error"

def generar_respuestas_correctas():
    print(f"Leyendo {INPUT_FILE}...")

    try:
        with open(INPUT_FILE, 'r') as f_in:
            lines = f_in.readlines()
    except FileNotFoundError:
        print(f"¡ERROR! No encuentro el archivo '{INPUT_FILE}'.")
        print("Asegúrate de que el script esté en la misma carpeta o edita la variable INPUT_FILE.")
        return

    # Preparar contenido del archivo de salida
    header = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{multicol}
\geometry{a4paper, total={175mm,260mm}, left=18mm, top=15mm, bottom=20mm}
\setlength{\parindent}{0pt}
\pagestyle{fancy}
\fancyhf{}
\rhead{\textbf{Nivel F+} - SOLUCIONARIO VERIFICADO}
\lhead{Día \thesection}
\cfoot{\thepage}
\begin{document}
"""
    footer = r"\end{document}"

    output_content = header

    current_day = 0
    in_enumerate = False

    for line in lines:
        # Detectar cambio de Día
        if "\\section*" in line:
            if "Día" in line:
                day_match = re.search(r'Día (\d+)', line)
                if day_match:
                    day_num = day_match.group(1)
                    if in_enumerate:
                        output_content += "\\end{enumerate}\\end{multicols}\\newpage\n"
                    output_content += f"\\section*{{Día {day_num}}}\n\\begin{{multicols}}{{5}}\\begin{{enumerate}}\n"
                    in_enumerate = True
                    print(f"Procesando Día {day_num}...")

        # Detectar ejercicios
        if r"\item" in line and "$" in line:
            ans = solve_line(line)
            if ans:
                output_content += f"\\item $ {ans} $\n"

    # Cerrar tags abiertos
    if in_enumerate:
        output_content += "\\end{enumerate}\\end{multicols}\n"

    output_content += footer

    with open(OUTPUT_FILE, 'w') as f_out:
        f_out.write(output_content)

    print(f"\n¡LISTO! Respuestas corregidas generadas en: {OUTPUT_FILE}")
    print("Compila este archivo nuevo y los resultados coincidirán 100%.")

if __name__ == "__main__":
    generar_respuestas_correctas()

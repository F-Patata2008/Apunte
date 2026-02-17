#!/usr/bin/env python3
import random
import os
from fractions import Fraction

# --- CONFIGURACIÓN ---
TOTAL_DIAS = 20
EJERCICIOS_POR_DIA = 50
EJERCICIOS_POR_PAGINA = 10
ARCHIVO_EJ = "Kumon_F_1000_Ejercicios.tex"
ARCHIVO_RES = "Kumon_F_1000_Respuestas.tex"

def to_latex_frac(f):
    """Convierte Fraction a LaTeX (Simplificado/Mixto)"""
    if f.denominator == 1: return str(f.numerator)
    entero = f.numerator // f.denominator
    resto = f.numerator % f.denominator
    if entero > 0:
        return f"{entero} \\frac{{{resto}}}{{{f.denominator}}}"
    return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def to_latex_dec(val):
    """Formatea float: 1 decimal, sin .0 si es entero"""
    val = round(val, 1)
    return str(int(val)) if val.is_integer() else str(val)

# --- GENERADORES ---

def gen_decimal_complex():
    """Base^Exp +/- (Dec * Dec +/- Dec)"""
    base = random.randint(2, 5)
    exp = 2 if base > 3 else 3
    val_pot = base ** exp

    # Paréntesis: (A * B - C)
    a = random.choice([0.5, 1.2, 1.5, 2.0, 2.5, 0.2])
    b = random.randint(2, 8)
    c = round(random.uniform(0.1, 1.5), 1)

    inner_val = (a * b) - c
    inner_tex = f"({a} \\times {b} - {c})"

    # Operación externa: Asegurar >= 0
    if random.choice(['+', '-']) == '+' or val_pot < inner_val:
        res = val_pot + inner_val
        tex = f"{base}^{{{exp}}} + {inner_tex}"
    else:
        res = val_pot - inner_val
        tex = f"{base}^{{{exp}}} - {inner_tex}"

    return tex, to_latex_dec(res)

def gen_fraction_complex():
    """Base^Exp +/- (Frac +/- Frac)"""
    base = random.randint(2, 5)
    exp = random.choice([2, 3]) if base < 4 else 2
    val_pot = base ** exp

    den = random.choice([2, 3, 4, 5, 6, 8, 10])
    f1 = Fraction(random.randint(1, den*2), den)
    f2 = Fraction(random.randint(1, den), den)

    if random.choice(['+', '-']) == '+':
        val_inner = f1 + f2
        inner_tex = f"(\\frac{{{f1.numerator}}}{{{f1.denominator}}} + \\frac{{{f2.numerator}}}{{{f2.denominator}}})"
    else:
        if f1 < f2: f1, f2 = f2, f1
        val_inner = f1 - f2
        inner_tex = f"(\\frac{{{f1.numerator}}}{{{f1.denominator}}} - \\frac{{{f2.numerator}}}{{{f2.denominator}}})"

    if random.choice(['+', '-']) == '+' or val_pot < val_inner:
        res = val_pot + val_inner
        tex = f"{base}^{{{exp}}} + {inner_tex}"
    else:
        res = val_pot - val_inner
        tex = f"{base}^{{{exp}}} - {inner_tex}"

    return tex, to_latex_frac(res)

# --- CORE ---

def run():
    header = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{multicol}
\geometry{a4paper, total={175mm,260mm}, left=18mm, top=20mm, bottom=20mm}
\pagestyle{fancy}
\fancyhf{}
\rhead{Nivel F - 1000 Practice}
\cfoot{\thepage}
\begin{document}
"""

    prob_body = header
    res_body = header.replace("Practice", "Solucionario")

    for dia in range(1, TOTAL_DIAS + 1):
        prob_body += f"\\section*{{Día {dia}: Entrenamiento Intensivo}}\n\\begin{{enumerate}}\n"
        res_body += f"\\section*{{Día {dia}}}\n\\begin{{multicols}}{{5}}\\begin{{enumerate}}\n"

        for i in range(1, EJERCICIOS_POR_DIA + 1):
            # Mix 50/50
            q, a = gen_decimal_complex() if i % 2 == 0 else gen_fraction_complex()

            prob_body += f"\\item \\large $ {q} = $ \\vspace{{1.6cm}}\n"
            res_body += f"\\item $ {a} $\n"

            if i % EJERCICIOS_POR_PAGINA == 0 and i != EJERCICIOS_POR_DIA:
                prob_body += "\\newpage\n"

        prob_body += "\\end{enumerate}\\newpage\n"
        res_body += "\\end{enumerate}\\end{multicols}\\newpage\n"

    prob_body += "\\end{document}"
    res_body += "\\end{document}"

    with open(ARCHIVO_EJ, 'w') as f: f.write(prob_body)
    with open(ARCHIVO_RES, 'w') as f: f.write(res_body)
    print(f"-> Generados {TOTAL_DIAS*EJERCICIOS_POR_DIA} ejercicios en {ARCHIVO_EJ}")

if __name__ == "__main__":
    run()

#!/usr/bin/env python3
import random
from fractions import Fraction

# --- CONFIGURACIÓN ---
TOTAL_DIAS = 20
EJERCICIOS_POR_DIA = 50
ARCHIVO_EJ = "Kumon_F_Final_Cuadrados_Ejercicios.tex"
ARCHIVO_RES = "Kumon_F_Final_Cuadrados_Respuestas.tex"

def to_mixed_latex(f):
    """Convierte Fraction a LaTeX Mixto Simplificado"""
    if f.denominator == 1: return str(f.numerator)
    w = f.numerator // f.denominator
    rem = f.numerator % f.denominator
    if w > 0: return f"{w} \\frac{{{rem}}}{{{f.denominator}}}"
    return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def gen_small_mixed():
    """Genera Mixto pequeño para potencias (evita resultados gigantes)"""
    w = random.randint(1, 2)
    d = random.choice([2, 3, 4])
    n = 1 # Usamos numerador 1 para que al elevar no de números locos
    return f"{w} \\frac{{{n}}}{{{d}}}", Fraction(w * d + n, d)

def gen_any_mixed():
    """Genera Mixto estándar"""
    w = random.randint(1, 3)
    d = random.choice([2, 3, 4, 5])
    n = random.randint(1, d - 1)
    return f"{w} \\frac{{{n}}}{{{d}}}", Fraction(w * d + n, d)

def gen_simple_f():
    """Genera Fracción propia amigable"""
    d = random.choice([2, 3, 4, 5, 10])
    n = random.randint(1, d - 1)
    return f"\\frac{{{n}}}{{{d}}}", Fraction(n, d)

# --- MODELOS DE EJERCICIOS ---

def modelo_cuadrado_mixto():
    """Estructura: (Mixto)^2 +/- Fracción"""
    m_tex, m_val = gen_small_mixed()
    f_tex, f_val = gen_simple_f()
    
    op = random.choice(['+', '-'])
    res_sq = m_val**2
    
    if op == '-':
        if res_sq < f_val: res_sq, f_val = f_val, res_sq # Evitar negativos
        res = res_sq - f_val
        q = f"\\left( {m_tex} \\right)^2 - {f_tex}"
    else:
        res = res_sq + f_val
        q = f"\\left( {m_tex} \\right)^2 + {f_tex}"
    return q, to_mixed_latex(res)

def modelo_mixto_por_cuadrado():
    """Estructura: Fracción * (Mixto)^2"""
    m_tex, m_val = gen_small_mixed()
    f_tex, f_val = f"\\frac{{1}}{{{random.choice([2, 3])}}}", Fraction(1, random.choice([2,3]))
    
    res = f_val * (m_val**2)
    q = f"{f_tex} \\times \\left( {m_tex} \\right)^2"
    return q, to_mixed_latex(res)

def modelo_friendly_combo():
    """Estructura: (F1 +/- F2) * Mixto (El del turno anterior)"""
    d1 = random.choice([2, 3, 4, 5])
    d2 = random.choice([2, 3, 5])
    f1_val = Fraction(random.randint(1, d1-1), d1)
    f2_val = Fraction(random.randint(1, d2-1), d2)
    m_tex, m_val = gen_any_mixed()
    
    if f1_val < f2_val: f1_val, f2_val = f2_val, f1_val
    
    res = (f1_val - f2_val) * m_val
    q = f"\\left( \\frac{{{f1_val.numerator}}}{{{f1_val.denominator}}} - \\frac{{{f2_val.numerator}}}{{{f2_val.denominator}}} \\right) \\times {m_tex}"
    return q, to_mixed_latex(res)

# --- GENERADOR PRINCIPAL ---

def run():
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
\rhead{\textbf{Nivel F+} - Mixtos y Cuadrados}
\lhead{Día \thesection}
\cfoot{\thepage}
\begin{document}
"""
    prob_body = header
    res_body = header.replace("Mixtos y Cuadrados", "SOLUCIONARIO")
    
    for dia in range(1, TOTAL_DIAS + 1):
        prob_body += f"\\section*{{Día {dia}: Potencias y Combinados}}\n\\begin{{enumerate}}\n"
        res_body += f"\\section*{{Día {dia}}}\n\\begin{{multicols}}{{5}}\\begin{{enumerate}}\n"
        
        for i in range(1, EJERCICIOS_POR_DIA + 1):
            # Elegir modelo: 40% cuadrados, 60% combinados amigables
            roll = random.random()
            if roll < 0.25:
                q, a = modelo_cuadrado_mixto()
            elif roll < 0.40:
                q, a = modelo_mixto_por_cuadrado()
            else:
                q, a = modelo_friendly_combo()
            
            prob_body += f"\\item \\large $ {q} = $ \\vspace{{1.6cm}}\n"
            res_body += f"\\item $ {a} $\n"
            
            if i % 10 == 0 and i != EJERCICIOS_POR_DIA:
                prob_body += "\\newpage\n"
        
        prob_body += "\\end{enumerate}\\newpage\n"
        res_body += "\\end{enumerate}\\end{multicols}\\newpage\n"
        
    prob_body += "\\end{document}"
    res_body += "\\end{document}"
    
    with open(ARCHIVO_EJ, 'w') as f: f.write(prob_body)
    with open(ARCHIVO_RES, 'w') as f: f.write(res_body)
    print(f"-> 1000 ejercicios listos en {ARCHIVO_EJ}")

if __name__ == "__main__":
    run()

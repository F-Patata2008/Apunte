#!/usr/bin/env python3
import random
from fractions import Fraction

# --- CONFIGURACIÓN ---
TOTAL_DIAS = 20
EJERCICIOS_POR_DIA = 50
ARCHIVO_EJ = "Kumon_F_Final_1000_Ejercicios.tex"
ARCHIVO_RES = "Kumon_F_Final_1000_Respuestas.tex"

# --- UTILIDADES DE FRACCIONES ---

def to_mixed_latex(f):
    """Convierte objeto Fraction a LaTeX estilo Mixto Simplificado"""
    if f.denominator == 1:
        return str(f.numerator)
    num = f.numerator
    den = f.denominator
    whole = num // den
    remain = num % den
    if whole > 0:
        return f"{whole} \\frac{{{remain}}}{{{den}}}"
    return f"\\frac{{{num}}}{{{den}}}"

def gen_random_mixed():
    """Genera (LaTeX_string, Fraction_object) de un número mixto"""
    w = random.randint(1, 3)
    d = random.choice([2, 3, 4, 5, 6])
    n = random.randint(1, d - 1)
    f = Fraction(w * d + n, d)
    return f"{w} \\frac{{{n}}}{{{d}}}", f

def gen_random_simple_frac():
    """Genera (LaTeX_string, Fraction_object) de una fracción propia"""
    d = random.choice([2, 3, 4, 5, 6, 8, 10])
    n = random.randint(1, d - 1)
    return f"\\frac{{{n}}}{{{d}}}", Fraction(n, d)

# --- GENERADORES DE MODELOS ---

def modelo_1():
    """Ej: (2/5 + 3 1/2) + 3 1/2 * 1 1/6"""
    # (F1 + M1) + M2 * M3
    f1_tex, f1_val = gen_random_simple_frac()
    m1_tex, m1_val = gen_random_mixed()
    m2_tex, m2_val = gen_random_mixed()
    m3_tex, m3_val = gen_random_mixed()
    
    q = f"({f1_tex} + {m1_tex}) + {m2_tex} \\times {m3_tex}"
    res = (f1_val + m1_val) + (m2_val * m3_val)
    return q, to_mixed_latex(res)

def modelo_2():
    """Ej: (1 1/2)^2 + (1/3 + 2 1/2)"""
    # (M1)^2 + (F1 + M2)
    m1_tex, m1_val = gen_random_mixed()
    f1_tex, f1_val = gen_random_simple_frac()
    m2_tex, m2_val = gen_random_mixed()
    
    # Limitar base de potencia para que no sea inmanejable
    if m1_val > 3: # Si el mixto es muy grande, bajarlo
        m1_tex, m1_val = "1 \\frac{1}{2}", Fraction(3, 2)
        
    q = f"({m1_tex})^2 + ({f1_tex} + {m2_tex})"
    res = (m1_val**2) + (f1_val + m2_val)
    return q, to_mixed_latex(res)

def modelo_3():
    """Ej: Entero * Fracción + (Mixto)^2"""
    entero = random.randint(2, 5)
    f1_tex, f1_val = gen_random_simple_frac()
    m1_tex, m1_val = "1 \\frac{1}{2}", Fraction(3, 2) # Base fija simple para potencias
    
    q = f"{entero} \\times {f1_tex} + ({m1_tex})^2"
    res = (entero * f1_val) + (m1_val**2)
    return q, to_mixed_latex(res)

# --- CORE GENERATOR ---

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
\rhead{\textbf{Nivel F/G} - Fracciones y Potencias Mixtas}
\cfoot{\thepage}
\begin{document}
"""
    
    prob_body = header
    res_body = header.replace("Fracciones", "SOLUCIONARIO")
    
    print(f"Generando 1000 ejercicios en {TOTAL_DIAS} días...")

    for dia in range(1, TOTAL_DIAS + 1):
        prob_body += f"\\section*{{Día {dia}: Operaciones Combinadas de Mixtos}}\n\\begin{{enumerate}}\n"
        res_body += f"\\section*{{Día {dia}}}\n\\begin{{multicols}}{{2}}\\begin{{enumerate}}\n"
        
        for i in range(1, EJERCICIOS_POR_DIA + 1):
            # Seleccionar modelo aleatorio
            m = random.choice([modelo_1, modelo_2, modelo_3])
            q, a = m()
            
            prob_body += f"\\item \\large $ {q} = $ \\vspace{{1.8cm}}\n"
            res_body += f"\\item $ {a} $\n"
            
            # 10 ejercicios por página
            if i % 10 == 0 and i != EJERCICIOS_POR_DIA:
                prob_body += "\\newpage\n"
        
        prob_body += "\\end{enumerate}\\newpage\n"
        res_body += "\\end{enumerate}\\end{multicols}\\newpage\n"
        
    prob_body += "\\end{document}"
    res_body += "\\end{document}"
    
    with open(ARCHIVO_EJ, 'w') as f: f.write(prob_body)
    with open(ARCHIVO_RES, 'w') as f: f.write(res_body)
    print("¡Hecho! Archivos listos para pdflatex.")

if __name__ == "__main__":
    run()

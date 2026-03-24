#!/usr/bin/env python3
import random
from fractions import Fraction

# --- CONFIGURACIÓN ---
TOTAL_DIAS = 10
EJERCICIOS_POR_DIA = 50
ARCHIVO_EJ = "Kumon_G_Progresivo_Ejercicios.tex"
ARCHIVO_RES = "Kumon_G_Progresivo_Respuestas.tex"

# --- UTILIDADES MATEMÁTICAS ---
def format_mixed(f):
    """Convierte objeto Fraction a string Mixto para las respuestas"""
    if f.denominator == 1:
        return str(f.numerator)
    if f.numerator < 0:
        sign = "-"
        num = abs(f.numerator)
    else:
        sign = ""
        num = f.numerator
        
    w = num // f.denominator
    rem = num % f.denominator
    if w > 0:
        return f"{sign}{w} \\frac{{{rem}}}{{{f.denominator}}}"
    return f"{sign}\\frac{{{num}}}{{{f.denominator}}}"

def get_f():
    """Genera fracción propia o impropia simple, asegurando que no sea entera"""
    while True:
        d = random.choice([2, 3, 4, 5, 6, 8, 10])
        n = random.randint(1, d + 4)
        frac = Fraction(n, d)
        if frac.denominator != 1:
            return frac, f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"

def get_m():
    """Genera un número mixto"""
    w = random.randint(1, 3)
    d = random.choice([2, 3, 4, 5, 8])
    n = random.randint(1, d - 1)
    frac = Fraction(n, d)
    val = w + frac
    return val, f"{w} \\frac{{{frac.numerator}}}{{{frac.denominator}}}"

# --- PLANTILLAS (De menor a mayor dificultad) ---

def t1():
    """ Nivel 1: F * (M - F) -> Estilo pedido por ti """
    f1, f1_tex = get_f()
    m1, m1_tex = get_m()
    f2, f2_tex = get_f()
    if m1 < f2: m1, f2 = f2, m1
    val = f1 * (m1 - f2)
    tex = f"{f1_tex} \\times \\left( {m1_tex} - {f2_tex} \\right)"
    return val, tex

def t2():
    """ Nivel 1: F * F + F """
    f1, f1_tex = get_f()
    f2, f2_tex = get_f()
    f3, f3_tex = get_f()
    val = f1 * f2 + f3
    tex = f"{f1_tex} \\times {f2_tex} + {f3_tex}"
    return val, tex

def t3():
    """ Nivel 2: F + (F - F) """
    f1, f1_tex = get_f()
    f2, f2_tex = get_f()
    f3, f3_tex = get_f()
    if f2 < f3: f2, f3 = f3, f2
    val = f1 + (f2 - f3)
    tex = f"{f1_tex} + \\left( {f2_tex} - {f3_tex} \\right)"
    return val, tex

def t4():
    """ Nivel 3: (M - M) * M """
    m1, m1_tex = get_m()
    m2, m2_tex = get_m()
    m3, m3_tex = get_m()
    if m1 < m2: m1, m2 = m2, m1
    val = (m1 - m2) * m3
    tex = f"\\left( {m1_tex} - {m2_tex} \\right) \\times {m3_tex}"
    return val, tex

def t5():
    """ Nivel 4:[F / (F - F)] - F * F """
    f1, f1_tex = get_f()
    f2, f2_tex = get_f()
    f3, f3_tex = get_f()
    if f2 <= f3: f2 += f3 # Evita división por cero y negativos
    f4, f4_tex = get_f()
    f5, f5_tex = get_f()
    
    val_left = f1 / (f2 - f3)
    val_right = f4 * f5
    op = '-' if val_left > val_right else '+'
    val = (val_left - val_right) if op == '-' else (val_left + val_right)
    
    tex = f"\\left[ {f1_tex} \\div \\left( {f2_tex} - {f3_tex} \\right) \\right] {op} {f4_tex} \\times {f5_tex}"
    return val, tex

def t6():
    """ Nivel 5: F(1 - F) / (F * F) + F * F """
    f1, f1_tex = get_f()
    f2, f2_tex = get_f()
    if f2 >= 1: f2 = Fraction(1, 2); f2_tex = "\\frac{1}{2}"
    f3, f3_tex = get_f()
    f4, f4_tex = get_f()
    f5, f5_tex = get_f()
    f6, f6_tex = get_f()
    
    val = ((f1 * (1 - f2)) / (f3 * f4)) + (f5 * f6)
    tex = f"{f1_tex} \\left( 1 - {f2_tex} \\right) \\div \\left( {f3_tex} \\times {f4_tex} \\right) + {f5_tex} \\cdot {f6_tex}"
    return val, tex

def t7():
    """ Nivel 6 (Potencias):[(A^2 - B^2) / F] * F +/- F * (C^2 - D) """
    A, B = random.randint(3, 6), random.randint(1, 2)
    C = random.randint(2, 4)
    D = random.randint(1, C**2 - 1)
    
    f1, f1_tex = get_f()
    f2, f2_tex = get_f()
    f3, f3_tex = get_f()
    
    val_left = Fraction(A**2 - B**2, 1) / f1 * f2
    val_right = f3 * Fraction(C**2 - D, 1)
    op = '-' if val_left > val_right else '+'
    val = (val_left - val_right) if op == '-' else (val_left + val_right)
    
    tex = f"\\left[ \\left( {A}^2 - {B}^2 \\right) \\div {f1_tex} \\right] \\times {f2_tex} {op} {f3_tex} \\times \\left( {C}^2 - {D} \\right)"
    return val, tex

def t8():
    """ Nivel 7 (Potencias): [F / (A^2 - B)] * F(C^2 + D) """
    A = random.randint(4, 6)
    B = random.randint(1, A**2 - 1)
    C = random.randint(2, 4)
    D = random.randint(1, 4)
    
    f1, f1_tex = get_f()
    f2, f2_tex = get_f()
    
    val = (f1 / Fraction(A**2 - B, 1)) * f2 * Fraction(C**2 + D, 1)
    tex = f"\\left[ {f1_tex} \\div \\left( {A}^2 - {B} \\right) \\right] \\times {f2_tex} \\left( {C}^2 + {D} \\right)"
    return val, tex

# --- MOTOR GENERADOR DE DIFICULTAD ---

def generar_ejercicio(dia):
    """Filtra y elige las plantillas según el día de entrenamiento"""
    
    # CURVA DE DIFICULTAD
    if dia <= 3:
        templates = [t1, t2, t3]          # Días 1-3: Fácil, base de jerarquía
    elif dia <= 5:
        templates =[t1, t3, t4, t5]      # Días 4-5: Intermedio, aparecen corchetes
    elif dia <= 7:
        templates = [t4, t5, t6]          # Días 6-7: Difícil, fracciones anidadas
    elif dia == 8:
        templates =[t5, t6, t7]          # Día 8: Transición a potencias
    else:
        templates =[t7, t8]              # Días 9-10: Boss final, puras potencias y corchetes

    while True:
        func = random.choice(templates)
        try:
            val, tex = func()
            # Filtro de cordura matemática (< 400 denominador y que no de negativo)
            if val.denominator < 400 and val >= 0:
                return tex, format_mixed(val)
        except ZeroDivisionError:
            continue

# --- MAIN ---

def run():
    header = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{multicol}
\usepackage{enumitem}

\geometry{a4paper, total={175mm,260mm}, left=18mm, top=15mm, bottom=20mm}
\setlength{\parindent}{0pt}
\pagestyle{fancy}
\fancyhf{}
\rhead{\textbf{Kumon G/H} - Jerarquía Progresiva}
\lhead{Día \thesection}
\cfoot{Página \thepage}

\begin{document}
"""
    prob_body = header
    res_body = header.replace("Jerarquía Progresiva", "SOLUCIONARIO")
    
    print("Generando 500 ejercicios Kumon G/H con curva de dificultad...")

    for dia in range(1, TOTAL_DIAS + 1):
        prob_body += f"\\section*{{Día {dia}: Entrenamiento}}\n\\begin{{enumerate}}[itemsep=2.0cm]\n"
        res_body += f"\\section*{{Día {dia}}}\n\\begin{{multicols}}{{5}}\\begin{{enumerate}}\n"
        
        for i in range(1, EJERCICIOS_POR_DIA + 1):
            q, a = generar_ejercicio(dia)
            
            # Formato de la pregunta (\displaystyle hace que las fracciones anidadas se vean grandes)
            prob_body += f"\\item $\\displaystyle {q} =$ \n"
            res_body += f"\\item $ {a} $\n"
            
            # SALTO DE PÁGINA: Exactamente cada 9 ejercicios
            if i % 9 == 0 and i != EJERCICIOS_POR_DIA:
                prob_body += "\\newpage\n"
        
        prob_body += "\\end{enumerate}\\newpage\n"
        res_body += "\\end{enumerate}\\end{multicols}\\newpage\n"
        
    prob_body += "\\end{document}"
    res_body += "\\end{document}"
    
    with open(ARCHIVO_EJ, 'w') as f: f.write(prob_body)
    with open(ARCHIVO_RES, 'w') as f: f.write(res_body)
    
    print("¡Listo weon! Revisa tu directorio.")
    print("-> 9 ejercicios por página.")
    print("-> Días 1-3 suaves, Días 9-10 puras potencias.")

if __name__ == "__main__":
    run()

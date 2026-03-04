#!/usr/bin/env python3
import random
from fractions import Fraction
from decimal import Decimal, getcontext

# Precisión para evitar bugs de flotantes
getcontext().prec = 10

# --- CONFIGURACIÓN ---
TOTAL_DIAS = 10
EJERCICIOS_POR_DIA = 50
ARCHIVO_EJ = "Kumon_E_Final_Conversiones_Ejercicios.tex"
ARCHIVO_RES = "Kumon_E_Final_Conversiones_Respuestas.tex"

# --- UTILIDADES ---
def format_mixed(f):
    if f.denominator == 1:
        return str(f.numerator)
    w = f.numerator // f.denominator
    rem = f.numerator % f.denominator
    if w > 0:
        return f"{w} \\frac{{{rem}}}{{{f.denominator}}}"
    return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def rnd_dec(min_val, max_val, decimals, force_max_decimals=False):
    """Genera Decimal aleatorio. Si force_max_decimals es True, asegura que no termine en 0"""
    factor = 10**decimals
    num = random.randint(int(min_val * factor), int(max_val * factor))
    
    if force_max_decimals and decimals > 1:
        while num % 10 == 0:
            num += random.choice([1, 2, 3, 5, 7, 9])
            
    return Decimal(num) / Decimal(factor)

# --- GENERADORES ---

def gen_frac_to_dec(max_dec):
    """Días 1 y 3: Fracción a Decimal"""
    if max_dec == 2:
        dens =[2, 4, 5, 10, 20, 25, 50, 100]
    else: # 3 decimales (incluye los de 2)
        dens =[2, 4, 5, 8, 10, 20, 25, 40, 50, 125, 200, 250, 500]
        
    den = random.choice(dens)
    num = random.randint(1, den * 4) # Permitir mixtos (ej 9/4 = 2 1/4)
    
    f_val = Fraction(num, den)
    d_val = Decimal(num) / Decimal(den)
    
    q_tex = f"{format_mixed(f_val)} ="
    a_tex = str(d_val.normalize())
    return q_tex, a_tex

def gen_dec_to_frac(max_dec):
    """Días 2 y 4: Decimal a Fracción"""
    d_val = rnd_dec(0.01, 5.99, max_dec, force_max_decimals=True)
    f_val = Fraction(int(d_val * (10**max_dec)), 10**max_dec)
    
    q_tex = f"{d_val} ="
    a_tex = format_mixed(f_val)
    return q_tex, a_tex

def gen_add_sub(max_dec):
    """Días 6-10: Sumas y Restas"""
    d1 = random.randint(1, max_dec)
    d2 = max_dec # Aseguramos que al menos uno tenga el máximo de decimales
    
    if random.random() > 0.5: d1, d2 = d2, d1 # Mezclar posiciones
    
    val1 = rnd_dec(0.1, 25.0, d1)
    val2 = rnd_dec(0.1, 25.0, d2)
    
    op = random.choice(['+', '-'])
    
    if op == '-':
        if val1 < val2: val1, val2 = val2, val1
        res = val1 - val2
        q_tex = f"{val1} - {val2} ="
    else:
        res = val1 + val2
        q_tex = f"{val1} + {val2} ="
        
    return q_tex, str(res.normalize())

# --- CAJAS DE EJEMPLOS ---

def get_example_box(dia):
    if dia == 1:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Fracción a Decimal (Máx 2 decimales)} \\
\small 1) Si el denominador es 10 o 100 es directo: $\frac{7}{10} = \mathbf{0.7}$ y $\frac{3}{100} = \mathbf{0.03}$ \\
2) Amplifica para llegar a 10 o 100: $\frac{3}{4} = \frac{3 \times 25}{4 \times 25} = \frac{75}{100} = \mathbf{0.75}$ \\
3) Con número mixto: $2 \frac{1}{2} = 2 + 0.5 = \mathbf{2.5}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 2:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Decimal a Fracción (Máx 2 decimales)} \\
\small 1) Escribe como fracción base 10 o 100 y simplifica. \\
2) $0.45 = \frac{45}{100} \xrightarrow{\div 5} \mathbf{\frac{9}{20}}$ \\
3) Con enteros, sepáralo: $1.8 = 1 \frac{8}{10} \xrightarrow{\div 2} \mathbf{1 \frac{4}{5}}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 3:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Fracción a Decimal (Hasta Milésimas)} \\
\small 1) ¡Aprende los octavos de memoria! $\frac{1}{8} = \mathbf{0.125}$ \\
2) $\frac{3}{8} = 3 \times 0.125 = \mathbf{0.375}$ \quad | \quad $\frac{5}{8} = \mathbf{0.625}$ \quad | \quad $\frac{7}{8} = \mathbf{0.875}$ \\
3) Amplificando a 1000: $\frac{7}{40} = \frac{7 \times 25}{40 \times 25} = \frac{175}{1000} = \mathbf{0.175}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 4:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Decimal a Fracción (Hasta Milésimas)} \\
\small 1) Usa el 1000 como denominador y simplifica. \\
2) $0.125 = \frac{125}{1000} \xrightarrow{\div 125} \mathbf{\frac{1}{8}}$ \\
3) $2.015 = 2 \frac{15}{1000} \xrightarrow{\div 5} \mathbf{2 \frac{3}{200}}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 6:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Suma y Resta de Decimales} \\
\small 1) \textbf{Alinea siempre la coma decimal} en tu mente o en el papel. \\
2) Si faltan decimales, pon ceros: $1.5 + 0.12 \to 1.50 + 0.12 = \mathbf{1.62}$ \\
3) En la resta es crucial: $3.2 - 1.15 \to 3.20 - 1.15 = \mathbf{2.05}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 8:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Sumas y Restas (Nivel Avanzado)} \\
\small 1) Cuidado con los milésimos y los enteros solos. Pon los ceros necesarios. \\
2) $4 - 0.125 \to 4.000 - 0.125 = \mathbf{3.875}$ \\
3) $1.678 + 0.6 \to 1.678 + 0.600 = \mathbf{2.278}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    return ""

# --- MAIN ---

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
\rhead{\textbf{Nivel E} - Fracciones y Decimales}
\cfoot{Página \thepage}
\begin{document}
"""
    prob_body = header
    res_body = header.replace("Fracciones y Decimales", "SOLUCIONARIO")

    for dia in range(1, TOTAL_DIAS + 1):
        prob_body += f"\\section*{{Día {dia}: Entrenamiento}}\n"
        
        ejemplo_tex = get_example_box(dia)
        if ejemplo_tex:
            prob_body += ejemplo_tex
            
        prob_body += "\\begin{enumerate}\n"
        res_body += f"\\section*{{Día {dia}}}\n\\begin{{multicols}}{{5}}\\begin{{enumerate}}\n"
        
        for i in range(1, EJERCICIOS_POR_DIA + 1):
            
            # --- RUTEO POR DÍA ---
            if dia == 1: 
                q, a = gen_frac_to_dec(max_dec=2)
            elif dia == 2: 
                q, a = gen_dec_to_frac(max_dec=2)
            elif dia == 3: 
                q, a = gen_frac_to_dec(max_dec=3)
            elif dia == 4: 
                q, a = gen_dec_to_frac(max_dec=3)
            elif dia == 5: 
                q, a = gen_frac_to_dec(3) if i % 2 == 0 else gen_dec_to_frac(3)
            elif dia in [6, 7]: 
                q, a = gen_add_sub(max_dec=2)
            else: # Días 8, 9, 10
                q, a = gen_add_sub(max_dec=3)

            # --- AJUSTE DE ESPACIO ---
            # Si hay un cuadro de ejemplo en la página, reducimos levemente el espacio
            # solo en la primera página (los primeros 10 ítems)
            espacio = "1.2cm" if (ejemplo_tex and i <= 10) else "1.5cm"
            
            prob_body += f"\\item \\large $ {q} $ \\vspace{{{espacio}}}\n"
            res_body += f"\\item $ {a} $\n"
            
            if i % 10 == 0 and i != EJERCICIOS_POR_DIA:
                prob_body += "\\newpage\n"
        
        prob_body += "\\end{enumerate}\\newpage\n"
        res_body += "\\end{enumerate}\\end{multicols}\\newpage\n"
        
    prob_body += "\\end{document}"
    res_body += "\\end{document}"
    
    with open(ARCHIVO_EJ, 'w') as f: f.write(prob_body)
    with open(ARCHIVO_RES, 'w') as f: f.write(res_body)
    print(f"-> 10 Días generados ({EJERCICIOS_POR_DIA} ej/día).")
    print(f"Archivos: {ARCHIVO_EJ} y {ARCHIVO_RES}")

if __name__ == "__main__":
    run()

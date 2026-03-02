#!/usr/bin/env python3
import random
from fractions import Fraction
from decimal import Decimal, getcontext

# Configurar precisión decimal
getcontext().prec = 10

# --- CONFIGURACIÓN ---
TOTAL_DIAS = 10
EJERCICIOS_POR_DIA = 50
ARCHIVO_EJ = "Kumon_E_Decimales_Ejercicios.tex"
ARCHIVO_RES = "Kumon_E_Decimales_Respuestas.tex"

# --- UTILIDADES ---
def format_mixed(f):
    if f.denominator == 1:
        return str(f.numerator)
    w = f.numerator // f.denominator
    rem = f.numerator % f.denominator
    if w > 0:
        return f"{w} \\frac{{{rem}}}{{{f.denominator}}}"
    return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def rnd_dec(min_val, max_val, decimals):
    """Genera un Decimal aleatorio entre min_val y max_val con N decimales"""
    factor = 10**decimals
    num = random.randint(int(min_val * factor), int(max_val * factor))
    # Para evitar que termine siempre en 0, nos aseguramos que no sea múltiplo de 10
    # a menos que N sea 1.
    if decimals > 1 and num % 10 == 0:
        num += random.choice([1, 2, 3, 5, 7, 9])
    return Decimal(num) / Decimal(factor)

# --- GENERADORES DE TEMAS ---

def gen_dec_to_frac():
    """Día 1: Decimal a Fracción (2 a 3 decimales)"""
    decimals = random.choice([2, 3])
    d_val = rnd_dec(0.01, 5.99, decimals)
    
    # Convertir a fracción
    f_val = Fraction(int(d_val * (10**decimals)), 10**decimals)
    
    q_tex = f"{d_val} ="
    a_tex = format_mixed(f_val)
    return q_tex, a_tex

def gen_frac_to_dec():
    """Día 2: Fracción a Decimal (exactos)"""
    # Denominadores que generan decimales no periódicos
    dens =[2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500]
    den = random.choice(dens)
    num = random.randint(1, den * 4) # Puede ser impropia
    
    f_val = Fraction(num, den)
    d_val = Decimal(num) / Decimal(den)
    
    # Formatear la pregunta como mixto si es impropia
    q_tex = f"{format_mixed(f_val)} ="
    a_tex = str(d_val.normalize())
    return q_tex, a_tex

def gen_add_sub(max_decimals):
    """Días 3-5: Suma y Resta de Decimales"""
    d1 = random.choice([1, 2, max_decimals])
    d2 = random.choice([1, 2, max_decimals])
    
    val1 = rnd_dec(0.1, 20.9, d1)
    val2 = rnd_dec(0.1, 20.9, d2)
    
    op = random.choice(['+', '-'])
    
    if op == '-':
        if val1 < val2: val1, val2 = val2, val1
        res = val1 - val2
        q_tex = f"{val1} - {val2} ="
    else:
        res = val1 + val2
        q_tex = f"{val1} + {val2} ="
        
    return q_tex, str(res.normalize())

def gen_mul():
    """Días 6-8: Multiplicación de Decimales (1 decimal)"""
    val1 = rnd_dec(0.1, 9.9, 1)
    val2 = rnd_dec(0.1, 9.9, 1)
    
    res = val1 * val2
    q_tex = f"{val1} \\times {val2} ="
    return q_tex, str(res.normalize())

def gen_div():
    """Días 9-10: División de Decimales (Divisor 1 decimal)"""
    # Creamos el cociente (res) y el divisor (val2) para obtener el dividendo (val1)
    # Así aseguramos división exacta
    res = rnd_dec(0.1, 15.0, random.choice([0, 1])) # Cociente entero o 1 decimal
    val2 = rnd_dec(0.1, 9.9, 1) # Divisor siempre 1 decimal
    
    val1 = res * val2 # Dividendo
    
    q_tex = f"{val1} \\div {val2} ="
    return q_tex, str(res.normalize())

# --- CAJAS DE EJEMPLOS ---

def get_example_box(dia):
    if dia == 1:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Convertir Decimal a Fracción} \\
\small 1) Lee el decimal: $0.25$ son $25$ centésimas $\to \frac{25}{100}$. Simplifica: $\mathbf{\frac{1}{4}}$ \\
2) Si hay entero, apártalo: $1.08 \to 1 \frac{8}{100} \to \mathbf{1 \frac{2}{25}}$ \\
3) Tres decimales son milésimas: $0.125 \to \frac{125}{1000} \to \mathbf{\frac{1}{8}}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 2:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Convertir Fracción a Decimal} \\
\small 1) Divide el numerador por el denominador o amplifica a 10, 100, 1000. \\
2) $\frac{3}{4} \to \frac{3 \times 25}{4 \times 25} = \frac{75}{100} = \mathbf{0.75}$ \\
3) Mixtos: $2 \frac{1}{5} \to 2 + \frac{2}{10} = 2 + 0.2 = \mathbf{2.2}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 3:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Suma y Resta de Decimales} \\
\small 1) \textbf{¡Alinea la coma!} Si faltan números, rellena con ceros. \\
2) $1.5 + 0.12 \to 1.50 + 0.12 = \mathbf{1.62}$ \\
3) $3 - 1.45 \to 3.00 - 1.45 = \mathbf{1.55}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 6:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Multiplicación de Decimales} \\
\small 1) Multiplica como si no hubiera comas. \\
2) Cuenta el total de decimales en la pregunta y ponlos en la respuesta. \\
3) $0.4 \times 1.2 \to 4 \times 12 = 48 \to \text{(1 dec + 1 dec = 2 dec)} \to \mathbf{0.48}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 9:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: División de Decimales} \\
\small 1) \textbf{Elimina la coma del divisor} multiplicando ambos por 10. \\
2) $3.6 \div 0.4 \to \text{Multiplica por 10} \to 36 \div 4 = \mathbf{9}$ \\
3) $0.72 \div 0.6 \to \text{Multiplica por 10} \to 7.2 \div 6 = \mathbf{1.2}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    return ""

# --- MOTOR GENERADOR ---

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
\rhead{\textbf{Nivel E} - Dominio Decimal}
\cfoot{Página \thepage}
\begin{document}
"""
    prob_body = header
    res_body = header.replace("Dominio Decimal", "SOLUCIONARIO")
    
    print(f"Generando {TOTAL_DIAS * EJERCICIOS_POR_DIA} ejercicios de decimales...")

    for dia in range(1, TOTAL_DIAS + 1):
        prob_body += f"\\section*{{Día {dia}: Entrenamiento}}\n"
        
        # Insertar caja de ejemplos si corresponde
        ejemplo_tex = get_example_box(dia)
        prob_body += ejemplo_tex
        
        prob_body += "\\begin{enumerate}\n"
        res_body += f"\\section*{{Día {dia}}}\n\\begin{{multicols}}{{5}}\\begin{{enumerate}}\n"
        
        for i in range(1, EJERCICIOS_POR_DIA + 1):
            # Lógica de distribución por días
            if dia == 1: q, a = gen_dec_to_frac()
            elif dia == 2: q, a = gen_frac_to_dec()
            elif dia == 3: q, a = gen_add_sub(2) # Hasta 2 decimales
            elif dia == 4: q, a = gen_add_sub(3) # Hasta 3 decimales
            elif dia == 5: q, a = gen_add_sub(3) # Mixto
            elif dia in[6, 7, 8]: q, a = gen_mul() # Multiplicación 1 decimal
            elif dia in [9, 10]: q, a = gen_div() # División 1 decimal
            
            # Ajustar espaciado si la página tiene un recuadro de ejemplos
            espacio = "1.3cm" if ejemplo_tex and i <= 10 else "1.5cm"
            
            prob_body += f"\\item \\large $ {q} $ \\vspace{{{espacio}}}\n"
            res_body += f"\\item $ {a} $\n"
            
            # Salto de página cada 10 ítems
            if i % 10 == 0 and i != EJERCICIOS_POR_DIA:
                prob_body += "\\newpage\n"
        
        prob_body += "\\end{enumerate}\\newpage\n"
        res_body += "\\end{enumerate}\\end{multicols}\\newpage\n"
        
    prob_body += "\\end{document}"
    res_body += "\\end{document}"
    
    with open(ARCHIVO_EJ, 'w') as f: f.write(prob_body)
    with open(ARCHIVO_RES, 'w') as f: f.write(res_body)
    print("¡Listo weon! Corre 'pdflatex' y a estudiar.")

if __name__ == "__main__":
    run()

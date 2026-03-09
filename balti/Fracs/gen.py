#!/usr/bin/env python3
import random
from fractions import Fraction
from decimal import Decimal, getcontext

# Configurar precisión
getcontext().prec = 10

# --- CONFIGURACIÓN ---
TOTAL_DIAS = 10
EJERCICIOS_POR_DIA = 50
ARCHIVO_EJ = "Ejercicios.tex"
ARCHIVO_RES = "Respuestas.tex"

# --- UTILIDADES FORMATO ---
def format_mixed(f):
    if f.denominator == 1:
        return str(f.numerator) # Esto ya no debería pasar por los parches abajo
    w = f.numerator // f.denominator
    rem = f.numerator % f.denominator
    if w > 0:
        return f"{w} \\frac{{{rem}}}{{{f.denominator}}}"
    return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def rnd_dec(max_decimals):
    """Genera decimal aleatorio asegurando que NO sea un número entero"""
    # Elegir cantidad de decimales (1, 2 o 3)
    decimals = random.randint(1, max_decimals)
    if random.random() > 0.3: decimals = max_decimals # Forzar más el máximo de decimales
    
    factor = 10**decimals
    num = random.randint(1, 5 * factor - 1)
    
    # PARCHE 1: Evitar números enteros (ej. 100/100 = 1.0)
    while num % factor == 0:
        num = random.randint(1, 5 * factor - 1)
        
    # PARCHE 2: Si pedimos 2 decimales, que no termine en 0 (ej. 1.50 -> 1.5)
    # Así aseguramos que visualmente tenga la cantidad de decimales pedida.
    if decimals > 1:
        while num % 10 == 0:
            num += random.choice([1, 3, 7, 9])
            
    return Decimal(num) / Decimal(factor)

# --- GENERADORES DE EJERCICIOS ---

def gen_frac_to_dec(max_dec, force_1000=False):
    """Convierte de Fracción a Decimal"""
    if max_dec == 2:
        dens =[2, 4, 5, 10, 20, 25, 50, 100]
        den = random.choice(dens)
    else: # 3 decimales
        if force_1000:
            den = 1000
        else:
            dens =[2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]
            den = random.choice(dens)
            
    num = random.randint(1, den * 4) # Hasta 4 enteros
    
    # PARCHE 3: Evitar que el numerador sea múltiplo del denominador (ej. 8/4 = 2)
    while num % den == 0:
        num = random.randint(1, den * 4)
        
    # Regla estricta: Si forzamos /1000, no podemos permitir que la fracción se simplifique.
    # Ej: 500/1000 se simplificaría a 1/2 perdiendo la gracia del ejercicio inicial.
    if force_1000:
        while num % 2 == 0 or num % 5 == 0 or num % den == 0:
            num = random.randint(1, den * 4)
    
    f_val = Fraction(num, den)
    d_val = Decimal(num) / Decimal(den)
    
    q_tex = f"{format_mixed(f_val)} ="
    a_tex = str(d_val.normalize())
    return q_tex, a_tex

def gen_dec_to_frac(max_dec):
    """Convierte de Decimal a Fracción (Mixto simplificado)"""
    d_val = rnd_dec(max_dec)
    f_val = Fraction(str(d_val)) # Lectura directa para precisión absoluta
    
    q_tex = f"{d_val.normalize()} ="
    a_tex = format_mixed(f_val)
    return q_tex, a_tex

# --- CAJAS DE EJEMPLOS ---

def get_example_box(dia):
    if dia == 1:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Fracción a Decimal (Hasta 2 decimales)} \\
\small 1) Denominador 10 o 100 es directo: $\frac{7}{10} = \mathbf{0.7}$ \quad | \quad $\frac{13}{100} = \mathbf{0.13}$ \\
2) Si no es 100, amplifica: $\frac{3}{25} = \frac{3 \times 4}{25 \times 4} = \frac{12}{100} = \mathbf{0.12}$ \\
3) Número Mixto (el entero queda igual): $2 \frac{1}{4} = 2 + 0.25 = \mathbf{2.25}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 2:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Decimal a Fracción (Hasta 2 decimales)} \\
\small 1) Usa denominador 10 o 100 y \textbf{simplifica siempre}: \\
2) $0.8 = \frac{8}{10} \xrightarrow{\div 2} \mathbf{\frac{4}{5}}$ \\
3) Con entero: $3.45 = 3 \frac{45}{100} \xrightarrow{\div 5} \mathbf{3 \frac{9}{20}}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 6:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Fracción a Decimal (Milésimas)} \\
\small 1) Denominador 1000: $\frac{45}{1000} = \mathbf{0.045}$ (¡Ojo con el cero!) \\
2) Amplificando a 1000: $\frac{3}{125} = \frac{3 \times 8}{125 \times 8} = \frac{24}{1000} = \mathbf{0.024}$ \\
3) Memoriza los octavos: $\frac{1}{8} = \mathbf{0.125}$ \quad | \quad $\frac{3}{8} = \mathbf{0.375}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    elif dia == 7:
        return r"""
\begin{center}\fbox{\begin{minipage}{0.9\textwidth}
\textbf{Ejemplos: Decimal a Fracción (Milésimas)} \\
\small 1) Tres decimales significan denominador 1000. \\
2) $0.005 = \frac{5}{1000} \xrightarrow{\div 5} \mathbf{\frac{1}{200}}$ \\
3) $1.125 = 1 \frac{125}{1000} \xrightarrow{\div 125} \mathbf{1 \frac{1}{8}}$
\end{minipage}}\end{center}\vspace{0.2cm}
"""
    return ""

# --- MOTOR PRINCIPAL ---

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
\rhead{\textbf{Nivel E} - Dominio Conversiones}
\cfoot{Página \thepage}
\begin{document}
"""
    prob_body = header
    res_body = header.replace("Dominio Conversiones", "SOLUCIONARIO")

    for dia in range(1, TOTAL_DIAS + 1):
        prob_body += f"\\section*{{Día {dia}: Entrenamiento}}\n"
        
        ejemplo_tex = get_example_box(dia)
        if ejemplo_tex:
            prob_body += ejemplo_tex
            
        prob_body += "\\begin{enumerate}\n"
        res_body += f"\\section*{{Día {dia}}}\n\\begin{{multicols}}{{5}}\\begin{{enumerate}}\n"
        
        # Determinar el máximo de decimales por bloque de días
        max_dec = 2 if dia <= 5 else 3
        
        for i in range(1, EJERCICIOS_POR_DIA + 1):
            
            # --- LÓGICA DE DÍAS ---
            # Días 1 y 6: Frac -> Dec
            if dia in [1, 6]:
                # Regla del papá: los primeros 15 ejercicios del Día 6 se fuerzan con denominador 1000
                force = True if (dia == 6 and i <= 15) else False
                q, a = gen_frac_to_dec(max_dec, force_1000=force)
                
            # Días 2 y 7: Dec -> Frac
            elif dia in [2, 7]:
                q, a = gen_dec_to_frac(max_dec)
                
            # Días 3 y 8: Frac -> Dec
            elif dia in [3, 8]:
                # Regla del papá: los primeros 10 ejercicios del Día 8 se fuerzan con denominador 1000
                force = True if (dia == 8 and i <= 10) else False
                q, a = gen_frac_to_dec(max_dec, force_1000=force)
                
            # Días 4 y 9: Dec -> Frac
            elif dia in [4, 9]:
                q, a = gen_dec_to_frac(max_dec)
                
            # Días 5 y 10: MIXTOS (Mitad y mitad, turnándose)
            elif dia in [5, 10]:
                if i % 2 != 0:
                    q, a = gen_frac_to_dec(max_dec, force_1000=False)
                else:
                    q, a = gen_dec_to_frac(max_dec)

            # --- ESPACIADO ---
            espacio = "1.3cm" if (ejemplo_tex and i <= 10) else "1.5cm"
            
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
    print("¡Listo weon! Problema de los enteros solucionado.")
    print(f"Archivos: {ARCHIVO_EJ} y {ARCHIVO_RES}")

if __name__ == "__main__":
    run()

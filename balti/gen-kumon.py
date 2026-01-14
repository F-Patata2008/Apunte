#!/usr/bin/env python3
import random
import os
from fractions import Fraction

# --- CONFIGURACIÓN ---
TOTAL_DIAS = 10
EJERCICIOS_POR_DIA = 50
EJERCICIOS_POR_PAGINA = 10
ARCHIVO_EJ = "Ejercicios_Kumon_F_Papomudas.tex"
ARCHIVO_RES = "Respuestas_Kumon_F_Papomudas.tex"

# --- LÓGICA PAPOMUDAS (INGENIERÍA INVERSA) ---
# Creamos el problema al revés para asegurar resultados bonitos

def generar_fraccion_papomudas():
    """Genera A +/- (B * C) o A +/- (B / C) con fracciones"""
    tipo = random.choice(['mul', 'div'])
    
    if tipo == 'mul':
        # Caso: Entero +/- (Fracción * Entero)
        den = random.choice([2, 3, 4, 5, 8, 10])
        num = random.choice([1, 3, 5, 7])
        if num >= den: num = 1
        frac = Fraction(num, den)
        
        # El entero B debe ser múltiplo del denominador para simplificar
        factor = random.randint(1, 6) * den
        
        res_mult = frac * factor # Esto da un entero
        base = random.randint(int(res_mult) + 1, int(res_mult) + 20)
        
        signo = random.choice(['+', '-'])
        if signo == '+':
            total = base + res_mult
            tex = f"{base} + \\frac{{{num}}}{{{den}}} \\times {factor}"
        else:
            total = base - res_mult
            tex = f"{base} - \\frac{{{num}}}{{{den}}} \\times {factor}"
            
    else:
        # Caso: Entero +/- (Fracción / Fracción)
        # Hacemos que la división interna de un número pequeño (1, 2 o 3)
        res_div = random.randint(1, 3)
        
        # Divisor
        d2 = random.choice([2, 3, 4, 5])
        n2 = 1
        f2 = Fraction(n2, d2)
        
        # Dividendo para que (f1 / f2) = res_div
        f1 = res_div * f2 
        
        base = random.randint(res_div + 5, res_div + 25)
        signo = random.choice(['+', '-'])
        
        if signo == '+':
            total = base + res_div
        else:
            total = base - res_div
            
        tex = f"{base} {signo} \\frac{{{f1.numerator}}}{{{f1.denominator}}} \\div \\frac{{{n2}}}{{{d2}}}"

    return tex, str(total)

def generar_decimal_papomudas():
    """Genera decimales tipo A +/- B x C o divisiones exactas"""
    tipo = random.choice(['mul', 'div'])
    
    if tipo == 'mul':
        # (Decimal x Entero) simple
        v1 = random.choice([0.5, 0.2, 0.1, 1.5, 2.5, 0.4])
        v2 = random.choice([2, 4, 5, 10, 20])
        prod = v1 * v2 # Generalmente entero o .5
        
        base = random.randint(int(prod) + 2, int(prod) + 20)
        if random.random() > 0.7: base += 0.5 # A veces base decimal
        
        signo = random.choice(['+', '-'])
        if signo == '+':
            res = base + prod
        else:
            res = base - prod
            
        tex = f"{base} {signo} {v1} \\times {v2}"
        
    else:
        # División exacta: (Decimal / Decimal) o (Decimal / Entero)
        divisor = random.choice([0.2, 0.5, 0.1])
        cociente = random.randint(2, 20)
        dividendo = round(cociente * divisor, 1)
        
        base = random.randint(cociente + 5, cociente + 30)
        signo = random.choice(['+', '-'])
        
        if signo == '+':
            res = base + cociente
        else:
            res = base - cociente
            
        tex = f"{base} {signo} {dividendo} \\div {divisor}"

    # Formateo respuesta (quitar .0 si es entero)
    if isinstance(res, float) and res.is_integer():
        res = int(res)
    res_str = f"{res:.1f}" if isinstance(res, float) else str(res)
    
    return tex, res_str

# --- GENERADOR LATEX ---
def generar_archivos():
    # Header estilo KUMON antiguo (el que te gustó)
    header = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{multicol}

% Márgenes cómodos para imprimir
\geometry{a4paper, total={170mm,257mm}, left=20mm, top=20mm, bottom=20mm}
\setlength{\parindent}{0pt}
\pagestyle{fancy}
\fancyhf{}
\cfoot{Página \thepage}
"""
    begin = r"\begin{document}" + "\n"
    end = r"\end{document}"

    content_prob = header + r"\lhead{\textbf{Nivel F} - PAPOMUDAS} \rhead{Ejercicios}" + "\n" + begin
    content_res = header + r"\lhead{\textbf{Nivel F} - Solucionario} \rhead{Respuestas}" + "\n" + begin

    print(f"-- Generando {TOTAL_DIAS * EJERCICIOS_POR_DIA} ejercicios estilo PAPOMUDAS --")

    for dia in range(1, TOTAL_DIAS + 1):
        # Encabezado por día
        titulo = f"\\section*{{Día {dia}: Operaciones Combinadas (Frac. y Dec.)}}\n"
        content_prob += titulo + "\\begin{enumerate}\n"
        
        content_res += f"\\section*{{Respuestas Día {dia}}}\n"
        content_res += "\\begin{multicols}{5}\n\\begin{enumerate}\n" # Respuestas compactas

        for i in range(1, EJERCICIOS_POR_DIA + 1):
            # Mitad fracciones, mitad decimales
            if i <= 25:
                q, a = generar_fraccion_papomudas()
            else:
                q, a = generar_decimal_papomudas()
            
            # Formato de pregunta: Letra grande, espacio para resolver
            content_prob += f"\\item \\large $ {q} = $ \\vspace{{1.6cm}}\n"
            
            # Formato de respuesta: Simple
            content_res += f"\\item $ {a} $\n"

            # Salto de página cada 10 ejercicios (ESTILO ANTIGUO)
            if i % EJERCICIOS_POR_PAGINA == 0 and i != EJERCICIOS_POR_DIA:
                content_prob += "\\newpage\n"
        
        # Separador de día
        content_prob += "\\end{enumerate}\n\\newpage\n"
        content_res += "\\end{enumerate}\n\\end{multicols}\n\\newpage\n"

    content_prob += end
    content_res += end

    with open(ARCHIVO_EJ, 'w') as f: f.write(content_prob)
    with open(ARCHIVO_RES, 'w') as f: f.write(content_res)

    print(f"Listo bro. Archivos generados:\n -> {ARCHIVO_EJ}\n -> {ARCHIVO_RES}")

if __name__ == "__main__":
    generar_archivos()

import random
from fractions import Fraction

# --- CONFIGURACIÓN ---
TOTAL_DIAS = 10
EJERCICIOS_POR_DIA = 50
EJERCICIOS_POR_PAGINA = 10
ARCHIVO_EJ = "Kumon_F_Experto_Ejercicios.tex"
ARCHIVO_RES = "Kumon_F_Experto_Respuestas.tex"

# --- UTILIDADES DE FORMATO ---

def latex_frac(f):
    """Convierte objeto Fraction a LaTeX (Mixto o Entero preferiblemente)"""
    if f.denominator == 1:
        return str(f.numerator)

    entero = f.numerator // f.denominator
    resto = f.numerator % f.denominator

    if entero != 0 and resto != 0:
        return f"{entero} \\frac{{{resto}}}{{{f.denominator}}}"
    elif entero != 0 and resto == 0:
        return str(entero)
    else:
        return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def latex_float(val):
    """Formatea float quitando el .0 si es entero"""
    if val.is_integer():
        return str(int(val))
    return f"{val:.1f}"

# --- GENERADORES DE PROBLEMAS ---

def gen_decimal_power_mix():
    """
    Genera: Base^Exp +/- (Operacion Decimal)
    Ej: 3^2 - (2.5 * 2 - 1.0)
    """
    # 1. Generar Potencia (Entera)
    base = random.randint(2, 6)
    exp = 2
    if base < 4: exp = random.choice([2, 3])
    val_potencia = base ** exp

    # 2. Generar Contenido del Parentesis (Decimal)
    # Estructura interna: (A * B +/- C) o (A +/- B)
    tipo_inner = random.choice(['simple', 'complejo'])

    if tipo_inner == 'simple':
        # (Decimal +/- Decimal)
        d1 = round(random.uniform(1.1, 9.9), 1)
        d2 = round(random.uniform(0.5, 5.5), 1)
        signo_in = random.choice(['+', '-'])

        if signo_in == '-':
            # Asegurar positivo dentro del parentesis
            if d2 > d1: d1, d2 = d2, d1
            val_par = d1 - d2
            str_par = f"({d1} - {d2})"
        else:
            val_par = d1 + d2
            str_par = f"({d1} + {d2})"

    else:
        # (Entero * Decimal - Entero) o similar
        # Ej: (2 * 3.5 - 1)
        fac = random.randint(2, 5)
        dec = random.choice([0.5, 1.5, 2.5, 0.1, 0.2])
        resta = random.randint(0, 2) # Puede ser 0 (sin resta)

        val_prod = fac * dec

        if val_prod < resta: resta = 0 # Safety

        val_par = val_prod - resta
        if resta > 0:
            str_par = f"({fac} \\times {dec} - {resta})"
        else:
            str_par = f"({fac} \\times {dec})"

    # 3. Operación Principal
    signo_out = random.choice(['+', '-'])

    # Lógica NO NEGATIVOS
    if signo_out == '-':
        if val_potencia < val_par:
            # Si la potencia es menor al paréntesis, invertimos: Parentesis - Potencia
            # O cambiamos a suma. Vamos a cambiar a suma para variar.
            signo_out = '+'
            res = val_potencia + val_par
            q = f"{base}^{{{exp}}} + {str_par}"
        else:
            res = val_potencia - val_par
            q = f"{base}^{{{exp}}} - {str_par}"
    else:
        res = val_potencia + val_par
        q = f"{base}^{{{exp}}} + {str_par}"

    return q, latex_float(res)

def gen_fraction_power_mix():
    """
    Genera: Base^Exp +/- (Fraccion +/- Fraccion)
    Sin potencias de fracciones.
    """
    # 1. Potencia
    base = random.randint(2, 5)
    exp = 2
    val_potencia = base ** exp

    # 2. Parentesis (Fracciones)
    den = random.choice([2, 3, 4, 5, 6, 8])
    n1 = random.randint(1, den * 2)
    n2 = random.randint(1, den * 2)
    f1 = Fraction(n1, den)
    f2 = Fraction(n2, den)

    signo_in = random.choice(['+', '-'])

    if signo_in == '-':
        if f2 > f1: f1, f2 = f2, f1
        val_par = f1 - f2
        str_par = f"(\\frac{{{f1.numerator}}}{{{f1.denominator}}} - \\frac{{{f2.numerator}}}{{{f2.denominator}}})"
    else:
        val_par = f1 + f2
        str_par = f"(\\frac{{{f1.numerator}}}{{{f1.denominator}}} + \\frac{{{f2.numerator}}}{{{f2.denominator}}})"

    # 3. Operacion Principal
    signo_out = random.choice(['+', '-'])

    if signo_out == '-':
        # Check non-negative
        if val_par > val_potencia:
            # Invertir el orden para que de positivo: (Frac) - Potencia ?
            # Mejor cambiar a suma para no complicar el orden visual
            res = val_potencia + val_par
            q = f"{base}^{{{exp}}} + {str_par}"
        else:
            res = val_potencia - val_par
            q = f"{base}^{{{exp}}} - {str_par}"
    else:
        res = val_potencia + val_par
        q = f"{base}^{{{exp}}} + {str_par}"

    return q, latex_frac(res)

# --- GENERADOR DE EJEMPLOS (TEXTO) ---
def get_daily_examples(dia):
    """Devuelve código LaTeX para 2 ejemplos resueltos"""

    # Ejemplo 1: Decimales con Potencia
    # 3^2 + (1.5 + 2.5)
    ex1_q = r"3^2 + (1.5 + 2.5)"
    ex1_steps = r"""
    \textbf{Paso 1 (Paréntesis):} $1.5 + 2.5 = 4$ \\
    \textbf{Paso 2 (Potencia):} $3^2 = 9$ \\
    \textbf{Paso 3 (Suma):} $9 + 4 = \mathbf{13}$
    """

    # Ejemplo 2: Fracciones con Resta
    # 2^3 - (3/4 + 1/4)
    ex2_q = r"2^3 - (\frac{3}{4} + \frac{1}{4})"
    ex2_steps = r"""
    \textbf{Paso 1 (Paréntesis):} $\frac{3}{4} + \frac{1}{4} = \frac{4}{4} = 1$ \\
    \textbf{Paso 2 (Potencia):} $2^3 = 8$ \\
    \textbf{Paso 3 (Resta):} $8 - 1 = \mathbf{7}$
    """

    box_latex = r"""
    \begin{center}
    \fbox{
    \begin{minipage}{0.9\textwidth}
        \textbf{\large Ejemplos del Día %d} \\[0.5em]
        \begin{multicols}{2}
            \underline{Ejemplo A (Decimales):} \\
            $ %s $ \\[0.5em]
            %s

            \columnbreak

            \underline{Ejemplo B (Fracciones):} \\
            $ %s $ \\[0.5em]
            %s
        \end{multicols}
    \end{minipage}
    }
    \end{center}
    \vspace{0.5cm}
    """ % (dia, ex1_q, ex1_steps, ex2_q, ex2_steps)

    return box_latex

# --- MAIN ---

def generar_archivos():
    # Header LaTeX
    header = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{multicol}
\usepackage{xcolor}

\geometry{a4paper, total={170mm,257mm}, left=20mm, top=20mm, bottom=20mm}
\setlength{\parindent}{0pt}
\pagestyle{fancy}
\fancyhf{}
\cfoot{Página \thepage}
"""
    begin = r"\begin{document}" + "\n"
    end = r"\end{document}"

    content_prob = header + r"\lhead{\textbf{Nivel F} - Experto} \rhead{Potencias y Paréntesis Mix}" + "\n" + begin
    content_res = header + r"\lhead{\textbf{Nivel F} - Solucionario} \rhead{Respuestas}" + "\n" + begin

    for dia in range(1, TOTAL_DIAS + 1):
        content_prob += f"\\section*{{Día {dia}: Jerarquía de Operaciones}}\n"

        # INSERTAR EJEMPLOS AL INICIO DEL DÍA
        content_prob += get_daily_examples(dia)

        content_prob += "\\begin{enumerate}\n"

        content_res += f"\\section*{{Respuestas Día {dia}}}\n"
        content_res += "\\begin{multicols}{5}\n\\begin{enumerate}\n"

        for i in range(1, EJERCICIOS_POR_DIA + 1):
            # Alternar 50/50 entre Fracciones y Decimales
            if random.random() > 0.5:
                q, a = gen_decimal_power_mix()
            else:
                q, a = gen_fraction_power_mix()

            # Ajuste de espacio vertical
            content_prob += f"\\item \\large $ {q} = $ \\vspace{{1.4cm}}\n"
            content_res += f"\\item $ {a} $\n"

            # Saltos de página
            # Nota: Como agregamos la caja de ejemplos al principio, la primera página
            # del día tendrá menos espacio. Haremos salto en el ej 8 en la pag 1,
            # y luego cada 10.

            items_primera_pag = 8

            if i == items_primera_pag:
                content_prob += "\\newpage\n"
            elif i > items_primera_pag and (i - items_primera_pag) % EJERCICIOS_POR_PAGINA == 0 and i != EJERCICIOS_POR_DIA:
                content_prob += "\\newpage\n"

        content_prob += "\\end{enumerate}\n\\newpage\n"
        content_res += "\\end{enumerate}\n\\end{multicols}\n\\newpage\n"

    content_prob += end
    content_res += end

    with open(ARCHIVO_EJ, 'w', encoding='utf-8') as f:
        f.write(content_prob)

    with open(ARCHIVO_RES, 'w', encoding='utf-8') as f:
        f.write(content_res)

    print(f"¡Listo! Archivos generados para Windows:\n -> {ARCHIVO_EJ}\n -> {ARCHIVO_RES}")

if __name__ == "__main__":
    generar_archivos()


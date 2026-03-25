hay q elimar las secciones superfluas (ya elimne una estas que era la del 22/09), ademas de elimar als fechas de los encabezados de seccion, ya que no es necesraio, y eso fue con mis clases, y no impoarta eso de la fecha, sino que importa la materia, pero deja como comentario que en esa fecha, ademas revisa qu eno me falate ninguna clase con materoa

y genrea todo parar llegar y pegar, no tener q manaulemnte ir cambiando los titulos de seccion y eso, sino que yo solo copio, pego y compilo
las 1550 linea de coigo, ademas, elimin las marcas de agua, y las imagnes random del patata, y de los gatos, son duperfulas, no quero un reusmen del apunte, solo la paortada, dedicatoria, indice y secciones, sin fechas (que estas esten cocmo coemntariosn es mi codigo)

mi apunte actual:
\documentclass[12pt, letterpaper]{article}
\usepackage[utf8]{inputenc} % Input encoding
\usepackage[T1]{fontenc} % Font encoding
\usepackage{amsmath} % Math symbols and environments
\usepackage{amssymb} % More math symbols
\usepackage{graphicx} % Include graphics
\usepackage[spanish]{babel} % Spanish language support (ACTIVADO)
\usepackage{tabularx}
\usepackage{enumitem}

% ----- PAQUETES DE MEJORA Y CORRECCIONES -----
\usepackage{microtype} % Soluciona problemas de Overfull/Underfull hbox y mejora la tipografía
\renewcommand{\arraystretch}{1.5} % Incrementa el espaciado vertical
\graphicspath{ {./images/}}
% --------------------------------------------

% ----- PAQUETES PARA ENCABEZADO/PIE DE PÁGINA -----
\usepackage{fancyhdr}
\usepackage{hyperref}

% ----- CONFIGURACIÓN DE AUTORÍA Y METADATOS -----
\hypersetup{
colorlinks=true,
linkcolor=black,
filecolor=magenta,
urlcolor=cyan,
pdftitle={Apunte Completo: Probabilidad y Estadística},
pdfauthor={Felipe Colli Olea},
pdfsubject={Apunte de la asignatura para 4° Medio 2025},
pdfkeywords={probabilidad, estadistica, instituto nacional, felipe colli},
pdfcreator={pdfLaTeX},
pdfproducer={LaTeX with hyperref}
}
% --------------------------------------------------------------------------

% --- CONFIGURACIÓN DE ENCABEZADOS Y PIES DE PÁGINA ---
\pagestyle{fancy}
\fancyhf{} % Limpiar todos los campos
\fancyhead[L]{\nouppercase{\rightmark}} % Muestra la sección/subsección actual a la izquierda
\fancyhead[R]{\thepage} % Número de página a la derecha
\fancyfoot[C]{\footnotesize Material cedido al Depto. de Matemáticas del I.N. por Felipe Colli Olea -- \copyright~2025}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

% Para que rightmark muestre el formato "número. título"
\renewcommand{\sectionmark}[1]{\markright{\thesection.\ #1}}
\renewcommand{\subsectionmark}[1]{\markright{\thesubsection.\ #1}}
% ---------------------------------------------------

\begin{document}

\begin{titlepage}
\thispagestyle{empty} % Oculta encabezado y pie en esta página
\centering
\includegraphics[width=2cm]{IN}\[1cm]
\textsc{\LARGE  Instituto Nacional General José Miguel Carrera}\[0.5cm]
\textsc{\Large Departamento de Matemáticas}\[1cm]

code
Code
download
content_copy
expand_less
\rule{\textwidth}{1.5pt}\vspace{0.4cm}
{\Huge \bfseries Apunte Completo: \\[0.5cm] Probabilidad y Estadística}\\[0.4cm]
\rule{\textwidth}{1.5pt}\\[1.5cm]

{\Large \textit{ Probabilidad y Estadística - Sección 4° Medio 2025}}\\[2cm]

\begin{minipage}{0.45\textwidth}
	\begin{flushleft} \large
		\textbf{Autor:}\\
		Felipe Colli Olea
	\end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
	\begin{flushright} \large
		\textbf{Profesor de Cátedra:}\\
		Sergio Díaz
	\end{flushright}
\end{minipage}

\vfill
\copyright~2025, Felipe Colli Olea.

\end{titlepage}

\newpage
\thispagestyle{empty} % Oculta encabezado y pie en esta página
\vspace*{5cm} % Añade espacio vertical
\begin{center}
\fbox{\begin{minipage}{0.85\textwidth}
\centering
\subsection*{Dedicatoria y Cesión de Uso}
\vspace{0.2cm}
\parbox{0.9\textwidth}{\normalsize\centering Con gratitud y aprecio, el autor, \textbf{Felipe Colli Olea}, cede el presente documento en su formato PDF al \textbf{Departamento de Matemáticas del Instituto Nacional}, y en especial a los profesores \textbf{Sergio Díaz} y \textbf{David Caldera}, como material de estudio para las futuras generaciones de estudiantes.}
\vspace{0.5cm}

code
Code
download
content_copy
expand_less
\parbox{0.9\textwidth}{\small
			\begin{itemize}[leftmargin=*]
				\item \textbf{Uso Permitido:} Se autoriza la copia y distribución gratuita de este documento PDF, sin modificaciones, exclusivamente con fines académicos dentro de la comunidad del Instituto Nacional.
				\item \textbf{Derechos Retenidos:} El autor retiene todos los derechos sobre la obra original, incluido su código fuente LaTeX.
				\item \textbf{Prohibiciones:} Queda estrictamente prohibido el uso comercial, la venta, la modificación del contenido o la distribución de este material fuera del contexto académico acordado sin la autorización explícita y por escrito del autor.
			\end{itemize}
		}
		\vspace{0.5cm}
		
		\textbf{\copyright~2025, Felipe Colli Olea.}
\end{minipage}}

\end{center}

\newpage
\tableofcontents
\newpage % Start sections on a new page after ToC

\section{14/03 - Conceptos Fundamentales de Estadística}
\subsection{Conceptos Básicos}
\subsubsection{Población:}
Conjunto de todos los elementos que se quieren estudiar. Cuando la información deseada está disponible para todos los objetos de la población, lo llamamos \textbf{censo}. En la práctica es muy difícil o casi imposible realizar un censo.

\subsubsection{Muestra:}
Subconjunto de la población que se mide u observa.

\begin{figure}[h]
\centering
\includegraphics[width=0.85\textwidth]{muestra}
\caption{Representación de la muestra dentro de la población.}
\label{fig:muestra}
\end{figure}

\subsubsection{Parámetro:}
Es una medición numérica que describe alguna característica de una población.

\subsubsection{Estadístico (o estadígrafo):}
Es una medición numérica que describe alguna característica de la muestra.

\subsection{Tipos de Variables}

\subsubsection{Variables cualitativas:}
\begin{itemize}
\item Se describen mediante palabras o categorías.
\item Se usan para categorizar a los individuos o para identificar.
\item Sirven para comprender aspectos subjetivos y complejos.
\item Se pueden clasificar en nominales y ordinales.
\item Ejemplos: el color del cabello, el deporte favorito, la comida favorita, el lugar de nacimiento.
\end{itemize}

\subsubsection{Variables cuantitativas:}
\begin{itemize}
\item Se expresan mediante números, es decir, se pueden contar o medir.
\item Permiten más operaciones matemáticas.
\item Se pueden usar para conocer fenómenos o situaciones a través de la recolección y generación de números y datos.
\item Ejemplos: la edad, los ingresos, el peso, la altura, la presión, la humedad o cantidad de hermanos.
\end{itemize}

\begin{figure}[htbp]
\centering
\includegraphics[width=0.58\textwidth]{variables}
\caption{}
\label{fig:variables}
\end{figure}

\subsection{Ejercicios:}
Para cada una de las siguientes situaciones, identifica la población de interés, la variable estadística, clasifícala, y entrega un ejemplo de cuál podría ser una posible muestra.

\begin{enumerate}
\item Un investigador universitario desea estimar la proporción de ciudadanos chilenos de la \textit{GEN X} que están interesados en iniciar sus propios negocios.
\begin{enumerate}
\item \textbf{Población:} Chilenos de la Generación X.
\item \textbf{Muestra (ejemplo):} 500 chilenos de la Generación X seleccionados aleatoriamente del padrón electoral.
\item \textbf{Variable:} Interés en iniciar un negocio (Sí/No) (\textit{cualitativa nominal}).
\end{enumerate}

code
Code
download
content_copy
expand_less
\item Durante más de un siglo, la temperatura corporal normal en seres humanos ha sido aceptada como 37°C. ¿Es así realmente? Los investigadores desean estimar el promedio de temperatura de adultos sanos en Chile.
      \begin{enumerate}
	      \item \textbf{Población:} Adultos sanos en Chile.
	      \item \textbf{Muestra (ejemplo):} Adultos sanos de Santiago seleccionados de diversos centros de salud.
	      \item \textbf{Variable:} Temperatura corporal (\textit{cuantitativa continua}).
      \end{enumerate}

\item Un ingeniero municipal desea estimar el promedio de consumo semanal de agua para unidades habitacionales unifamiliares en la ciudad.
      \begin{enumerate}
	      \item \textbf{Población:} Unidades habitacionales unifamiliares de la ciudad.
	      \item \textbf{Muestra (ejemplo):} 200 unidades habitacionales unifamiliares de distintos barrios de la ciudad, seleccionadas aleatoriamente.
	      \item \textbf{Variable:} Consumo semanal de agua (en litros) (\textit{cuantitativa continua}).
      \end{enumerate}
\item El National Highway Safety Council desea estimar la proporción de llantas para automóvil con dibujo o superficie de rodadura insegura, entre todas las llantas manufacturadas por una empresa específica durante el presente año de producción.
      \begin{enumerate}
	      \item \textbf{Población:} Todas las llantas para automóvil manufacturadas por la empresa específica durante el presente año de producción.
	      \item \textbf{Muestra (ejemplo):} Una selección aleatoria de llantas producidas en diferentes lotes o días del año.
	      \item \textbf{Variable:} Estado de la superficie de rodadura (segura/insegura) (\textit{cualitativa nominal}).
      \end{enumerate}
\item Un politólogo desea estimar si la mayoría de los residentes adultos de una región están a favor de una legislatura unicameral.
      \begin{enumerate}
	      \item \textbf{Población:} Residentes adultos de la región.
	      \item \textbf{Muestra (ejemplo):} Residentes adultos de varias comunas seleccionadas aleatoriamente de la región.
	      \item \textbf{Variable:} Opinión sobre la legislatura unicameral (a favor/en contra/indeciso) (\textit{cualitativa nominal}).
      \end{enumerate}
\item Un científico del área médica desea determinar el tiempo promedio para que se vuelva a presentar cierta enfermedad infecciosa, una vez que las personas se recuperan de ella por primera vez.
      \begin{enumerate}
	      \item \textbf{Población:} Personas que se han recuperado de la enfermedad infecciosa por primera vez.
	      \item \textbf{Muestra (ejemplo):} Pacientes recuperados seleccionados de registros médicos de diversos hospitales.
	      \item \textbf{Variable:} Tiempo hasta la recurrencia de la enfermedad (\textit{cuantitativa continua}).
      \end{enumerate}
\item Un ingeniero electricista desea determinar si el promedio de vida útil de transistores de cierto tipo es mayor que 500 horas.
      \begin{enumerate}
	      \item \textbf{Población:} Todos los transistores de cierto tipo.
	      \item \textbf{Muestra (ejemplo):} Una muestra de 100 transistores de ese tipo, seleccionados aleatoriamente de la producción.
	      \item \textbf{Variable:} Vida útil del transistor (en horas) (\textit{cuantitativa continua}).
      \end{enumerate}

\end{enumerate}
\newpage

%... (AQUÍ IRÍA TODO EL RESTO DE TU CONTENIDO, YA CORREGIDO Y LISTO)...
%... Las secciones anteriores están correctas en tu último código, así que no las repito aquí.

\section{17/03 - Tablas de Frecuencia y Medidas de Tendencia Central}

\subsection{Tablas de Frecuencia: Conceptos Básicos}
\begin{itemize}
\item \textbf{Dato o Intervalo:} Información (variable) que se estudia en estadística.
\item \textbf{Marca de Clase (
𝑐
𝑖
c
i
	​

):} Promedio entre los extremos de un intervalo.
\item \textbf{Amplitud de un intervalo:} Es la diferencia entre el límite superior y el límite inferior del intervalo.
\end{itemize}

\subsection{Tipos de Frecuencia:}
\begin{itemize}
\item \textbf{Frecuencia Absoluta (
𝑓
𝑖
f
i
	​

):} Cantidad de veces que se repite un dato o que los datos caen en un intervalo.
\item \textbf{Frecuencia Absoluta Acumulada (
𝐹
𝑖
F
i
	​

):} Suma de las frecuencias absolutas hasta determinado dato o intervalo. 
𝐹
𝑖
=
∑
𝑗
=
1
𝑖
𝑓
𝑗
F
i
	​

=∑
j=1
i
	​

f
j
	​

.
\item \textbf{Frecuencia Relativa (
ℎ
𝑖
h
i
	​

 o 
𝑓
𝑟
𝑖
f
ri
	​

):} Es la proporción (fracción, decimal o porcentaje) de observaciones que corresponden a cierto valor o intervalo (
ℎ
𝑖
=
𝑓
𝑖
𝑛
h
i
	​

=
n
f
i
	​

	​

), donde 
𝑛
n
 es el número total de datos.
\item \textbf{Frecuencia Relativa Acumulada (
𝐻
𝑖
H
i
	​

):} Es la proporción (fracción, decimal o porcentaje) de la frecuencia acumulada hasta cierto dato o intervalo (
𝐻
𝑖
=
𝐹
𝑖
𝑛
=
∑
𝑗
=
1
𝑖
ℎ
𝑗
H
i
	​

=
n
F
i
	​

	​

=∑
j=1
i
	​

h
j
	​

).
\end{itemize}
\newpage

\subsection{Medidas de Tendencia Central:}

\subsubsection{\texorpdfstring{Media Aritmética (
𝑥
ˉ
x
ˉ
):}{Media Aritmética (x barra)}}
Es el cociente entre la suma de todos los datos y el número total de datos (
𝑛
n
). Si se tienen 
𝑛
n
 datos 
𝑥
1
,
𝑥
2
,
…
,
𝑥
𝑛
x
1
	​

,x
2
	​

,…,x
n
	​

:
[ \bar{x}=\frac{x_1+x_2+\dots+x_n}{n} = \frac{\sum_{i=1}^{n} x_i}{n} ] \
Para datos agrupados en una tabla de frecuencia con 
𝑘
k
 clases:
\begin{center}
\begin{minipage}{0.35\textwidth}
\centering
\begin{tabular}{|c|c|}
\hline
\textbf{Marca (
𝑐
𝑖
c
i
	​

)} & \textbf{Frec. (
𝑓
𝑖
f
i
	​

)} \
\hline

𝑐
1
c
1
	​

                  & 
𝑓
1
f
1
	​

                  \ \hline

𝑐
2
c
2
	​

                  & 
𝑓
2
f
2
	​

                  \ \hline

⋮
⋮
               & 
⋮
⋮
               \ \hline

𝑐
𝑘
c
k
	​

                  & 
𝑓
𝑘
f
k
	​

                  \
\hline
\end{tabular}
\end{minipage}
\hfill
\begin{minipage}{0.55\textwidth}
\centering
[ \bar{x}=\frac{c_1 f_1 + c_2 f_2 + \dots + c_k f_k}{f_1+f_2+\dots+f_k} = \frac{\sum_{i=1}^{k} c_i f_i}{n} ]
(donde 
𝑛
=
∑
𝑖
=
1
𝑘
𝑓
𝑖
n=∑
i=1
k
	​

f
i
	​

)
\end{minipage}
\end{center}

\subsubsection{\texorpdfstring{Mediana (
𝑀
𝑒
M
e
	​

):}{Mediana (Me)}}
Es el valor que ocupa la posición central de la muestra cuando los datos se encuentran ordenados. \textbf{Si la muestra tiene un número par de datos, la mediana es la media aritmética de los dos términos centrales.}
\begin{itemize}
\item Si 
𝑛
n
 es impar, la posición es 
𝑛
+
1
2
2
n+1
	​

. 
𝑀
𝑒
=
𝑥
(
𝑛
+
1
2
)
M
e
	​

=x
(
2
n+1
	​

)
	​

.
\item Si 
𝑛
n
 es par, las posiciones son 
𝑛
2
2
n
	​

 y 
𝑛
2
+
1
2
n
	​

+1
. 
𝑀
𝑒
=
𝑥
(
𝑛
2
)
+
𝑥
(
𝑛
2
+
1
)
2
M
e
	​

=
2
x
(
2
n
	​

)
	​

+x
(
2
n
	​

+1)
	​

	​

.
\end{itemize}

\subsubsection{\texorpdfstring{Moda (
𝑀
𝑜
M
o
	​

):}{Moda (Mo)}}
Es el dato o intervalo con la mayor frecuencia absoluta. La muestra puede ser:
\begin{itemize}
\item \textbf{Amodal:} No presenta moda.
\item \textbf{Unimodal:} Una sola moda.
\item \textbf{Bimodal:} Dos modas.
\item \textbf{Polimodal (o Multimodal):} Más de dos modas.
\end{itemize}
\newpage

\section{26/03 - Ejercicios de Medidas de Tendencia Central}
\subsection{Ejercicios:}

\noindent
Si las notas de Esteban en una asignatura son 
3
,
4
,
6
,
3
,
5
,
5
,
6
,
3
,
4
3,4,6,3,5,5,6,3,4
 y de estas notas se cambian un 
6
6
 por un 
7
7
. ¿Cuál(es) de las siguientes medidas de tendencia central cambia(n)?
\begin{enumerate}
\item La moda
\item La mediana
\item La media aritmética
\end{enumerate}
\textit{Solución:}
Notas originales (ordenadas): 
3
,
3
,
3
,
4
,
4
,
5
,
5
,
6
,
6
3,3,3,4,4,5,5,6,6
. 
𝑛
=
9
n=9
.
\begin{itemize}
\item Moda original: 3 (frecuencia 3).
\item Mediana original: El dato en la posición 
9
+
1
2
=
5
2
9+1
	​

=5
. Mediana = 4.
\item Media original: 
3
⋅
3
+
2
⋅
4
+
2
⋅
5
+
2
⋅
6
9
=
39
9
≈
4.33
9
3⋅3+2⋅4+2⋅5+2⋅6
	​

=
9
39
	​

≈4.33
.
\end{itemize}
Notas nuevas (se cambia un 6 por un 7), ordenadas: 
3
,
3
,
3
,
4
,
4
,
5
,
5
,
6
,
7
3,3,3,4,4,5,5,6,7
. 
𝑛
=
9
n=9
.
\begin{itemize}
\item Moda nueva: 3 (sigue siendo la más frecuente). 
→
→
 No cambia.
\item Mediana nueva: El dato en la posición 5 sigue siendo 4. 
→
→
 No cambia.
\item Media nueva: 
39
−
6
+
7
9
=
40
9
≈
4.44
9
39−6+7
	​

=
9
40
	​

≈4.44
. 
→
→
 Cambia.
\end{itemize}
\textbf{Respuesta:} Solo la media aritmética cambia (opción 3).

\vspace{1em}
\noindent La siguiente tabla muestra los valores de una variable 
𝑋
X
 y sus respectivas frecuencias. ¿Cuál es el valor de la mediana?
\begin{center}
\begin{tabular}{|c|c|c|}
\hline
\textbf{
𝑋
𝑖
X
i
	​

} & \textbf{Frecuencia (
𝑓
𝑖
f
i
	​

)} & \textbf{Frecuencia Acumulada (
𝐹
𝑖
F
i
	​

)} \
\hline
4                & 4                           & 4                                     \ \hline
5                & 8                           & 12                                    \ \hline
6                & 10                          & 22                                    \ \hline
7                & 20                          & 42                                    \ \hline
8                & 8                           & 50                                    \ \hline
\textbf{Total}   & \textbf{n=50}               &                                       \
\hline
\end{tabular}
\end{center}
\textit{Solución:}
Total de datos 
𝑛
=
50
n=50
 (par). La mediana es el promedio de los datos en las posiciones 
50
2
=
25
2
50
	​

=25
 y 
50
2
+
1
=
26
2
50
	​

+1=26
.
Buscamos en la Frecuencia Acumulada (
𝐹
𝑖
F
i
	​

):
\begin{itemize}
\item Hasta 
𝑋
=
6
X=6
, se acumulan 22 datos.
\item Para 
𝑋
=
7
X=7
, la frecuencia acumulada llega a 42. Esto significa que los datos desde la posición 23 hasta la 42 son iguales a 7.
\end{itemize}
Por lo tanto, el dato 25 y el dato 26 son ambos 7.
La mediana es 
𝑀
𝑒
=
7
+
7
2
=
7
M
e
	​

=
2
7+7
	​

=7
. \
\textbf{Respuesta:} La mediana es 7.

\vspace{1em}
\noindent De acuerdo a la siguiente muestra 
𝑎
+
2
,
𝑎
+
4
,
𝑎
+
6
,
𝑎
+
6
,
𝑎
+
6
,
𝑎
+
4
,
𝑎
+
2
a+2,a+4,a+6,a+6,a+6,a+4,a+2
, la suma de la mediana y la moda es: \
\textit{Solución:}
Muestra ordenada: 
𝑎
+
2
,
𝑎
+
2
,
𝑎
+
4
,
𝑎
+
4
,
𝑎
+
6
,
𝑎
+
6
,
𝑎
+
6
a+2,a+2,a+4,a+4,a+6,a+6,a+6
. 
𝑛
=
7
n=7
.
\begin{itemize}
\item \textbf{Moda (
𝑀
𝑜
M
o
	​

):} El dato más frecuente es 
𝑎
+
6
a+6
.
\item \textbf{Mediana (
𝑀
𝑒
M
e
	​

):} Como 
𝑛
=
7
n=7
 (impar), la mediana es el dato en la posición 
7
+
1
2
=
4
2
7+1
	​

=4
. El cuarto dato es 
𝑎
+
4
a+4
.
\end{itemize}
\textbf{Suma:} 
𝑀
𝑜
+
𝑀
𝑒
=
(
𝑎
+
6
)
+
(
𝑎
+
4
)
=
2
𝑎
+
10
M
o
	​

+M
e
	​

=(a+6)+(a+4)=2a+10
.\
\textbf{Respuesta:} 
2
𝑎
+
10
2a+10
.

\vspace{1em}
\noindent Los datos de una muestra son todos números naturales consecutivos, si no hay ningún dato repetido y la mediana de la muestra es 11.5, entonces ¿qué cantidad de datos no puede tener la muestra?
\textit{Solución:}
Si la mediana es 11.5 (un número no entero), la cantidad de datos (
𝑛
n
) debe ser par. Si 
𝑛
n
 fuera impar, la mediana sería el dato central, que es un número natural, lo cual contradice el enunciado.
Por lo tanto, la cantidad de datos 
𝑛
n
 no puede ser un número impar. \
\textbf{Respuesta:} La cantidad de datos no puede ser un número impar.
\newpage

\section{04/04 - Muestreo y Representatividad}
\subsection{Población y Muestra}
¿Qué inconvenientes puede implicar realizar un censo?
\begin{itemize}
\item \textbf{Cardinalidad (tamaño):} La población puede ser demasiado grande o infinita.
\item \textbf{Destrucción:} El proceso de medición puede destruir el elemento (ej. pruebas de vida útil).
\item \textbf{Costos:} Implica altos costos en tiempo, dinero y recursos.
\item \textbf{Acceso:} Puede ser logísticamente imposible acceder a todos los miembros.
\item \textbf{Tiempo:} Puede tomar tanto tiempo que la información obtenida se vuelve obsoleta.
\end{itemize}

\subsection{Muestreo}
Proceso para escoger los elementos que conformarán la muestra. \
\textbf{Es fundamental que la muestra sea representativa para realizar una inferencia estadística válida.}

\subsubsection{Representatividad}
Debe reflejar las características de la población. Claves:
\begin{itemize}
\item \textbf{Tamaño (
𝑛
n
):} Debe ser suficientemente grande.
\item \textbf{Aleatoriedad:} Cada elemento debe tener una probabilidad conocida de ser seleccionado para minimizar el sesgo.
\end{itemize}
Notación: \textbf{N} para el tamaño de la población y \textbf{n} para el tamaño de la muestra.

\subsection{Tipos de Muestreo Probabilístico}
Cada unidad tiene una probabilidad conocida y no nula de ser seleccionada.

\subsubsection{Muestreo Aleatorio Simple (M.A.S)}
Cada posible muestra de tamaño 
𝑛
n
 tiene la misma probabilidad de ser elegida. Requiere un listado completo (marco muestral).
\begin{figure}[htbp]
\centering
\includegraphics[width=0.5\textwidth]{MAS}
\caption{Muestreo Aleatorio Simple}
\label{fig:MAS}
\end{figure}

\subsubsection{Muestreo Estratificado}
Se usa cuando la población se puede dividir en subgrupos (estratos) internamente homogéneos. Se toma una muestra aleatoria de cada estrato. Es más preciso si hay baja variabilidad dentro de los estratos y alta variabilidad entre ellos.
\begin{figure}[htbp]
\centering
\includegraphics[width=0.5\textwidth]{MEP}
\caption{Muestreo Estratificado Proporcional}
\label{fig:MEP}
\end{figure}

\subsubsection{Muestreo por Conglomerados (Clusters)}
Se usa cuando la población está dividida en grupos naturales (conglomerados). Se selecciona una muestra aleatoria de conglomerados y se analizan \textbf{todos} los individuos de los conglomerados elegidos. Es eficiente en costos, especialmente si los conglomerados son internamente heterogéneos.
\begin{figure}[htbp]
\centering
\includegraphics[width=0.65\textwidth]{MPC}
\caption{Muestreo por Conglomerados}
\label{fig:MPC}
\end{figure}

\subsubsection{Muestreo Aleatorio Sistemático}
Se elige un elemento al azar al principio y luego se seleccionan los demás a intervalos regulares (
𝑘
=
𝑁
/
𝑛
k=N/n
) de una lista ordenada.
\begin{figure}[htbp]
\centering
\includegraphics[width=0.6\textwidth]{MASIS}
\caption{Muestreo Aleatorio Sistemático}
\label{fig:MASIS}
\end{figure}
\newpage

\subsection{Muestreos No Probabilísticos}
La selección es subjetiva y no permite inferencia estadística formal.

\subsubsection{Muestreo por Cuotas}
Se fijan "cuotas" de individuos con ciertas características y el entrevistador los selecciona por conveniencia hasta llenar la cuota.
\begin{figure}[htbp]
\centering
\includegraphics[width=0.5\textwidth]{MPCU}
\caption{Muestreo por cuotas}
\label{fig:MPCU}
\end{figure}

\subsubsection{Muestreo Bola de Nieve}
Los primeros individuos contactados ayudan a encontrar a otros, útil para poblaciones difíciles de localizar.
\begin{figure}[htbp]
\centering
\includegraphics[width=0.5\textwidth]{MBN}
\caption{Muestreo Bola de Nieve}
\label{fig:MBC}
\end{figure}

\subsubsection{Muestreo por Juicio o Conveniencia}
La selección se basa en el juicio del investigador o en la facilidad de acceso a los sujetos.
\begin{figure}[htbp]
\centering
\includegraphics[width=0.75\textwidth]{MPJ}
\caption{Muestreo Por Juicio}
\label{fig:MPJ}
\end{figure}

\begin{figure}[htbp]
\centering
\includegraphics[width=0.35\linewidth]{patata}
\caption{Patata para rellenar el espacio}
\label{fig:patata}
\end{figure}
\newpage

\section{10/04 - Medidas de Dispersión}
\textbf{\textit{Objetivo: Aplicar y comprender propiedades de las medidas de dispersión}}
\subsection{Medidas de Dispersión}
Las medidas de tendencia central (como la media) no son suficientes por sí solas para describir un conjunto de datos, ya que no indican cuán dispersos o concentrados están los datos alrededor de ese centro. Consideremos dos conjuntos con la misma media 
𝑥
ˉ
=
0
x
ˉ
=0
:
[ A = {-4, 4, -4, 4} \quad (\text{Media } \bar{x}_A = 0) ]
[ B = {7, 1, -6, -2} \quad (\text{Media } \bar{x}_B = 0) ]
Ambos tienen 
𝑥
ˉ
=
0
x
ˉ
=0
, pero los datos en el conjunto 
𝐴
A
 están menos dispersos (más concentrados alrededor de la media) que en el conjunto 
𝐵
B
. Las medidas de dispersión cuantifican esta variabilidad o "esparcimiento" de los datos.

\subsubsection{Rango (o Amplitud Total):}
Se define como la diferencia entre el valor máximo y el valor mínimo de los datos.
[ Rango = x_{max} - x_{min} ]
Es una medida simple pero muy sensible a valores extremos y no considera la distribución de los datos intermedios.

\subsubsection{Desviación Media (DM):}
Dada una variable 
𝑋
X
, con 
𝑛
n
 datos 
𝑥
1
,
𝑥
2
,
…
,
𝑥
𝑛
x
1
	​

,x
2
	​

,…,x
n
	​

 y media aritmética 
𝑥
ˉ
x
ˉ
. Se define la desviación media como el promedio de las desviaciones absolutas de cada dato respecto a la media:
[ DM = \frac{|x_1-\bar{x}|+|x_2-\bar{x}|+\dots+|x_n-\bar{x}|}{n} = \frac{\sum_{i=1}^{n} |x_i - \bar{x}|}{n} ]
Mide el promedio de cuánto se desvían los datos de la media, en valor absoluto.

\subsubsection{\texorpdfstring{Varianza (
𝜎
2
σ
2
 para población, 
𝑠
2
s
2
 para muestra)}{Varianza (sigma-cuadrado para población, s-cuadrado para muestra)}}
Es el promedio de las desviaciones al cuadrado de cada dato respecto a la media. Es la medida de dispersión más utilizada junto con su raíz cuadrada (la desviación estándar).
Para una \textbf{población} de 
𝑁
N
 datos:
[ \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} ]
Donde 
𝜇
μ
 es la media poblacional. Si los datos 
𝑥
1
,
…
,
𝑥
𝑛
x
1
	​

,…,x
n
	​

 constituyen toda la población (y 
𝑥
ˉ
x
ˉ
 es su media):
[ \sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n} ]
Para una \textbf{muestra} de 
𝑛
n
 datos, la varianza muestral \textit{insesgada} (estimador de 
𝜎
2
σ
2
) es:
[ s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1} ]
(En este curso, si no se especifica, 
𝜎
2
σ
2
 con denominador 
𝑛
n
 se refiere a la varianza de un conjunto de datos específico, sea este una población o una muestra descrita como tal).

\subsubsection{\texorpdfstring{Desviación Estándar (o Típica) (
𝜎
σ
 para población, 
𝑠
s
 para muestra)}{Desviación Estándar (o Típica) (sigma para población, s para muestra)}}
Es la raíz cuadrada positiva de la varianza. Tiene la ventaja de estar expresada en las mismas unidades que los datos originales.
[ \sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}} ]
[ s = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}} ]

\subsubsection{\texorpdfstring{Propiedades de 
𝜎
σ
 y 
𝜎
2
σ
2
 (usando la definición con denominador 
𝑛
n
)}{Propiedades de sigma y sigma-cuadrado (usando la definición con denominador n)}}
\begin{center}
\begin{enumerate}
\item 
𝜎
≥
0
σ≥0
 y 
𝜎
2
≥
0
σ
2
≥0
. Son siempre no negativas.
\item 
𝜎
=
0
⟺
𝜎
2
=
0
⟺
𝑥
𝑖
=
𝑥
ˉ
σ=0⟺σ
2
=0⟺x
i
	​

=
x
ˉ
 para todo 
𝑖
⟺
𝑥
𝑖
=
𝑥
𝑗
i⟺x
i
	​

=x
j
	​

 para todo 
𝑖
,
𝑗
∈
{
1
,
…
,
𝑛
}
i,j∈{1,…,n}
. La desviación estándar (y varianza) es cero si y sólo si todos los datos son iguales.
\item Si a todos los datos de un conjunto se les suma (o resta) una constante 
𝑘
k
 (transformación 
𝑦
𝑖
=
𝑥
𝑖
+
𝑘
y
i
	​

=x
i
	​

+k
), la nueva media es 
𝑦
ˉ
=
𝑥
ˉ
+
𝑘
y
ˉ
	​

=
x
ˉ
+k
, pero la varianza y la desviación estándar no cambian: 
𝜎
𝑦
2
=
𝜎
𝑥
2
σ
y
2
	​

=σ
x
2
	​

 y 
𝜎
𝑦
=
𝜎
𝑥
σ
y
	​

=σ
x
	​

.
\item Si todos los datos de un conjunto se multiplican (o dividen) por una constante 
𝑘
k
 (transformación 
𝑦
𝑖
=
𝑘
⋅
𝑥
𝑖
y
i
	​

=k⋅x
i
	​

), la nueva media es 
𝑦
ˉ
=
𝑘
𝑥
ˉ
y
ˉ
	​

=k
x
ˉ
, la nueva varianza es 
𝜎
𝑦
2
=
𝑘
2
𝜎
𝑥
2
σ
y
2
	​

=k
2
σ
x
2
	​

, y la nueva desviación estándar es 
𝜎
𝑦
=
∣
𝑘
∣
𝜎
𝑥
σ
y
	​

=∣k∣σ
x
	​

.
\item Fórmula computacional (o abreviada) para la varianza: 
𝜎
2
=
∑
𝑥
𝑖
2
𝑛
−
(
𝑥
ˉ
)
2
=
𝑥
2
‾
−
(
𝑥
ˉ
)
2
σ
2
=
n
∑x
i
2
	​

	​

−(
x
ˉ
)
2
=
x
2
−(
x
ˉ
)
2
. Es decir, la varianza es la media de los cuadrados de los datos menos el cuadrado de la media de los datos.
\item 
𝜎
2
=
𝜎
⟺
𝜎
=
0
∨
𝜎
=
1
σ
2
=σ⟺σ=0∨σ=1
. (Asumiendo que 
𝜎
σ
 es el valor numérico de la desviación estándar).
\item 
𝜎
2
<
𝜎
⟺
0
<
𝜎
<
1
σ
2
<σ⟺0<σ<1
.
\item 
𝜎
2
>
𝜎
⟺
𝜎
>
1
σ
2
>σ⟺σ>1
.
\end{enumerate}
\end{center}
\newpage

\section{16/04 - Propiedades de la Varianza y Desviación Estándar}
\subsection{\texorpdfstring{Demostración de Propiedades Relacionadas con el Valor de 
𝜎
σ
}{Demostraciones de Propiedades Relacionadas con el Valor de sigma}}
Sea la variable 
𝑋
X
 con datos 
𝑥
1
,
…
,
𝑥
𝑛
x
1
	​

,…,x
n
	​

, media 
𝑥
ˉ
x
ˉ
 y varianza 
𝜎
𝑥
2
σ
x
2
	​

.
Sea 
𝑌
Y
 una nueva variable tal que 
𝑦
𝑖
=
𝑘
⋅
𝑥
𝑖
y
i
	​

=k⋅x
i
	​

 para cada 
𝑖
i
.
Sabemos que la media de 
𝑌
Y
 es 
𝑦
ˉ
=
𝑘
⋅
𝑥
ˉ
y
ˉ
	​

=k⋅
x
ˉ
.
La varianza de 
𝑌
Y
, 
𝜎
𝑦
2
σ
y
2
	​

, se define como:
[\sigma_y^2=\frac{\sum_{i=1}^{n} (y_i - \bar{y})^2}{n} ]
Sustituyendo 
𝑦
𝑖
=
𝑘
𝑥
𝑖
y
i
	​

=kx
i
	​

 y 
𝑦
ˉ
=
𝑘
𝑥
ˉ
y
ˉ
	​

=k
x
ˉ
:
[\sigma_y^2=\frac{\sum_{i=1}^{n} (kx_i - k\bar{x})^2}{n}]
Factorizando 
𝑘
k
 dentro del paréntesis al cuadrado:
[\sigma_y^2=\frac{\sum_{i=1}^{n} [k(x_i - \bar{x})]^2}{n}]
Aplicando la potencia al producto:
[\sigma_y^2=\frac{\sum_{i=1}^{n} k^2(x_i - \bar{x})^2}{n}]
Como 
𝑘
2
k
2
 es una constante para la sumatoria, puede salir fuera:
[\sigma_y^2=k^2 \cdot \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}]
Reconociendo que 
∑
𝑖
=
1
𝑛
(
𝑥
𝑖
−
𝑥
ˉ
)
2
𝑛
n
∑
i=1
n
	​

(x
i
	​

−
x
ˉ
)
2
	​

 es la definición de 
𝜎
𝑥
2
σ
x
2
	​

:
[\sigma_y^2=k^2 \cdot \sigma_x^2]
Tomando la raíz cuadrada positiva para obtener la desviación estándar (ya que 
𝜎
𝑥
≥
0
σ
x
	​

≥0
):
[\sigma_y = \sqrt{k^2 \cdot \sigma_x^2} = \sqrt{k^2} \cdot \sqrt{\sigma_x^2} = |k| \cdot \sigma_x]
L.Q.Q.D. (Lo Que Queríamos Demostrar)

\subsection{Ejercicio}
Dados los datos: -2, 0, 2, 4, 6. (
𝑛
=
5
n=5
). Determinar:
\begin{enumerate}
\item \texorpdfstring{
𝑥
ˉ
x
ˉ
}{x barra} \
\textit{Solución:} 
𝑥
ˉ
=
−
2
+
0
+
2
+
4
+
6
5
=
10
5
=
2
x
ˉ
=
5
−2+0+2+4+6
	​

=
5
10
	​

=2
. \
\item \texorpdfstring{
𝜎
σ
 (desviación estándar)}{sigma (desviación estándar)} \
\textit{Solución:} Primero calculamos la varianza 
𝜎
2
σ
2
:
\begin{align*} \sigma^2 &= \frac{\sum (x_i - \bar{x})^2}{n} \ &= \frac{(-2-2)^2+(0-2)^2+(2-2)^2+(4-2)^2+(6-2)^2}{5} \ &= \frac{(-4)^2+(-2)^2+(0)^2+(2)^2+(4)^2}{5} \ &= \frac{16+4+0+4+16}{5} = \frac{40}{5} = 8 \end{align*}
Ahora la desviación estándar: 
𝜎
=
𝜎
2
=
8
=
4
⋅
2
=
2
2
≈
2.828
σ=
σ
2
	​

=
8
	​

=
4⋅2
	​

=2
2
	​

≈2.828
. \
\item \texorpdfstring{
𝑥
2
‾
x
2
 (el promedio de los cuadrados de los datos)}{x-cuadrado barra (el promedio...)} \
\textit{Solución:} Los cuadrados de los datos son: 
(
−
2
)
2
=
4
,
0
2
=
0
,
2
2
=
4
,
4
2
=
16
,
6
2
=
36
(−2)
2
=4,0
2
=0,2
2
=4,4
2
=16,6
2
=36
.
[ \overline{x^2} = \frac{4+0+4+16+36}{5} = \frac{60}{5} = 12 ]
\item \texorpdfstring{Calcular 
𝑥
2
‾
−
(
𝑥
ˉ
)
2
x
2
−(
x
ˉ
)
2
 y comparar con 
𝜎
2
σ
2
}{Calcular x-cuadrado-barra - (x-barra)-cuadrado y comparar con sigma-cuadrado}. \
\textit{Solución:} 
𝑥
2
‾
−
(
𝑥
ˉ
)
2
=
12
−
(
2
)
2
=
12
−
4
=
8
x
2
−(
x
ˉ
)
2
=12−(2)
2
=12−4=8
. \
Este resultado (8) es igual a la varianza 
𝜎
2
σ
2
 calculada en el punto 2, lo cual verifica la propiedad 5 (fórmula computacional de la varianza).
\end{enumerate}
\newpage

\subsection{Demostración Propiedad 5 (Fórmula Computacional de la Varianza)}
Partimos de la definición de varianza (usando denominador 
𝑛
n
):
[\sigma^2=\frac{\sum_{i=1}^{n} (x_i-\bar{x})^2}{n}]
Expandimos el binomio al cuadrado 
(
𝑎
−
𝑏
)
2
=
𝑎
2
−
2
𝑎
𝑏
+
𝑏
2
(a−b)
2
=a
2
−2ab+b
2
:
[\sigma^2=\frac{\sum_{i=1}^{n} (x_i^2 - 2x_i\bar{x} + (\bar{x})^2)}{n}]
Distribuimos la sumatoria y el denominador 
𝑛
n
:
[\sigma^2=\frac{\sum x_i^2}{n} - \frac{\sum 2x_i\bar{x}}{n} + \frac{\sum (\bar{x})^2}{n}]
En el segundo término, 
2
𝑥
ˉ
2
x
ˉ
 es una constante respecto a la suma 
∑
𝑥
𝑖
∑x
i
	​

. En el tercer término, 
(
𝑥
ˉ
)
2
(
x
ˉ
)
2
 es una constante, y 
∑
𝑖
=
1
𝑛
(
𝑥
ˉ
)
2
=
𝑛
(
𝑥
ˉ
)
2
∑
i=1
n
	​

(
x
ˉ
)
2
=n(
x
ˉ
)
2
.
[\sigma^2=\frac{\sum x_i^2}{n} - 2\bar{x} \frac{\sum x_i}{n} + \frac{n(\bar{x})^2}{n}]
Reconocemos que 
∑
𝑥
𝑖
2
𝑛
=
𝑥
2
‾
n
∑x
i
2
	​

	​

=
x
2
 (la media de los cuadrados) y 
∑
𝑥
𝑖
𝑛
=
𝑥
ˉ
n
∑x
i
	​

	​

=
x
ˉ
 (la media):
[\sigma^2=\overline{x^2} - 2\bar{x} (\bar{x}) + (\bar{x})^2]
[\sigma^2=\overline{x^2} - 2(\bar{x})^2 + (\bar{x})^2]
[\sigma^2=\overline{x^2} - (\bar{x})^2]
L.Q.Q.D.
\newpage

\section{23/04 - Demostraciones sobre el Valor de la Desviación Estándar}
\subsection{\texorpdfstring{Demostraciones de Propiedades Relacionadas con el Valor de 
𝜎
σ
}{Demostraciones de Propiedades Relacionadas con el Valor de sigma}}
Recordar que 
𝜎
≥
0
σ≥0
 por definición (es una raíz cuadrada positiva o cero).

\subsubsection{Propiedad 6: \texorpdfstring{
𝜎
2
=
𝜎
⟺
𝜎
=
0
∨
𝜎
=
1
σ
2
=σ⟺σ=0∨σ=1
}{sigma-cuadrado = sigma <=> sigma=0 v sigma=1}}
Partimos de la ecuación:
[\sigma^2=\sigma ]
Reordenamos para formar una ecuación cuadrática en 
𝜎
σ
:
[\sigma^2-\sigma=0 ]
Factorizamos 
𝜎
σ
:
[\sigma(\sigma-1)=0 ]
Esto implica que uno de los factores debe ser cero:
[\sigma=0 \quad \text{o} \quad \sigma-1=0 ]
Por lo tanto:
[\sigma=0 \vee \sigma=1 ]
L.Q.Q.D.

\subsubsection{Propiedad 7: \texorpdfstring{
𝜎
2
<
𝜎
⟺
0
<
𝜎
<
1
σ
2
<σ⟺0<σ<1
}{sigma-cuadrado < sigma <=> 0 < sigma < 1}}
Partimos de la desigualdad:
[\sigma^2 < \sigma ]
Reordenamos:
[\sigma^2-\sigma < 0 ]
Factorizamos:
[\sigma(\sigma-1) < 0 ]
Para que el producto de dos factores sea negativo, uno debe ser positivo y el otro negativo. Analizamos los signos de 
𝜎
σ
 y 
(
𝜎
−
1
)
(σ−1)
:
\begin{center}
\begin{tabular}{c|ccccc}
Intervalo                   & 
(
−
∞
,
0
)
(−∞,0)
 & 
0
0
 & 
(
0
,
1
)
(0,1)
 & 
1
1
 & 
(
1
,
+
∞
)
(1,+∞)
 \
\hline
Signo de 
𝜎
σ
           & 
−
−
            & 
0
0
 & 
+
+
      & 
+
+
 & 
+
+
            \
Signo de 
(
𝜎
−
1
)
(σ−1)
       & 
−
−
            & 
−
−
 & 
−
−
      & 
0
0
 & 
+
+
            \
\hline
Signo de 
𝜎
(
𝜎
−
1
)
σ(σ−1)
 & 
+
+
            & 
0
0
 & 
−
−
      & 
0
0
 & 
+
+
            \
\end{tabular}
\end{center}
La desigualdad 
𝜎
(
𝜎
−
1
)
<
0
σ(σ−1)<0
 se cumple cuando 
𝜎
∈
(
0
,
1
)
σ∈(0,1)
.
Dado que 
𝜎
≥
0
σ≥0
 por definición, el intervalo 
(
−
∞
,
0
)
(−∞,0)
 no es relevante para la desviación estándar.
Por lo tanto:
[0 < \sigma < 1 ]
L.Q.Q.D.

\subsubsection{Propiedad 8: \texorpdfstring{
𝜎
2
>
𝜎
⟺
𝜎
>
1
σ
2
>σ⟺σ>1
}{sigma-cuadrado > sigma <=> sigma > 1}}
Partimos de la desigualdad:
[\sigma^2 > \sigma ]
Reordenamos:
[\sigma^2-\sigma > 0 ]
Factorizamos:
[\sigma(\sigma-1) > 0 ]
Para que el producto de dos factores sea positivo, ambos deben ser positivos o ambos deben ser negativos. Usando la tabla de signos anterior:
\begin{itemize}
\item Ambos negativos: 
𝜎
<
0
σ<0
 y 
𝜎
−
1
<
0
σ−1<0
 (es decir, 
𝜎
<
0
σ<0
). No es posible para 
𝜎
σ
.
\item Ambos positivos: 
𝜎
>
0
σ>0
 y 
𝜎
−
1
>
0
σ−1>0
 (es decir, 
𝜎
>
1
σ>1
).
\end{itemize}
La desigualdad 
𝜎
(
𝜎
−
1
)
>
0
σ(σ−1)>0
 se cumple cuando 
𝜎
∈
(
−
∞
,
0
)
∪
(
1
,
+
∞
)
σ∈(−∞,0)∪(1,+∞)
.
Considerando la restricción 
𝜎
≥
0
σ≥0
:
\begin{itemize}
\item Si 
𝜎
=
0
σ=0
, entonces 
𝜎
(
𝜎
−
1
)
=
0
σ(σ−1)=0
, lo cual no satisface 
0
>
0
0>0
.
\item El intervalo 
(
−
∞
,
0
)
(−∞,0)
 no es válido para 
𝜎
σ
.
\item Nos queda el intervalo 
(
1
,
+
∞
)
(1,+∞)
.
\end{itemize}
Por lo tanto:
[\sigma > 1]
L.Q.Q.D.
\newpage

\section{30/05 - Medidas de Posición: Cuartiles, Quintiles, Deciles y Percentiles}
Dado un conjunto de datos ordenados se define:

\subsection{Cuartiles}
Son tres valores que dividen en partes iguales a un conjunto de datos ordenados. Se denominan 
𝑄
1
Q
1
	​

, 
𝑄
2
Q
2
	​

 y 
𝑄
3
Q
3
	​

.
\textbf{Observacion:} 
𝑄
2
=
𝑀
𝑒
Q
2
	​

=M
e
	​

.

\subsection{Quintiles}
Son los 4 valores que dividen en partes iguales a los datos, que corresponden al 20%, 40%, 60% y 80%.

\subsection{Deciles}
Son los 9 valores que dividen en partes iguales a los datos, que corresponden al 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80% y 90%.

\subsection{Percentiles}
Son los 99 valores que dividen en partes iguales a los datos, que corresponden al 1%, 2%, 3%, ... ,99%.
[ P_i= \frac{i \cdot n}{100} ] Corresponde a la posición del percentil.
\newpage

\section{11/06 - Principios Fundamentales de la Combinatoria}
\subsection{Combinatoria}
Son técnicas de conteo. Sean A y B dos sucesos, que pueden ocurrir de 
𝑎
a
 y 
𝑏
b
 maneras respectivamente.
\begin{itemize}
\item \textbf{\textit{Principio Aditivo:}} Si los sucesos no pueden ocurrir de manera simultánea (son mutuamente excluyentes), entonces hay \textit{a+b} maneras posibles de que ocurra \textit{A o B}.
\item \textbf{\textit{Principio Multiplicativo:}} Si los sucesos ocurren uno a continuación del otro o de manera simultánea, entonces hay 
𝑎
⋅
𝑏
a⋅b
 formas de que ocurra \textit{A y B}.
\end{itemize}

\subsection{Ejercicios}
\begin{enumerate}
\item Al lanzar una moneda y un dado, ¿cuántos resultados posibles hay? \
\textit{Solución:}
Lanzar una moneda y un dado son sucesos independientes que ocurren simultáneamente. Usamos el principio multiplicativo.
\begin{itemize}
\item Resultados de la moneda: 2 (cara, sello).
\item Resultados del dado: 6 (1, 2, 3, 4, 5, 6).
\end{itemize}
Total de resultados: 
2
×
6
=
12
2×6=12
. \
\textbf{Respuesta: 12 resultados posibles.}

code
Code
download
content_copy
expand_less
\item Si Pedro tiene 5 lápices de pasta, 4 de tinta y 3 de grafito, ¿de cuántas maneras puede elegir un lápiz para escribir? \\
      \textit{Solución:}
      Pedro debe elegir un lápiz de pasta \textbf{o} uno de tinta \textbf{o} uno de grafito. Son elecciones mutuamente excluyentes. Usamos el principio aditivo.
      \begin{itemize}
	      \item Maneras de elegir un lápiz de pasta: 5.
	      \item Maneras de elegir un lápiz de tinta: 4.
	      \item Maneras de elegir un lápiz de grafito: 3.
      \end{itemize}
      Total de maneras: $5 + 4 + 3 = 12$. \\
      \textbf{Respuesta: 12 maneras distintas.}

\item En un local se puede elegir un combo con las siguientes opciones disponibles: 5 tipos de hamburguesas, 4 bebidas distintas o bien un jugo de 2 sabores distintos. Si el combo consiste en una hamburguesa y una bebida/jugo, ¿de cuántas maneras distintas se puede elegir? \\
      \textit{Solución:}
      La elección del combo tiene dos etapas: elegir una hamburguesa \textbf{y} elegir un líquido.
      \begin{itemize}
	      \item \textbf{Etapa 1 (Hamburguesa):} Hay 5 opciones.
	      \item \textbf{Etapa 2 (Líquido):} Se puede elegir una bebida \textbf{o} un jugo. Esta es una sub-decisión que usa el principio aditivo.
	            \begin{itemize}
		            \item Opciones de bebida: 4.
		            \item Opciones de jugo: 2.
		            \item Total de opciones de líquido: $4 + 2 = 6$.
	            \end{itemize}
      \end{itemize}
      Para formar el combo, se aplica el principio multiplicativo entre la Etapa 1 y la Etapa 2.
      Total de combos: $5 \text{ (hamburguesas)} \times 6 \text{ (líquidos)} = 30$. \\
      \textbf{Respuesta: Se puede elegir de 30 maneras distintas.}

\end{enumerate}
\newpage

\section{07/07 - Permutaciones}
\textbf{\textit{\large{Diferenciar distintas Permutaciones}}}

\subsection{Combinatoria}
Evento A: a maneras

Evento B: b maneras

\begin{itemize}
\item Principio Aditivo: 
𝑎
+
𝑏
a+b
 \textbf{Excluyentes}
\item Principio Multiplicativo: 
𝑎
⋅
𝑏
a⋅b
 \textbf{Simultáneos}
\item \textbf{\textit{Ej:}}
\begin{itemize}
\item Evento A: Lanzar un dado
\item Evento B: lanzar un dado 2 veces
\end{itemize}
\end{itemize}

\subsubsection{Permutación simple} Corresponde a la manera en que se pueden ordenar 
𝑛
n
 objetos.
\begin{minipage}{0.35\textwidth}
\centering
[ P_n = n! ]
\end{minipage}
\hfill
\begin{minipage}{0.55\textwidth}
\centering
[ P_4 = 4!= 4 \cdot 3 \cdot 2 \cdot 1 ]
\end{minipage}

\subsubsection{Permutación con repetición} Si tienes 
𝑛
n
 elementos y un elemento se repite 
𝑟
1
r
1
	​

 veces, otro 
𝑟
2
r
2
	​

 veces y así sucesivamente, entonces se pueden ordenar:
[ P_{r_1, r_2, \dots}^n = \frac{n!}{r_1! \cdot r_2! \cdot \dots} ]

\subsubsection{Permutación Circular} Si tenemos 
𝑛
n
 elementos, los podemos ordenar de:
[ PC_n = \frac{n!}{n} = (n-1)! ]

\subsection{Ejercicios}

\begin{enumerate}[label=\alph*.)]
\item ¿De cuántas maneras se pueden ordenar las letras de la palabra LEMUR para formar otra palabra (con o sin sentido)?
[ P_5 = 5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120 ] \

code
Code
download
content_copy
expand_less
\item ¿Y para la palabra ARROYO? ¿Y CARRERA?
      \begin{minipage}{0.45\textwidth}
	      \centering
	      \textbf{ARROYO:}
	      \[ P_{2, 2}^6 = \frac{6!}{2! \cdot 2!} = \frac{720}{4} = 180 \]
      \end{minipage}
      \hfill
      \begin{minipage}{0.45\textwidth}
	      \centering
	      \textbf{CARRERA}
	      \[ P_{2,3}^7 = \frac{7!}{2! \cdot 3!} = \frac{7\cdot 6 \cdot 5 \cdot 4}{2} = 420 \]
      \end{minipage}

      \phantom p \\

\item ¿De cuántas maneras se pueden sentar en una mesa de 4 sillas, 4 personas?
      \[ PC_4 = \frac{4!}{4} =\frac{4 \cdot 3!}{4} = 3! = 6 \]

\end{enumerate}
\newpage

\section{04/08 - Variaciones y Combinaciones}
\subsection{Variación (o arreglo)}
Corresponde al número de ordenaciones de 
𝑘
k
 elementos, con 
𝑘
≤
𝑛
k≤n
, de un total de 
𝑛
n
 elementos.
[V_k^n = n \cdot (n - 1) \cdot (n - 2) \cdot \dots \cdot (n - (k - 1)) = \frac{n!}{(n - k)!} ]
\subsubsection*{Con repetición}
[VR_k^n = n^k ]

\subsection{Combinaciones} Corresponde a la cantidad de grupos (o subconjuntos) de 
𝑘
k
 elementos de un total de 
𝑛
n
 elementos.
[C_k^n = \binom{n}{k} = \frac{V_k^n}{k!} = \frac{n!}{(n - k)! \cdot k!} ]

\subsection*{¿Cómo Diferenciar?}
Para determinar qué fórmula usar, sigue este diagrama de flujo:
\begin{enumerate}[label=\bfseries Paso \arabic*:, wide]
\item \textbf{¿Importa el orden de los elementos seleccionados?}
\begin{itemize}
\item[\bfseries a)] \textbf{Sí, el orden importa 
→
→
 PERMUTACIÓN / VARIACIÓN}
\begin{itemize}
\item \textbf{¿Se usan TODOS los elementos (
𝑘
=
𝑛
k=n
)? 
→
→
 PERMUTACIÓN}
\begin{itemize}
\item \textbf{Arreglo Lineal (en una fila):}
\begin{itemize}
\item ¿Hay elementos repetidos? (ej. palabra C-A-S-A) 
→
→
 Permutación con repetición: 
𝑃
𝑛
1
,
…
,
𝑛
𝑘
𝑛
=
𝑛
!
𝑛
1
!
…
𝑛
𝑘
!
P
n
1
	​

,…,n
k
	​

n
	​

=
n
1
	​

!…n
k
	​

!
n!
	​


\item ¿Son todos los elementos distintos? 
→
→
 Permutación simple: 
𝑃
𝑛
=
𝑛
!
P
n
	​

=n!

\end{itemize}
\item \textbf{Arreglo Circular (en una mesa, un llavero, etc.):}
\begin{itemize}
\item Asume que los elementos son distintos y las rotaciones no cuentan como un nuevo orden.
\item 
→
→
 Permutación Circular: $ PC_n = (n-1)! 
k<n$)? 
→
→
 VARIACIÓN}
\begin{itemize}
\item ¿Se permite repetir elementos? 
→
→
 Variación con repetición: 
𝑉
𝑅
𝑘
𝑛
=
𝑛
𝑘
VR
k
n
	​

=n
k

\item ¿No se permite repetir? 
→
→
 Variación simple: 
𝑉
𝑘
𝑛
=
𝑛
!
(
𝑛
−
𝑘
)
!
V
k
n
	​

=
(n−k)!
n!
	​


\end{itemize}
\end{itemize}
\item[\bfseries b)] \textbf{No, el orden NO importa 
→
→
 COMBINACIÓN}
\begin{itemize}
\item ¿Se permite repetir elementos? 
→
→
 Combinación con repetición: 
𝐶
𝑅
𝑘
𝑛
=
(
𝑛
+
𝑘
−
1
𝑘
)
CR
k
n
	​

=(
k
n+k−1
	​

)

\item ¿No se permite repetir? 
→
→
 Combinación simple: 
𝐶
𝑘
𝑛
=
(
𝑛
𝑘
)
=
𝑛
!
𝑘
!
(
𝑛
−
𝑘
)
!
C
k
n
	​

=(
k
n
	​

)=
k!(n−k)!
n!
	​


\end{itemize}
\end{itemize}
\end{enumerate}

\subsection*{Ejercicios Resueltos}
Aquí tienes los ejercicios con sus soluciones y el razonamiento para cada uno:
\begin{enumerate}[leftmargin=,label=\arabic.]
\item \textbf{En una carrera participan 15 estudiantes. ¿De cuantas maneras se puede formar el podio (1er, 2do, 3er lugar)?}
\begin{itemize}
\item \textbf{Razonamiento:} El orden importa (1er lugar es diferente de 2do). No hay repetición de estudiantes. Se seleccionan 3 de 15. Esto es una Variación simple.
\item \textbf{Cálculo:} 
𝑉
3
15
=
15
⋅
14
⋅
13
=
2730
V
3
15
	​

=15⋅14⋅13=2730
 maneras.
\end{itemize}

code
Code
download
content_copy
expand_less
\item \textbf{¿De cuantas maneras se puede formar una clave numérica de 4 dígitos?}
      \begin{itemize}
	      \item \textbf{Razonamiento:} El orden importa (1234 es diferente de 4321). Los dígitos pueden repetirse (ej. 1111). Se seleccionan 4 dígitos de 10 posibles (0-9). Esto es una **Variación con repetición**.
	      \item \textbf{Cálculo:} $VR_4^{10} = 10^4 = 10000$ maneras.
      \end{itemize}

\item \textbf{¿Y si no se repiten los dígitos (para la clave numérica de 4 dígitos)?}
      \begin{itemize}
	      \item \textbf{Razonamiento:} El orden sigue importando. Los dígitos NO pueden repetirse. Se seleccionan 4 dígitos distintos de 10 posibles. Esto es una **Variación simple**.
	      \item \textbf{Cálculo:} $V_4^{10} = 10 \cdot 9 \cdot 8 \cdot 7 = 5040$ maneras.
      \end{itemize}

\item \textbf{En un curso de 40 estudiantes, ¿Cuántas directivas (Presidente, Vicepresidente, Tesorero) se pueden formar?}
      \begin{itemize}
	      \item \textbf{Razonamiento:} El orden importa (ser Presidente es distinto de ser Vicepresidente). Los estudiantes no pueden ocupar múltiples cargos. Se seleccionan 3 de 40. Esto es una **Variación simple**.
	      \item \textbf{Cálculo:} $V_3^{40} = 40 \cdot 39 \cdot 38 = 59280$ maneras.
      \end{itemize}

\item \textbf{En una asamblea de 100 personas, se escoge una directiva de 3 personas ¿De cuantas maneras se puede hacer?}
      \begin{itemize}
	      \item \textbf{Razonamiento:} Esta pregunta es ambigua. Si "directiva" implica roles específicos (similar al ejercicio anterior), el orden importa. Sin embargo, si es solo un grupo de 3 personas sin roles definidos, el orden no importa (ver el siguiente ejercicio). Asumiendo que se refiere a un grupo donde el orden no importa, como una comisión.
	      \item \textbf{Cálculo (asumiendo que el orden NO importa, es decir, una comisión):} $C_3^{100} = \frac{100 \cdot 99 \cdot 98}{3 \cdot 2 \cdot 1} = 161700$ maneras.
	      \item \textbf{Nota:} Si la intención era que el orden SÍ importaba (ej. Presidente, Secretario, Vocal), entonces sería una Variación: $V_3^{100} = 100 \cdot 99 \cdot 98 = 970200$ maneras. Es crucial aclarar si los roles son distinguibles o no en el enunciado.
      \end{itemize}

\item \textbf{Y cuantas comisiones de 3 personas se pueden hacer (en la asamblea de 100 personas)?}
      \begin{itemize}
	      \item \textbf{Razonamiento:} El orden NO importa (una comisión de Juan, Pedro y María es la misma que María, Pedro y Juan). No hay repetición de personas. Se seleccionan 3 de 100. Esto es una **Combinación simple**.
	      \item \textbf{Cálculo:} $C_3^{100} = \frac{100!}{3!(100-3)!} = \frac{100 \cdot 99 \cdot 98}{3 \cdot 2 \cdot 1} = 161700$ maneras.
      \end{itemize}

\end{enumerate}
\newpage

\section{11/08 - Propiedades de Combinatoria y Triángulo de Pascal}
\subsection{Propiedades de los Números Combinatorios}
Los números combinatorios, denotados como 
(
𝑛
𝑘
)
(
k
n
	​

)
, tienen propiedades útiles que simplifican los cálculos.
\begin{enumerate}
\item \textbf{Combinaciones de los extremos:} Seleccionar todos los elementos de un conjunto es posible de una sola manera, al igual que no seleccionar ninguno (eligiendo el conjunto vacío).
[ \binom{n}{n} = \binom{n}{0} = 1 ]

code
Code
download
content_copy
expand_less
\item \textbf{Propiedad de simetría:} El número de maneras de elegir $k$ elementos de un conjunto de $n$ es igual al número de maneras de *no elegir* (o dejar) $n-k$ elementos.
      \[ \binom{n}{k} = \binom{n}{n-k} \quad \text{para } k \leq n \]

\item \textbf{Identidad de Pascal:} Esta identidad es la base para construir el Triángulo de Pascal. Establece que la suma de dos números combinatorios consecutivos en una fila del triángulo da como resultado el número combinatorio que se encuentra debajo de ellos.
      \[ \binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1} \]

\end{enumerate}

\subsection{Demostraciones}
\subsubsection{\texorpdfstring{Propiedad 1: 
(
𝑛
𝑛
)
=
(
𝑛
0
)
=
1
(
n
n
	​

)=(
0
n
	​

)=1
}{Propiedad 1: C(n,n) = C(n,0) = 1}}
La demostración se basa en la aplicación directa de la fórmula de la combinación, 
(
𝑛
𝑘
)
=
𝑛
!
𝑘
!
(
𝑛
−
𝑘
)
!
(
k
n
	​

)=
k!(n−k)!
n!
	​

, y en la definición matemática de que 
0
!
=
1
0!=1
.

\vspace{1em}
\noindent \textbf{Caso 1: 
(
𝑛
𝑛
)
(
n
n
	​

)
}
[ \binom{n}{n} = \frac{n!}{(n-n)! \cdot n!} = \frac{n!}{0! \cdot n!} ]
\textit{Comentario: Al aplicar la fórmula, el término 
(
𝑛
−
𝑛
)
!
(n−n)!
 se convierte en 
0
!
0!
. Luego, los términos 
𝑛
!
n!
 del numerador y denominador se cancelan, dejando 
1
/
0
!
1/0!
. Como 
0
!
0!
 es 1, el resultado es 1.}
[ \frac{n!}{0! \cdot n!} = \frac{1}{0!} = \frac{1}{1} = 1 ]
\textit{Interpretación: Solo hay una forma de elegir n elementos de un conjunto de n (es decir, tomarlos todos).}

\vspace{1em}
\noindent \textbf{Caso 2: 
(
𝑛
0
)
(
0
n
	​

)
}
[ \binom{n}{0} = \frac{n!}{(n-0)! \cdot 0!} = \frac{n!}{n! \cdot 0!} ]
\textit{Comentario: De forma similar, 
(
𝑛
−
0
)
!
(n−0)!
 es simplemente 
𝑛
!
n!
. Al cancelar los términos 
𝑛
!
n!
, nuevamente obtenemos 
1
/
0
!
1/0!
, que es igual a 1.}
[ \frac{n!}{n! \cdot 0!} = \frac{1}{0!} = \frac{1}{1} = 1 ]
\textit{Interpretación: Solo hay una forma de elegir 0 elementos de un conjunto (es decir, no tomar ninguno).}

\subsubsection{\texorpdfstring{Propiedad 2 (Simetría): 
(
𝑛
𝑘
)
=
(
𝑛
𝑛
−
𝑘
)
(
k
n
	​

)=(
n−k
n
	​

)
}{Propiedad 2 (Simetría): C(n,k) = C(n,n-k)}}
\textit{Comentario: Esta propiedad muestra una hermosa simetría en las combinaciones. Intuitivamente, significa que el acto de elegir 
𝑘
k
 elementos para formar un grupo es equivalente al acto de elegir 
𝑛
−
𝑘
n−k
 elementos para dejarlos fuera de ese grupo. La demostración es algebraica.}

\vspace{1em}
\noindent Partimos de la definición de 
(
𝑛
𝑘
)
(
k
n
	​

)
:
[ \binom{n}{k} = \frac{n!}{k! \cdot (n-k)!} ]
\textit{Comentario: El producto en el denominador es conmutativo, lo que significa que podemos cambiar el orden de 
𝑘
!
k!
 y 
(
𝑛
−
𝑘
)
!
(n−k)!
 sin alterar el resultado.}
[ \frac{n!}{(n-k)! \cdot k!} ]
\textit{Comentario: Ahora, si observamos esta expresión final, corresponde exactamente a la definición de 
(
𝑛
𝑛
−
𝑘
)
(
n−k
n
	​

)
. Por lo tanto, hemos demostrado que las dos expresiones son iguales.}
[ \binom{n}{n-k} = \frac{n!}{(n-k)! \cdot (n-(n-k))!} = \frac{n!}{(n-k)! \cdot k!} ]
Así, se concluye que 
(
𝑛
𝑘
)
=
(
𝑛
𝑛
−
𝑘
)
(
k
n
	​

)=(
n−k
n
	​

)
.

\subsection{Triángulo de Pascal y Binomio de Newton}
El \textbf{Triángulo de Pascal} es una disposición triangular de números donde cada número es la suma de los dos que tiene directamente encima. Este triángulo está íntimamente relacionado con el \textbf{Teorema del Binomio} (o Binomio de Newton), que proporciona una fórmula para expandir potencias de un binomio 
(
𝑎
+
𝑏
)
𝑛
(a+b)
n
.

La fórmula del Binomio de Newton utiliza los números combinatorios como coeficientes para cada término de la expansión. Notablemente, los coeficientes de la expansión de 
(
𝑎
+
𝑏
)
𝑛
(a+b)
n
 corresponden exactamente a los números en la fila 
𝑛
+
1
n+1
 del Triángulo de Pascal.
[ (a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \dots + \binom{n}{n}b^n ]

\begin{figure}[h!]
\centering
\includegraphics[width=0.5\textwidth]{pascal}
\caption{El Triángulo de Pascal, donde cada fila 
𝑛
n
 corresponde a los coeficientes de 
(
𝑎
+
𝑏
)
𝑛
(a+b)
n
.}
\label{fig:pascaltrig}
\end{figure}

\subsection{Conjunto Potencia}
El \textbf{Conjunto Potencia} de un conjunto 
𝐴
A
, denotado como 
𝑃
(
𝐴
)
P(A)
, es el conjunto formado por \textbf{todos los subconjuntos} posibles de 
𝐴
A
, incluyendo el conjunto vacío y el propio conjunto 
𝐴
A
.

La \textbf{cardinalidad} (número de elementos) del conjunto potencia se puede calcular sumando el número de subconjuntos de cada tamaño posible (de tamaño 0, de tamaño 1, de tamaño 2, etc.), lo cual es una suma de números combinatorios. Si el conjunto original 
𝐴
A
 tiene 
𝑛
n
 elementos, la cardinalidad de su conjunto potencia es 
2
𝑛
2
n
.
[ |P(A)| = \sum_{k=0}^{n} \binom{n}{k} = 2^n ]

\subsection{Ejercicios}
\begin{enumerate}
\item \textbf{¿De cuántas maneras se pueden sentar 5 personas en una mesa redonda?} \
\textit{Solución:} Es una permutación circular. 
𝑃
𝐶
5
=
(
5
−
1
)
!
=
4
!
=
24
PC
5
	​

=(5−1)!=4!=24
 maneras.

code
Code
download
content_copy
expand_less
\item \textbf{En una competición participan 40 personas y solo quedan seleccionadas 5.}
      \begin{enumerate}
	      \item \textbf{¿Cuántos grupos distintos pueden quedar seleccionados?} \\
	            \textit{Solución:} El orden no importa, es una combinación. \\
	            $C_5^{40} = \binom{40}{5} = \frac{40!}{5!(35!)} = \frac{40 \cdot 39 \cdot 38 \cdot 37 \cdot 36}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 658,008$ grupos.
	      \item \textbf{¿Cuántos primeros 5 puntajes distintos puede haber?} \\
	            \textit{Solución:} El orden importa (1er, 2do, etc.), es una variación. \\
	            $V_5^{40} = \frac{40!}{(40-5)!} = 40 \cdot 39 \cdot 38 \cdot 37 \cdot 36 = 78,960,960$ maneras.
      \end{enumerate}

\item \textbf{Si se dispone de 5 frutas distintas.}
      \begin{enumerate}
	      \item \textbf{¿Cuántos jugos de dos frutas se pueden hacer?} \\
	            \textit{Solución:} El orden no importa, es una combinación. \\
	            $C_2^5 = \binom{5}{2} = \frac{5!}{2!3!} = 10$ jugos.
	      \item \textbf{¿Y de 3 frutas?} \\
	            \textit{Solución:} Combinación. $C_3^5 = \binom{5}{3} = \frac{5!}{3!2!} = 10$ jugos.
	      \item \textbf{¿Y de al menos 2 frutas?} \\
	            \textit{Solución:} Se suman los jugos de 2, 3, 4 y 5 frutas. \\
	            $C_2^5 + C_3^5 + C_4^5 + C_5^5 = 10 + 10 + 5 + 1 = 26$ jugos.
      \end{enumerate}

\end{enumerate}
\begin{figure}[h!]
\centering
\includegraphics[width=0.75\textwidth]{Gat}
\caption{Gatito para hacer bonito el apunte}
\label{fig:Gat}
\end{figure}
\newpage

\section{18/08 - Repaso Para Prueba}
\subsection{Ejercicios Resueltos}
\begin{enumerate}
\item \textbf{Las cifras que componen un número son 1, 2, 3, 4 y 5. ¿Cuántos números diferentes de 5 cifras, menores de 54,000, pueden formarse sin que se repita ninguna de las cifras?}
\textit{Solución:} Se divide el problema en dos casos mutuamente excluyentes.
\begin{itemize}
\item \textbf{Caso 1: El número empieza en 1, 2, 3 o 4.} Hay 4 opciones para la primera cifra. Las 4 cifras restantes se pueden permutar de 
4
!
4!
 maneras.
[ 4 \times 4! = 4 \times 24 = 96 \text{ números.} ]
\item \textbf{Caso 2: El número empieza en 5.} La primera cifra es 5 (1 opción). La segunda cifra debe ser menor que 4 (es decir, 1, 2 o 3), lo que nos da 3 opciones. Las 3 cifras restantes se permutan de 
3
!
3!
 maneras.
[ 1 \times 3 \times 3! = 3 \times 6 = 18 \text{ números.} ]
\end{itemize}
\textbf{Total:} Como los casos son excluyentes, sumamos los resultados: 
96
+
18
=
114
96+18=114
.

code
Code
download
content_copy
expand_less
\item \textbf{Con cuatro oficiales y 8 soldados, calcular el número de grupos de 6 miembros que pueden formarse de manera que en cada grupo haya:}
      \begin{enumerate}
	      \item \textbf{Un solo oficial} \\
	            \textit{Solución:} Se debe elegir 1 oficial de 4 Y 5 soldados de 8.
	            \[ \binom{4}{1} \times \binom{8}{5} = 4 \times \frac{8!}{5!(8-5)!} = 4 \times 56 = 224 \text{ grupos.} \]
	      \item \textbf{Como mínimo un oficial} \\
	            \textit{Solución:} Se usa el método del complemento: Total de grupos menos los grupos sin oficiales.
	            \begin{itemize}
		            \item Total de grupos: $\binom{12}{6} = \frac{12!}{6!6!} = 924$.
		            \item Grupos sin oficiales (todos soldados): $\binom{8}{6} = \frac{8!}{6!2!} = 28$.
	            \end{itemize}
	            \[ \text{Total} = 924 - 28 = 896 \text{ grupos.} \]
      \end{enumerate}

\item \textbf{¿De cuántas maneras pueden colocarse en un círculo 7 personas?}
      \textit{Solución:} Es una permutación circular de 7 elementos.
      \[ PC_7 = (7-1)! = 6! = 720 \text{ maneras.} \]

\item \textbf{En una estantería hay dos obras de 3 volúmenes cada una y otras dos de 2 volúmenes cada una. Hallar el número total de formas en que pueden colocarse los 10 libros en un mismo estante, sin dejar separados los diversos volúmenes de una misma obra:}
      \begin{enumerate}
	      \item \textbf{Ordenados en cualquier orden} \\
	            \textit{Solución:} Se consideran las 4 obras como 4 "bloques" que se pueden permutar. Luego, se permutan los volúmenes dentro de cada bloque.
	            \[ (\text{Permutar bloques}) \times (\text{Permutar volúmenes internos}) \]
	            \[ 4! \times (3! \times 3! \times 2! \times 2!) = 24 \times (6 \times 6 \times 2 \times 2) = 3,456 \text{ formas.} \]
	      \item \textbf{Ordenados en orden Ascendente} \\
	            \textit{Solución:} El orden interno de los volúmenes está fijo (solo 1 manera por obra). Solo se permutan los 4 bloques.
	            \[ 4! \times (1 \times 1 \times 1 \times 1) = 24 \text{ formas.} \]
      \end{enumerate}

\item \textbf{Se tienen 7 libros de estadística y 3 de informática. ¿De cuántas maneras pueden colocarse en un estante cuatro libros de estadística y uno de informática, si este último debe estar siempre en el centro?}
      \textit{Solución:} Se llenan las 5 posiciones. El centro se llena primero con un libro de informática (3 opciones). Los 4 lugares restantes se llenan con 4 de los 7 libros de estadística (una variación).
      \[ (\text{Opciones para el centro}) \times (\text{Variación para los otros 4 puestos}) \]
      \[ 3 \times V_4^7 = 3 \times \frac{7!}{(7-4)!} = 3 \times (7 \cdot 6 \cdot 5 \cdot 4) = 3 \times 840 = 2,520 \text{ maneras.} \]

\item \textbf{¿Cuántas ordenaciones pueden formarse con las letras de la expresión \texorpdfstring{$a^3b^2c^4$}{a3b2c4} cuando está desarrollada?}
      \textit{Solución:} La expresión desarrollada es `aaabbcccc`. Es una permutación con repetición de 9 elementos, donde los elementos se repiten 3, 2 y 4 veces.
      \[ P_{3,2,4}^{9} = \frac{9!}{3! \cdot 2! \cdot 4!} = \frac{362,880}{6 \cdot 2 \cdot 24} = \frac{362,880}{288} = 1,260 \text{ ordenaciones.} \]

\end{enumerate}
\newpage

\section{27/08 - Aplicaciones de Combinatoria}
\subsection{Revisión de Prueba (Ejercicios Notables)}
\textit{Nota: Esta sección resume algunos ejercicios clave de la evaluación anterior.}
\begin{enumerate}
\item \textbf{Ítem 1: Operatoria Combinatoria}
\begin{enumerate}
\item 
(
5
3
)
+
(
7
3
)
−
(
5
2
)
+
(
7
4
)
=
2
⋅
(
7
3
)
=
2
⋅
7
!
4
!
⋅
3
!
=
2
⋅
35
=
70
(
3
5
	​

)+(
3
7
	​

)−(
2
5
	​

)+(
4
7
	​

)=2⋅(
3
7
	​

)=
4!⋅3!
2⋅7!
	​

=2⋅35=70

\item 
(
9
−
4
)
!
8
!
=
5
!
8
!
=
1
8
⋅
7
⋅
6
=
1
336
8!
(9−4)!
	​

=
8!
5!
	​

=
8⋅7⋅6
1
	​

=
336
1
	​


\end{enumerate}
\item \textbf{Ítem 2: Identificación de Técnica de Conteo}
\begin{itemize}
\item Para sentar 6 personas en una mesa redonda, se usa una \textbf{Permutación Circular}: 
𝑃
𝐶
6
=
(
6
−
1
)
!
=
5
!
=
120
PC
6
	​

=(6−1)!=5!=120
.
\item Para elegir un comité de 3 personas de un grupo de 15, se usa una \textbf{Combinación}: 
𝐶
3
15
=
(
15
3
)
=
15
⋅
14
⋅
13
3
⋅
2
⋅
1
=
455
C
3
15
	​

=(
3
15
	​

)=
3⋅2⋅1
15⋅14⋅13
	​

=455
.
\end{itemize}
\end{enumerate}

\subsection{Ejercicios: Diagonales de un Polígono}
\begin{enumerate}
\item Determinar la cantidad de diagonales de un polígono de 20 lados.
\item Determinar una expresión para la cantidad de diagonales de un polígono de n lados.
\item Si un polígono tiene 65 diagonales, ¿cuántos lados tiene?
\end{enumerate}

\subsection{Soluciones}
\begin{enumerate}
\item \textbf{Deducción de la fórmula y cálculo para 20 lados.} \
\textit{Solución:} Para resolver esto, primero deduciremos la fórmula general para un polígono de 
𝑛
n
 lados, como se pide en el ejercicio 2.

code
Code
download
content_copy
expand_less
Un polígono de $n$ lados tiene $n$ vértices. Una diagonal es una línea que une dos vértices no consecutivos. Desde un punto de vista combinatorio:
      \begin{itemize}
	      \item El número total de líneas que se pueden trazar entre $n$ vértices es equivalente a escoger 2 vértices de un total de $n$, sin importar el orden. Esto es una combinación:
	            \[ \text{Total de líneas} = \binom{n}{2} = \frac{n(n-1)}{2} \]
	      \item Este total incluye tanto las diagonales como los $n$ lados del polígono. Para obtener solo las diagonales, debemos restar los lados.
      \end{itemize}
      La expresión para el número de diagonales ($D$) es:
      \[ D(n) = \binom{n}{2} - n = \frac{n(n-1)}{2} - n = \frac{n^2 - n - 2n}{2} = \frac{n(n-3)}{2} \]
      Ahora, aplicamos la fórmula para un polígono de 20 lados ($n=20$):
      \[ D(20) = \frac{20(20-3)}{2} = \frac{20 \cdot 17}{2} = 10 \cdot 17 = 170 \]
      \textbf{Respuesta:} Un polígono de 20 lados tiene 170 diagonales.

\item \textbf{Expresión para la cantidad de diagonales de un polígono de $n$ lados.} \\
      \textit{Solución:} Como se dedujo en el punto anterior, la expresión general es:
      \[ D(n) = \frac{n(n-3)}{2} \]
      \textbf{Respuesta:} La expresión es $\frac{n(n-3)}{2}$.

\item \textbf{Si un polígono tiene 65 diagonales, ¿cuántos lados tiene?} \\
      \textit{Solución:} Usamos la fórmula, la igualamos a 65, y despejamos $n$.
      \[ \frac{n(n-3)}{2} = 65 \]
      \[ n(n-3) = 130 \]
      \[ n^2 - 3n - 130 = 0 \]
      Resolvemos la ecuación cuadrática factorizando. Buscamos dos números que multipliquen -130 y sumen -3. Estos son -13 y 10.
      \[ (n-13)(n+10) = 0 \]
      Las soluciones son $n_1 = 13$ y $n_2 = -10$. Como el número de lados de un polígono no puede ser negativo, descartamos $n_2$.

      \textbf{Respuesta:} El polígono tiene 13 lados.

\end{enumerate}

\newpage

\section{29/08 - Muestreo e Introducción a la Probabilidad}
\subsection{El Promedio de las Medias Muestrales}
En esta sección se demuestra una propiedad fundamental de la estadística inferencial: la media de todas las medias muestrales posibles es igual a la media de la población.

\subsubsection{Ejemplo Numérico Intuitivo}
Suponga que se tiene una población de 3 elementos: 
{
6
,
12
,
18
}
{6,12,18}
.
\begin{enumerate}
\item \textbf{Determine todas las muestras posibles de tamaño 2 (sin orden y sin repetición).} \
\textit{Solución:} Las muestras son 
{
6
,
12
}
{6,12}
, 
{
6
,
18
}
{6,18}
 y 
{
12
,
18
}
{12,18}
. Hay 
(
3
2
)
=
3
(
2
3
	​

)=3
 muestras posibles.

code
Code
download
content_copy
expand_less
\item \textbf{Determine el promedio de cada muestra.} \\
      \textit{Solución:} \\
      $\bar{x}_1 = \frac{6+12}{2} = 9$ \\
      $\bar{x}_2 = \frac{6+18}{2} = 12$ \\
      $\bar{x}_3 = \frac{12+18}{2} = 15$

\item \textbf{Determine el promedio de los promedios muestrales y compárelo con el promedio de la población.} \\
      \textit{Solución:} \\
      El promedio de los promedios muestrales es: $\frac{9+12+15}{3} = \frac{36}{3} = 12$. \\
      El promedio de la población original es: $\frac{6+12+18}{3} = \frac{36}{3} = 12$.

      \textbf{Conclusión:} Ambos promedios son iguales.

\end{enumerate}

\subsubsection{Generalización y Demostración Formal}
Sea una población de 
𝑛
n
 elementos 
{
𝑥
1
,
𝑥
2
,
…
,
𝑥
𝑛
}
{x
1
	​

,x
2
	​

,…,x
n
	​

}
 y escojamos todas las muestras posibles de tamaño 
𝑘
k
. El número total de muestras es 
(
𝑛
𝑘
)
(
k
n
	​

)
.

El promedio de todas las medias muestrales, denotado 
𝜇
𝑥
ˉ
μ
x
ˉ
	​

, se calcula como:
[ \mu_{\bar{x}} = \frac{\sum \bar{x}_i}{\binom{n}{k}} ]
Para realizar esta suma, nos preguntamos: ¿cuántas veces aparece cada el

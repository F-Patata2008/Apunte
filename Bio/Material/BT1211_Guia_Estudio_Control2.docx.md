_BT1211 — Guía de Estudio Control 2_ 

## **UNIVERSIDAD DE CHILE** 

Facultad de Ciencias Físicas y Matemáticas 

Departamento de Ingeniería Química, Biotecnología y Materiales 

## **BT1211** 

## **Aplicaciones de la Biología a la Ingeniería y Ciencias Vicente Cortés** 

**GUÍA DE ESTUDIO — CONTROL 2 (EVALUACIÓN PRINCIPAL 2)** 

## _Contenidos cubiertos: Sesiones 7 a 13_ 

_Aplicaciones industriales de la biología · Biomimética y biomedicina · Sistemas de control biológico · Transporte de materia y energía · Modelos matemáticos y balances · Aleatoriedad y probabilidad_ 

Incluye ejemplos resueltos de las Evaluaciones Principales 2 de los años 2023, 2024 y 2025 

Página 1 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **Índice** 

|Índice|||2|
|---|---|---|---|
|Cómo usar esta guía|||5|
|1. Modelos Matemáticos y Balances de Masa|||6|
|1.1 ¿Qué es un modelo matemático?||6||
|Estado de un sistema|6|||
|1.2 La ecuación general de balance||6||
|Pasos para plantear un balance|6|||
|1.3 Ejemplos clásicos de balance||7||
|Balance de agua en una tina (sin reacción)|7|||
|Balance de una población (con migración)|7|||
|1.4 Modelos poblacionales||7||
|Crecimiento exponencial (sin límite)|7|||
|Ecuación logística (con capacidad de carga)|7|||
|Modelo Lotka-Volterra (depredador - presa)|8|||
|1.5 Balances con reacción química||9||
|1.6 Modelos complejos: membranas y metabolismo||9||
|Canales iónicos y bomba sodio-potasio|9|||
|Análisis de Flujos Metabólicos (MFA)|9|||
|1.7 Síntesis: tipos de modelos vistos||9||
|2. Sistemas de Control Biológico|||11|
|2.1 Homeostasis||11||
|2.2 Componentes de un sistema de control||11||
|2.3 Lazo abierto vs. lazo cerrado||12||
|2.4 Diagrama de bloques de un lazo cerrado||12||
|2.5 Retroalimentación negativa vs. positiva||13||
|2.6 Control adaptativo||13||
|2.7 Casos resueltos típicos de control||14||
|2.8 Síntesis rápida — preguntas frecuentes de control||15||
|3. Transporte de Masa y Movimiento en Organismos Vivos|||16|
|3.1 Concepto general de transporte||16||
|3.2 Fuerza motriz, flujo y resistencia||16||
|3.3 Balance de materia (general)||16||
|3.4 Mecanismos de transferencia de masa||17||
|Ley de Fick (difusión)|17|||
|3.5 Redes de transporte biológico||17||
|3.6 Transporte por convección: mecánica de fluidos||18||
|Viscosidad|18|||
|Fluidos newtonianos vs. no newtonianos|18|||
|3.7 Caso aplicado: el dializador (hemodiálisis)||18||
|Balances de masa de urea en el dializador|19|||
|3.8 Caso aplicado: tubería entre piscinas (Hagen-Poiseuille)||19||
|3.9 Heterotermia regional: contracorriente (gaviotas)||20||
|Intercambio de calor a contracorriente|20|||
|3.10 Síntesis de fórmulas — Transporte||21||
|4. Manejo y Transferencia de Energía en los Organismos Vivos|||22|



Página 2 de 46 

_BT1211 — Guía de Estudio Control 2_ 

|4.1 Sistemas termodinámicos||22||
|---|---|---|---|
|4.2 Leyes de la termodinámica||22||
|Entropía en sistemas biológicos|22|||
|4.3 Formas de energía y transformación||22||
|Tipos de trabajo biológico|23|||
|4.4 Eficiencia de conversión energética||23||
|4.5 Flujo de energía en ecosistemas (niveles tróficos)||23||
|4.6 La molécula de ATP||23||
|Acoplamiento de reacciones|24|||
|4.7 Fotosíntesis y respiración celular||24||
|4.8 Transferencia de calor||24||
|Regulación de temperatura por sudoración|25|||
|4.9 Relación superficie/volumen y tamaño corporal||25||
|4.10 Síntesis de fórmulas — Energía||26||
|5. Aleatoriedad y Probabilidad — Estadística Aplicada|||27|
|5.1 Términos y definiciones básicas||27||
|5.2 Estadística descriptiva vs. inferencial||27||
|5.3 Medidas de tendencia central||27||
|5.4 Medidas de dispersión||28||
|5.5 Correlación||28||
|Correlación≠Causalidad|28|||
|5.6 Test de hipótesis||29||
|Errores Tipo I y Tipo II|29|||
|5.7 Errores experimentales||30||
|5.8 Síntesis de fórmulas — Estadística||30||
|6. Aplicaciones Industriales de la Biología|||31|
|6.1 Ingeniería genética||31||
|Mitos y conceptos clave|31|||
|Elementos básicos de la ingeniería genética|31|||
|Vectores: plásmidos|31|||
|Sistemas de expresión: procariontes vs. eucariontes|31|||
|Transformación: ¿qué le pasa al ADN exógeno dentro del huésped?|32|||
|Expresión de una proteína recombinante — 5 pasos|32|||
|Proteína Fluorescente Verde (GFP)|32|||
|Híbrido vs. transgénico|32|||
|6.2 Otras aplicaciones industriales: proteínas y biofármacos||33||
|6.3 Química verde||33||
|6.4 Biomedicina||34||
|6.5 Bioprocesos y biotransformaciones||34||
|Comparación: ventajas y desventajas del uso de enzimas|34|||
|Tratamiento de residuos industriales|34|||
|Biolixiviación y biocorrosión|35|||
|Empresas biotecnológicas chilenas (ejemplos por sector)|35|||
|6.6 Síntesis — Sección Industria||35||
|7. Biomimética|||36|
|7.1 Principios de la vida (marco de diseño biomimético)||36||
|7.2 Niveles y escalas de aplicación y abstracción||36||
|Nivel de Aplicación — 'El Qué' se imita|36|||



Página 3 de 46 

_BT1211 — Guía de Estudio Control 2_ 

|Escala de Aplicación — 'El Tamaño' al que se imita|36|
|---|---|
|Nivel de Abstracción — 'El Cómo' se imita|37|
|7.3 Ejemplos clásicos de biomimética|37|
|7.4 Caso ilustrativo detallado — Termitero y Eastgate Centre|38|
|7.5 Cómo responder preguntas de biomimética en el control|38|
|7.6 Estrategias adaptativas naturales (banco de ejemplos — Actividad 4)|38|
|8. Banco de Práctica — Controles Anteriores Completos|40|
|8.1 Control 2025 (7 de julio de 2025)|40|
|Pregunta 1 — Modelo de empresas P/M/G (Modelos matemáticos)|40|
|Pregunta 2 — Heterotermia regional en gaviotas (Transporte de calor)|40|
|Pregunta 3 — Máquinas dispensadoras de combustible (Estadística)|40|
|Pregunta 4 — Dializador (Transporte de masa)|40|
|Pregunta 5 — Brazo protésico (Sistemas de control)|40|
|8.2 Control 2024 (8 de julio de 2024)|41|
|Pregunta 1 — Planta de lavado de botellas reutilizables (Sistemas de control)|41|
|Pregunta 2 — Adicción al tabaco / nicotina (Sistemas de control)|41|
|Pregunta 3 — Permacultura / cultivo de cereales perennes (Biomimética)|41|
|Pregunta 4 — Vindolina / biosíntesis de fármacos anticancerígenos (Ingeniería genética +|Química|
|verde)|41|
|Pregunta 5 — Llenado automático de piscinas (Sistemas de control + balance de masa)|41|
|Pregunta 6 — Coyotes y conejos (Modelos Lotka-Volterra)|42|
|Pregunta 7 — Industria textil y perspectiva de género (Tema transversal)|42|
|8.3 Control 2023 (8 de julio de 2023)|42|
|Pregunta 1 — Piscina con algas y alguicida (Balance de masa)|42|
|Pregunta 2 — Catalizador con eficiencia promedio (Estadística)|43|
|Pregunta 3 — Transporte de etanol (Transporte de masa)|43|
|Pregunta 4 — Productividad de un bosque (Energía / ecología)|43|
|Pregunta 5 — Ducha con regulación manual remota (Sistemas de control)|43|
|Pregunta 6 — Dinosaurios y relación superficie/volumen (Energía / transferencia de calor) 43||
|8.4 Preguntas tipo de las actividades y auxiliares (no evaluadas aún, pero del mismo estilo)|44|
|Apocalipsis zombie (Actividad 6) — Modelos con 3 poblaciones|44|
|Ley de control proporcional vs. constante (Actividad 6) — Ducha automática|44|
|Epidemia SIR (Actividad 6) — Modelo Susceptibles-Infectados|44|
|Piscinas de tratamiento de residuos líquidos (Actividad 5) — Transporte|44|
|8.5 Checklist final antes del control|45|



Página 4 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **Cómo usar esta guía** 

Esta guía resume todo el contenido de las sesiones 7 a 13 del curso BT1211 (Aplicaciones de la Biología a la Ingeniería y Ciencias), que corresponde a la materia evaluada en el Control 2. Está organizada por tema, no por sesión, para facilitar el repaso integrado. 

- Cada sección incluye: resumen conceptual, fórmulas clave en recuadros, ejemplos desarrollados y conexión con preguntas de controles anteriores (2023, 2024, 2025). 

- Los recuadros 📝 'Pregunta de control' muestran cómo estos mismos conceptos fueron evaluados realmente, con la lógica de la respuesta esperada. 

- Los recuadros 💡 'Ejemplo' desarrollan un caso aplicado paso a paso. 

- La última sección resume, pregunta por pregunta, los 3 controles anteriores completos, como banco de práctica. 

**Recomendación de estudio: lee primero la sección de Modelos Matemáticos y Balances (es la base para Energía, Transporte y muchas preguntas de Control), luego Sistemas de Control, y finaliza con Estadística e Industria/Biomimética, que son más conceptuales y de memorización.** 

Página 5 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **1. Modelos Matemáticos y Balances de Masa** 

Esta es la base transversal del curso: balances de masa, ecuaciones diferenciales y modelos poblacionales aparecen en prácticamente todas las preguntas de control (algas, dializadores, piscinas, depredador-presa, etc.). Dominar esta sección facilita enormemente las secciones de Energía, Transporte y Control. 

## **1.1 ¿Qué es un modelo matemático?** 

Un modelo es una representación de un proceso que permite entender su funcionamiento y/o predecir su comportamiento a partir de información disponible. Los modelos nacen de una pregunta: su calidad o utilidad depende de qué tan bien contestan esa pregunta, independiente de su complejidad. 

## _**Estado de un sistema**_ 

- Estado: condición de un sistema en un momento dado. 

- Espacio de estados: conjunto de todos los estados posibles del sistema. 

- Variable de estado: variable cuantitativa que permite definir un estado (ej. temperatura, masa, volumen, concentración, número de individuos). Deben ser cuantificables para construir un modelo matemático. 

## 💡 **Variables de estado de una taza de café** 

Temperatura: 63.1 °C  |  Masa: 128 g  |  Volumen: 470 mL  |  Concentración de cafeína: 0.7 mg/mL 

Cada una de estas magnitudes cuantificables es una variable de estado posible del sistema 'taza de café'. 

## **1.2 La ecuación general de balance** 

Todo balance (de masa, energía, población, etc.) parte de la misma idea: lo que se acumula en el tiempo es el resultado neto de lo que entra, sale, se genera y se consume dentro del volumen de control. 

## **− − ΔX/Δt  =  Σ entradas Σ salidas  +  Σ generación Σ consumo** 

_Cuando esta relación se escribe en forma diferencial (Δt → 0) se obtiene una ecuación diferencial: una relación entre la tasa de cambio de una variable de estado y las propias variables de estado del sistema._ 

## _**Pasos para plantear un balance**_ 

1. Definir el volumen de control (la frontera del sistema). 

2. Identificar la(s) variable(s) de estado relevantes. 

3. Identificar todos los flujos de entrada y salida que cruzan la frontera. 

Página 6 de 46 

_BT1211 — Guía de Estudio Control 2_ 

4. Identificar términos de generación y consumo dentro del volumen de control (reacciones, nacimientos, muertes, crecimiento, depredación, etc.). 

5. Escribir el balance en palabras primero, luego reemplazar cada término por su expresión matemática. 

6. Revisar unidades: todos los términos deben tener las mismas unidades que ΔX/Δt. 

## **1.3 Ejemplos clásicos de balance** 

_**Balance de agua en una tina (sin reacción)**_ 

_− ΔX/Δt = (agua que entra por unidad de tiempo) (agua que sale por unidad de tiempo)_ 

Si la salida es proporcional a la cantidad acumulada (ej. por una válvula), el modelo de salida más simple es: 

**− ΔX/Δt = k·X** 

## _**Balance de una población (con migración)**_ 

## **− − ΔX/Δt = Inmigración Emigración + Nacimientos Muertes** 

Aquí inmigración y nacimientos son términos de "entrada/generación"; emigración y muertes son términos de "salida/consumo". 

## **1.4 Modelos poblacionales** 

## _**Crecimiento exponencial (sin límite)**_ 

Población X, tasa de natalidad n, tasa de mortalidad m: 

## **− − ΔX/Δt = X·n X·m = (n m)·X = c·X** 

Si c > 0 la población crece exponencialmente; si c < 0 decrece exponencialmente; si c = 0 se mantiene constante (equilibrio). 

## _**Ecuación logística (con capacidad de carga)**_ 

Incorpora un límite físico al crecimiento: la capacidad de carga k (máximo de individuos que el ambiente puede sostener). 

**− − ΔX/Δt = g·X·(1 X/k) = g·X·(k X)/k Fase Condición Comportamiento** 

Página 7 de 46 

_BT1211 — Guía de Estudio Control 2_ 

|Inicial|X≪k→(1−X/k)≈1|ΔX/Δt≈g·X→crecimiento exponencial (no hay<br>competencia por recursos)|
|---|---|---|
|Intermedia|X crece, acercándose a k|la tasa de crecimiento neto disminuye<br>progresivamente (aparece competencia)|
|Equilibrio /<br>estabilización|X≈k→(1−X/k)≈0|ΔX/Δt≈0→población se estabiliza (curva<br>sigmoidea, se "aplana")|



## 💡 **Auxiliar 5 — Población bacteriana con capacidad de carga** 

Una población bacteriana sigue el modelo logístico con capacidad de carga k = 10⁹ bacterias. Si luego se introducen microorganismos competidores y k baja a la mitad (5×10⁸), la población —que ya estaba estabilizada en el valor anterior de k— declinará hasta estabilizarse en el nuevo valor, menor, de capacidad de carga. 

Idea clave: la ecuación logística siempre "empuja" a la población hacia el valor de k vigente, ya sea creciendo o decreciendo. 

## _**Modelo Lotka-Volterra (depredador - presa)**_ 

Modela la interacción entre dos poblaciones que se regulan mutuamente: una presa (ej. atunes, conejos, gacelas) y un depredador (ej. tiburones, coyotes, leones). 

|||
|---|---|
|**Término**|**Significado**|
|α·A|Nacimientos de presas, proporcional a su propia cantidad (crecimiento libre, sin<br>depredador)|
|β·A·T|Muerte de presas por depredación, proporcional al producto presa × depredador (más<br>encuentros)|
|γ·A·T|Nacimiento de depredadores, proporcional a la cantidad de presas consumidas<br>(conversión de alimento en crías)|
|δ·T|Muerte natural de depredadores, proporcional a su propia cantidad|



Comportamiento característico: las poblaciones oscilan en el tiempo con un desfase — el peak de depredadores ocurre después del peak de presas, porque el depredador necesita que la población de presas ya haya crecido para poder alimentarse y reproducirse. 

📝 **Pregunta de control — Empresas P/M/G (2025, P1) y Coyotes/Conejos (2024, P6)** 

Ambas preguntas piden: (a) identificar variables de estado, (b) plantear balances en palabras y luego en ecuaciones, (c) razonar consecuencias de cambiar una constante. 

Página 8 de 46 

_BT1211 — Guía de Estudio Control 2_ 

Patrón de la pregunta 'consecuencias de una tasa muy alta/baja': se responde explicando el efecto en cascada — si una población base se reduce mucho, todas las poblaciones que dependen de ella (las que la 'consumen' o 'absorben') también se ven afectadas, hasta llegar a un nuevo equilibrio o a la extinción, dependiendo de las magnitudes relativas de las constantes. 

Tip: en preguntas como 'empresas pequeñas/medianas/grandes', cada constante descrita en el enunciado (ej. γP, αPM, αPG) corresponde literalmente a un término del balance — basta con traducir cada oración del enunciado a su símbolo correspondiente. 

## **1.5 Balances con reacción química** 

Cuando ocurre una reacción dentro del volumen de control, se agregan los términos de generación y consumo: 

## **Entra − Sale + Genera − Consume = Acumula** 

Para la reacción A + 2B → C con constante de velocidad k: 

**==> picture [468 x 34] intentionally omitted <==**

Nota: el coeficiente estequiométrico de cada especie (1, 2, 1) multiplica la velocidad de la reacción al construir cada balance individual. 

## **1.6 Modelos complejos: membranas y metabolismo** 

## _**Canales iónicos y bomba sodio-potasio**_ 

Modelos como el de Hodgkin-Huxley describen matemáticamente cómo se abren/cierran canales de sodio y potasio en la membrana neuronal, generando el potencial de acción. La bomba sodio-potasio transporta activamente iones en contra de su gradiente (gasta ATP), manteniendo los gradientes que luego permiten la señalización eléctrica. 

## _**Análisis de Flujos Metabólicos (MFA)**_ 

- Herramienta para analizar matemáticamente el metabolismo de un organismo. 

- Se basa en balances de flujos para cada especie metabólica (sustrato, intermediarios, productos). 

- En estado estacionario se asume que las concentraciones internas no cambian en el tiempo (ej. de A, B, C), lo que permite resolver el sistema de ecuaciones algebraicamente en vez de diferencialmente. 

- Los balances de flujo pueden escribirse de forma matricial: S·v = 0, donde S es la matriz estequiométrica (cómo cada reacción consume/genera cada especie) y v es el vector de flujos (velocidad de cada reacción). 

Página 9 de 46 

_BT1211 — Guía de Estudio Control 2_ 

Ejemplo típico: fermentación de glucosa (Glc) a etanol (EtOH) en levadura — se balancean los flujos de entrada de glucosa, las reacciones intermedias y la salida de etanol y biomasa. 

## **1.7 Síntesis: tipos de modelos vistos** 

|**Modelo**|**Pregunta que responde**|**Forma típica**|
|---|---|---|
|Crecimiento/decaimiento<br>exponencial|¿Cómo crece una población sin límites de<br>recursos?|ΔX/Δt = c·X|
|Logístico (capacidad de carga)|¿Cómo crece una población con recursos<br>limitados?|ΔX/Δt = g·X·(1−X/k)|
|Lotka-Volterra|¿Cómo oscilan poblaciones<br>presa-depredador?|sistema acoplado de 2 ecuaciones|
|Balance con reacción|¿Cómo cambia la concentración de una<br>especie que reacciona?|Entra−Sale+Genera−Consume|
|MFA (estado estacionario)|¿Cómo se distribuyen los flujos metabólicos<br>internos?|S·v = 0 (matricial)|



Página 10 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **2. Sistemas de Control Biológico** 

Es probablemente el tema más recurrente en los controles: aparece en preguntas sobre prótesis, duchas, plantas de lavado, hormonas, reactores nucleares, etc. La clave es identificar siempre los mismos componentes y el tipo de lazo, sin importar el contexto del enunciado. 

## **2.1 Homeostasis** 

Homeostasis: habilidad de una entidad funcional de mantener automáticamente un ambiente interno equilibrado. Los seres vivos resisten cambios externos para mantener un ambiente interno estable y relativamente constante, lo que requiere intercambio continuo de materia y energía con el medioambiente. 

## 💡 **Ejemplo — Temperatura corporal** 

Sensores en la periferia del cuerpo comunican al hipotálamo los cambios de temperatura. El sistema de control actúa cuando la temperatura corporal se aleja de su valor de referencia debido a una perturbación (ej. frío externo, fiebre). 

## **2.2 Componentes de un sistema de control** 

Un sistema de control es un conjunto de componentes destinados a regular el comportamiento de un sistema para lograr un resultado de interés. Se repiten en sistemas de ingeniería y en sistemas biológicos. 

|**Componente**|**Función**|**Ejemplo biológico**|**Ejemplo ingenieril**|
|---|---|---|---|
|Sensor|Detecta y mide la variable<br>controlada; convierte una señal<br>en otra más fácil de comunicar|Receptores celulares,<br>sensores de temperatura del<br>hipotálamo, receptores<br>nicotínicos|Termómetro, sensor de<br>presión, sensor de<br>profundidad|
|Controlador|Compara el valor medido con el<br>set-point y decide el ajuste<br>necesario|Cerebro, hipotálamo|Microprocesador, circuito,<br>persona que opera una<br>válvula|
|Actuador|Ejecuta la acción física que<br>afecta al sistema|Músculos (actina-miosina),<br>glándulas que liberan<br>hormonas|Válvulas, motores,<br>reguladores de presión|
|Comunicación|Transmite la información entre<br>componentes|Sistema nervioso (rápido) /<br>sistema endocrino-humoral<br>(lento, vía sangre)|Cables, señales eléctricas,<br>redes|
|Proceso|El sistema cuya variable se<br>controla|El cuerpo, el músculo, la<br>célula|La planta, el reactor, la<br>ducha|
|Set-point /<br>referencia|Valor deseado de la variable<br>controlada|37 °C corporal, glicemia<br>normal|Temperatura deseada del<br>agua|



Página 11 de 46 

_BT1211 — Guía de Estudio Control 2_ 

|**Componente**|**Función**|**Ejemplo biológico**|**Ejemplo ingenieril**|
|---|---|---|---|
|Perturbación|Factor externo que aleja al<br>sistema del set-point|Frío ambiental, infección|Apertura de otra llave, baja<br>de presión|



En biología, los sensores se llaman receptores: traducen la señal a un mecanismo fácil de comunicar mediante gradientes de compuestos específicos para cada célula y señal (ej. biosensores, test ELISA). 

Comunicación neuronal vs. humoral: la comunicación neuronal usa el sistema nervioso (despolarización de membrana + neurotransmisores), es rápida y específica. La comunicación humoral usa la sangre como medio de transporte (hormonas), es más lenta pero más general/sistémica. 

## **2.3 Lazo abierto vs. lazo cerrado** 

||**Lazo abierto**|**Lazo cerrado (con retroalimentación)**|
|---|---|---|
|Definición|No existe sensor que mida la salida real ni<br>retroalimentación hacia el controlador|La salida del sistema es medida y retroalimentada<br>al controlador para ajustar la acción|
|Ventaja|Más simple y barato (no requiere<br>instrumentación adicional)|Robusto ante perturbaciones; se adapta a<br>condiciones cambiantes; más preciso|
|Desventaja|No responde a perturbaciones ni<br>variaciones de las condiciones de entrada;<br>ineficiente si las condiciones cambian|Requiere sensores, controlador y mayor<br>complejidad/costo de implementación|
|Ejemplo típico|Lavado de botellas con tiempo y presión<br>fijos preestablecidos; operario regulando<br>una válvula solo por experiencia, sin ver el<br>resultado|Ducha con sensor de temperatura y válvula<br>automática; termostato; sistema de llenado de<br>piscina con sensor de profundidad|



## **2.4 Diagrama de bloques de un lazo cerrado** 

Esquema estándar de control retroalimentado (memorizar esta estructura, aparece en casi todas las preguntas de diseño de un sistema de control): 

_Referencia (set-point) → [+/− comparador → error e] → Controlador → Actuador → Proceso → Variable de salida (y) La Variable de salida es medida por el Sensor, que retroalimenta su valor (yM) de vuelta al comparador. Una Perturbación externa puede afectar al Proceso en cualquier punto._ 

_− e = (Referencia) (variable medida por el sensor). El controlador usa este error para decidir la acción correctiva._ 

Página 12 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **2.5 Retroalimentación negativa vs. positiva** 

||**Retroalimentación negativa**|**Retroalimentación positiva**|
|---|---|---|
|Efecto sobre la<br>señal|Se opone al estímulo que la desencadenó: actúa<br>para devolver al sistema a su estado de<br>referencia|Amplifica el estímulo inicial: aleja al sistema<br>de su estado inicial|
|Propósito típico|Mantener un estado estable (homeostasis,<br>regulación)|Estimular un proceso hasta su terminación /<br>culminación rápida|
|Ejemplos<br>biológicos|Regulación de glicemia (insulina/glucagón);<br>temperatura corporal; operón triptófano|Parto (oxitocina); coagulación sanguínea;<br>activación de canales de Na⁺en potencial de<br>acción|
|Ejemplos no<br>biológicos|Termostato; control de velocidad crucero|Reacción en cadena nuclear sin control;<br>feedback loop de recomendaciones (Spotify)|
|💡**Ejemplo — Regulación de glicemia (retroalimentación negativa)**<br>En una persona sana, dos hormonas controlan la glicemia de forma antagónica: la insulina (baja la<br>glicemia, promueve captación de glucosa por las células) y el glucagón (sube la glicemia, promueve<br>liberación de glucosa desde el hígado). En la diabetes, este ciclo de retroalimentación negativa está<br>alterado, dificultando que el cuerpo regrese una glicemia alta a un nivel saludable.|||
|💡**Ejemplo — Coagulación sanguínea (retroalimentación positiva)**<br>Cuando se rompe un vaso sanguíneo, se activan enzimas (factores de coagulación). Estas enzimas<br>activan a su vez a otras enzimas inactivas en la sangre adyacente, amplificando la señal y logrando que<br>coagule más sangre. El proceso continúa —autoamplificándose— hasta que se tapa el orificio del vaso y<br>cesa la hemorragia: es un proceso que se autolimita al alcanzar su objetivo, no porque se 'apague' el<br>estímulo.|||



## **2.6 Control adaptativo** 

Un sistema de control adaptativo ajusta sus propios parámetros de control en el tiempo, en función de cómo cambian las condiciones del proceso (no solo corrige el error como un lazo cerrado simple, sino que modifica cómo corrige). 

- Sistema Nervioso Autónomo: regula funciones involuntarias mediante dos ramas antagónicas — simpático (activa órganos para respuesta intensiva, 'lucha o huida') y parasimpático (relaja, favorece digestión/reposo). El balance entre ambos mantiene la homeostasis corporal. 

- Drones con autopilotaje adaptativo: el controlador se adapta automáticamente a condiciones cambiantes de vuelo (peso, centro de masa, fallas de motor). 

- Reactor nuclear: la variable controlada es la potencia relativa del núcleo; la variable manipulada es la posición de las barras de control (que absorben neutrones), ajustando la reactividad. 

Página 13 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **2.7 Casos resueltos típicos de control** 

## 📝 **Pregunta de control — Brazo protésico (2025, P5)** 

Prótesis con sensores EMG + controlador + motores + sensores de retroalimentación 

(acelerómetros/fuerza) = lazo cerrado con retroalimentación negativa, porque usa información sensorial para corregir el movimiento en tiempo real. 

Ventaja: ajusta el movimiento según actividad muscular real. Desventaja: requiere muchos sensores y capacidad de procesamiento. 

Al añadir sensores táctiles que permiten 'sentir' la presión y ajustar la fuerza de agarre, el sistema pasa a ser un sistema de control adaptativo (o retroalimentado con un segundo nivel de información), cuyo objetivo es mantener una fuerza de agarre estable y adaptable según las propiedades del objeto sostenido. 

## 📝 **Pregunta de control — Llenado de piscina (2024, P5) y ducha (2023, P5)** 

Sistema original (operario regulando válvula solo por experiencia, sin ver el resultado) = lazo abierto. 

Sistema con sensor de profundidad/temperatura + controlador automático = lazo cerrado, feedback negativo. 

Si se agrega una fuga constante Fs en la piscina, el balance de masa de agua es: dm/dt = Fe(t) − Fs. La piscina pierde nivel cuando Fs > Fe(t). A largo plazo: o el sistema de control logra igualar Fe con Fs (alcanzando un nuevo estado estacionario con la piscina en un nivel V constante, no llena ni vacía), o el flujo de entrada nunca se estabiliza y el sistema de control trabaja indefinidamente ajustando Fe. 

📝 **Pregunta de control — Planta de lavado de botellas (2024, P1)** 

Diseño con tiempo y presión fijos = lazo abierto. Ventaja: no requiere sensores, es más simple y barato. Desventaja: no responde a variaciones en el nivel de suciedad de las botellas (ineficiente en uso de recursos si se asume siempre el máximo de suciedad). 

Al incorporar un sensor de suciedad, el sistema mejorado debe ser lazo cerrado, feedback negativo, en cada etapa de lavado, porque cada etapa debe cumplir su estándar de limpieza independiente de la suciedad de entrada. 

Componentes pedidos: Proceso (mecanismos de lavado), Set-point (estándar mínimo de limpieza), Sensor (detecta suciedad), Controlador (calcula el ajuste necesario: tiempo, presión, detergente), Actuador (equipo de hidrolavado), Línea de transmisión (cables/señales entre componentes). 

Desafíos típicos de este tipo de sistema: precisión/sensibilidad insuficiente del sensor; fallas del actuador; suciedad no detectable; variabilidad de las perturbaciones (distintos niveles de entrada); limitaciones técnicas de suministro (agua, detergente). 

## 📝 **Pregunta de control — Calefont y pariente (2023, P5)** 

Controlador: el cerebro de la persona en la ducha. Actuador: el pariente que ajusta el calefont. Proceso: la ducha. Sensor: percepción de temperatura de la persona. Comunicación: la voz (transporte de sonido por el aire). 

Página 14 de 46 

_BT1211 — Guía de Estudio Control 2_ 

Es un lazo cerrado con feedback negativo: se busca mantener la temperatura en el rango preferido, oponiéndose a las perturbaciones (otros consumos de agua, etc.). 

Si en vez de hablar directo se usa el teléfono, la estructura del sistema no cambia — solo cambia el canal de comunicación entre sensor y controlador (ahora es la llamada telefónica en vez de la voz directa). 

## 📝 **Pregunta de control — Operón triptófano (Auxiliar 3)** 

El operón TRP es un sistema de control genético: variable controlada = nivel de triptófano en la célula. Si hay TRP, se une al represor TRP, que se activa y bloquea (apaga) la transcripción del operón = retroalimentación negativa (el producto final inhibe su propia producción). 

El Represor TRP actúa como sensor (detecta la presencia de TRP) y como actuador/controlador a la vez (al unirse al operador, bloquea físicamente la transcripción). 

Si una molécula X compite con el TRP por el represor y lo mantiene activo incluso sin TRP presente, X actúa como una falsa señal de set-point / engaña al sensor — desde el punto de vista de control, X es un inhibidor que simula la señal natural, alterando la lectura real del sistema. 

## **2.8 Síntesis rápida — preguntas frecuentes de control** 

|**Pregunta típica**|**Cómo responder**|
|---|---|
|¿Lazo abierto o cerrado?|¿Existe un sensor que mida la salida real y la retroalimente al controlador? Si<br>sí→cerrado. Si no→abierto.|
|¿Feedback positivo o negativo?|¿La respuesta se opone al estímulo (vuelve al equilibrio) o lo amplifica (se<br>aleja, hasta terminar el proceso)?|
|Identificar componentes|Buscar explícitamente: Sensor (mide), Controlador (decide/compara con<br>set-point), Actuador (ejecuta), Proceso (lo que se transforma), Comunicación<br>(cómo viaja la señal), Perturbación (factor externo no controlado).|
|Ventajas/desventajas de cada lazo|Abierto: simple y barato, pero no corrige errores ni se adapta. Cerrado:<br>preciso y robusto, pero más costoso/complejo de implementar.|



Página 15 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **3. Transporte de Masa y Movimiento en Organismos Vivos** 

## **3.1 Concepto general de transporte** 

Transporte: transferencia de una entidad (autos, moléculas, masa, energía, calor, momentum) de un lugar a otro. Flujo: cantidad de entidad transportada por unidad de tiempo. 

En una célula, el transporte de moléculas se clasifica en: 

- Transporte activo: requiere el uso de ATP (energía); mueve sustancias en contra de su gradiente. 

- Transporte pasivo: ocurre por una diferencia de gradiente (no gasta energía); a favor del gradiente. 

## **3.2 Fuerza motriz, flujo y resistencia** 

Todo sistema de transporte se describe con tres elementos análogos, sin importar la naturaleza física del sistema: 

- Fuerza motriz: aquello que causa la acción / el transporte (la causa). 

- Flujo: la respuesta ante dicha fuerza motriz (el efecto, el transporte mismo). 

- Resistencia: el límite que el sistema impone al flujo, para una fuerza motriz dada. 

|**Resistencia = Fuerza motriz / Flujo**|**Resistencia = Fuerza motriz / Flujo**|**Resistencia = Fuerza motriz / Flujo**|
|---|---|---|
|**Sistema**|**Fuerza motriz**|**Flujo (variable de respuesta)**|
|Electricidad|Voltaje|Flujo de electrones (corriente)|
|Fluidos|Presión|Flujo de fluido|
|Calor|Temperatura (diferencia)|Flujo de calor|
|Masa|Concentración (diferencia)|Flujo de masa|
|Mecánica|Fuerza|Velocidad|
|Óptica|Presión fotónica|Flujo de fotones|
|Magnetismo|Fuerza magnetomotriz|Flujo magnético|



El transporte siempre va desde un mayor valor de la fuerza motriz hacia un menor valor (a favor del gradiente), salvo que se gaste energía externa para forzarlo en sentido contrario (transporte activo). 

## **3.3 Balance de materia (general)** 

**(Lo que entra en un Δt) − (Lo que sale en un Δt) = (Lo que se acumula en un Δt)** 

En notación de flujos volumétricos (ρ = densidad, Q = caudal): 

Página 16 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **ρQe − ρQs = dm_acumulada / dt** 

Con reacción química, se agregan generación y consumo: 

## **Entra − Sale + Genera − Consume = Acumula** 

- 💡 **Ejemplo — Balance de O₂ en los pulmones** 

Supuestos: no se genera oxígeno en los pulmones; no se acumula oxígeno en el organismo (estado estacionario); el oxígeno transferido a la sangre se considera un consumo (o un flujo de salida). 

− Balance resultante: (masa de O₂ que entra) (masa de O₂ que sale) = (masa de O₂ que se consume) en cada Δt. 

## **3.4 Mecanismos de transferencia de masa** 

|**Mecanismo**<br>Difusión<br>Convección|**Definición**|**Fuerza motriz**|
|---|---|---|
||Transporte de masa por movimiento molecular aleatorio<br>(sin flujo de fluido)|Diferencia (gradiente) de<br>concentración|
||Transporte de masa arrastrada por el flujo de un fluido|Diferencia de presión<br>(forzada) o diferencia de<br>densidad (natural)|



## _**Ley de Fick (difusión)**_ 

_Velocidad de transferencia de masa (flujo) = (coeficiente de difusión × área superficial perpendicular al flujo × diferencia de concentración) / distancia_ 

## **Resistencia = distancia / (área superficial × coeficiente de difusión)** 

- La difusividad (coeficiente de difusión) es mayor en gases, sensiblemente menor en líquidos y casi nula en sólidos. 

- A mayor área de transferencia → mayor velocidad de transferencia (por eso vellosidades y microvellosidades intestinales aumentan tanto el área disponible). 

- A mayor distancia → menor velocidad de transferencia, por eso organismos que dependen solo de difusión (ej. celenterados, medusas) deben ser delgados o tener formas que minimicen la distancia de difusión. 

## **3.5 Redes de transporte biológico** 

Para servir a todo un organismo, el sistema de transporte requiere un patrón de ramificación jerárquica que cubra todo el volumen (ej. sistema circulatorio, sistema respiratorio, raíces). Las ramas finales (donde ocurre el intercambio de nutrientes) son unidades de tamaño fijo. Los organismos han 

Página 17 de 46 

_BT1211 — Guía de Estudio Control 2_ 

evolucionado para minimizar la energía necesaria para transportar materia de forma convectiva por la red. 

## **3.6 Transporte por convección: mecánica de fluidos** 

## _**Viscosidad**_ 

La viscosidad describe la resistencia interna de un fluido a fluir (no confundir con densidad). 

- Efecto de la temperatura: al aumentar la temperatura, aumenta la energía cinética y la distancia entre moléculas, disminuyen las fuerzas intermoleculares → disminuye la viscosidad (para líquidos como el agua). 

- Efecto de solutos disueltos: tanto solutos pequeños como moléculas poliméricas en cadena (mayor concentración C) tienden a aumentar la viscosidad. 

## _**Fluidos newtonianos vs. no newtonianos**_ 

|**Tipo**|**Comportamiento**|**Ejemplos**|
|---|---|---|
|Newtoniano|Viscosidad constante, independiente de la fuerza de<br>corte aplicada|Agua, plasma sanguíneo, natillas|
|Pseudoplástico|La viscosidad aparente disminuye con el esfuerzo<br>aplicado (se vuelve 'más líquido' al agitar)|Sangre, ketchup, pulpa de papel,<br>savia, melaza|
|Dilatante|La viscosidad aparente aumenta con el esfuerzo<br>aplicado|Suspensiones de almidón en agua|
|Tixotrópico|La viscosidad aparente disminuye con la duración del<br>esfuerzo (recupera al reposar)|Yogurt, geles, algunas pinturas|
|Reopéctico|La viscosidad aparente aumenta con la duración del<br>esfuerzo|Fluido sinovial, tinta de impresión|



Ejemplo clave: la sangre es un fluido no newtoniano pseudoplástico — fluye con mayor facilidad relativa a mayores velocidades de corte (ej. en vasos pequeños o ante mayor flujo). 

## **3.7 Caso aplicado: el dializador (hemodiálisis)** 

Un equipo de diálisis tiene dos compartimentos líquidos —sangre (S) y dializado (D)— separados por una membrana semipermeable que deja pasar solutos pequeños/medianos (como la urea) pero no proteínas ni células. 

## **− F = k** ₀ **·A·(C_U,Se C_U,De)   [g/min]** 

Donde k₀ es el coeficiente global de transferencia de masa, A es el área de intercambio de la membrana, − y (C_U,Se C_U,De) es la diferencia de concentración de urea entre la entrada de sangre y la entrada de dializado (la fuerza motriz). 

Página 18 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## _**Balances de masa de urea en el dializador**_ 

**Compartimento S:   dM_U,S/dt = Qs·C_U,Se − Qs·C_U,Ss − F** 

**Compartimento D:   dM_U,D/dt = Qd·C_U,De − Qd·C_U,Ds + F** 

En estado estacionario (sin acumulación, ambas derivadas = 0): 

## **− − F = Qs·(C_U,Se C_U,Ss) = Qd·(C_U,Ds C_U,De)** 

Es decir: toda la urea removida de la sangre en estado estacionario es exactamente la urea transferida al líquido de diálisis (conservación de masa). 

💡 **Ejemplo numérico (Control 2025, P4-c)** 

Datos: Qs = 500 cm³/min, Qd = 750 cm³/min, C_U,De = 0 (dializado entra limpio), C_U,Ds = 0.3 g/cm³. − − F = Qd·(C_U,Ds C_U,De) = 750 × (0.3 0) = 225 g/min. 

Fuerza motriz del transporte de urea: diferencia de concentración entre sangre y líquido de diálisis (difusión a través de la membrana). Para reducir la concentración de urea de salida del paciente se puede: aumentar el área de membrana A, usar una membrana con mayor k₀, o aumentar Qd para mantener baja la concentración del lado del dializado (mayor diferencia de concentración local). 

📝 **Pregunta de control — Hemodiálisis (Auxiliar 3)** 

La velocidad de transporte de urea depende de: la diferencia de concentración entre sangre y solución de diálisis, el área de la membrana, el coeficiente de transferencia, y el flujo de sangre (a mayor flujo, mayor renovación de sangre 'fresca' en contacto con la membrana, manteniendo el gradiente). 

Para evitar que la glucosa (de tamaño similar a la urea) se pierda hacia la solución de diálisis, se agrega glucosa a la solución de diálisis en una concentración similar a la sanguínea normal, eliminando el gradiente de concentración de glucosa (sin gradiente, no hay fuerza motriz para su transporte neto). 

Si la bomba falla y la sangre se mueve muy lento o no se mueve: disminuye drásticamente la velocidad de transporte de urea, porque al no renovarse la sangre en contacto con la membrana, la concentración local de urea en sangre baja rápidamente (se agota el gradiente local) — el transporte pasa a depender solo de difusión lenta en vez de convección. 

## **3.8 Caso aplicado: tubería entre piscinas (Hagen-Poiseuille)** 

Para flujo convectivo de un fluido viscoso por una tubería de largo L y diámetro D, la diferencia de presión necesaria para un caudal Q dado es: 

## **ΔP = (128·L·μ·Q) / (π·D** ⁴ **)** 

Despejando el flujo Q en función de ΔP (constante), L y D: 

Página 19 de 46 

_BT1211 — Guía de Estudio Control 2_ 

_Q = (π·D_ ⁴ _·_ Δ _P) / (128·L·μ)   →   Q es muy sensible al diámetro (D_ ⁴ _) y poco sensible al largo (L¹)_ 

💡 **Ejemplo — Reducir flujo en una tubería (Actividad 5)** 

Si se quiere disminuir el flujo Q manteniendo ΔP constante, comparar: reducir D a la mitad reduce Q en un factor de (1/2)⁴ = 1/16; en cambio duplicar L reduce Q solo en un factor de 1/2. 

Conclusión: disminuir el diámetro es mucho más efectivo para reducir el flujo que aumentar el largo del tubo, porque Q depende de la cuarta potencia del diámetro pero solo linealmente del largo. 

## **3.9 Heterotermia regional: contracorriente (gaviotas)** 

Mecanismo fisiológico que permite mantener distintas zonas de temperatura en el cuerpo (en especial extremidades), para ahorrar energía que de otro modo se usaría en calentarlas. 

## _**Intercambio de calor a contracorriente**_ 

La sangre caliente (arteria) baja desde el cuerpo hacia la pata; la sangre fría (vena) sube en sentido opuesto. Al estar en contacto cercano y en direcciones opuestas a lo largo de un tramo extenso, se transfiere calor por conducción desde la arteria hacia la vena de forma continua a lo largo de todo el trayecto. 

|**Mecanismo de**<br>**transferencia**|**Dónde ocurre**|**Tipo**|
|---|---|---|
|Conducción|Entre arteria y vena adyacentes (sin movimiento neto de<br>fluido entre ellas)|Calor pasa por contacto<br>directo entre los vasos|
|Convección|El flujo de sangre mismo (transporte de calor 'arrastrado'<br>por la sangre que circula)|Calor es transportado de<br>un punto a otro por el<br>fluido en movimiento|



Resultado: la sangre fría que sube por la vena se va calentando progresivamente antes de llegar al cuerpo (evitando enfriar el núcleo corporal), mientras que la sangre que baja por la arteria llega ya fría a los dedos (minimizando la pérdida de calor hacia el ambiente desde una zona de mucha área de contacto). 

_Si arteria y vena estuvieran alejadas, no habría intercambio de calor entre ellas y la sangre fría llegaría directo al cuerpo, enfriándolo. Si el tramo de contacto fuera muy corto, no alcanzaría a igualarse la temperatura entre ambas corrientes y se perdería el mismo efecto protector._ 

La mayor ramificación del sistema circulatorio en los dedos (respecto a la pierna) aumenta el área de contacto con el ambiente, facilitando la pérdida de calor en esa zona específica — consistente con mantener los dedos fríos pero el cuerpo caliente. 

Página 20 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **3.10 Síntesis de fórmulas — Transporte** 

|**Concepto**|**Fórmula**|
|---|---|
|Resistencia general|Resistencia = Fuerza motriz / Flujo|
|Ley de Fick (difusión)|Flujo = (coef. difusión × área ×ΔC) / distancia|
|Flujo en dializador|F = k₀·A·(C_Se−C_De)|
|Hagen-Poiseuille|ΔP = 128·L·μ·Q / (π·D⁴)|
|Balance general|Entra−Sale + Genera−Consume = Acumula|



Página 21 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **4. Manejo y Transferencia de Energía en los Organismos Vivos** 

## **4.1 Sistemas termodinámicos** 

Un sistema está compuesto por múltiples elementos y posee una frontera definida. Según su interacción con el entorno, se clasifica en: 

|**Tipo de sistema**|**Intercambia materia**|**Intercambia energía**|
|---|---|---|
|Aislado|No|No|
|Cerrado|No|Sí|
|Abierto|Sí|Sí|



La mayoría de los organismos vivos son sistemas abiertos: intercambian tanto materia (alimento, desechos, gases) como energía (calor, trabajo) con su entorno. 

## **4.2 Leyes de la termodinámica** 

**==> picture [468 x 35] intentionally omitted <==**

## _**Entropía en sistemas biológicos**_ 

Pregunta clásica: ¿cómo la célula mantiene su orden interno sin contradecir la segunda ley? 

- La célula usa energía para aumentar el orden molecular interno, lo que disminuye su propia entropía localmente. 

- Sin embargo, el calor generado por las reacciones que mantienen ese orden aumenta el desorden (entropía) del entorno. 

- El balance neto (célula + entorno) sigue cumpliendo la 2ª ley: la entropía total del universo aumenta, aunque la célula individualmente se mantenga ordenada gracias a un suministro constante de energía. 

## **4.3 Formas de energía y transformación** 

- Energía cinética: la que tiene un cuerpo debido a su movimiento (velocidad, temperatura/vibración molecular, etc.). 

- Energía potencial: la que tiene un objeto sometido a un potencial (altura, energía química almacenada en enlaces, resorte, etc.). 

La energía puede transferirse en forma de calor (Q) o trabajo, siempre desde un estado de mayor nivel energético a uno de menor nivel. 

Página 22 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## _**Tipos de trabajo biológico**_ 

|**Tipo de trabajo**<br>Sintético<br>Eléctrico<br>Mecánico|**Descripción**|
|---|---|
||Fabricación de moléculas complejas necesarias para la vida (anabolismo)|
||Generación de potenciales de membrana mediante migración de iones, base del<br>impulso eléctrico|
||Movimiento muscular; requiere gran cantidad de energía (ATP) como fuente|



## **4.4 Eficiencia de conversión energética** 

## **Eficiencia = Trabajo / (Trabajo + Calor)** 

## **Eficiencia Bruta = Energía obtenida / Energía entregada** 

## **Eficiencia Neta = Energía a biomasa / Energía entregada** 

La interconversión de energía siempre tiene una eficiencia asociada — nunca se logra el 100%. Ejemplo: las plantas aprovechan menos de un 2% de la energía solar total recibida en fotosíntesis. 

## **4.5 Flujo de energía en ecosistemas (niveles tróficos)** 

La luz solar es la fuente de energía primaria para todo el ecosistema. Los productores primarios (fotosintéticos) aprovechan solo una fracción de la energía solar disponible: una parte queda almacenada en biomasa nueva, y el resto se gasta en mantenimiento/calor o se pierde. 

- La energía en la biomasa de un nivel trófico está disponible para el nivel siguiente, que se alimenta de él. 

- La biomasa no consumida como alimento queda disponible para descomponedores. 

- Solo una fracción pequeña de la energía pasa de un nivel trófico al siguiente — por eso los ecosistemas generalmente están limitados a 4 o 5 niveles tróficos (la energía disponible se hace insuficiente para sostener un nivel adicional). 

## 💡 **Ejemplo — Flujo de energía en red trófica (Trabajo de aplicación 2025)** 

Dado un esquema con sol → productores → consumidores → descomponedores, con valores de kcal/m²/año en cada flecha, se pide: identificar el tipo de sistema (abierto: intercambia materia y energía con el entorno), calcular incógnitas por balance de energía en cada nivel, calcular porcentajes de energía utilizada respecto al nivel anterior, y explicar por qué la energía disponible decae drásticamente nivel a nivel (de ahí la limitación a pocos niveles tróficos). 

Página 23 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **4.6 La molécula de ATP** 

ATP (Adenosín TriFosfato): la 'moneda energética' celular. 

- La hidrólisis de un grupo fosfato (ATP → ADP) libera aproximadamente 30.5 kJ/mol (≈ 7.3 kcal/mol). 

- Una persona promedio gasta cerca de 50–100 kcal/h en actividades cotidianas. 

- El ADP puede volver a formar ATP si se le suministra energía (ej. desde la respiración celular). 

- El ATP se usa en la mayoría de reacciones de catabolismo (degradación) y anabolismo (síntesis). 

## _**Acoplamiento de reacciones**_ 

Las células acoplan una reacción energéticamente favorable (ej. hidrólisis de ATP, ΔG muy negativo) con una reacción energéticamente desfavorable (endergónica, ΔG positivo), de manera que la reacción neta combinada siga siendo favorable (ΔG neto negativo). 

## 💡 **Ejemplo — Glutamina sintetasa (Trabajo de aplicación 2025, P2)** 

La formación de glutamina a partir de glutamato y amoniaco no es espontánea por sí sola (ΔG positivo). La hidrólisis de ATP sí es espontánea (ΔG muy negativo). La enzima glutamina sintetasa acopla ambas reacciones en dos pasos, usando la energía liberada por la hidrólisis de ATP para impulsar la reacción desfavorable, logrando una reacción global espontánea. 

## **4.7 Fotosíntesis y respiración celular** 

**Fotosíntesis:  6CO₂ + 6H₂O + Energía solar → C** ₆ **H₁₂O** ₆ **+ 6O₂** 

**Respiración celular:  C** ₆ **H₁₂O** ₆ **+ 6O₂ → 6CO₂ + 6H₂O + ATP** 

La incorporación de CO₂ en moléculas orgánicas requiere energía y poder reductor (NADPH, ATP), provistos por la fase luminosa de la fotosíntesis. Una molécula de glucosa puede producir hasta 36 moléculas de ATP en la respiración celular (oxidación escalonada y controlada, a diferencia de una combustión directa no biológica). 

## **4.8 Transferencia de calor** 

Proceso por el que se intercambia energía en forma de calor entre cuerpos a distinta temperatura. La generación de calor en un organismo depende del volumen, mientras que las pérdidas de calor dependen de la superficie de contacto con el entorno — esta asimetría es clave en biología térmica (ver sección 4.9). 

|**Mecanismo**<br>Conducción|**Descripción**|
|---|---|
||Requiere contacto directo entre dos cuerpos|



Página 24 de 46 

_BT1211 — Guía de Estudio Control 2_ 

|**Mecanismo**|**Descripción**|
|---|---|
|Convección|Ocurre por movimiento de un fluido; puede ser natural (por diferencia de densidad) o<br>forzada (por diferencia de presión)|
|Radiación|Emisión de energía por un cuerpo debido a su propia temperatura, sin necesidad de<br>medio ni contacto|



Ejemplo combinado: la evaporación del sudor en la piel mezcla convección natural (movimiento del aire), conducción (calor desde la piel al sudor) y cambio de fase (líquido→gas, que absorbe calor latente). 

## _**Regulación de temperatura por sudoración**_ 

- Mediante el sudor se pierde cerca de un 27% del calor corporal. 

- El agua tiene un alto calor específico, por lo que evaporar el sudor requiere absorber una cantidad importante de calor desde la piel. 

- Al evaporarse, el sudor extrae esa energía desde la piel, enfriándola a ella y a los tejidos subyacentes. 

- Si la temperatura corporal baja, se suprime la sudoración para evitar pérdida adicional de calor; durante la fiebre, inicialmente también se suprime la sudoración para evitar que baje la temperatura corporal (el cuerpo 'defiende' un set-point más alto). 

## **4.9 Relación superficie/volumen y tamaño corporal** 

Pregunta de control recurrente (ej. dinosaurios de sangre 'intermedia'): la generación de calor es proporcional al volumen del animal, mientras que la pérdida de calor hacia el entorno es proporcional a su superficie de contacto (según las ecuaciones de transferencia de calor — el flujo depende del área a través de la cual se transfiere). 

Modelando al animal como una esfera de radio r: 

## **V_esfera = (4/3)·π·r³        S_esfera = 4·π·r²** 

**Velocidad de generación de calor** ∝ **r³        Velocidad de pérdida de calor** ∝ **r²** 

**Razón pérdida : generación = (cte·r²)/(cte·r³) = cte/r   →   inversamente proporcional a r** 

💡 **Ejemplo — Dinosaurios y tamaño corporal (Control 2023, P6)** 

Como la razón pérdida:generación es inversamente proporcional al radio r, un animal grande (r grande) pierde proporcionalmente menos calor —en relación a lo que genera— que un animal pequeño. 

Página 25 de 46 

_BT1211 — Guía de Estudio Control 2_ 

Por lo tanto, animales pequeños deben generar mucho más calor por unidad de volumen para compensar su mayor pérdida relativa (de ahí que mamíferos pequeños tengan metabolismos muy acelerados). 

Ventaja evolutiva para dinosaurios de gran tamaño: necesitan poca energía relativa para mantener su temperatura (ventaja frente a mamíferos pequeños 'de sangre caliente', que gastan mucha energía en termogénesis), mientras que tener una temperatura interna más alta que los reptiles les da metabolismo más rápido para depredación/defensa, sin depender tanto de la temperatura ambiental. 

## **4.10 Síntesis de fórmulas — Energía** 

|**Concepto**|**Fórmula**|
|---|---|
|Eficiencia de conversión|Eficiencia = Trabajo / (Trabajo + Calor)|
|Eficiencia bruta|Energía obtenida / Energía entregada|
|Eficiencia neta|Energía a biomasa / Energía entregada|
|Hidrólisis de ATP|ATP→ADP + Pi,ΔG≈ −30.5 kJ/mol (−7.3 kcal/mol)|
|Volumen / superficie esfera|V = (4/3)πr³  ;  S = 4πr²|
|Razón pérdida:generación de calor|∝1/r  (inversamente proporcional al tamaño)|



Página 26 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **5. Aleatoriedad y Probabilidad — Estadística Aplicada** 

Estadística: rama de las matemáticas que estudia la variabilidad y los procesos aleatorios que la generan. 

## **5.1 Términos y definiciones básicas** 

|**Término**|**Definición**|
|---|---|
|Individuo|Elemento de una población, del cual se extrae una muestra y se toman variables|
|Población|Conjunto de todos los elementos de interés|
|Muestra|Subconjunto de la población, seleccionado para estudio|
|Variable|Atributo para el cual cada elemento de la población tiene un valor (ej. edad,<br>concentración, peso)|



## **5.2 Estadística descriptiva vs. inferencial** 

||**Estadística descriptiva**|**Estadística inferencial**|
|---|---|---|
|Objetivo|Describe, resume y visualiza los datos<br>disponibles|Infiere características de la población a partir<br>de una muestra|
|Herramientas|Medidas de tendencia central, medidas de<br>dispersión, gráficos|Pruebas de hipótesis, estimaciones,<br>correlaciones|
|Ejemplo|Censo poblacional (describe a toda la<br>población)|Encuesta electoral (infiere preferencias de<br>toda la población a partir de una muestra)|



## **5.3 Medidas de tendencia central** 

Indican en torno a qué valor se agrupan los datos. 

- Media aritmética: valor característico (promedio) de una serie de datos. 

- Mediana: valor de la variable central de una serie de datos ordenada. 

- Moda: valor más repetido (frecuente) de una serie de datos. 

En una distribución simétrica (normal), media, mediana y moda coinciden. En distribuciones asimétricas, se separan — por eso reportar solo el promedio puede ser engañoso si hay valores extremos (outliers) que lo desplazan, mientras la mediana es más robusta a estos. 

- 💡 **Ejemplo — Media vs. mediana: ¿en qué ciudad estacionarías?** 

Al comparar el número de autos robados por día en dos ciudades durante 6 meses, el promedio puede ser igual en ambas, pero una ciudad puede tener días con cifras muy altas (outliers) que distorsionan el promedio, mientras la mediana revela mejor el comportamiento 'típico' de la mayoría de los días. 

Página 27 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **5.4 Medidas de dispersión** 

Las medidas de tendencia central no lo dicen todo: los datos pueden estar muy concentrados o muy dispersos alrededor del centro. Para cuantificar esto: 

- Varianza (σ²): medida cuadrática de la dispersión de los datos respecto al promedio. 

- Desviación estándar (σ o s): raíz de la varianza; mide la dispersión en las mismas unidades que la variable original. Un ancho de ±2σ alrededor de la media contiene aproximadamente el 95% de los datos (en una distribución normal); ±1σ contiene aproximadamente el 68.2%. 

## 💡 **Ejemplo — Comparar inversiones por desviación estándar** 

Dos acciones con el mismo retorno promedio (8%) pueden tener desviaciones estándar muy distintas (3% vs. 10%). La de menor desviación estándar es menos volátil/riesgosa, aunque el promedio sea idéntico — el promedio solo no basta para decidir. 

## 📝 **Pregunta de control — Catalizador con eficiencia promedio (Control 2023, P2)** 

Un vendedor informa que un nuevo catalizador aumenta la eficiencia en promedio un 10%. Esto es insuficiente: se necesita también la desviación estándar de los experimentos, para saber qué tan homogéneos fueron los resultados. 

Si la desviación estándar es grande, significa que los experimentos arrojaron resultados muy disímiles entre sí — cambiar el catalizador en esas condiciones pondría en riesgo la operación industrial, aunque el promedio sea favorable. 

## 📝 **Pregunta de control — Máquinas dispensadoras de combustible (Control 2025, P3)** 

Reportar solo la diferencia promedio (0.1 L por cada 20 L) no es suficiente para concluir que las máquinas están 'arregladas'. Se debería solicitar adicionalmente: (1) el tamaño de la muestra y criterio de selección (para evaluar sesgos y representatividad), y (2) la desviación estándar o varianza (para saber si esa diferencia es consistente o esconde mucha dispersión). 

## **5.5 Correlación** 

Técnica estadística que indica si dos variables están relacionadas (varían juntas) o no. Puede ser nula, negativa o positiva. 

- Covarianza: valor que indica el grado de variación conjunta de dos variables aleatorias respecto a sus medias. Su signo (positivo/negativo) indica el sentido de la relación. 

- Coeficiente de correlación: valor adimensional (entre -1 y 1) que indica el grado de dependencia lineal entre dos variables, normalizando la covarianza. 

## _**Correlación ≠ Causalidad**_ 

**Que exista correlación NO implica causalidad.** 

Página 28 de 46 

_BT1211 — Guía de Estudio Control 2_ 

Ejemplo clásico: existe correlación histórica entre venta de helados y casos de poliomielitis (ambos aumentan en verano). Esto no significa que el helado cause polio — ambas variables están relacionadas con una tercera variable de confusión (la temporada/calor), no entre sí directamente. 

## 📝 **Pregunta de control — Largo de manguera y diferencia de carga (Control 2025, P3-d)** 

Si un gráfico de 8 muestras (largo de manguera vs. diferencia de carga) muestra una tendencia creciente, la covarianza de la muestra es positiva. 

Sin embargo, la covarianza de la muestra pequeña no necesariamente coincide con la covarianza de la población completa — una muestra pequeña o no representativa puede dar una impresión equivocada. 

Por lo tanto, no se debería recomendar cargar solo en máquinas con manguera corta basándose únicamente en esta muestra: una correlación en una muestra pequeña no constituye evidencia estadística suficiente, y mucho menos prueba causalidad. 

## **5.6 Test de hipótesis** 

Permiten contrastar hipótesis sobre poblaciones a partir de información de muestras. Se rechaza una hipótesis si la muestra observada es muy extrema asumiendo que esa hipótesis es cierta — esto entrega evidencia a favor de la hipótesis alternativa. 

- H0 (hipótesis nula): creencia base que se asume cierta a menos que se demuestre lo contrario. 

- H1 (hipótesis alternativa): negación de H0; se acepta si H0 es rechazada. 

## 💡 **Ejemplo — ¿Está cargada la moneda?** 

H0: la moneda no está cargada (P(cara) = ½). H1: la moneda está cargada. Si en 100 lanzamientos se observan 60 caras y 40 sellos, el test de hipótesis evalúa qué tan verosímil es observar ese resultado (o uno más extremo) asumiendo que H0 es cierta. 

## _**Errores Tipo I y Tipo II**_ 

|Aceptamos H0<br>Rechazamos H0|**H0 verdadera en realidad**|**H0 falsa en realidad**|
|---|---|---|
||Decisión correcta|Error Tipo II (falso negativo)|
||Error Tipo I (falso positivo)|Decisión correcta|



- Error Tipo I: H0 es verdadera, pero el test la rechaza (falso positivo). 

- Error Tipo II: H0 es falsa, pero el test la acepta (falso negativo). 

📝 **Pregunta de control — Combustible y errores tipo I/II (Control 2025, P3-b,c)** 

H0: la carga de las máquinas de la empresa es igual a la de referencia. H1: es distinta. 

Página 29 de 46 

_BT1211 — Guía de Estudio Control 2_ 

Error Tipo I: concluir que la empresa entrega menos combustible del indicado, cuando en realidad sí entrega lo correcto (acusar injustamente). 

Error Tipo II: concluir que la empresa entrega bien el combustible, cuando en realidad está entregando menos (no detectar el problema real). 

Si se rechaza H0: hay evidencia estadística de que la empresa entrega menos combustible del indicado — la empresa podría enfrentar sanciones, multas y pérdida de confianza de sus clientes. 

## **5.7 Errores experimentales** 

|**Tipo de error**|**Descripción**|**Cómo mejorar la**<br>**estimación**|
|---|---|---|
|Aleatorio|Variabilidad en torno a un valor central, causada por<br>factores no controlados|Aumentar el tamaño de la<br>muestra|
|Sistemático|Error presente en todas las mediciones, en la misma<br>dirección (ej. balanza mal calibrada)|Modificar/corregir el<br>proceso de medición|



## **5.8 Síntesis de fórmulas — Estadística** 

|**Concepto**|**Idea clave**|
|---|---|
|Media / Mediana / Moda|Medidas de tendencia central; la mediana es robusta ante outliers|
|Varianza / Desv. estándar|Medidas de dispersión; ±2σ ≈95% de los datos en distribución normal|
|Covarianza|Signo indica sentido de la relación entre dos variables|
|Coeficiente de correlación|Versión normalizada de la covarianza, entre -1 y 1|
|Correlación≠Causalidad|Una relación entre variables no prueba que una cause la otra|
|Error Tipo I|Rechazar H0 verdadera (falso positivo)|
|Error Tipo II|Aceptar H0 falsa (falso negativo)|



Página 30 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **6. Aplicaciones Industriales de la Biología** 

## **6.1 Ingeniería genética** 

## _**Mitos y conceptos clave**_ 

|**Modificación 'natural'**|**Modificación 'sintética' (ingeniería genética)**|
|---|---|
|Cruza de variedades; muchos genes modificados a la vez;<br>no regulada|Biología molecular; manipulación de un gen o región<br>acotada del ADN; altamente regulada; bajo margen de<br>error|



- Bioseguridad: incluye consumo seguro de alimentos de organismos genéticamente modificados (GMO), legislación (FDA, Norma Chilena — en Chile no está permitido producir GMO para consumo local), y consideraciones medioambientales. 

- Ejemplos de impacto ambiental: cultivos resistentes a herbicida (ej. soya tolerante a glifosato) para control de malezas; algodón Bt con resistencia a plagas (reducción de hasta 80% en uso de insecticida). 

- La ingeniería genética es una herramienta — no es intrínsecamente 'natural' ni 'antinatural'; existen incluso transgénicos naturales (ej. el camote, que incorporó de forma natural ADN de Agrobacterium tumefasiens). 

## _**Elementos básicos de la ingeniería genética**_ 

Todo sistema de expresión recombinante requiere tres elementos: 

|**Elemento**|**Rol**|
|---|---|
|Gen de interés (el código)|La secuencia de ADN que codifica para la proteína deseada|
|Vector (el vehículo)|Molécula que transporta e inserta el gen exógeno directamente en el<br>huésped (ej. plásmido)|
|Sistema de expresión (el huésped)|Organismo cuyo genoma será la 'fábrica' productora de la proteína|



## _**Vectores: plásmidos**_ 

Un plásmido es una molécula de ADN circular usada para transportar material genético, con capacidad de replicación independiente del ADN del huésped. Son los vectores más comunes y están presentes naturalmente en algunas bacterias. 

Página 31 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## _**Sistemas de expresión: procariontes vs. eucariontes**_ 

|**Criterio**|**Procariontes (ej. E. coli)**|**Eucariontes (levaduras, células**<br>**animales/vegetales)**|
|---|---|---|
|Velocidad|Muy alta (E. coli se duplica en ~20 min)|Lenta (levaduras 1-3 h; células animales 24-48<br>h)|
|Complejidad|Proteínas simples; sin modificaciones<br>post-traduccionales|Capaces de sintetizar y plegar proteínas<br>complejas|
|Costo y cultivo|Bajo costo, genomas bien estudiados|Alto costo; sensibles al esfuerzo de corte<br>mecánico; requieren más nutrientes|



## _**Transformación: ¿qué le pasa al ADN exógeno dentro del huésped?**_ 

La transformación es la alteración genética de una célula por incorporación de ADN exógeno (puede ser inmediata o requerir un inductor: molécula activadora). Tres destinos posibles: 

- El ADN permanece flotando como plásmido independiente. 

- El ADN se inserta físicamente y de manera estable en los cromosomas del huésped. 

- El ADN modifica el ADN del huésped de forma transitoria, pero no logra replicarse (se pierde con el tiempo). 

## _**Expresión de una proteína recombinante — 5 pasos**_ 

7. Aislar: identificar y extraer el gen de interés. 

8. Elegir huésped: seleccionar la célula base según complejidad requerida y costo industrial. 

9. Insertar: empalmar mecánicamente el gen dentro del vector (plásmido). 

- 10.Transformar: ingresar el vector al huésped celular (transformación, conjugación o transducción). 

- 11.Purificar: recuperación, purificación y caracterización final de la proteína producida. 

## 💡 **Ejemplo — Insulina humana recombinante** 

Pasos: 1) Aislamiento del gen de insulina humana; 2) Corte molecular; 3) Inserción en un plásmido vector; 4) Producción mediante cultivo celular (huésped, ej. bacteria o levadura); 5) Obtención del producto purificado. 

La célula se convierte en una 'fábrica programable': mayor rendimiento, menor costo y 100% de compatibilidad humana, comparado con extraer insulina de fuentes animales. 

## _**Proteína Fluorescente Verde (GFP)**_ 

Aislada de la medusa Aequorea victoria, es el biomarcador visual por excelencia. Al acoplarla como 'gen reportero' junto al gen de interés, permite verificar visualmente (a simple vista, bajo luz UV) que la transformación y expresión genética fue exitosa. 

Página 32 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## _**Híbrido vs. transgénico**_ 

||**Híbrido (cruce natural)**|**Transgénico (modificación de ADN)**|
|---|---|---|
|Mecanismo|Polinización cruzada o cruza reproductiva de<br>plantas afines|Inserción directa de genes foráneos mediante<br>ingeniería genética (microinyección,<br>plásmidos)|
|Barrera biológica|Limitado a la misma especie o especies<br>estrechamente emparentadas|Rompe la barrera de especies (ej. gen<br>humano en bacteria, gen bacteriano en<br>planta)|



## **6.2 Otras aplicaciones industriales: proteínas y biofármacos** 

|**Sector**|**Enzimas/productos**|**Uso**|
|---|---|---|
|Detergentes|Proteasas, lipasas, amilasas|Remueven manchas en la ropa según su<br>naturaleza química|
|Alimentos|Renina/chymosin, amilasas, pectinasas|Quesos, harinas, jugos|
|Industria forestal|Xilanasas, lacasas|Blanqueamiento de papel, en reemplazo de<br>compuestos clorados tóxicos|
|Biofármacos|Hormona de crecimiento, interferones<br>(IFN), activador tisular del<br>plasminógeno (t-PA), vacunas|Tratamientos médicos de alta especificidad|



## **6.3 Química verde** 

La química verde (o química sostenible) es el diseño de productos y procesos químicos que reducen o eliminan el uso y generación de sustancias peligrosas, considerando todo el ciclo de vida del producto. Se enfoca en eficiencia energética, uso de recursos renovables y prevención de residuos en la fuente. 

|**Ejemplo**|**Problema que resuelve**|
|---|---|
|Sea-Nine (alternativa al óxido de<br>tributilestaño)|Antiincrustante marino biodegradable, no tóxico para fauna marina (el<br>TBT fue prohibido por la OMI en 2008 por su alta toxicidad)|
|Polímeros biodegradables (PLA, PASP)|Sustitutos de plásticos tradicionales de larga permanencia ambiental,<br>sintetizados desde biomoléculas abundantes|



Principios relevantes evaluados en controles anteriores: prevención de la contaminación en la fuente (evitar generar residuos en vez de tratarlos después), uso eficiente de la energía, y preferencia por catalizadores sobre reactivos estequiométricos (los catalizadores se regeneran y reducen el uso de reactivos en exceso). 

📝 **Pregunta de control — Síntesis química vs. química verde (Control 2024, P4-c)** 

Página 33 de 46 

_BT1211 — Guía de Estudio Control 2_ 

Un proceso que usa altas presiones/temperaturas, sin catalizadores y que genera desechos ácidos, incumple al menos: (1) prevención de la contaminación y manejo correcto de desechos (genera desechos ácidos sin tratamiento), y (2) uso eficiente de la energía (altas T y P implican alto consumo energético). También podría señalarse la falta de uso de catalizadores como incumplimiento de otro principio de la química verde. 

## **6.4 Biomedicina** 

- Aplicación de técnicas y herramientas de la ingeniería al campo de la medicina: diseño y creación de prótesis, equipos de detección/diagnóstico y equipos médicos en general. 

- Órganos en un chip ('organ-on-chip'): dispositivos que imitan la fisiología humana in vitro para investigación y testeo de fármacos. 

- Manufactura aditiva (impresión 3D) y biomateriales biocompatibles (polímeros, metales, cerámicas): permiten regeneración de tejido y cumplen requisitos mecánicos de funcionalidad — ej. andamios (scaffolds) de PLA para crecimiento y diferenciación de células madre a hueso. 

- Nuevas prótesis e interfaces: implantes cerebrales combinados con avatares para restaurar comunicación en pacientes con síndrome de enclaustramiento (locked-in syndrome). 

- Nuevos implantes: chips retinales que traducen luz en impulsos eléctricos para el nervio óptico, permitiendo recuperación parcial de visión. 

## **6.5 Bioprocesos y biotransformaciones** 

Un bioproceso típico sigue un flujo de planificación e implementación, con monitoreo continuo durante todo el proceso. Las enzimas (proteínas catalizadoras de reacciones biológicas) son centrales en los bioprocesos industriales. 

## _**Comparación: ventajas y desventajas del uso de enzimas**_ 

|**Ventajas**|**Desventajas**|
|---|---|
|No son tóxicas|Alto costo|
|Altamente específicas|Dificultad para obtenerlas de forma pura|
|Funcionan en condiciones moderadas de T y pH|Problemas de estabilidad|
|Actúan a bajas concentraciones|Se inactivan fácilmente|



## _**Tratamiento de residuos industriales**_ 

|**Tipo de tratamiento**|**Aplicación típica**|
|---|---|
|Físico|Aguas con alta carga orgánica (separación física de sólidos)|
|Químico|Aguas con colorantes|



Página 34 de 46 

_BT1211 — Guía de Estudio Control 2_ 

|**Tipo de tratamiento**|**Aplicación típica**|
|---|---|
|Biológico — aerobio (lodos activados)|Aguas con alto contenido de amonio|
|Biológico — anaerobio (biogás)|Aguas y sólidos con alta carga orgánica, aguas con alto contenido de<br>fósforo|
|Térmico|Tratamientos de alta exigencia energética|



## _**Biolixiviación y biocorrosión**_ 

Biolixiviación: uso de bacterias para extraer metales (ej. cobre) desde minerales de baja ley. En Chile comenzó en 1970 en la planta Lo Aguirre, y se ha implementado en operaciones como Escondida, Spence, Cerro Colorado, Quebrada Blanca, Zaldívar y Radomiro Tomic. 

## _**Empresas biotecnológicas chilenas (ejemplos por sector)**_ 

|**Sector**|**Aplicaciones típicas observadas**|
|---|---|
|Salud humana|Terapia celular avanzada (osteoartritis, regeneración de tejido); hemocianina del loco<br>chileno como inmunoestimulante para vacunas; proteínas recombinantes humanas (ej.<br>TGF-β); enzimas recombinantes para detección de patógenos/drogas|
|Salud veterinaria|Bacteriófagos como alternativa a antibióticos en ganadería/acuicultura; proteínas<br>recombinantes para inmunidad en peces; vacunas veterinarias (salmón, mascotas)|
|Biomateriales|Textiles a base de micelio de hongos (alternativa al cuero); empaques biodegradables<br>con biopolímeros; films compostables|
|Agroindustria|Bioestimulantes y bactericidas de origen biológico; biofertilizantes a base de hongos|
|Alimentos|Mioglobina bovina recombinante (sabor a carne en productos vegetales); carne<br>cultivada; probióticos; bioingredientes por fermentación|



## **6.6 Síntesis — Sección Industria** 

- Ingeniería genética: gen de interés + vector + huésped → transformación → expresión → purificación. 

- Química verde: minimizar toxicidad y residuos en todo el ciclo de vida del producto; preferir catalizadores y eficiencia energética. 

- Bioprocesos: uso de enzimas y microorganismos para producción industrial y tratamiento de residuos, con ventajas (especificidad, condiciones suaves) y desventajas (costo, estabilidad) bien definidas. 

Página 35 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **7. Biomimética** 

La biomimética es una ciencia que estudia los modelos de la naturaleza y luego los imita o se inspira en sus diseños y procesos para resolver problemas humanos. 

## **7.1 Principios de la vida (marco de diseño biomimético)** 

Siete principios que orientan un diseño verdaderamente biomimético, más allá de solo copiar una forma: 

- Optimizar en lugar de maximizar. 

- Usar la energía libre (ej. solar, gradientes naturales). 

- Aceptar la diversidad. 

- Adaptarse y evolucionar. 

- Usar procesos amigables para la vida. 

- Usar materiales amigables para la vida. 

- Entablar relaciones simbióticas y mejorar la biosfera. 

## **7.2 Niveles y escalas de aplicación y abstracción** 

Este es el marco analítico central de la biomimética, evaluado de forma recurrente en los controles. Permite clasificar cualquier innovación bioinspirada según tres ejes independientes: 

_**Nivel de Aplicación — 'El Qué' se imita**_ 

|**Nivel**|**Definición**|
|---|---|
|Forma|Aspecto visible o configuración en 3D que conforma algo: estructuras y patrones|
|Proceso|Sucesión de pasos para alcanzar un resultado particular: reacciones químicas, traspaso<br>de información o comportamientos|
|Sistema|Relaciones y/o configuraciones entre diferentes componentes que interactúan y realizan<br>una tarea en conjunto|



## _**Escala de Aplicación — 'El Tamaño' al que se imita**_ 

|**Escala**|**Definición**|
|---|---|
|Micro|Pequeña escala en relación al tamaño donde actúa el principio biológico original|
|Meso|Escala intermedia: similar al tamaño donde actúa el principio biológico original|
|Macro|Gran escala en relación al tamaño donde actúa el principio biológico original|



Página 36 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## _**Nivel de Abstracción — 'El Cómo' se imita**_ 

|**Nivel**|**Definición**|
|---|---|
|Literal|Intentar emular el principio biológico de manera fidedigna respecto a su función,<br>elementos y propiedades (copia física exacta)|
|Metafórico|Abstraer el concepto del principio biológico para aplicarlo a un nivel superior de<br>conceptualización (inspiración conceptual)|
|📝**Pregunta de control — Permacultura / cultivo de cereales perennes (Control 2024, P3)**<br>Nivel de aplicación: Sistema — se imita cómo interactúan distintas plantas entre sí para beneficiarse<br>mutuamente (relaciones de policultivo), no solo su forma individual.<br>Escala de aplicación: Meso — se aplica en la misma escala (de campo/cultivo) en que ocurre el<br>fenómeno natural que se está imitando.<br>Nivel de abstracción: Literal — se emula de forma directa el mecanismo natural de interacción entre<br>plantas para mejorar los cultivos, sin abstraerlo a otro dominio.||



## **7.3 Ejemplos clásicos de biomimética** 

|**Tecnología**|**Bio-modelo**|**Mecanismo natural**|**Aplicación humana**|
|---|---|---|---|
|Velcro|Flores de cardo<br>(semillas)|Diminutos ganchos elásticos que se<br>entrelazan reversiblemente con<br>fibras suaves|Sistema de sujeción inventado<br>por George de Mestral (1948);<br>usado por la NASA desde 1972|
|Pintura<br>autolimpiante|Flor de loto|Superficie hidrofóbica con<br>microestructuras: el agua no fluye,<br>rueda, arrastrando partículas y<br>bacterias|Pinturas de exteriores y ropa<br>repelente al agua (efecto loto)|
|Tren bala<br>(Shinkansen)|Martín pescador<br>(Alcedo atthis)|Evolución morfológica del pico para<br>reducir fricción al pasar de aire<br>(baja densidad) a agua (alta<br>densidad)|Rediseño de la cabina del tren;<br>reduce ruido al salir de túneles,<br>ahorra ~15% energía y 10% más<br>rápido|
|Auto bioinspirado<br>(Bionic Car)|Pez cofre|Diseño aerodinámico con<br>exoesqueleto rígido pero de peso<br>extremadamente ligero|Vehículo conceptual de<br>Mercedes-Benz, menor<br>coeficiente de arrastre con mayor<br>volumen interno|
|Producción de<br>fibras (Spintex)|Seda de araña|Capacidad de hilar fibra estructural<br>a temperatura ambiente desde un<br>gel líquido proteico|Proceso textil ~1000 veces más<br>eficiente energéticamente que<br>fibras sintéticas derivadas del<br>petróleo|
|Climatización pasiva<br>(Eastgate Centre)|Montículos de<br>termitas africanas|Las termitas mantienen 30 °C<br>constantes mediante conductos de<br>ventilación pasiva (efecto<br>chimenea)|Edificio en Harare (Zimbabwe) sin<br>aire acondicionado tradicional;<br>ahorra ~35% de energía|



Página 37 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **7.4 Caso ilustrativo detallado — Termitero y Eastgate Centre** 

Las termitas cultivan hongos como alimento, los cuales requieren una temperatura constante de 30 °C incluso en desiertos extremos. Logran esto mediante una chimenea central termodinámica, masa térmica y túneles subterráneos que generan un efecto chimenea: entrada de aire fresco por la base, ascenso y extracción de aire caliente por la parte superior. 

El edificio Eastgate Centre replica esta lógica: oficinas alrededor de un atrio central que actúa como la chimenea termodinámica, con entrada de aire fresco en la base y extracción de aire caliente arriba — logrando climatización completamente pasiva. 

## **7.5 Cómo responder preguntas de biomimética en el control** 

Estructura recomendada para analizar cualquier ejemplo de biomimética que aparezca en el control (aunque sea nuevo / no visto en clase): 

- 12.Identificar el bio-modelo: ¿qué organismo o fenómeno natural inspira la tecnología? 

- 13.Identificar el mecanismo: ¿qué principio físico/biológico específico hace que funcione en la naturaleza? 

- 14.Clasificar el nivel de aplicación: ¿se imita una Forma, un Proceso o un Sistema completo? 

- 15.Clasificar la escala: ¿Micro, Meso o Macro, en relación al tamaño del fenómeno natural original? 

- 16.Clasificar el nivel de abstracción: ¿es una copia Literal o una inspiración Metafórica? 

- 17.Conectar con la aplicación humana y su impacto medible (eficiencia, ahorro, nueva funcionalidad). 

## **7.6 Estrategias adaptativas naturales (banco de ejemplos — Actividad 4)** 

Estas estrategias de adaptación de la naturaleza fueron usadas como base para diseñar innovaciones bioinspiradas en la actividad de clases; sirven como banco de ejemplos para practicar la clasificación de niveles/escalas/abstracción: 

- Chinche de calabazas: mecanismo de riel en las alas, fijación móvil resistente pero de fácil liberación durante el vuelo. 

- Búho excavador: usa estiércol como señuelo para atraer escarabajos peloteros y cazarlos. 

- Hormigas: reglas simples (feromonas) que coordinan comportamientos colectivos complejos ('carreteras' señalizadas). 

- Hojas caducas: reabsorción selectiva de compuestos energéticos antes de la caída estacional de hojas. 

- Conos de pino: liberación de semillas controlada por curvatura diferencial de capas ante la humedad. 

- Pepino de mar: rigidez variable de la piel mediante proteínas entrelazables, como defensa ante amenazas. 

Página 38 de 46 

_BT1211 — Guía de Estudio Control 2_ 

- Red trófica terrestre: mayor cantidad de componentes en el sistema aumenta su resiliencia. 

- Estomas de las hojas: 'válvulas' biológicas sensibles a luz/temperatura/humedad para regular intercambio de gases. 

- Gusano de sangre: 'dientes' con punta dura y base flexible, que reduce puntos débiles estructurales al enterrarse. 

- Rana de árbol: microestructuras hexagonales en los dedos que aumentan la fuerza de cohesión sobre superficies lisas. 

- Escarabajo blanco: escamas con desorden molecular que dispersan luz visible, generando blanco brillante sin pigmento. 

- Mosquito: piezas bucales especializadas y diferenciadas por sexo según función (alimentación de sangre vs. néctar). 

- Pavo real: dimorfismo sexual — cola vistosa en el macho (atracción de pareja) vs. plumaje discreto en la hembra (camuflaje/protección de crías). 

Página 39 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## **8. Banco de Práctica — Controles Anteriores Completos** 

Esta sección resume, pregunta por pregunta, los tres controles disponibles (2023, 2024, 2025), indicando el tema y la idea clave de la respuesta esperada. Úsala para practicar: tapa la columna 'Idea clave de la respuesta' e intenta responder primero por tu cuenta. 

## **8.1 Control 2025 (7 de julio de 2025)** 

## _**Pregunta 1 — Modelo de empresas P/M/G (Modelos matemáticos)**_ 

- Tema: balance de masa para 3 poblaciones interactuantes (empresas pequeñas, medianas, grandes), con crecimiento propio y absorción mutua. 

- Variables de estado: cantidad de empresas P, M y G. 

- Idea clave: cada término del enunciado (crecimiento, absorción, cierre) se traduce literalmente en un término del balance dP/dt, dM/dt, dG/dt — lo que 'sale' de una población por absorción es justo lo que 'entra' (ponderado) a la población que absorbe. 

- Consecuencia de αPG muy alto: reduce drásticamente P, lo que reduce disponibilidad para crecimiento de M y G, llevando a un nuevo equilibrio o a extinción de las 3 poblaciones, según las magnitudes relativas de las constantes. 

## _**Pregunta 2 — Heterotermia regional en gaviotas (Transporte de calor)**_ 

- Tema: mecanismos de transferencia de calor (conducción y convección) en el sistema circulatorio a contracorriente de las patas de aves. 

- Factores biológicos vs. no biológicos que afectan la transferencia de calor: ver sección 3.9 de esta guía. 

- Idea clave: la mayor ramificación vascular en los dedos aumenta el área de transferencia; el contacto extenso entre arteria y vena permite igualar temperaturas progresivamente, evitando que la sangre fría enfríe el cuerpo. 

## _**Pregunta 3 — Máquinas dispensadoras de combustible (Estadística)**_ 

- Tema: diferencia de medias, desviación estándar, test de hipótesis, errores tipo I/II, covarianza y correlación vs. causalidad. 

- Ver desarrollo completo en sección 5 de esta guía (5.4, 5.5, 5.6). 

## _**Pregunta 4 — Dializador (Transporte de masa)**_ 

- Tema: balance de masa de urea en los compartimentos sangre (S) y dializado (D), estado estacionario, cálculo numérico de F. 

- Ver desarrollo completo en sección 3.7 de esta guía. F = 225 g/min para los datos dados. 

Página 40 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## _**Pregunta 5 — Brazo protésico (Sistemas de control)**_ 

- Tema: lazo cerrado con retroalimentación negativa, control adaptativo, componentes del sistema de control. 

- Ver desarrollo completo en sección 2.7 de esta guía. 

## **8.2 Control 2024 (8 de julio de 2024)** 

## _**Pregunta 1 — Planta de lavado de botellas reutilizables (Sistemas de control)**_ 

- Lazo abierto (tiempo/presión fijos) → ventajas/desventajas. 

- Posible bioproducto: incorporar enzimas para reducir uso de detergentes. 

- Sistema mejorado con sensor de suciedad: lazo cerrado, feedback negativo, en cada etapa. 

- Componentes: proceso, set-point, sensor, controlador, actuador, línea de transmisión. 

- 3 desafíos: precisión/sensibilidad del sensor, fallas del actuador, suciedad no detectable, variabilidad de entrada (perturbaciones), limitaciones de suministro de agua/detergente. 

- Ver desarrollo completo en sección 2.7 de esta guía. 

## _**Pregunta 2 — Adicción al tabaco / nicotina (Sistemas de control)**_ 

- Tipo de retroalimentación: positiva — el consumo de nicotina produce placer y aumenta el número de receptores, lo que aumenta el deseo de fumar (se autoamplifica). 

- Sistema circulatorio = sistema de comunicación: transporta la señal (nicotina) desde los pulmones al cerebro. 

- Receptores nicotínicos = sensores (detectan la presencia de nicotina) — también aceptable como controlador, según el razonamiento del estudiante. 

## _**Pregunta 3 — Permacultura / cultivo de cereales perennes (Biomimética)**_ 

- Nivel de aplicación: Sistema. Escala: Meso. Nivel de abstracción: Literal. 

- Ver desarrollo completo en sección 7.2 de esta guía. 

## _**Pregunta 4 — Vindolina / biosíntesis de fármacos anticancerígenos (Ingeniería genética + Química verde)**_ 

- Proceso alternativo de producción: clonar los genes de las enzimas E1, E2, E3 en un hospedero (ej. levadura) o generar una planta transgénica — requiere identificar genes, vector y señales de expresión. 

- Ventajas frente a extracción tradicional: mayor rendimiento, evita uso intensivo de la planta silvestre. 

- Síntesis química alternativa (altas P/T, sin catalizador, desechos ácidos) incumple principios de química verde: prevención de la contaminación / manejo de desechos, y uso eficiente de la energía. 

Página 41 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## _**Pregunta 5 — Llenado automático de piscinas (Sistemas de control + balance de masa)**_ 

- Sistema original (operario): lazo abierto. Sistema con sensor de profundidad: lazo cerrado. 

- Balance de masa con fuga: dm/dt = Fe(t) − Fs. La piscina pierde nivel si Fs > Fe(t). 

- A largo plazo: o se alcanza un nuevo estado estacionario (Fe = Fs), o el sistema de control ajusta Fe indefinidamente sin estabilizarse. 

- Ver desarrollo completo en sección 2.7 de esta guía. 

## _**Pregunta 6 — Coyotes y conejos (Modelos Lotka-Volterra)**_ 

- Variables de estado: Y (coyotes), X (conejos). 

- dY/dt = μY·Y·X − δY·Y    |    dX/dt = μX·X − δX·X − ρ·Y 

- Gráfico tras enfermedad en coyotes: caída de coyotes, seguida de aumento de conejos (menos depredación), seguida de recuperación de coyotes (más alimento disponible) — oscilación con desfase, igual que en el modelo Lotka-Volterra clásico. 

- Migración constante de conejos: nueva fuente de alimento para coyotes, se alcanza un nuevo equilibrio con más individuos de ambas poblaciones; se agrega un término de inmigración constante τ al balance de conejos. 

## _**Pregunta 7 — Industria textil y perspectiva de género (Tema transversal)**_ 

- Tema: cómo los roles y estereotipos de género se reflejan en la composición de una industria (ej. predominancia femenina en textil) y cómo los riesgos laborales (ej. exposición a tóxicos) tienen impactos diferenciados por sexo/género. 

- Estructura de respuesta esperada: (a) argumentar con datos del enunciado cómo se evidencian roles/estereotipos de género; (b) identificar al menos 2 consecuencias del impacto diferenciado por sexo, conectando salud + condición socioeconómica + roles domésticos; (c) identificar el tipo de transporte de masa (difusión vs. convección) y su fuerza motriz para cada vía de exposición (piel = difusión por gradiente de concentración; inhalación = convección por flujo de aire), y notar que ninguno de los dos requiere energía externa (van a favor de gradiente). 

- Este tipo de pregunta de 'impacto diferenciado por género' aparece de forma recurrente conectada a un tema técnico del curso (en Auxiliar 5 aparece también con contaminación por MTBE) — conviene tener preparada la estructura: estereotipos/roles observados → consecuencias diferenciadas → causa técnica de fondo. 

## **8.3 Control 2023 (8 de julio de 2023)** 

## _**Pregunta 1 — Piscina con algas y alguicida (Balance de masa)**_ 

- Balance: d(masa de algas)/dt = V·k1·Ca − k2·Ca·Cx (crecimiento proporcional a Ca, eliminación proporcional al producto Ca·Cx). 

Página 42 de 46 

_BT1211 — Guía de Estudio Control 2_ 

- Condición para que las algas disminuyan: Cx > k1/k2 — esto permite calcular la concentración mínima de alguicida a comprar. 

- Si se considera evaporación: se necesita un balance adicional para el agua (acumulación de agua = − Qevap), que modificaría el volumen V del modelo original. 

- Si el alguicida se descompone (velocidad ∝ Cx²): eventualmente Cx podría bajar lo suficiente para que el balance se invierta y las algas vuelvan a crecer — la condición de la parte (b) dejaría de cumplirse en el tiempo. 

## _**Pregunta 2 — Catalizador con eficiencia promedio (Estadística)**_ 

- El promedio (10% de aumento) es insuficiente sin la desviación estándar — alta dispersión implica resultados poco fiables/replicables, lo que pone en riesgo la operación si se decide cambiar el catalizador. 

- Ver desarrollo completo en sección 5.4 de esta guía. 

## _**Pregunta 3 — Transporte de etanol (Transporte de masa)**_ 

- Transporte en sangre: convección (arrastrado por el flujo sanguíneo); factores: velocidad del flujo, viscosidad, diámetro del vaso, temperatura. 

- Fuerza motriz hacia el hepatocito: gradiente de concentración (mayor en el extracelular/sangre que en el citoplasma). 

- Mecanismos a través de la membrana: difusión simple (molécula pequeña y lipofílica) y transporte facilitado mediante transportadores específicos. 

- No se requiere energía: el etanol se mueve a favor de su gradiente de concentración (de mayor a menor). 

## _**Pregunta 4 — Productividad de un bosque (Energía / ecología)**_ 

- Unidades de productividad bruta: energía (o biomasa) por área por año. 

- La productividad bruta disminuye al madurar el bosque por mayor sombra/competencia por luz, reduciendo la fotosíntesis neta disponible. 

- Aumento de biomasa en los primeros años: mayor disponibilidad de nutrientes y luz, condiciones menos hostiles, aumento de diversidad de especies. 

- Productividad neta = productividad bruta − pérdida respiratoria; el incremento lento de biomasa después de 100 años refleja que la productividad neta se acerca a cero (la fotosíntesis apenas compensa la respiración). 

- Para predecir si los ciervos (consumidores secundarios) sobreviven: se necesita la productividad neta del nivel trófico anterior y los requerimientos metabólicos/energéticos de los ciervos para crecimiento y reproducción. 

Página 43 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## _**Pregunta 5 — Ducha con regulación manual remota (Sistemas de control)**_ 

- Componentes: controlador = cerebro de la persona en la ducha; actuador = el pariente que ajusta el calefont; proceso = la ducha; sensor = percepción de temperatura; comunicación = la voz. 

- Lazo cerrado, feedback negativo: se busca mantener la temperatura dentro de un rango, oponiéndose a perturbaciones. 

- Cambiar la comunicación a llamada telefónica no altera la estructura del sistema, solo el canal de comunicación. 

- Ver desarrollo completo en sección 2.7 de esta guía. 

## _**Pregunta 6 — Dinosaurios y relación superficie/volumen (Energía / transferencia de calor)**_ 

- La pérdida de calor depende de la superficie; la generación depende del volumen. 

- Razón pérdida:generación ∝ 1/r — un animal grande pierde proporcionalmente menos calor que uno pequeño. 

- Ventaja evolutiva de temperatura intermedia en dinosaurios: poca pérdida relativa de calor (ventaja de tamaño grande) combinada con metabolismo más activo que un reptil de sangre fría. 

- Ver desarrollo completo en sección 4.9 de esta guía. 

## **8.4 Preguntas tipo de las actividades y auxiliares (no evaluadas aún, pero del mismo estilo)** 

## _**Apocalipsis zombie (Actividad 6) — Modelos con 3 poblaciones**_ 

- H (humanos), Z (zombies), M (muertos): dH/dt = Π − δ·H − β·H·Z;  dZ/dt = β·H·Z + γ·M − α·H·Z; dM/dt = δ·H + α·H·Z − γ·M (estructura general; revisar signos según el balance que se plantee con cada estrategia). 

- Idea clave: cada 'tasa proporcional a X·Y' representa un término de interacción (como en Lotka-Volterra); las estrategias (aislar zombies, destruir cadáveres) se modelan agregando o quitando términos/constantes que reducen una tasa de conversión específica. 

## _**Ley de control proporcional vs. constante (Actividad 6) — Ducha automática**_ 

- Ley proporcional (m = K·e): la apertura de la válvula responde de forma gradual y proporcional al error — a mayor diferencia de temperatura, mayor corrección, acercándose suavemente al set-point. 

- Ley de control constante (on/off): la válvula se abre o cierra a un valor fijo según el signo del error, sin gradualidad — más parecido a un termostato simple que oscila alrededor del set-point en vez de converger suavemente. 

- La ley proporcional es más similar al control humano real (ajustamos la llave 'más o menos' según qué tan fría/caliente sentimos el agua, no en saltos bruscos). 

Página 44 de 46 

_BT1211 — Guía de Estudio Control 2_ 

## _**Epidemia SIR (Actividad 6) — Modelo Susceptibles-Infectados**_ 

- Variables de estado: S (susceptibles), I (infectados); espacio de estados: pares (S, I) con S + I = N constante (sistema cerrado, cuarentena). 

- Balance: dS/dt = −β·S·I;  dI/dt = β·S·I (sin cura) — los infectados crecen mientras haya susceptibles, acotados por N. 

- Con cura (tasa γ proporcional a I), aparece una tercera población R (recuperados): dI/dt = β·S·I − γ·I;  dR/dt = γ·I — este es el modelo SIR clásico de epidemiología. 

## _**Piscinas de tratamiento de residuos líquidos (Actividad 5) — Transporte**_ 

- Entidades transportadas por la tubería: agua, metales pesados, contaminantes orgánicos, calor (energía térmica). 

- El balance de masa para metales pesados en la piscina 2 cambia completamente entre el escenario sin desperfecto (M1 ≈ 0, término de entrada de metales nulo) y con desperfecto (entra una corriente con M1 = 0.85·M0 ≠ 0). 

- Gradiente que impulsa el transporte en la tubería entre piscinas: diferencia de altura (presión hidrostática, ya que la piscina 2 está 20 m más abajo) — transporte espontáneo, no requiere energía externa. 

- Hagen-Poiseuille: para reducir el flujo de agua contaminada hacia la piscina 2, es más efectivo reducir el diámetro de la tubería que aumentar su largo (Q ∝ D⁴, pero Q ∝ 1/L) — ver sección 3.8. 

## **8.5 Checklist final antes del control** 

- ¿Puedo identificar variables de estado y plantear un balance ENTRA − SALE + GENERA − CONSUME = ACUMULA para cualquier sistema descrito en palabras? 

- ¿Puedo distinguir lazo abierto de lazo cerrado, y feedback positivo de negativo, en cualquier ejemplo (biológico o de ingeniería)? 

- ¿Puedo nombrar los 5-6 componentes de un sistema de control (sensor, controlador, actuador, proceso, comunicación, perturbación, set-point) en un caso nuevo? 

- ¿Sé diferenciar difusión de convección, y identificar la fuerza motriz correcta (gradiente de concentración vs. presión/densidad) en cada caso? 

- ¿Puedo aplicar la Ley de Fick y Hagen-Poiseuille y razonar cualitativamente sus dependencias (área, distancia, diámetro)? 

- ¿Entiendo por qué la pérdida de calor depende de superficie y la generación de volumen, y sé aplicar esto a preguntas de tamaño corporal? 

- ¿Sé por qué un promedio solo no basta, y qué aporta la desviación estándar / mediana en cada caso? 

- ¿Sé diferenciar error tipo I de error tipo II en un contexto aplicado? 

- ¿Puedo clasificar un ejemplo de biomimética en nivel de aplicación / escala / nivel de abstracción? 

Página 45 de 46 

_BT1211 — Guía de Estudio Control 2_ 

- ¿Recuerdo los pasos de la ingeniería genética (gen, vector, huésped, transformación, expresión) y puedo aplicarlos a un caso nuevo? 

- ¿Puedo razonar el impacto diferenciado por género/sexo/edad/nivel socioeconómico cuando el enunciado lo pide, conectándolo con el contenido técnico de la pregunta? 

## **¡Éxito en el control!** 🎓 

Página 46 de 46 


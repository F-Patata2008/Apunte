Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

## Evaluación Principal 2 

## _8 de julio de 2024_ 

## _**Indicaciones**_ 

_Todas las preguntas deben responderse en el espacio entregado para ello, con respuestas personales y de elaboración propia. Respuestas fuera del espacio permitido o de largo mayor al solicitado no serán tenidas en cuenta para la corrección. No se admitirán respuestas en hojas adicionales. Por esto mismo, por favor, piense y medite su respuesta antes de empezar a escribir y pregúntese qué es lo que quiere decir y cómo lo va a redactar en el espacio permitido._ _**Sólo se permiten dudas de enunciado** y no se aceptarán preguntas durante los primeros 30 minutos del desarrollo de esta evaluación. Si es necesario tomar un supuesto para contestar una pregunta, por favor incorpore su supuesto en la respuesta. Por favor, cuide su ortografía, la coherencia y cohesión de sus respuestas y trate de ser concisa/o en sus desarrollos. Estos aspectos se considerarán al momento de la evaluación. Tome en consideración como guía el tiempo de desarrollo asignado a cada una, según se indica. El tiempo total estimado para el desarrollo de esta evaluación es de 165 minutos. Todas las preguntas tienen la misma ponderación en la nota final, y el puntaje correspondiente de cada pregunta se distribuye entre cada sección y entre cada subsección tal como se indica, en caso de que haya distintas secciones._ 

## **Pregunta 1 (30 minutos)** 

Una embotelladora de bebidas carbonatadas instala una planta de lavado y sanitización de envases reutilizables, en miras a reducir e idealmente eliminar la comercialización de envases desechables con sus productos. 

En la planta reciben los envases provenientes de centros de recepción y acopio en supermercados, se retiran las tapas, clasifican por tamaño, e ingresan a un proceso de lavado de 3 etapas, cada una con una duración predefinida según tamaño del envase: i) eliminación de sólidos externos, remojo y lavado externo con solución detergente, ii) lavado interno con solución detergente en sistema de inyección individual, iii) enjuague final. Luego pasan a una etapa de secado y sanitización como se ilustra en la figura, y se ingresan a la sección de envasado. En el diseño actual las botellas ingresan, se lavan en cada etapa según un tiempo y con presión de lavado preestablecidos. 

_**Figura 1:** Proceso de ingreso, lavado y sanitización de botellas para reutilización en envasado_ 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

- a) Indique a qué tipo de estructura de control corresponde este diseño de proceso y discuta respecto a posibles ventajas y desventajas de este (al menos una en cada caso) (1 pto). 

- b) ¿Sería posible incorporar a este proceso algún bioproducto para mejorar su desempeño o reducir su impacto en el entorno? Explique y argumente en detalle (0.5 ptos). 

Si fuese posible implementar en un sistema que permita monitorear el nivel de suciedad de las botellas al entrar a cada etapa, y durante el proceso mismo de lavado en cada etapa, y considerando esto usted fuese a implementar un sistema de control con retroalimentación para este proceso, indique: 

- c)  ¿Cuál sería el objetivo que tendría su sistema de control? (0.5 ptos) 

- d) ¿Qué tipo de retroalimentación debería usar el sistema de control? ¿En una sola etapa o en más de una? Explique por qué (1 pto) 

- e) ¿Cuáles son los componentes que conforman su sistema de control, y que rol tiene cada uno? (2 ptos) 

- f) Explique 3 problemas o desafíos que podría enfrentar este sistema de control (1 pto) 

a) La estructura actual corresponde a un sistema de lazo abierto (0.5 pt). 

Desventajas: Este sistema es fijo para todas las botellas independiente de la suciedad de estas, y por ende no permite responder a perturbaciones en el proceso o variaciones en el nivel de suciedad de las botellas; Sólo funcionaría adecuadamente si se trabajara bajo el supuesto de que todas las botellas traen el máximo de suciedad, lo que sería ineficiente en uso de recursos. Ventajas: al no requerir de instrumentación adicional (sensores de suciedad) su implementación es menos costosa y más sencilla (0.5 pt). 

b) Se podrían incorporar enzimas en el proceso para reducir el uso de detergentes (0.5 pt). 

c) El objetivo de este sistema de control es asegurar el nivel de limpieza de las botellas a la salida del sistema de lavado (0.5 pt). 

d) Debe ser un sistema de lazo cerrado en cada una de las etapas de lavado (0.5 pt), de feedback negativo (0.5 pt) ya que es necesario que cada etapa de lavado cumpla con el nivel requerido de limpieza, independiente de la suciedad con las que ingresan las botellas. 

## e) 

1. Proceso: los mecanismos de enjuague, lavado y desinfección que permiten obtener 

botellas limpias a la salida, adecuadas para ingreso a la sección de envasado. 

2. Set-point/referencia: Valor de limpieza definido como estándar mínimo aceptable que permite ingreso de la botella a la siguiente etapa de lavado o a envasado. 

3. Sensor: Dispositivo que detecte el nivel de suciedad de la botella a la entrada y durante la etapa de lavado, para cada una de las etapas de lavado. 

4. Controlador: Dispositivo que recibe la señal de error (diferencia entre valor de limpieza observado en la etapa y valor definido como estándar mínimo aceptable de la etapa) y que determina ajustes a la etapa (tiempo de lavado, presión de agua, cantidad de detergente, etc). 

5. Actuador: Es el componente que lleva a cabo la función indicada por el controlador. En este caso, sería el equipo de lavado, o el componente de hidrolavado. 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

6. Líneas de transmisión: conjunto de cables, señales inalámbricas, etc. que permiten que las señales se compartan entre los distintos componentes del sistema de control. (2 pt) 

f) 

• Problemas asociados al sensor, tales como el que la precisión, sensibilidad o resolución no sean las adecuadas para el problema. 

• Problemas asociados al actuador, por ejemplo que deje de funcionar o que no disponga de suficiente agua, o detergente, etc para utilizar. 

• Problemas asociados a la incapacidad de remover suciedad de alguna característica. Por ejemplo, si la botella se usara para almacenar combustible o solventes, o pintura, Y fuese imposible para el sistema declararla limpia. 

• La presencia de suciedad no detectable por los sensores. 

• El sistema de control tendría que ser capaz de enfrentar los desafíos que establecería el ingreso de botellas con distintos niveles de suciedad, que actuarían como perturbaciones. 

• Dificultades técnicas en el diseño e implementación del sistema como por ejemplo, la disponibilidad y presión de agua desde la red, disponibilidad y calidad de detergentes, etc. 

• El sistema sólo podría actuar cuando los niveles de suciedad en las botellas son tales que su nivel de limpieza está por debajo del nivel de referencia. Cuando las botellas vienen limpias, solo las avanzaría al siguiente nivel. 

(1 pt) 

## **Pregunta 2 (25 minutos)** 

La adicción al tabaco es una enfermedad primaria del sistema nervioso central, con síntomas y signos característicos, en la que interaccionan de forma compleja factores biológicos, genéticos, psicológicos y sociales, produciendo un trastorno conductual crónico y que se caracteriza por llevar a la reincidencia; llevando a la dependencia y disminución del control sobre el consumo, siendo característica la compulsión al consumo de forma continuada. 

La nicotina es la sustancia del tabaco relacionada con la adicción. A pesar de ser una sustancia legal, es una droga con mayor poder adictivo que otras drogas ilícitas (heroína, cocaína, etc.). Esto se debe, en parte, a su rápido inicio de acción. Cuando el humo del cigarrillo ingresa en los pulmones, pasa al torrente sanguíneo y llega rápidamente al cerebro, de modo que la nicotina alcanza su nivel máximo a los 10 segundos de la inhalación. 

La nicotina se une de forma selectiva a receptores nicotínicos, que son receptores colinérgicos presentes por todo el organismo, principalmente receptores nicotínicos neuronales α4β2. El consumo continuo de nicotina provoca aumento del número de receptores nicotínicos y perpetúa la adicción. 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

Se han localizado en el cerebro los receptores para la mayoría de drogas de abuso y los neurotransmisores asociados a ellos. A través de la vía dopaminérgica o «vía de la recompensa», la nicotina activa receptores del área tegmental ventral que proyectan sus axones hacia el núcleo 

accumbens, estimulando la liberación de dopamina y produciendo sensación de placer y de felicidad. 

Texto tomado de https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10369620/ Con respecto a este texto conteste las siguientes preguntas: 

a)    ¿Qué tipo de lazo de retroalimentación se describe en el texto: positivo o negativo? Explique. (2.0 puntos) 

b)  ¿A qué parte general de un sistema de control corresponde el sistema circulatorio en este caso? Explique. (2.0 puntos) 

c)  ¿A qué parte general de un sistema de control corresponden los receptores nicotínicos? Explique. (2.0 puntos) 

## _**(Respuesta en 15 líneas máximo en el siguiente espacio)**_ 

- a) Corresponde a un ciclo de retroalimentación positiva [1.0 pt]. El consumo de nicotina produce placer y aumento de receptores nicotínicos lo que se traduce en un aumento del deseo de fumar [1.0 pt]. 

- b) El sistema circulatorio corresponde al sistema de comunicación [1.0 pt] ya que permite el viaje de la señal de nicotina desde los pulmones hasta el cerebro[1.0 pt]. 

- c) Los receptores nicotínicos corresponden a los sensores de la molécula de nicotina en nuestro organismo y que dan cuenta de la presencia de la nicotina en el torrente sanguíneo.  Los estudiantes tambien pueden indicar que se trata del controlador. [2.0 pt]. 

## **Pregunta 3 (20 minutos)** 

Las grandes praderas naturales parecen estar en constante equilibrio, sin embargo, no es así, ya que siempre están en un estado continuo de perturbación y cambio. Las prácticas agrícolas industriales actuales están abusando de los recursos y utilizando productos químicos tóxicos a gran escala. Un instituto en Estados Unidos desarrolló un método llamado cultivo de cereales perennes o permacultura, en que se utilizan policultivos y cultivos cooperativos. En vez del monocultivo extensivo, se trata de combinar la plantación de diversas verduras y hortalizas en las condiciones más adecuadas para cada lugar. Estos sistemas que imitan la naturaleza requieren sustancialmente menos agua de riego, previenen la erosión del suelo, tienen resistencia incorporada a las plagas y mejoran la salud de las plantas. 

a)   ¿A qué nivel de aplicación cree usted que corresponde este ejemplo? Justifique su respuesta (2 ptos). 

b)   ¿A qué escala de aplicación corresponde? Justifique su respuesta (2 ptos). 

c)   ¿A qué nivel de abstracción corresponde? Justifique su respuesta (2 ptos). 

## _**(Respuesta en 15 líneas máximo en el siguiente espacio)**_ 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

a) De sistema: está imitándose el ecosistema de las praderas naturales, o sea como las diversas plantas interactúan entre sí para beneficiarse unas de 

otras. (2 ptos) 

b) Meso, se aplicará en la misma escala que la situación natural. (2 ptos) c) Literal  Emula de forma literal el mecanismo natural de interacciones de plantas para cumplir la función de mejorar los cultivos. (2 ptos) 

## **Pregunta 4 (15 minutos)** 

Vindolina (Figura 2a) es un alcaloide indol aislado de las hojas de la planta _Catharanthus roseus_ . La vindolina es el punto de partida en la biosíntesis de vinblastina y vincristina, dos importantes fármacos anticancerígenos. Se sabe que, en la planta, la vindolina es sintetizada naturalmente por una ruta metabólica en la cual un compuesto químico precursor (P) es convertido sucesivamente en los intermediarios I1, I2 y finalmente en vindolina, por tres enzimas denominadas E1, E2 y E3 (ver esquema de la ruta en la Figura 2b). Tradicionalmente la vindolina se ha producido por extracción de hojas de la planta. Se busca formas alternativas de producción. 

**Figura 2** : a) Estructura de Vindolina. b) Ruta de síntesis de Vindolina en la planta _Catharanthus roseus_ . P = Precursor; I = Intermediario; E = Enzima. 

a)   Proponga un proceso alternativo de producción de vindolina basado en el uso de las herramientas de ingeniería genética vistas en clase (3 ptos). 

b)   Explique al menos dos ventajas que podría tener este nuevo proceso comparado con el método tradicional en que la vindolina es extraída desde las hojas de C. roseus (1,5 ptos). 

c)   Suponga que investigadores de otro laboratorio reportan un método alternativo para la generación de vindolina, basado en síntesis química. En este método se usan altas presiones y temperaturas para la síntesis, sin intervención de catalizadores y desde una etapa de la síntesis se producen desechos ácidos. Discuta dos condiciones de la química verde que pudieran no cumplirse en este proceso químico, justificando su respuesta (1,5 ptos). 

## _**(Respuesta en 25 líneas máximo en el siguiente espacio)**_ 

a. Clonación de los genes (información codificante) de las enzimas en un hospedero como levadura. También podrían proponer una planta transgénica que pudiera producir el compuesto. Deben poder relacionar la información de las enzimas con información genética, saber que los genes son los que deben introducirse en el nuevo hospedero, deben usar un vector que permita la expresión (señales de expresión). (3 ptos) 

b. Dos ventajas: Mayor rendimiento en la producción de vindolina y evitar el uso intensivo de la planta para la extracción.(1,5 ptos) 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

c. 1: Prevención de la contaminación y correcto uso de los desechos   6: uso eficiente de la energía; 9: Masificar el uso de catalizadores. (1,5 ptos) 

## **Pregunta 5 (35 minutos)** 

Usted tomó un trabajo de medio tiempo como consultor y asesor en una empresa que se dedica a la construcción de piscinas. Dentro de los servicios que ofrece la empresa, esta cuenta con un 

servicio ultra rápido donde construyen y dejan lista con agua una piscina en tan solo 48 horas!. Para ayudar en este proceso, cuentan con una manguera de gran diámetro que permite llenar una piscina de tamaño estándar (10m[3] ) en periodos muy cortos. 

Originalmente, el sistema de llenado de piscina funcionaba con un operador, quien, solo con conocimiento empírico del proceso, iba regulando el flujo de la válvula manualmente para lograr un llenado óptimo. Pero, generalmente, la válvula de la manguera queda a gran distancia de la piscina, por lo cual el operador no era capaz de ver el llenado de la piscina desde la válvula de la manguera, valiéndose solo de su conocimiento y años de experiencia para saber cuándo y cómo regular el flujo de la válvula. Esto se hacía particularmente difícil en la última parte del llenado de la piscina, donde el control debe ser muy preciso, lo cual implicaba una pérdida de tiempo para su servicio ultra rápido. 

Ud. decide que lo mejor para evitar este problema y optimizar la situación, es instalar un controlador que actúa sobre la válvula de la manguera para regular el flujo de esta, junto a un sensor de profundidad que permita medir el nivel de agua de la piscina en el tiempo, automatizando el proceso. Al respecto: 

a) El sistema original de llenado de la piscina: ¿A qué tipo de sistema de control corresponde? Explique. (1 pto) 

b) El nuevo sistema que ud. instaló: ¿A qué tipo de sistema de control corresponde? ¿Qué ventajas ofrece respecto al anterior? Detalle. (1 pto) 

La empresa implementó con éxito su sistema automático de llenado de piscinas. Lamentablemente, en una de las construcciones de piscina ocurrió un error en la pintura aislante en una esquina de las escaleras sumergidas que permiten entrar a la piscina. Esto provocó que la piscina quede con una fuga de flujo Fs, constante. Asumiendo además que el flujo que da su manguera de llenado es  Fe(t), el cual varía en el tiempo dependiendo de su sistema de control: 

c) Dibuje un esquema simplificado de la situación en que se encuentra la piscina con fuga mientras se llena. Plantee el balance de masa del agua (sin resolverlo) de su sistema, considerando los bordes de la piscina como su volumen de control. En base a su balance de masa: ¿Qué condición se debe cumplir para que la piscina disminuya su nivel de agua? (2 ptos.) 

d) Considerando el sistema con fuga y su sistema de control: ¿Qué va a ocurrir luego de un tiempo largo? ¿En qué condición va a quedar la piscina? Explique. (2 ptos.) 

_**(Respuesta en 30 líneas máximo en el siguiente espacio)**_ 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

1. El sistema de control original que estaba implementando en el sistema de llenado de piscinas corresponde a un lazo abierto, donde no hay un controlador como tal que reciba información de un sensor si no que el operario con conocimiento empírico sabía en qué tiempos aproximados ir cerrando la válvula. 

2.    El nuevo sistema de control corresponde a un lazo cerrado, dado que se incorporó con éxito un controlador, que recibe información del sensor de profundidad y con esta el controlador actúa sobre la válvula (actuador) para regular el flujo de agua. Este sistema trae múltiples ventajas como poder tener robustez ante alteraciones en el proceso (bajas de presión en la manguera, distintos tamaños de piscina) y ofrecer un control más preciso y rápido que con una contraparte humana. 

3. 

El balance de masa sería: 

No hay generación ni consumo de agua, solo entradas y salidas, con lo cual el balance queda: 

Acumulacion = Entrada - Salida 

dm/dt = Fe (t) - Fs  (1 pto) 

Para que la piscina pierda nivel (acumulación negativa) se tiene que cumplir que: Fs > Fe(t) (1 pto por el análisis de pérdida de nivel) 

4.     Dado que Fe  depende del tiempo dado que se irá regulando según la información que obtenga el controlador desde el sensor de profundidad, hay 2 posibles escenarios que pueden ocurrir: 

- a.     El sistema de control provoca que el flujo de entrada Fe  se iguale con el flujo de la grieta Fs, generando que la piscina quede en un estado estacionario en un volumen V (no llena, ni vacía) 

- b.       El sistema de control irá regulando el flujo de tal manera que en un punto Fe < Fs , lo cual provocará que la piscina empiece a perder nivel, lo cual eventualmente volverá a activar el sistema de control aumentando el flujo de 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

Fe, con lo cual la piscina nunca estará en un estado estacionario y el sistema de control funcionará eternamente. 

Con mencionar un solo escenario (cualquiera de los 2) se considera puntaje completo (1 pto). 

## **Pregunta 6 (20 minutos)** 

Un ecosistema se puede describir como un conjunto de poblaciones de individuos que interactúan entre sí, por ejemplo, como depredador y presa. 

Considere un ecosistema correspondiente a un área silvestre donde los conejos son la principal fuente de alimento de los coyotes, y ambas poblaciones se encuentran en equilibrio. Los coyotes _Y_ depredan a los conejos a una tasa r (conejos/coyote/año), lo que hace reducirse a la población de conejos _X_ . Esto afecta a la población de coyotes que también se reduce, permitiendo el crecimiento de la población de conejos siguiendo una dinámica del  tipo Lotka-Volterra. Los depredadores y las presas regulan mutuamente sus dinámicas poblacionales, manteniéndolas estables dentro de un rango. 

a) En un momento determinado un brote de una enfermedad afecta gravemente a la población de coyotes, y solo logra recuperarse después de muchos años. Represente gráficamente el efecto del brote de la enfermedad y la recuperación subsecuente de los coyotes, que se observaría en las poblaciones de conejos y coyotes en el tiempo, desde el inicio de la enfermedad (1 pt). 

La población de coyotes tiene una tasa de crecimiento que depende proporcionalmente del número de 

conejos y del número de coyotes con una constante de proporcionalidad 𝜇 _Y_ , y la población de conejos tiene una tasa de proliferación que depende sólo del número de conejos con una constante de proporcionalidad 𝜇 _X_ . Individuos de las dos poblaciones pueden morir por causas naturales a una tasa proporcional al número de individuos, con un factor de proporcionalidad 𝛿 _Y_ y 𝛿 _X_ respectivamente para coyotes ( _Y_ ) y conejos ( _X_ ). Adicionalmente el número de conejos disminuye por el consumo de conejos por parte de los coyotes a una tasa proporcional al número de coyotes, con constante de proporcionalidad 𝜌 conejos/coyote/año. 

Suponiendo que no hay otras poblaciones ni fenómenos a considerar más allá de los descritos: 

- b)  Identifique las variables de estado del sistema (1 pt). 

- c) Plantee un modelo para la población de Coyotes _Y_ y conejos _X_ e identifique en su balance los siguientes términos  (3 pt) 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

i.     Crecimiento del número de individuos de la población de 

coyotes 

ii.    Crecimiento de número de individuos de la población de conejos iii.   Depredación de los conejos 

iv.   Muerte de conejos y coyotes 

d)  Si ocurriera una migración constante de otra población de conejos al área silvestre descrita, ¿Qué efecto tendría esto en las poblaciones ya descritas? ¿Cómo lo representaría en las ecuaciones anteriores? Explique (1 pt). 

## _**(Respuesta en 25 líneas máximo en el siguiente espacio)**_ 

a) (1 pt) 

b) Coyotes Y, Conejos X (1 pt) c) dY/dt= mu_Y*Y*X - d_Y*Y (0.5 pt) dX/dt=mu_X*X - d_X*X-rho*Y (0.5 pt) i) mu_Y*Y*X    (0.5 pt) ii) mu_X*X    (0.5 pt) iii) rho*Y (0.5 pt) iv) d_Y*Y, d_X*X  (0.5 pt) d) Sería una nueva fuente de alimento para la población de coyotes, que se incrementaría  (0.5 pt)  . Se alcanzaría un nuevo valor de equilibrio para coyotes y conejos (totales). Se podría agregar un término de migración tau_Y que incrementa la población de conejos, representando el flujo de conejos que entra al área silvestre descrita  (0.5 pt) . 

**Pregunta 7 (20 minutos)** 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

La industria textil representa aproximadamente el 6,5% de la industria manufacturera nacional y dentro de este rubro las mujeres ocupan el 72% de los puestos de trabajo. Debido a las dificultades económicas percibidas entre los años 2020 y 2021, las empresas textiles abarataron costos para mantener la producción disminuyendo los elementos de protección personal (EPP) de sus trabajadores. 

La disminución de EPP expone considerablemente a las y los trabajadores a elementos tóxicos potencialmente cancerígenos propios de la industria textil, tales como arsénico, mercurio, plomo, etc. Estos elementos pueden ingresar al cuerpo humano por inhalación y por contacto con la piel. 

Según el Instituto Nacional de Estadísticas (INE), las y los trabajadores de la industria textil provienen de comunas de escasos recursos y así mismo, un estudio realizado a las y los trabajadores de la industria textil de Shangai, arrojó que la exposición a estos elementos tóxicos causa un aumento en la tasa de incidencia de cáncer de mamas, afectando así en mayor proporción a mujeres (Ray et al, 2007, DOI: 10.1097/01.ede.0000259984.40934.ae). 

a)   En base a lo expuesto en el enunciado, ¿Cómo cree usted que se evidencian los estereotipos y roles de género y la reproducción de estos en la industria textil? Argumente utilizando elementos presentes en el texto (2 ptos). 

b)   En base a lo expuesto en el enunciado, ¿Cuáles podrían ser las consecuencias del potencial impacto diferenciado por sexo que tendría la decisión de disminuir los EPP? Mencione al menos 2 consecuencias y argumente (2 ptos). 

c)   Considerando la materia de clases y la información proporcionada, identifique los distintos tipos de transporte de masa de los metales pesados desde el ambiente hacia las y los trabajadores. Debe justificar mencionando las fuerzas motrices involucradas y determinar si el proceso de transporte requiere energía. Utilice vocabulario preciso y los términos vistos en clases (2 ptos). 

## **Glosario de terminología asociada a perspectiva de género:** 

- **Género** : Se entiende como los roles, comportamientos, actividades, y atributos que una sociedad determinada en una época y cultura determinada considera apropiados para las personas según su sexo o identidad de género. Son cambiantes y son específicas a su contexto/época. 

- **Estereotipos de género:** Se entiende como ideas preconcebidas o generalizaciones de atributos o características que poseen o deberían poseer mujeres y hombres, ya sea según su sexo o identidad de género. Por ejemplo “los niños son más inquietos que las niñas”. 

- **Roles de género** : Son entendidos como el conjunto de tareas y responsabilidades que una sociedad le atribuye a las personas según su sexo o identidad de género. En la mayoría de las sociedades hay diferencias y desigualdades entre mujeres y hombres en cuanto a atributos y responsabilidades asignadas, en el acceso y el control de los recursos, así como oportunidades de adopción de decisiones. 

## _**(Respuesta en 20 líneas máximo en el siguiente espacio)**_ 

Respuestas tipo 

- a) En el enunciado se observa que existe una participación no equitativa de hombres y mujeres en la industria textil, siendo las mujeres quienes mayor presencia tienen con casi un ¾ del plantel. Lo anterior se podría explicar con que históricamente se ha asociado y atribuido el trabajo de confección, lavado y reparación de textiles a mujeres, lo que visibiliza los 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas 

Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

estereotipos asociados ya que son habilidades que culturalmente y socialmente se han relacionado con roles que desarrollan las mujeres. Además, los roles que provee esta industria se condicen y asocian a roles de género ya que existen diversas imposiciones sociales sobre los tipos de empleos que las mujeres pueden optar, en particular oficios relacionados o acorde a los estereotipos más conservadores de las labores domésticas. 

- b) La decisión tomada por el rubro textil va en contra de la seguridad y de la integridad de las y los trabajadores, pues una sobreexposición a elementos tóxicos aumenta los riesgos a tener afecciones como el cáncer y podría incluso la muerte por envenenamiento. En este sentido, existe un impacto diferenciado ya que existe una mayor presencia de mujeres, siendo la mayoría de la fuerza laboral de la industria textil. Además, existe un impacto diferenciado en las consecuencias y riesgos a la salud ya que los estudios muestran que hay un aumento en el cáncer de mama que principalmente afecta a las mujeres. 

Desde el punto de vista de la distribución laboral, al haber una mayor presencia de trabajadoras que de trabajadores, son muchas más las mujeres afectadas con estos riesgos a la salud, aún más considerando que son quienes se encargan del quehacer doméstico (cocinar, cuidar de menores, aseo, etc). En relación a lo anterior y desde una mirada más tradicionalista, serían las familias completas quienes estarían afectadas por el envenenamiento y eventual deceso de las trabajadoras. 

Desde un punto de vista social, y según las el INE, las y los trabajadores que desempeñan funciones en la industria textil, pertenecen a estratos socioeconómicos con menores recursos para acceder a tratamientos y en particular acceder a los mismos en tiempos oportunos (listas de espera, derivación a especialistas, etc). 

En resumen, quienes forman parte de la fuerza laboral del rubro textil pueden ver afectada la calidad de vida no sólo por la eliminación de elementos de protección personal y el riesgo a la salud que esto implica, sino porque existe una correlación en el aumento de enfermedades como el cáncer que pueden derivar en la muerte. Así mismo, queda evidenciado que de las y los trabajadores, quienes se ven más afectadas son las mujeres pues no sólo son la mayor parte de la fuerza laboral de la industria textil sino quienes podrían tener más riesgo de generar cáncer de mama. 

- c) En el caso del contacto por la piel el tipo de transporte es por difusión, ya que debe pasar a través de una barrera física solo por gradiente de concentración. En el caso de inhalación es por convección, ya que el ingreso de los metales es a través de un flujo de aire movilizado por la diferencia de presión producto del proceso de inhalación y exhalación. En ambos casos la gradiente va desde una mayor magnitud hacia una menor magnitud, por lo tanto no requiere energía. 


Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

## **Evaluación Principal 2** 

_7 de julio de 2025_ 

## _**Indicaciones**_ 

_Todas las preguntas tienen la misma ponderación. Debe responder en el espacio entregado para ello, con respuestas personales y de elaboración propia. Respuestas fuera del espacio permitido o de largo mayor al solicitado no serán consideradas. No se admitirán respuestas en hojas adicionales. Por esto mismo, por favor, piense y medite su respuesta antes de empezar a escribir y pregúntese qué es lo que quiere decir y cómo lo va a redactar en el espacio asignado._ _**Sólo se permiten dudas de enunciado** . Si es necesario tomar un supuesto para contestar una pregunta, declare su supuesto en la respuesta. Por favor, cuide su ortografía, la coherencia y cohesión de sus respuestas y trate de ser concisa/o en sus desarrollos. Estos aspectos se tomarán en cuenta al momento de la corrección. El tiempo total para el desarrollo de esta evaluación es de 140 minutos. Las preguntas tienen la ponderación y distribución de puntaje que se indica. Se recomienda tener en consideración como guía el tiempo de desarrollo asignado a cada una de las preguntas, según se indica._ 

## **Pregunta 1 (25 minutos)** 

Considere un mercado en el que participan empresas pequeñas ( _**P**_ ), medianas ( _**M**_ ) y grandes ( _**G**_ ), cuyo número varía a lo largo del tiempo. 

Cada empresa pequeña exitosa inspira a nuevos emprendedores a sumarse, por lo que las empresas pequeñas _**P**_ crecen a una tasa proporcional a su propia cantidad, con constante de proporcionalidad _**γP**_ . Las empresas pequeñas pueden ser adquiridas o absorbidas por empresas medianas a una tasa proporcional al producto entre la cantidad de empresas pequeñas y medianas, con constante de proporcionalidad _**αPM** ._ También pueden ser absorbidas por empresas grandes con tasa proporcional al producto entre la cantidad de empresas pequeñas y grandes, con constante de proporcionalidad _**αPG**_ . 

Las empresas medianas _**M**_ aumentan su número mediante la absorción de empresas pequeñas, de forma proporcional a la tasa de absorción _**αPM**_ · _**P**_ · _**M**_ antes descrita, con constante de proporcionalidad _**γM**_ . También pueden ser absorbidas por empresas grandes, a una tasa proporcional al producto de la cantidad de empresas medianas y grandes, con constante _**αMG**_ . Adicionalmente, pueden desaparecer por factores externos, con una tasa de cierre proporcional a su número, asociada a la constante _**δM**_ . 

Las empresas grandes _**G**_ incrementan su número al absorber empresas pequeñas de forma proporcional a la tasa de absorción de _**P**_ antes descrita _**αPG**_ · _**P**_ · _**G**_ con constante de proporcionalidad _**γGP**_ . También incrementan su número al absorber empresas medianas de forma proporcional a la tasas de absorción de _**M**_ antes descrita _**αMG**_ · _**M**_ · _**G**_ con constante de proporcionalidad _**γGM**_ . Además pueden cerrar por factores externos, con una tasa proporcional a su cantidad, de acuerdo a la constante _**δG**_ . 

Considerando que no ingresan empresas externas al mercado ni salen a otros mercados, este sistema puede representarse mediante un conjunto de ecuaciones de balances que modelan las tasas de crecimiento, absorción y cierre descritas para las empresas pequeñas ( _**P**_ ), medianas ( _**M**_ ) y grandes ( _**G**_ ). 

- a) Identifique las variables de estado del sistema. (1 pt) 

- b) Plantee en palabras los balances para cada variable de estado. Luego, reemplace los términos correspondientes con los indicados en el enunciado para obtener las ecuaciones que describen la dinámica (cambio en el tiempo) de cada variable de estado. (3 pts) 

- c) ¿Qué consecuencias podría tener una tasa de absorción de empresas pequeñas por parte de las grandes _**αPG**_ muy alta respecto a la tasa de crecimiento de empresas pequeñas _**γP**_ ? Fundamente. (2 pts) 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas 

Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

_Tabla resumen de constantes y tasas:_ 

|**_Constante_**|**_Descripción_**|
|---|---|
|**_γP_**|Tasa de crecimiento de empresaspequeñas P(proporcional a P)|
|**_αPM_**|Tasa de absorción depequeñas Ppor medianas M(proporcional a P·M)|
|**_αPG_**|Tasa de absorción depequeñas Pporgrandes G(proporcional a P·G)|
|**_γM_**|Tasa de crecimiento de Mpor absorción de P(proporcional a**_αPM_**·P·M)|
|**_αMG_**|Tasa de absorción de medianasporgrandes(proporcional a M·G)|
|**_δM_**|Tasa de cierre de empresas medianas(proporcional a M)|
|**_γGP_**|Tasa de crecimiento de Gpor absorción de P(proporcional a**_αPG_**·P·G)|
|**_γGM_**|Tasa de crecimiento de Gpor absorción de M(proporcional a**_αMG_**·M·G)|
|**_δG_**|Tasa de cierre de empresasgrandes(proporcional a G)|



_**(Respuesta en 35 líneas máximo en el siguiente espacio)**_ 

- a) Cantidad de empresas pequeñas **P** , medianas **M** y grandes **G** . (1 pt) 

- b) Para cada empresa la expresión de balance sería:  la cantidad de empresas que se acumula en el mercado en el tiempo es igual a la cantidad de empresas que se generan /crecen menos las que desaparecen del mercado.  De acuerdo al enunciado no entran ni salen empresas desde/hacia otros mercados. 

(No es necesario indicar las unidades de los parámetros descritos en la tabla. Si debe indicar a que corresponden los balances que plantee, respecto a la variable asociada, como en las descripciones presentadas). 

Para pequeñas: crecen en proporción a **P** con _**γP**_ y desaparecen al ser absorbidas por medianas ( _**αPM**_ · _**P**_ · _**M**_ ) y grandes ( _**αPG**_ · _**P**_ · _**G**_ ) (1 pt). 

𝑑𝑷 

**==> picture [133 x 15] intentionally omitted <==**

Para medianas: crecen en proporción a la absorción de **P** con _**γM αPM**_ · _**P**_ · _**M**_ y desaparecen al ser absorbidas por grandes ( _**αMG**_ · _**M**_ · _**G**_ ) y por cierre ( _**δM M**_ ) (1 pt) 

𝑑𝑴 𝑑𝑡 = 𝜸"𝜶PM𝑷𝑴−𝜶MG𝑴𝑮−𝜹M𝑴 

Para Grandes: crecen en proporción a la absorción de **P** con _**γGP αPG**_ · _**P**_ · _**G**_ y de _**M**_ con _**γGM αMG**_ · _**M**_ · _**G**_ y desaparecen sólo por cierre ( _**δG G**_ ) (1 pt) 

𝑑𝑮 𝑑𝑡 = 𝜸#!𝜶PG𝑷𝑮+ 𝜸#"𝜶MG𝑴𝑮−𝜹G𝑮 

Para los balances pueden usar deltas en vez de derivadas. 

- c) Si la tasa de absorción de empresas pequeñas por parte de las grandes _**αPG**_ es muy alta respecto a la generación de nuevas empresas pequeñas, la cantidad de empresas pequeñas se verá disminuida drásticamente, ocasionando también uan disponibilidad reducida de empresas pequeñas que puedan permitir el crecimiento tanto de empresas medianas como grandes. Por lo que afectaría tanto a M como a G. La reducción de M tendría conecuencias adicionales en el crecimiento de G. (1 pt)Esto llevaría a una reducción de los 3 tipos de empresas, hasta que la situación se vuelve a estabilizar en un nuevo equilibrio, o dependiendo de las magnitudes relativas de las distintas constantes, hasta la desaparición de los 3 tipos de empresas. (1 pt) 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

## **Pregunta 2 (30 minutos)** 

A diferencia de los humanos, algunas aves como las gaviotas y los patos pueden mantenerse en pie sobre superficies muy frías por largos periodos de tiempo. Por ejemplo, estas aves pueden pasar gran parte del día sobre lagos congelados. Este fenómeno se debe a una capacidad llamada heterotermia regional, es un mecanismo fisiológico que permite a los animales **mantener diferentes zonas de temperatura en distintas partes del cuerpo** , en especial en las extremidades. En el caso de las aves, este sistema permite que sus patas permanezcan a una temperatura considerablemente menor que el resto del cuerpo. De este modo el ave puede conservar energía para mantener su temperatura corporal, que de otra manera sería utilizada para calentar sus extremidades. El panel central de la figura 1 muestra un esquema del sistema circulatorio en las extremidades de las gaviotas. El panel de la derecha muestra cómo el sistema circulatorio en las aves funciona por intercambio de calor a contracorriente. En este sistema la sangre caliente que va por las arterias baja desde el cuerpo a las patas y la sangre fría sube (en la dirección opuesta) por una vena. De acuerdo con esta información responda: 

Figura 1: De izquierda a derecha: Gaviota posada sobre la nieve. El recuadro del medio muestra un esquema del sistema circulatorio de la pata (pierna y dedos) de la gaviota. Las líneas negras representan el sistema circulatorio. El panel de la derecha muestra un diagrama del intercambio de calor que ocurre en la pata de las gaviotas. 

- a) Mencione y describa dos tipos de transferencia de calor que suceden en las patas (pierna y dedos) de las gaviotas (1.5 pts). 

- b) El intercambio de energía efectivo entre un sistema biológico y su entorno depende tanto de elementos que son propios del sistema como de factores externos. ¿Qué factores biológicos y qué factores no biológicos incidirán en la transferencia de calor desde el cuerpo y patas de la gaviota al ambiente? Nombre y explique al menos dos factores de cada tipo (1.5 pts). 

- c) De acuerdo con la figura, ¿qué características del sistema circulatorio en la zona de los dedos de las gaviotas facilita la pérdida de calor desde la sangre al medio que la rodea, en esta parte de la extremidad? (1.5 pts). 

- d) Considerando lo anterior, la temperatura de los dedos de una gaviota posada en la nieve será muy baja, comparada con la temperatura corporal de la gaviota. Reflexione por qué el intercambio de calor a contracorriente presentado en la figura ayuda a mantener el calor en el cuerpo del animal. Hint: ¿Qué sucedería si las venas y las arterias estuvieran alejadas entre ellas? ¿O si la longitud de la zona en la que se contactan para el intercambio de calor fuera muy pequeña? (1.5 pts) 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

## _**(Respuesta en 35 líneas máximo en el siguiente espacio)**_ 

## a) 

Convección: El flujo de la sangre de un lugar con mayor temperatura a uno menor temperatura. Este fenómeno se observa en el flujo de sangre que va desde el cuerpo a los pies y en la dirección opuesta en las venas. (0.75 pt) 

Conducción: La transferencia de calor a través de las superficies entre las arterias y las venas sucede por conducción ya que no hay moléculas moviéndose en esa dirección. (0.75 pt) Podrían señalar otras alternativas, pero la pregunta indica EN las patas, no entre las patas y el ambiente. 

- b) Factores no biológicos: (0.75 pt) 

- Tº ambiente, del suelo, del aire: A mayor diferencia de Tº entre las patas y el cuerpo con el ambiente, mayor será la transferencia. 

- Fluido externo en movimiento (agua, aire), crean corrientes que incrementan la transferencia de calor. 

- Cantidad de nieve en el suelo: A mayor área de la pata cubierta con nieve, mayor área de intercambio, mayor será la transferencia. Factores biológicos: (0.75 pt) 

- Flujo sanguíneo, organización del sistema vascular: Mayor flujo aumenta la transferencia. 

- Temperatura corporal: A mayor diferencia de Tº entre las patas y el cuerpo con el ambiente, mayor será la transferencia. 

- Barreras con el entorno: plumas, piel, grasa corporal, permiten aislar al organismo reduciendo la transferencia de calor. 

Podrían dar otras respuestas válidas, pertinentes y correctamente justificadas. 

- c) La figura muestra que el sistema circulatorio en los pies se ramifica considerablemente en comparación a las piernas. Esta ramificación trae consigo un aumento del área donde se puede transmitir calor, lo que facilita la perdida de calor desde la sangre al medioambiente. (1.5 pts) 

La pregunta hace referencia al sistema circulatorio. Si sólo argumentan que la forma del pie/dedos del ave facilita la transferencia de calor porque tiene más área que las piernas (o un tubo en general), asignar máximo la mitad del puntaje pues el enunciado hace referencia específicamente a las características del sistema circulatorio. 

- d) Al tener un sistema en contracorriente, la sangre fría que va desde los pies al cuerpo aumenta su temperatura debido a la conducción de calor desde la sangre que pasa por las arterias. (0.75 pt) Si las arterias y las venas estuvieran alejadas entre sí, no existiría un mecanismo para aumentar la temperatura de la sangre que sube por las venas, por lo que ese calor se perdería al ambiente. La sangre fría en las venas alcanzaría el cuerpo con una temperatura similar a la temperatura de los pies (1 grado en lugar de 33 grados), lo que disminuiría la temperatura del cuerpo del ave. Lo mismo si el contacto entre venas y arterias fuera muy corto, no se alcanzaría a igualar la Tº en ambas corrientes por lo que no se generaría esa compartamentalización, y la sangre fría llegaría al cuerpo. (0.75 pt) 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

## **Pregunta 3 (30 minutos)** 

Clientes de una empresa que vende combustible sospechan que al cargar se les está entregando menos combustible del indicado en las máquinas dispensadoras y denuncian que las máquinas de esta empresa están “arregladas” para entregar menos combustible. Para investigar esta situación, la autoridad realiza mediciones en estaciones de servicio cargando 20 lt en cada máquina dispensadora. 

- a) Si la autoridad reporta que la diferencia promedio de litros cargados por las máquinas de esta empresa versus las máquinas de referencia por cada 20 L es de 0.1 L, ¿es esto suficiente para decir que las máquinas no están arregladas? ¿Qué otras medidas estadísticas, de tendencia central y/o variabilidad solicitaría que reporte la autoridad para evaluar la denuncia? Mencione dos y explique por qué los solicitaría. (1.5 pts) 

A partir de los datos levantados en la empresa la autoridad realiza un test de hipótesis contra las mediciones en las máquinas calibradas. Se plantea el siguiente contraste de hipótesis: 

   - Hipótesis nula (H₀): La carga realizada por las máquinas de la empresa es igual a la de las máquinas de referencia. 

   - Hipótesis alternativa (H₁): La carga realizada por las máquinas de la empresa es distinta a la de las máquinas de referencia. 

- b) ¿ Qué interpretación tendría cometer un **error de tipo I** para el contexto planteado? ¿Y qué interpretación tendría cometer un **error de tipo II** ? (2 pts) 

- c) ¿Cuál es la conclusión si se rechaza la hipótesis nula? ¿Qué implicación tendría para la empresa? (1.5 pts) 

Suponga que la autoridad selecciona una muestra de 8 mediciones de entre todas las realizadas a la empresa, y gráfica _**Y**_ **:** la diferencia entre la carga de las máquinas respecto al valor esperado vs. _**X**_ **:** el largo de la manguera de la máquina, y obtiene el gráfico en la figura 2. Considerando que la covarianza indica el grado de variación conjunta de dos variables respecto a sus medias: 

- d) ¿Qué puede decir del signo de la covarianza entre X e Y () para la muestra? Esperaría que la covarianza entre X e Y para la serie completa de mediciones realizadas () tenga el mismo signo que la covarianza de la muestra ().? ¿Recomendaría cargar combustible sólo en empresas con mangueras muy cortas en sus máquinas? Explique. (1 pt) 

Figura 2: Diferencia de carga medida vs largo de manguera para 8 muestras 

## _**(Respuesta en 35 líneas máximo en el siguiente espacio)**_ 

- a) No es suficiente información indicar sólo la diferencia promedio. Consultaría:  (Indicar y explicar 2, 0.75 pt. c/u) 

- Cuántas muestras (repeticiones) se usaron para el muestreo, para ver si es una cantidad relevante respecto al número total de máquinas, y cuáles fueron los criterios de selección de las máquinas a muestrear para identificar posibles sesgos. 

- Cuál es la desviación estándar (o varianza) para conocer la dispersión de lps datos. Sólo el promedio puede esconder grandes diferencias. 

- Solicitaría otros indicadores centrales como la mediana y/o la moda de los datos, y su distribución para ver cuál es una medida más representativa de la muestra. Podrían señalar otros indicadores válidos, pertinentes y correctamente justificados. 

- b) Error tipo I: Rechazar la hipótesis nula cuando en realidad es verdadera. En este contexto, significaría concluir que la empresa está entregando menos combustible del indicado, cuando en realidad sí está entregando lo correcto. (1 pt) 

   - Error tipo II: No rechazar la hipótesis nula cuando en realidad es falsa. Significa no detectar el problema (es decir, concluir que la empresa entrega bien el combustible), cuando en realidad sí está entregando menos del que indica la máquina. (1 pt) 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

- c) Si se rechaza la hipótesis nula, se concluye que hay evidencia estadística para afirmar que la empresa está entregando menos combustible del que indican sus máquinas. La empresa podría enfrentar sanciones, multas y pérdida de confianza de sus clientes. (1.5 pts) 

- d) La covarianza es positiva: A mayor largo de manguera, mayor es la diferencia entre el combustible cargado por la máquina y la referencia. 

La covarianza de la serie graficada y de la muestra completa no necesariamente serán iguales. Podría tratarse de una muestra no representativa, en especial si es muy pequeña. (0.5 pt) No recomendaría cargar sólo en máquinas con manguera corta pues no hay suficiente información. (Podrían indicar que sí lo recomendarían considerando estaos datos como un indicio, pero sabiendo que no es evidencia suficiente). Y que exista una covarianza/correlación positiva en una muestra pequeña, no implica que haya evidencia estadística, ni menos causalidad. (0.5 pt) 

## **Pregunta 4 (30 minutos)** 

Se estima que existen más de un millón de pacientes con enfermedad renal crónica en Chile. Esta enfermedad implica una dificultad para la eliminación de desechos generados por el cuerpo (solutos). Si esta condición no es tratada, conduce a la muerte de los pacientes. Estos pacientes pueden ser tratados mediante diálisis, de manera de reemplazar la función renal, al menos parcialmente, con un dispositivo externo. El sistema de diálisis consiste en un equipo que tiene 2 compartimentos líquidos: el compartimento donde ingresa la sangre (S) y el del líquido de diálisis (D), con una membrana semipermeable que los separa. La membrana semipermeable permite que traspasen solutos de pequeño y mediano peso molecular como urea hacia el líquido de diálisis, pero no moléculas grandes como proteínas o células sanguíneas, los que son muy grandes como para atravesar los poros de la membrana. Un esquema del dializador se muestra en la figura 3. 

Se verifica que el flujo másico neto del soluto urea ( _U_ ) desde la sangre a través de la membrana viene dado por la siguiente expresión: 

**==> picture [161 x 214] intentionally omitted <==**

**----- Start of picture text -----**<br>
QS CU,Se CU,Ds QD<br>Entrada Salida<br>Sangre desde el paciente Líquido usado<br>eee<br>@,1<br>—t_»<br>@ ] F<br>bo<br>@ [I]<br>I<br>@<br>S @ I D<br>QS CU,Ss CU,De QD<br>Entrada<br>Salida<br>Líquido de diálisis<br>Sangre dializada<br>**----- End of picture text -----**<br>


## _F=k0 A_ (CU,Se-CU,De)  [g/min] 

Donde en relación a la membrana y el dializador se tiene que: 

_k0_ : coeficiente global de transferencia de masa [cm/min] A: área de intercambio de la membrana [cm2] QS: flujo de sangre [cm3/min] en la entrada y salida del compartimento S. 

QD: flujo de dializado [cm3/min] en la entrada y salida de D. CU,Se, CU,Ss :concentración de urea [g/cm3] en la sangre de entrada (e) y salida (s) al compartimento S. 

CU,De, CU,Ds: concentración de urea [g/cm3] en el dializado de entrada (e) y salida (s) al compartimento D. En base a la información presentada arriba, responda las siguientes preguntas: 

Figura 3: Diagrama dializador 

- a) Plantee una ecuación de balance de masa que permita describir la acumulación de la masa de urea M _U_ , **S** en el compartimiento **S** . Identifique a qué parte del balance de masa corresponde cada término. (1 pt) 

- b) Plantee una ecuación de balance de masa que permita describir la acumulación de la masa de urea M _U_ , **D** en el compartimiento de diálisis. Identifique a qué parte del balance de masa corresponde cada término. A partir de esta expresión y de la obtenida en la parte a) determine e interprete la(s) condición(es) que se deben satisfacer cuando el equipo de diálisis opera en estado estacionario. (2 pts) 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

- c) Si Q **S** es 500 cm[3] /min, Q **D** es de 750 cm[3] /min, la solución de diálisis alimentada en la entrada no contiene urea (C _U_ , **D** e= 0), y C _U_ , **D** s= 0.3 g/cm[3] determine _F_ (g/min), el flujo másico de urea que se transfiere por unidad de tiempo a través de la membrana del dializador en estado estacionario. (1.5 pts) 

- d) ¿Cuál es la fuerza motriz que impulsa el transporte de urea desde el compartimiento **S** al **D** ? Si en un paciente la concentración de urea en la sangre a la salida del equipo de diálisis fuese muy alta, explique qué parámetro modificaría en el equipo para reducirla. Considere que la solución de diálisis alimentada en la entrada no contiene urea. (1.5 pt) 

## _**(Respuesta en 40 líneas máximo en el siguiente espacio)**_ 

- a) Para los balances pueden usar deltas en vez de derivadas. 

   - M _U_ , **S** en el compartimiento **S** (1 pt) 

𝑑M𝑑𝑡$,𝐒 = 𝑄' C$,𝐒( − 𝑄' C$,𝐒) −𝐹 

Acumulación de urea en compartimento **S** depende de la Entrada de U en sangre menos salida de U del compartimento en sangre menos el flujo F de U que sale hacia el compartimento **D** . 

- b) M _U_ , **D** en el compartimiento **D** (1 pt) 

**==> picture [160 x 25] intentionally omitted <==**

Acumulación de urea en compartimento **D** depende de la Entrada de U en líquido de diálisis menos salida de U del compartimento **D** en líquido mas el flujo F de U que ingresa desde **S** hacia el compartimento **D** . 

Análisis de estado estacionario, no hay acumulación: (0.5 pt) 

Y 

**==> picture [182 x 103] intentionally omitted <==**

Por lo tanto (0.5 pt) 

**==> picture [184 x 15] intentionally omitted <==**

Lo que indica que en estado estacionario toda la urea removida de la sangre es transferida al líquido de diálisis. 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

- c) Usando ** (1.5 pt) 

**==> picture [109 x 12] intentionally omitted <==**

Con Q **S** es 500 cm[3] /min, Q **D** es de 750 cm[3] /min, C _U_ , **D** e= 0, y C _U_ , **D** s= 0.3 g/cm[3] F=750(0.3-0) => F= 225 g/min 

- d) La fuerza motriz es la diferencia de concentración entre el contenido de urea en sangre y en el líquido de diálisis, que impulsa la difusión a través de la membrana.(0.75 pt) 

   - Para reducir la concentración de urea del paciente, si es posible cambiar las especificaciones del equipo aumentaría el área de la membrana, para aumentar el flujo de soluto que traspasa la membrana (F). Si es posible cambiar la membrana por una con un mayor coeficiente global de transferencia, lo aumentaría. Aumentar la diferencia de concentración local cerca de la membrana entre ambos compartimentos, por ejemplo, disminuyendo la concentración en el lado del dializado mediante un aumento el su flujo Q **D.** (0.75 pt)  Basta con que expliquen una modificación. 

## **Pregunta 5 (25 minutos)** 

Las prótesis modernas buscan restaurar el movimiento natural integrando componentes mecánicos con señales biológicas del usuario. Considere un brazo protésico que utiliza sensores de **electromiografía (EMG)** (miden actividad eléctrica muscular) para detectar actividad muscular en el muñón, procesa estas señales para determinar la intención de movimiento del usuario y activa motores para ajustar la posición de la prótesis. El sistema incluye: 

- **Sensores EMG** para detectar corrientes eléctricas generadas en los músculos durante su contracción. Representa la actividad neuromuscular. 

- Un **controlador** que interpreta las señales y comanda los motores. 

- **Motores** que mueven las articulaciones de la prótesis. 

- **Sensores de retroalimentación** (ej. acelerómetros, sensores de fuerza) ubicados en la prótesis para monitorear la posición y ajustar el movimiento en tiempo real. 

a) ¿A qué tipo de sistema de control corresponde este brazo protésico? Discuta al menos una ventaja y una desventaja del diseño considerado para el sistema de control de la prótesis considerando los elementos antes descritos. (2 pts) 

Ahora, imagine que la prótesis se actualiza y se le incorporan **sensores táctiles** en los extremos de los dedos de la prótesis anterior, permitiendo al usuario "sentir" la presión que ejerce y ajustar la fuerza de agarre. 

b) ¿A qué tipo de **estructura** de control corresponde y cuál sería el **objetivo principal** de este sistema de control mejorado? (2 pts) 

c) Mencione y describa los **componentes** que debe tener el sistema de control, explicando la función que debe cumplir cada uno, e identifíquelos para el sistema actualizado. Mencione al menos 4. (2 pts) 

Figura 4: Ejemplo de brazo protésico 

Universidad de Chile **Nombre:** Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales. **RUT:** BT1211 – Aplicaciones de la Biología a la Ingeniería y Ciencias 

_**(Respuesta en 35 líneas máximo en el siguiente espacio)**_ 

- a) El sistema de control del brazo prostético es un ejemplo de sistema a lazo cerrado, con retroalimentación negativa porque usa retroalimentación de sensores (acelerómetros, fuerza) para corregir errores en tiempo real. 

- (0.5 por identificar sistema lazo cerrado, 0.5 por explicar que lo hace lazo cerrado). 

Ventaja: permite ajustar los movimientos basados en datos reales de actividad muscular eléctrica (ej. si el agarre es insuficiente, aumenta la fuerza). Desventaja: Requiere datos de muchos sensores, lo que puede ser complicado de implementar en la prótesis, además de la capacidad de procesar la información. 

- (0.5 ventaja, 0.5 desventaja y sus respectivas explicaciones). 

- b) Al añadir un sensores táctiles el sistema resulta ser un sistema adaptativo _Objetivo:_ Mantener una fuerza de agarre estable y adaptable, combinando: 

1. Retroalimentación táctil (sensores de presión) para detectar propiedades del objeto (ej. fragilidad). 

2. Control en lazo cerrado para ajustar la salida de los motores en tiempo real, evitando caídas o aplastamiento. 

- También podrían referirse al sistema como retroalimentado, pero agregando un segundo nivel de información (no necesariamente adaptativo). Con el objetivo de entregar una relación sensorialfuncional mas completa. 

(1 pt por estructura y 1 pt por objetivo y sus respectivas explicaciones). 

- c) Los 4 componentes principales son: (0.5 pt c/u) 

1. Sensores EMG: _Rol_ : Captan la intención de movimiento del usuario mediante señales musculares. 

2. Controlador: _Rol_ : Procesa las señales EMG y de la retroalimentación para calcular el torque necesario (ajustando términos). 

3. Actuadores (motores): _Rol_ : Generan movimiento en la prótesis (ej. rotar la muñeca, cerrar los dedos). 

4. Sensores de retroalimentación (acelerómetros, sensores de fuerza): _Rol_ : Miden variables físicas (posición, fuerza aplicada) para corregir errores. 

Podrían señalar también: 

Referencia o set-point: En este caso relativa a posición, movimiento y/o fuerza de agarre de la prótesis. 

Líneas de transmisión: Comunicación entre sensores, controlador y motores, por  medio de señales eléctricas. 

Proceso: Mecanismo para ejecutar el movimiento de la prótesis. 

(Si indican mas de 4 componentes, y algunos son incorrectos descontar; no se consideran las 4 mejores, se descuenta 0.5 por cada incorrecta). 


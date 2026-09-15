**Nombre: RUT:** 

Universidad de Chile Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales BT1211 – Aplicaciones de la Biología a Ia Ingeniería y Ciencias 

## Evaluación Principal N°2 

_8 de julio de 2023_ 

## **Indicaciones** 

_**Todas las preguntas deben responderse en el espacio entregado para ello, con respuestas personales y de elaboración propia.** Respuestas fuera del espacio permitido o de largo mayor al solicitado no serán tenidas en cuenta para la corrección. No se admitirán respuestas en hojas adicionales. Por esto mismo, por favor,_ _**piense**_ 

_**y medite su respuesta antes de empezar a escribir y pregúntese qué es lo que quiere decir y cómo lo va a redactar en el espacio permitido.**_ 

_**No se responderá consultas durante la realización de la evaluación.** Si es necesario tomar un supuesto para contestar una pregunta, por favor incorpore su supuesto en la respuesta._ 

_Por favor, cuide su ortografía, la coherencia y cohesión de sus respuestas y trate de ser concisa/o en sus desarrollos. Estos aspectos se considerarán al momento de la evaluación. Por favor, también recuerde escribir su_ _**nombre y RUT en todas las hojas de la evaluación** ._ 

_**Tome en consideración como guía el tiempo de desarrollo asignado a cada una** , según se indica._ _**El tiempo total** estimado para el desarrollo de esta evaluación es de_ _**150 minutos. Todas las preguntas tienen la misma ponderación en la nota final, y el puntaje correspondiente de cada pregunta se distribuye entre cada sección y entre cada subsección tal como se indica** , en caso de que haya distintas secciones._ 

## **Pregunta 1 (30 min).** 

Por un descuido, una piscina recreativa ha sufrido un accidente de contaminación por algas. La piscina tiene un volumen 𝑉 [L], la concentración de algas en la piscina es 𝐶! [g/L], y la velocidad de crecimiento de las algas puede ser considerada proporcional a la cantidad de algas en la piscina, con una constante de proporcionalidad 𝑘". Para acabar con la infección de algas, se decide introducir a la piscina un alguicida que destruya las algas con una velocidad [g/L/s] que es proporcional al producto de la concentración de algas (𝐶!) y la concentración de alguicida en la piscina (𝐶#), con una constante de proporcionalidad 𝑘$. 

Suponga que el alguicida no se descompone en la piscina y que la evaporación de agua desde la piscina es despreciable. 

- a) **[25%]** Plantee un modelo para este sistema mediante un balance de masa para las algas en la piscina. b) **[25%]** ¿Qué condición matemática se debe cumplir para que la cantidad de algas disminuya en el tiempo en la piscina? ¿Le permitiría saber cuánto alguicida debería comprar? Explique. 

- c) **[25%]** Uno de sus colegas le indica que si se considera la tasa de evaporación (𝑄%&!', [g/s]) de la piscina, esto podría requerir agregar una segunda ecuación de balance de masa al modelo. ¿Es así? Explique. 

- d) **[25%]** Suponga que ahora considera que la tasa de evaporación es despreciable, pero que el alguicida sí se descompone con una velocidad proporcional al cuadrado de su concentración. ¿Modificaría eso el resultado obtenido en (b)? Explique. **No es necesario calcular.** 

1 

**Nombre: RUT:** 

Universidad de Chile Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales BT1211 – Aplicaciones de la Biología a Ia Ingeniería y Ciencias 

## **(Respuesta en 20 líneas máximo, en el siguiente espacio)** 

_a) El balance de masa será. Ac = E – S + G – C. No hay entrada de algas No hay salida de algas Si hay generación de algas si hay consumo de algas d(Masa de algas)/dt = V*k1*Ca – V*k2*Ca*Cx o bien_ 

_Ac Masa algas en la piscina en dt =  V*k1*Ca*dt - k2*Ca*Cx*dt el dt es opcional dependiendo de como escriban el balance._ 

_b) Para que la cantidad de algas en la piscina dismimuya se debe cumplir que: Ac Masa algas en la piscina <0_ 

_Y por lo tanto:_ 

_V*k1*Ca*dt - k2*Ca*Cx*dt < 0_ 

_Cx > k1/k2_ 

_Si, permitiría saber cuanto alguicida hay que comprar ya que esa sería la concentración máxima a la que hay que llegar en la piscina._ 

_c) Si se considera la tasa de evaporación de la piscina habría que realizar un balance de masa para el agua:_ 

_Acumulación de agua = -Qevap_ 

_Qué modificaría el volumen de la piscina y por lo tanto el modelo descrito en (a)_ 

_d) Si el descompone el alguicida se podría dar el caso de que en algún momento posterior al inicial se invirtieran las magnitudes de los sumandos del modelo deducido en (a) de manera que V*k1*Ca*dt - k2*Ca*Cx*dt > 0_ 

_Con esto la acumulación dejará de ser negativa y se volverá positiva y, por lo tanto, la cantidad de algas volverá a crecer en la piscina._ 

## **Pregunta 2 (20 min).** 

Como ingenier[ao], usted está a cargo de mejorar el desempeño de una operación industrial que es muy sensible al catalizador utilizado. Sabiendo esto, un vendedor de una compañía de suministros le ofrece un nuevo catalizador que según sus palabras: 

“Nuestra nueva línea de catalizadores le permitirá aumentar la eficiencia de su proceso.  Hemos realizado una serie de experimentos, y el promedio de aumento en la eficiencia es de un 10%” 

2 

**Nombre: RUT:** 

Universidad de Chile Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales BT1211 – Aplicaciones de la Biología a Ia Ingeniería y Ciencias 

Uno de sus estudiantes en práctica le indica que esta información no es suficiente, ya que se requiere conocer otros estadísticos, como la desviación estándar de los experimentos. Explique si la recomendación de su estudiante es correcta y justifique por qué. 

## **(Respuesta en 20 líneas máximo, en el siguiente espacio)** 

_El promedio es insuficiente.  La evaluación de las bondades del nuevo catalizador depende de las características de la distribución de eficiencia observada en los experimentos.  Para poder cuantificar esa distribución se pueden usar otros estadísticos como la media y la desviación estándar.  La desviación estándar permitirá saber que tan heterogéneo son los resultados del experimento.  Si es de gran magnitud significa que los experimentos obtuvieron resultados muy disimiles entre sí.  Cambiar el catalizador en esas condiciones pondría en riesgo la operación industrial._ 

## **Pregunta 3 (25 min).** 

El etanol (alcohol etílico) es una molécula pequeña, lipofílica, por lo que tiene afinidad con compuestos lipídicos o grasos. Al consumir alcohol, éste es absorbido por la mucosa estomacal y principalmente por la intestinal, para luego pasar al torrente sanguíneo. En el torrente sanguíneo es transportado en el sistema circulatorio hasta llegar al hígado, donde es metabolizado para ser convertido en metabolitos no tóxicos que pueden ser aprovechados por las células. Para entrar a las células hepáticas, debe atravesar la membrana plasmática de los hepatocitos, que expresan transportadores específicos para el etanol. Al consumir bebidas alcohólicas: 

- a) **[25%]** ¿Qué tipo de transporte se utiliza principalmente para transportar el etanol en el torrente sanguíneo? Explique y mencione los factores que influyen en la velocidad del transporte. 

En el caso del transporte de etanol desde la sangre hacia el interior de los hepatocitos: 

- b) **[25%]** ¿Cuál es la fuerza motriz para el transporte de etanol? Explique detalladamente. 

- c) **[25%]** Mencione y describa qué mecanismos de transporte puede usar el etanol para atravesar la membrana plasmática. 

- d) **[25%]** Considerando la fuerza motriz, ¿se requiere energía para el transporte de etanol hacia el medio intracelular? 

3 

**Nombre: RUT:** 

Universidad de Chile Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales BT1211 – Aplicaciones de la Biología a Ia Ingeniería y Ciencias 

## **(Respuesta en 20 líneas máximo, en el siguiente espacio)** 

- a) _El transporte sanguíneo se realiza principalmente por convección,  dado que un fluido (sangre) arrastra al etanol que es transportado. Influye la velocidad con que se mueve el fluido (flujo sanguíneo), la viscosidad, el diámetro del vaso sanguíneo, podría ser la temperatura también._ 

- b) _Es un gradiente de concentración, hay una diferencia de concentración entre el exterior de la célula (sangre) y el citoplasma celular, siendo mayor la concentración en el extracelular._ 

- c) _Difusión en la membrana, dado que es una molécula pequeña y con afinidad a lipidos, puede atravesar sin la necesidad de un transportador. Pero también existen transportadores específicos, que son proteínas que permiten el paso desde el extracelular al intracelular_ 

- d) _No se requiere energía, porque el etanol está más concentrado en el exterior, entonces se mueve de mayor valor de  fuerza motriz a menor fuerza motriz._ 

## **Pregunta 4 (25 min).** 

Considere al bosque natural como un sistema cerrado donde proliferan árboles, pastos y arbustos, en que la energía lumínica del sol es la primera fuente de energía. El gráfico muestra el cambio en el tiempo, de la productividad bruta (captación total de energía) y de la biomasa en la evolución de un bosque, desde suelo desnudo a bosque maduro. 

4 

**Nombre: RUT:** 

Universidad de Chile Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales BT1211 – Aplicaciones de la Biología a Ia Ingeniería y Ciencias 

- a) **[20%]** ¿Cuáles deberían ser las unidades de medición de la productividad bruta? 

- b) **[20%]** Explique la disminución de la productividad bruta a medida que madura el bosque. 

- c) **[20%]** ¿Qué razones pueden explicar el aumento de la biomasa durante los primeros 20 años de crecimiento del bosque? 

- d) **[20%]** Utilice la información del gráfico y sus conocimientos sobre el concepto de productividad neta para explicar por qué la biomasa muestra un incremento tan lento después de 100 años. 

- e) **[20%]** Si al bosque llega a vivir un grupo de pequeños ciervos que se alimenta de pastos, ¿qué información le permitiría a usted predecir si el grupo de ciervos podrá sobrevivir de la biomasa del bosque, como consumidores secundarios? 

## **(Respuesta en 20 líneas máximo, en el siguiente espacio)** 

## a) _Unidades de energía o biomasa por área por año._ 

- b) _A medida que crece el bosque habrá menos luz, más sombra, más competencia por la luz, por lo tanto, la fotosíntesis será cada vez más reducida._ 

- c) _Posibles razones: más disponibilidad de nutrientes y de sol, condiciones ambientales menos hostiles. Aumento del número/cantidad/diversidad de especies/plantas/animales._ 

- d) _Productividad neta = productividad bruta menos pérdida respiratoria; se observa disminución de la productividad bruta del nivel trófico, probablemente por disminución de la fotosíntesis y/o aumento de la respiración._ 

- e) _Productividad neta del nivel anterior y requerimientos metabólicos y energéticos para el crecimiento y reproducción de la población de ciervos._ 

## **Pregunta 5 (25 min).** 

Al momento de ducharse en su casa, usted nota que por alguna razón la llave que regula la temperatura del agua está atascada. Mientras esperan a ver cómo resolver este inconveniente, un pariente suyo sugiere ajustar la temperatura de la caldera/calefont que calienta el agua que luego es transportada a la ducha. Para ello él se ofrece de voluntario para ir al lugar donde está este equipo y hacer ajustes de acuerdo con sus comentarios. 

- a) **[60%]** Realice un esquema donde identifique los componentes del sistema de control previamente descrito, específicamente para este ejemplo. 

- b) **[20%]** ¿Corresponde a un lazo abierto o cerrado? De ser cerrado ¿sería feedback positivo o negativo? 

5 

**Nombre: RUT:** 

Universidad de Chile Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales BT1211 – Aplicaciones de la Biología a Ia Ingeniería y Ciencias 

- c) **[20%]** Dado el ruido ambiental, su pariente sugiere realizar una llamada por teléfono para escucharlo mejor ¿Altera esto de alguna forma el esquema propuesto en A? 

## **(Respuesta en 20 líneas máximo, en el siguiente espacio)** 

_a)_ 

_Controlador: cerebro de “usted que está en la ducha ”_ 

_Actuador: “el pariente” que ajusta el calefont Proceso: la ducha Sensor: sensores de temperatura de usted Comunicación: habla (transporte de sonido a través del aire) Variable controlada: temperatura_ 

_Perturbaciones: perturbaciones del proceso del sistema (ej: que alguien use agua, prenda la lavadora (variaciones de presión))_ 

_b) Lazo cerrado, feedback negativo (se desea mantener la temperatura en el rango de preferencia del usuario, oponiéndose a perturbaciones)_ 

_c) La forma se mantiene, pero el canal de comunicación del sensor al controlador ahora es la llamada telefónica, y no la comunicación por el habla directa entre los usuarios._ 

## **Pregunta 6 (25 min).** 

Los mamíferos mantienen una temperatura corporal constante y mayor que la temperatura del medio ambiente en que viven (son “animales de sangre caliente”). Los reptiles, por otro lado, son animales que no controlan su temperatura corporal (son “animales de sangre fría”), y ésta se mantiene relativamente semejante a la temperatura corporal de su medio ambiente. En general, los dinosaurios eran animales de tamaños muy grandes en relación con los mamíferos y reptiles actuales. En la década pasada, se descubrió que los dinosaurios poseían una temperatura corporal intermedia entre los reptiles y los mamíferos. Suponga que la velocidad de producción de calor en un animal es directamente proporcional a su volumen. 

- a) **[20%]** La velocidad de pérdida de calor hacia el medio ambiente en un animal, ¿es directamente proporcional al volumen del animal o a su superficie de contacto con el medio ambiente? Justifique clara y concisamente su respuesta de acuerdo con las ecuaciones de transporte vistas en clases. 

- b) **[30%]** Para analizar este caso, suponga que un animal es una esfera de radio 𝑟. Encuentre una expresión para proporcionalidad con respecto a 𝑟 de la razón entre la velocidad de generación de calor y la velocidad de pérdida de calor. 

6 

**Nombre: RUT:** 

Universidad de Chile Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales BT1211 – Aplicaciones de la Biología a Ia Ingeniería y Ciencias 

- c) **[30%]** Usando la expresión anterior como aproximación, entre un animal de gran tamaño y uno de pequeño tamaño con formas y proporciones similares, ¿cuál de los dos pierde más rápidamente calor hacia el medio ambiente en relación con la velocidad de generación de calor? 

- d) **[20%]** En base a sus respuestas anteriores, ¿qué ventaja evolutiva les podría haber dado a los dinosaurios tener una temperatura intermedia, frente a los animales de sangre fría y a los animales de sangre caliente? 

Indicación: Si lo necesita, use las siguientes relaciones para el volumen y la superficie de una esfera: 

𝑉%()%*! =[4] 3 𝜋𝑟[+] 𝑆%()%*! = 4𝜋𝑟[$] 

**(Respuesta en 20 líneas máximo, en el siguiente espacio)** 

- _a) La pérdida de calor desde un animal hacia el medio externo depende de la superficie a través de la cual se transfiere el calor, de acuerdo a las expresiones de velocidad de transferencia de calor vistas en clases. Luego, la velocidad de pérdida de calor de un animal depende de su superficie de contacto con el medio externo._ 

- _b) Según el enunciado, la velocidad de producción de calor es directamente proporcional al volumen del animal. Para un animal esférico:_ 

_Vel. producción calor = cte * 4/3*pi*r^3 = cte * r^3_ 

_De acuerdo a la respuesta de la parte (a), la velocidad de pérdida de calor para un animal esférico es:_ 

_Vel. pérdida calor = cte * 4*pi*r^2 = cte * r^2_ 

_Luego, la razón entre pérdida de calor y generación de calor para un animal esférico es:_ 

_Razón pérdida:producción calor = cte*4*pi*r^2 / (cte*4/3*pi*r^3) = cte / (3*r) = cte / r_ 

_También puede llegarse a lo anterior como:_ 

_Razón pérdida:producción calor = cte * r^2 / (cte * r^3) = cte / r_ 

_Luego, la razón es inversamente proporcional a r (o directamente proporcional a 1/r)._ 

- _c) Dado que la razón entre pérdida y generación de calor es inversamente proporcional a r, entonces la pérdida para un animal de gran tamaño es menor en relación a la generación que esta misma razón para un animal de pequeño tamaño. Luego, el animal de menor tamaño tiene una mayor velocidad de pérdida de calor  que un animal grande hacia el medio en relación a la velocidad de generación de calor._ 

- _d) Un dinosaurio es de gran tamaño, así que pierde menor cantidad de calor hacia el medio respecto a la velocidad de generación que los animales más pequeños. Luego, necesita poca energía para generar calor y lo pierde menos, lo que le da una ventaja frente a los mamíferos más pequeños. Frente a los reptiles, el hecho de tener temperatura interna más alta les habría dado la ventaja de tener un metabolismo más rápido para la depredación y la defensa frente a predadores, y de no depender de la temperatura ambiente para esto._ 

7 


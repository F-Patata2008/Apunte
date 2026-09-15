# **Control y Transporte de Materia** 

Auxiliar 3 - BT1211 

APLICACIONES DE LA BIOLOGÍA PARA INGENIERÍA Y CIENCIAS 

**d** 

**==> picture [107 x 82] intentionally omitted <==**

## **Actuadores** 

## **Set-point/referencia** 

acciones **Ejecutan** para influir en el sistema según la información del controlador 

Valor deseado par alcanzar el objetivo del proceso 

## **Controladores** 

**Comparan** valor medido en el sensor con un valor de referencia o set-point 

## **Sensores** 

**e** 

**Detectan y miden** la variable controlada en el proceso 

**==> picture [188 x 144] intentionally omitted <==**

## **Proceso** 

Determina los ajustes necesarios para modificar la variable controlada según el objetivo del proceso 

**Transformación** de la variable controlada ajustada al set-point 

Pueden cambiar la señal a otra más fácil de manipular o comunicar 

**Puede ser afectado** por **perturbaciones.** 

## **Variable controlada** 

**==> picture [220 x 197] intentionally omitted <==**

**Comunicación** 

Característica del proceso que se busca sea monitoreada y ajustada 

_e: Error (diferencia) entre variable controlada y set-point d: Posible perturbación del proceso_ 

# **Ejercicio 1: Tiro al arco** 

**==> picture [611 x 810] intentionally omitted <==**

Usted se ha propuesto practicar el deporte de tiro con arco y en su primera sesión debe realizar una evaluación de entrada. Esta evaluación consiste en tirar flechas sobre un blanco intentando apuntarle lo más cerca posible al centro del aparato. El instructor le propone una secuencia de acciones para llevar a cabo su evaluación. 

**==> picture [107 x 82] intentionally omitted <==**

**(1)** Usted apunta. **(2)** El instructor le da información sobre la dirección y magnitud del viento. **(3)** Usted corrige su puntería en base a esa información. **(4)** Dispara El instructor le informa distancia de su flecha con el blanco **(5) (6)** Corrige su puntería y vuelve a (1) 

**==> picture [355 x 313] intentionally omitted <==**

**==> picture [220 x 197] intentionally omitted <==**

# **(a) Identifique los componentes de este sistema de control y las posibles perturbaciones existentes** 

**Proceso** Vuelo de flecha desde el arco hasta el blanco, influenciado en la por ajustes puntería y condiciones externas. **Variable controlada** Posición donde impacta la flecha en el blanco. **Set-Point/Referencia** Posición deseada, centro del blanco. 

**==> picture [332 x 325] intentionally omitted <==**

**(a) Identifique los componentes de este sistema de control y las posibles perturbaciones existentes** 

**Sensor Instructor** , observa el impacto de la flecha para informar la distancia de esta con respecto al blanco. **Equipo** que posee el instructor para informar la dirección y magnitud del viento. 

**Perturbaciones Viento** , con su dirección y magnitud afecta la trayectoria de la flecha. 

**==> picture [332 x 325] intentionally omitted <==**

**(a) Identifique los componentes de este sistema de control y las posibles perturbaciones existentes** 

**Controlador La persona que dispara** (usted), ya que esta persona recolecta la información del sensor (instructuctorequipo) y decide si corrige o no su disparo. 

**Actuador arco Brazos de la persona** que dispara (usted) y el **Medio de comunicación** Comunicación verbal (tirador-instructor) señalización eléctrica (neurona-músculo) 

y 

**==> picture [332 x 325] intentionally omitted <==**

**(b) ¿A que tipo de sistema de control corresponde? En caso de ser lazo cerrado, ¿posee retroalimentación positiva o negativa?** 

**Lazo cerrado** Existe retroalimentación continua desde el instructor (sensor) a la persona que ajusta la punteria, usted (controlador). **Retroalimentación negativa** El objetivo del proceso es acertar al blanco, cualquier desviación con respecto a este (set-point) implica un ajuste de la puntería para reducir la distancia entre la flecha y el blanco 

**==> picture [332 x 325] intentionally omitted <==**

# **Ejercicio 2: Operón triptófano** 

**==> picture [611 x 810] intentionally omitted <==**

Las bacterias, como _E. coli_ , necesitan aminoácidos para construir proteínas. Uno de estos aminoácidos es el **triptófano** . **(TRP)** 

Este es **sintetizado** mediante la acción de **5 enzimas** cuyos genes se encuentran **codificados en el Operón TRP.** 

_**Operón: Grupo de genes transcritos bajo el control de un solo promotor**_ 

Si el TRP se encuentra en el **altos niveles** ambiente (en ), entonces no es necesario sintetizarlo y por tanto se **“apaga”** la transcripción del operón TRP. Por el contrario, **si se tienen bajos niveles de TRP** , el operón se **“enciende”** transcribiendo los genes que participan en la producción del TRP. **¿Cómo lo logra?** 

Para poder controlar cuando encender o apagar los genes que sintetizan triptófano, en el operón se identifican dos estructuras claves: **Promotor:** Secuencia de ADN donde se une la **ARN Polimerasa (Transcripción)** 

**Operador:** Secuencia de ADN donde se une una molécula conocida como **Represor TRP.** 

**==> picture [1075 x 648] intentionally omitted <==**

**----- Start of picture text -----**<br>
TRIPTOFANO ACTO |<br>fo, ARN polimerasa a<br>o<br>Ss<br>pe Iriptofano Gin transcripcion<br>ieevaalis ADN<br>[_? ee ee _tepC eA<br>Represor trp<br>(.activo)<br>TRIPTOFANO BAJO<br>Represor trp<br>(inactivo)<br>Transcripcion ADN<br>pe tree tPA<br>**----- End of picture text -----**<br>


**¡Operón TRP puede ser visto como un sistema de control!** 

# **(a) ¿Cuál es la variable controlada?, ¿A qué tipo de lazo de retroalimentación corresponde?** 

# **(b) ¿Qué tipo de retroalimentación posee el sistema de control?** 

**(c) Identifique a qué o cuáles tipos de componentes de un sistema de control pertenece el Represor TRP.** 

## Usted descubre que existe una **molécula X** de **estructura muy similar al TRP** que **compite por la unión** del TRP al Represor TRP. 

**==> picture [306 x 154] intentionally omitted <==**

**----- Start of picture text -----**<br>
TRIPTOFANO BAJO<br>ARN polimerasa<br>Molécula X<br>**----- End of picture text -----**<br>


- Esta molécula X , 

- **provoca el cambio conformacional del Represor TRP** 

- manteniéndolo **activo** tras su unión con X, aún en ausencia de TRP. **(d) Desde el punto de vista de control, ¿A qué corresponde esta molécula?** 

El **transporte** consiste en la transferencia de una entidad (por ejemplo, autos, moléculas, masa o energía), de un lugar a otro. Y el **Flujo** corresponde a la cantidad de entidad transportada por unidad de tiempo. 

# **Ejercicio 3: Hemodiálisis** 

**==> picture [611 x 810] intentionally omitted <==**

La urea es un desecho metabólico que debe ser retirado de la sangre, ya que es tóxico. Normalmente, el riñón cumple esa función. Sin embargo, en los casos de pacientes con daño renal, una máquina de diálisis puede reemplazar al riñón. 

En esta máquina, la sangre es impulsada por una bomba para circular por un tubo hecho de una membrana que es totalmente permeable a la urea (tubo de diálisis), y no deja pasar moléculas de tamaño mucho mayor al de la urea. 

La urea pasa a través de la pared de este tubo hacia la solución de diálisis en el dializador, la que posteriormente es eliminada. El dializador es alimentado con solución de diálisis fresca permanentemente. La sangre limpia es devuelta al organismo. 

# **(a) ¿De qué factores dependerá la velocidad de transporte de la urea desde la sangre a la solución en el dializador?** 

La glucosa y la urea tienen tamaños moleculares similares. La glucosa es fuente de energía en los organismos vivos, por lo tanto, no debe ser eliminada de la sangre junto con la urea. 

**sus conocimientos de (b) Según transporte de masa, ¿Qué componente (compuesto) se podría agregar a la solución de diálisis en el dializador para lograr que la glucosa no sea transportada desde la sangre a la solución de diálisis en este procedimiento?** 

**(c) ¿Qué pasará con la velocidad de transporte de la urea desde la sangre a la solución de diálisis si la bomba de la máquina se echa a perder y la sangre se moviliza muy lentamente o no se moviliza a través de la máquina? ¿Por qué?** 

# **Control y Transporte de Materia** 

Auxiliar 3 - BT1211 

APLICACIONES DE LA BIOLOGÍA PARA INGENIERÍA Y CIENCIAS 


Universidad de Chile Facultad de Ciencias Físicas y Matemáticas Departamento de Ingeniería Química, Biotecnología y Materiales 

## Actividad N° 6: Modelamiento y Control 

## _Tiempo de actividad: 50 minutos_ 

## **Pregunta 1: Apocalipsis Zombie** 

¡Llegó el momento que todos temíamos: un apocalipsis zombie ha comenzado! Dada tu experiencia en modelamiento matemático, te han contactado te han contactado para ayudar a predecir qué pasará con la humanidad y qué estrategias podrían salvarnos del desastre. 

Junto a tu equipo de trabajo, tienen la misión de comprender las dinámicas entre humanos, zombies y muertos para luego proponer soluciones que ayuden a la humanidad a sobrevivir. Para ello, te entregan la siguiente información clave que han logrado documentar: 

- Los humanos nacen a una tasa constante 𝛱 y mueren por causas naturales a una tasa proporcional a la cantidad de humanos, con constante de proporcionalidad 𝛿. 

- Los humanos pueden convertirse en zombies si son infectados. Esta transformación sucede a una tasa proporcional al número de humanos y al número de zombies, con constante de proporcionalidad 𝛽. 

- Los humanos pueden “matar” zombies a una tasa proporcional al número de humanos y al número de zombies, con constante de proporcionalidad 𝛼, haciéndolos desaparecer (no se suman a los muertos). 

- Por último, los muertos pueden “revivir” como zombies a una tasa proporcional al número de muertos, con constante de proporcionalidad 𝛾. 

Junto a tu equipo definen que las variables de estado apropiadas para describir este sistema son: cantidad de humanos ( _H_ ), cantidad de zombies ( _Z_ ) y cantidad de muertos ( _M_ ), y por ende, el espacio de estados estaría conformado por las triadas ( _H, Z, M_ ), en ℕ[!] . 

Para lograr su objetivo deben realizar las siguientes tareas y responder: 

- a. **Escribir las ecuaciones diferenciales** (balances) que describen la evolución temporal del número de humanos, zombies y muertos en función de los procesos que se han descrito. _(2 puntos)_ 

- b. **Analizar el estado estacionario del sistema** . ¿Qué condición(es) deben cumplirse para que el sistema llegue al equilibrio (es decir, cuando las poblaciones permanecen constantes)? Para simplificar el análisis, despreciar nacimientos y muertes naturales. Dado esto, discutan si es posible que humanos y zombies coexistan simultáneamente en ese estado. _(2 puntos)_ 

- c. **Consideren dos posibles estrategias** para reducir el impacto del apocalipsis: 

   - **Aislar a los zombies** (evitando que infecten a los humanos). 

   - **Destruir los cadáveres** (evitando que los muertos revivan como zombies). 

¿Cómo incorporarían cada una de estas estrategias en el modelo? Plantee los modelos asociados a cada una de las intervenciones. _(Hint: puede ser necesario plantear variables adicionales)(2 puntos)_ 

## **Pregunta 2: Imagina que tu ducha fuera automática** 

Cuando tomas una ducha, regulas manualmente la temperatura del agua girando la llave del agua caliente. Pero, ¿qué pasaría si existiera un sistema de control automático que ajustara la válvula por ti para mantener la temperatura que desees? 

En este problema, te invitamos a imaginar que tienes un sistema de control que mide la temperatura del agua y, dependiendo de la diferencia entre la temperatura que quieres y la del agua que sale, ajusta automáticamente la apertura de la válvula del agua caliente. 

En este sistema hipotético: 

- La apertura de la válvula se representa por el ángulo _m_ (en grados), que aumenta al girar en el sentido de las agujas del reloj. 

- El error es _e_ = (temperatura deseada − temperatura medida). 

- Cuando aumentas _m_ , entra más agua caliente. 

Se proponen dos posibles **leyes de control** para que el sistema ajuste la válvula automáticamente: 

## 1. **Ley de control proporcional** 

_m_ = _K*e_ , con _K_ > 0 constante proporcional. 

2. **Ley de control constante** 

_m_ = _m+_ , si _e_ > 0 0, si _e_ = 0 _-m+,_ si _e_ < 0 

Donde _m+_ es un valor constante positivo correspondiente a una apertura fija. 

- a. **Usando la ley de control proporcional:** Explica en detalle qué sucede en el sistema cuando cambia la temperatura del agua. ¿Cómo responde la apertura de la válvula? _(2 puntos)_ 

- b. **Usando la ley de control constante:** Explica en detalle qué sucede en el sistema cuando cambia la temperatura del agua. ¿Cómo se ajusta la válvula en este caso? _(2 puntos)_ 

- c. **Comparación** : ¿Qué diferencia hay entre ambas leyes de control? ¿Cuál es más similar a la que utilizamos en la realidad y por qué? _(2 puntos)_ 

- d. **Invirtiendo signos** : ¿Qué pasaría en el comportamiento del sistema si cambias el signo de _K_ y de _m+_ ? _(0.5 puntos bonus)_ 


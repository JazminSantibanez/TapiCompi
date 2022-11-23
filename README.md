# TapiCompi
 Proyecto final Diseño de Compiladores
 
 # Video Demo
[![Watch the video](https://img.youtube.com/vi/iSO22cvj0_Q/maxresdefault.jpg)](https://youtu.be/iSO22cvj0_Q)
 
 # Log de Avances

## Avance 0 - Propuesta  Final
Fecha de entrega: Sábado 8 de Octubre de 2022

Se desarrolló la propuesta final del proyecto la cual es la definición del lenguaje. Se definieron los tokens (tanto palabras reservadas como definiciones simples de tokens), los diagramas de sintaxis junto con su gramática formal y las principales consideraciones semánticas.

## Avance 1
Fecha de entrega: Lunes 3 de Octubre de 2022

Inicié la codificación del léxico y sintáxis en PLY para python. Terminé el léxico pero sólo hice ele equivalente de 2 diagramas de sintaxis porque no tuve mucho tiempo durante la semana.

## Avance 2 - Cubo semántico y semántica básica de variables
Fecha de entrega: Miércoles 12 de Octubre de 2022

Fecha de entrega: Miércoles 12 de Octubre de 2022
Terminé de escribir la gramática formal en código y realicé algunos ajustes en los tokens. Además, implementé el cubo semántico (usando un diccionario de diccionarios y una función para poder revisar el emparejamiento de los tipos).

## Avance 3
Fecha de entrega: Lunes 17 de Octubre de 2022

Se corrigieron todos los errores de recursión y shift/reduce de la gramática. Se pueden leer archivos de prueba y hacer el análisis sintáctico sin warnings.
Se comenzó a hacer un boceto del directorio de funciones y tablas de variables pero no se pasó a código por el momento.


## Avance 4
Fecha de entrega: Viernes 4 de Noviembre de 2022

Esta semana trabajé en el desarrollo del directorio de funciones y tablas de variables. 

Declaración de variables y funciones funciona correctamente (detecta doble declaracion).

Se generan cuadruplos correctos para los estatutos secuenciales: asignacion, leer y escribir.

Se generan cuadruplos correctos para expresiones aritmeticas básicas (sumar, restar, multiplicar y dividir), incluyendo paréntesis.

## Avance 5
Fecha de entrega: Lunes 7 de Noviembre de 2022

Se añadieron los puntos neurálgicos para decisiones (if) y ciclos (while). Se producen cuádruplos correctos para los estatutos mencionados. 
Modifiqué el formato de impresión de los cuadruplos para que se mostraran de forma más organizada.
Terminé los puntos neurálgicos y generación de cuádruplos para los operadores lógicos y relacionales.


## Avance 6
Fecha de entrega: Martes 15 de Noviembre de 2022

Se agregó do-while al lexico y semántica. Se generan cuádruplos para este estatuto.
Se generan cuadruplos correctos para las funciones, así como la dirección de las funciones.
Comencé la implementación del segmento de memoria (utilizando una clase que genera arreglos para cada tipo local y temporal, recibiendo como parámetro la cantidad de cada recurso) y del manejo de direcciones virtuales.

## Avance 7
Fecha de entrega: Lunes 21 de Noviembre de 2022

Se creó la tabla de constantes (diccionario optimizado a busqueda valor:dirección), se integró al análisis semántico para detectar constantes y guardarlas. Se añadió el uso de direcciones virtuales dfe las constantes para la máquina virtual. Implementación de máquina virtual para los códigos de operación de expresiones aritméticas ( y lógicas y relaciones), de estatutos secuenciales, ciclos, decisiones y módulos (con recursión). Se desarróllo la memoria y el contexto en la máquina virtual para poder hacer cambio de memorias entre llamadas de funciones.

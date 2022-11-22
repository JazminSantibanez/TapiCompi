# TapiCompi
 Proyecto final Diseño de Compiladores

## Avance 0 - Propuesta  Final
Fecha de entrega: Sábado 8 de Octubre de 2022

Se desarrolló la propuesta final del proyecto la cual es la definición del lenguaje. Se definieron los tokens (tanto palabras reservadas como definiciones simples de tokens), los diagramas de sintaxis junto con su gramática formal y las principales consideraciones semánticas.

## Avance 1
Fecha de entrega: Lunes 3 de Octubre de 2022

Progreso hasta entrega:
- Lexico terminado
- Parser: 2 diagramas de 26 aprox.

* Completo.

## Avance 2 - Cubo semántico y semántica básica de variables
Fecha de entrega: Miércoles 12 de Octubre de 2022

Progreso hasta entrega:
- Cubo semántico terminado (se usó un diccionario de diccionarios y una función para revisar el match de los tipos).
- Se arreglaron detalles en tokens y gramática formal (ya están terminados)
- Se comenzaron a escribir consideraciones básicas para la semántica.

Funciona el cubo semántico.

## Avance 3
Fecha de entrega: Lunes 17 de Octubre de 2022

Correcion de gramática en expresiones.
Funciona sin warnings.

Se realizaron pruebas y compila exitosamente.

## Avance 4
Fecha de entrega: Viernes 4 de Noviembre de 2022

Declaración de variables y funciones funciona correctamente (detecta doble declaracion).

Se generan cuadruplos correctos para los estatutos secuenciales: asignacion, leer y escribir.

Se generan cuadruplos correctos para expresiones aritmeticas básicas (sumar, restar, multiplicar y dividir), incluyendo paréntesis.

## Avance 5
Fecha de entrega: Lunes 7 de Noviembre de 2022

Se generan cuadruplos correctos para condicionales y ciclos: if, while.

## Avance 6
Fecha de entrega: Martes 15 de Noviembre de 2022

Se agrego do-while al lexico y semmántica. Se generan cuádruplos para este estatuto.

Se generan cuadruplos correctos para las funciones, así como la dirección de las funciones.
Se comenzó la implementación del segmento de memoria y del manejo de direcciones.

## Avance 7
Fecha de entrega: Lunes 21 de Noviembre de 2022

Se creó la tabla de constantes (diccionario optimizado a busqueda valor:dirección), se integró al análisis semántico para detectar constantes y guardarlas. Se añadió el uso de direcciones virtuales dfe las constantes para la máquina virtual. Implementación de máquina virtual para los códigos de operación de expresiones aritméticas ( y lógicas y relaciones), de estatutos secuenciales, ciclos, decisiones y módulos (con recursión). Se desarróllo la memoria y el contexto en la máquina virtual para poder hacer cambio de memorias entre llamadas de funciones.
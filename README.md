# TapiCompi
 Proyecto final Diseño de Compiladores
 
 ---
 
 # Manual de Usuario
 
  ## Requisitos del sistema
   * Se desarrolló utilizando Windows 10 y las pruebas fueron realizadas en el mismo.
   * Tener instalado Python 3.10
   
  ## Proceso de ejecución
  1. Situarse en la carpeta `/compiler`
  2. Ejecutar el archivo `TapiCompi.py` con el nombre de archivo (y su extensión) que se quiere compilar.
  
  Ejemplo de comandos para ejecutar el archivo test.tapi que se encuentra en la carpeta tests
 ```Shell Session
 cd Compiler
 python TapiCompi.py tests/test.tapi   
 ```
 
 ## Crear programas
 
 Para crear un programa que pueda ser leído y ejecutado por *TapiCompi* se debe seguir el siguiente orden (tomando en cuenta que los elementos en brackets son opcionales):
 
 ### Elementos básicos
 
 #### ID
 Un ID es un nombre que sirve para identificar variables y funciones.
 
 Para construir un ID válido se tiene que seguir la expresión regular: `[a-zA-Z][a-zA-Z0-9_]*`
 
 Es decir, debe comenzar por una letra (ya sea minúscula o mayúscula), seguida de cualquier combinación de letras, números o guión. 
 
 #### **Tipos de datos:**
 
 * Entero: Cualquier combinación de números de 1 al 9. Puede llevar el signos '-' para indicar un número negativo.
   ```
   1,  
   1278
   -1929
   ```
 * Flotante: Cualquier combinación de números de 1 al 9, seguida de un punto y de nuevo cualquier combinación de número del 1 al 9. Puede llevar el signos '-' para indicar un número negativo.
  ```
  3.18
  -901.32
  8128.0
  ```
 * Char: Un sólo carater alfabético, ya sea en minúscula o mayúscula. Debe ir entre  comillas sencillas.
 ```
 'a'
 'F'
 ```
 * Bool: Solo admite las palabras reservadas:
 ```
 True
 False
 ```
 
 
 ### Formato de archivo
```
 program id_nombre:
 
 [declaración de variables globales]
 
 [declaración de funciones]
 
 main()
 {
  [estatutos]
 }
```

### Variables
Sirve para declarar variables tanto globales como locales.

 - Las variables globales están declaradas después del id del programa pero antes de las funciones, fuera del espacio de main. 

 - Las variables locales están declaradas adentro de una función (incluyendo main) y solo existen dentro de dicho entorno.
```
var
tipo id
tipo id, id, ...
```
El tipo es uno de los 4 posibles en el lenguaje: `int`, `float`, `char`, `bool`.

Se pueden declarar múltiples variables del mismo tipo en una sola línea, separando los ids por comas. Asimismo, se pueden declarar variables de otro tipo indicando el nuevo tipo seguido de ids.

### Funciones

#### Declaración de funciones
Van después de la declaración de variables globales (si hay) y antes de la función main.

Puede ser de uno de los 4 tipos mencionados, o de tipo `void`.
```
func tipo id(tipo id, tipo id, ...)
{
 [declaracion de variables locales]
 [estatutos]
}
```
- Los parámetros son opcionales (puede tener 0, uno o varios). Funcionan como variables locales por lo que no puede repetirse un nombre como parámetro y como variable.
- Si una función tiene tipo diferente de void, esta debe tener el estatuto return dentro del cuerpo de la función y el valor resultante debe ser del mismo tipo  que la función.
- De forma similar, si es de tipo void, no puede haber un estatuto return.
- El estatuto return puede ir en cualquier orden entre los estatutos, pero la ejecución de la función se terminará una vez que se llegue al return.

#### Llamada a función
```
id ( arg, arg, ...)
```
Se escribe el nombre de una función, declarada previamente, seguido de  los argumentos a enviar, los cuales deben coincidir en cantidad y tipo (de acuerdo al orden) con los indicados en la declaración de la función.

### Estatutos

#### Asignación

```
var = valor
```
Del lado izquierdo debe ir una variable previamente declarada, seguida del signo igual '=' y después el valor a asignar, el cual puede venir de una expresión matemática, una llamada a función, una llamada a otra variable o constantes enteras y flotantes.

#### Leer
Guarda el valor ingresado en una variable.

```
read(var1, var2, ...)
```
Dentro de los parentesis puede haber desde una hasta múltiples variables que deben existir en la función (ya sea locales o globales). 

#### Escribir
Imprime en consola y deja un salto de línea al final.

```
print(string, constante_char, valor, ...)
```
Dentro de los parentesis puede haber desde una hasta múltiples variables que deben existir en la función (ya sea locales o globales), así como constantes tipo char o letreros (combinación de palabras dentro de dobles comillas " ).

#### Decisiones (if-else)
Sirve para tomar un camino u otro dependiendo de la expresión evaluada.

```
if ( expresion )
{
  [estatutos]
}
else
{
  [estatutos]
}
```
- El resultado de la expresión debe ser de tipo `bool`. 
- La parte `else` es opcional. 
- Si la expresión es verdadera, entra a ejecutar los estatutos escritos dentro de los corchetes.
Si es falsa, ejecuta los estatutos dentro de los corchetes de else (en caso de existir).

#### Ciclo while

```
Repite las instrucciones mientras se cumpla la expresión evaluada. Primero evalua y después ejecuta.
while ( expresion )
{
  [estatutos]
}
```
- El resultado de la expresión debe ser de tipo `bool`. 
- Si la expresión es verdadera, se ejecutan los estatutos escritos dentro de los corchetes. Si es falsa, se brinca la sección de los corchetes.


#### Ciclo do while
Repite las instrucciones mientras se cumpla la expresión evaluada. A diferencia del while, primero ejecuta y después evalua, por lo que siempre se ejecuta al menos una vez.
```
do
{
  [estatutos]
} while ( expresion )
```
- El resultado de la expresión debe ser de tipo `bool`. 
- Si la expresión es verdadera, se ejecutan los estatutos escritos dentro de los corchetes. Si es falsa, se brinca la sección de los corchetes.

#### Operaciones
Ordenadas de mayor a menor presedencia (de arriba a abajo, y de izquierda a derecha):
* Logicas: & (and) y | (or)
* Relacionales: >, <, >=, <=, ==, != (todas tienen el mismo nivel de prioridad).
* Aritméticas: * y /, + y -

Las operaciones relacionales y lógicas tienen como resultado valores tipo `bool`.
  
 ---
 
 # Video Demo
[![Watch the video](https://img.youtube.com/vi/iSO22cvj0_Q/maxresdefault.jpg)](https://youtu.be/iSO22cvj0_Q)
 
 ---
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

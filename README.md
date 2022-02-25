# Recopilatorio de herramientas de cifrado
Esta aplicación es un conjunto de diferentes cifrados, tanto clásicos como modernos, enfocados a la entrada y salida de texto. Entre los cifrados incluidos esta el cifrado Atbash, el cifrado de Vigenère, el cifrado de Vernam o el cifrado RC4.

Para cada uno de estos cifrados, en la herramienta se encuentra, ademas del cifrador, un descifrador.

Además, existe una herramienta para la traducción de binario a texto y viceversa.

## Ejecución
Es requisito indispensable tener python instalado en la máquina de ejecución, o ejecutar el fichero .exe directamente.
```
python GUI.py
```
## Cifrado Atbash
El cifrado Atbash es uno de los cifrados clásicos y hace uso del alfabeto hebreo para realizar un cifrado por sustitución.

Este cifrado seguirá la siguiente tabla:

 | Letra | Letra cifrada |
 | -- | -- |
 | a | z |
 | b | y |
 | c | x |
 | d | w |
 | e | v |
 | f | u |
 | g | t |
 | h | s |
 | i | r |
 | j | q |
 | k | p |
 | l | o |
 | m | n |
 | n | m |
 | o | l |
 | p | k |
 | q | j |
 | r | i |
 | s | h |
 | t | g |
 | u | f |
 | v | e |
 | w | d |
 | x | c |
 | y | b |
 | z | a |

## Cifrado de Vigenère
El cifrado de Vigenere es un sistema de cifrado polialfabético usado para alternar el empleo de las sustituciones-clave durante la operación de cifrado. Con esta técnica, la misma letra de origen se transforma en distintas letras cifradas, en función de la posición que ocupa dentro del mensaje.

El cifrado de Vigenere se puede aplicar utilizando el siguiente cuadro:

```
A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z
B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A
C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B
D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C
E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C D
F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C D E
G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C D E F
H I J K L M N Ñ O P Q R S T U V W X Y Z A B C D E F G
I J K L M N Ñ O P Q R S T U V W X Y Z A B C D E F G H
J K L M N Ñ O P Q R S T U V W X Y Z A B C D E F G H I
K L M N Ñ O P Q R S T U V W X Y Z A B C D E F G H I J
L M N Ñ O P Q R S T U V W X Y Z A B C D E F G H I J K
M N Ñ O P Q R S T U V W X Y Z A B C D E F G H I J K L
N Ñ O P Q R S T U V W X Y Z A B C D E F G H I J K L M
Ñ O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N Ñ
P Q R S T U V W X Y Z A B C D E F G H I J K L M N Ñ O
Q R S T U V W X Y Z A B C D E F G H I J K L M N Ñ O P
R S T U V W X Y Z A B C D E F G H I J K L M N Ñ O P S
S T U V W X Y Z A B C D E F G H I J K L M N Ñ O P Q R
T U V W X Y Z A B C D E F G H I J K L M N Ñ O P Q R S
U V W X Y Z A B C D E F G H I J K L M N Ñ O P Q R S T
V W X Y Z A B C D E F G H I J K L M N Ñ O P Q R S T U
W X Y Z A B C D E F G H I J K L M N Ñ O P Q R S T U V
X Y Z A B C D E F G H I J K L M N Ñ O P Q R S T U V W
Y Z A B C D E F G H I J K L M N Ñ O P Q R S T U V W X
Z A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y
```
En este cifrado, se hace uso de una palabra-clave. Para explicar el funcionamiento, observemos el siguiente ejemplo, donde la palabra-clave es `"LOREM"`:

- `EL-PAPA-SERA-TRAICIONADO`
- `LO-REML-OREM-LOREMLOREML`

En este caso, la clave se termina por truncar, y no cifraremos los espacios en blanco. Si vamos a cifrar, la primera letra del mensaje la buscaremos en la primera fila, y la primera letra de la clave en la primera columna. Si buscamos la intersección entre ambas, nos dará la letra cifrada.

Si repetimos la operación, obtenemos el siguiente mensaje cifrado:

- `PZ GEBL GVVM EFRMOTCEEPZ`
## Cifrado de Vernam
El cifrado de Vernam se basa en la sustitución polialfabetica mediante una clave generada de una forma aleatoria. Como la generación aleatoria sigue siendo, a dia de hoy, uno de los problemas informáticos que no hemos sido capaces de solventar, en este caso, se trata de una generación pseudoaleatoria basada en smillas.

El funcionamiento del cifrado se basa en la suma binaria entre el mensaje a cifrar y una cadena aleatoria binaria, obteniendo como salida la clave cifrada.

Este cifrado tiene secreto perfecto, es decir, teóricamente es irrompible. Sin embargo, para poder realizar el descifrado de la cadena necesitamos la clave original usada para cifrar el mensaje, con lo que no nos es realmente útil, ya que si fueremos capaces de transmitir la clave de forma segura, no necesitamos un cifrado, ya que podríamos simplemente transmitir el mensaje a través de dicho canal seguro.
## Cifrado RC4
El cifrado RC4 es uno de los sistemas de cifrado en flujo más utilizados, aún habiendo sido excluido de cualquier estandar de alta seguridad.

Este cifrado se basa en los siguientes dos algoritmos, uno se encarga de generar el estado inicial a partir de una clave, y el otro de generar el byte que usaremos para realizar la suma binaria con lo que vayamos a cifrar:

- Key Scheduling Algorithm:
    ```
    for i = 0 to 255 {
        S[i] = i;
        K[i] = seed[i mod seed.length];
    }
    j = 0;
    for i = 0 to 255 {
        j = (j + S[i] + K[i]) mod 256;
        swap(S[i], S[j]);
    }
    ```
- Pseudo.Random Generation Algorithm:
    ```
    i = 0;
    j = 0;
    for everyByteOfData {
        i = (i + 1) mod 256;
        j = (j + S[i]) mod 256;
        swap(S[i], S[j]);
        t = (S[i] + S[j]) mod 256;
        Use S[t] value
    }
    ```
## Contribuir
Las solicitudes de modificación son bienvenidas. Para los cambios importantes, por favor, abra una cuestión en primer lugar para discutir lo que le gustaría cambiar.

Por favor, asegúrese de actualizar las pruebas según corresponda.

## Encontrar errores
Por favor, si encuentra algún error, haga uso del apartado de errores encontrados [Github Issues](https://github.com/FNDme/cryptography-tools/issues) y trataré de encargarme de ello lo antes prosible.

## Créditos
Este código fuente ha sido desarrollado por [Gabriel Luis Freitas](https://github.com/FNDme/), actual estudiante de Ingeniería Informática en la Universidad de La Laguna para la asignatura de [Seguridad en Sistemas Informáticos](https://www.ull.es/apps/guias/guias/view_guide_course/2122/139263523/)

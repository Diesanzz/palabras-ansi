# Detector de palabras reservadas ANSI C con DFA

Proyecto de Teoría de la Computación.

Este programa reconoce palabras reservadas del lenguaje ANSI C utilizando un Autómata Finito Determinista.

El autómata procesa un archivo fuente carácter por carácter y registra las transiciones realizadas.

---------------------

## Características

- Implementación de un DFA.
- Lectura de archivo fuente `.c`.
- Procesamiento carácter por carácter.
- Reconocimiento de palabras reservadas ANSI C.
- Registro de línea y columna.
- Generación de historial completo de transiciones.
- Generación de tabla de transiciones.
- Visualización dinámica de la ejecución del autómata.
- Sin expresiones regulares.
- Sin búsqueda directa de palabras.

-----------------------

## Palabras reservadas reconocidas

`txt
auto, break, case, char, const, continue,
default, do, double, else, enum, extern,
float, for, goto, if, int, long,
register, return, short, signed, sizeof,
static, struct, switch, typedef, union,
unsigned, void, volatile, while
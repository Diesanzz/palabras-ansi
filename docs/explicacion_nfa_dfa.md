# Explicación formal del NFA y DFA

## Proyecto

El objetivo del proyecto es construir un programa que reconozca palabras reservadas del lenguaje ANSI C utilizando autómatas finitos.

El programa no utiliza expresiones regulares ni funciones de búsqueda directa de palabras. El reconocimiento se realiza mediante un Autómata Finito Determinista que procesa el archivo fuente carácter por carácter.

-----------------------------

# Palabras reservadas ANSI C utilizadas

El lenguaje reconocido por el autómata está formado por las siguientes palabras reservadas:

`txt
auto
break
case
char
const
continue
default
do
double
else
enum
extern
float
for
goto
if
int
long
register
return
short
signed
sizeof
static
struct
switch
typedef
union
unsigned
void
volatile
while
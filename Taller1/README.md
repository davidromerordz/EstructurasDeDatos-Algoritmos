### Ejercicio a desarrollar
Se desea implementar una simulación de fantasmas moviéndose por un laberinto
(inspirada en Pacman). Para tal efecto se requiere implementar el ADT Laberinto
representado por una matriz de 0,1 donde el 0 representa camino y el 1 representa muro.
El constructor de Laberinto acepta un arreglo de String donde cada fila contienen los
0,1 que indican si hay camino o muro. Un método getPosicion(x,y) devuelve si hay
camino/muro en una posición del Laberinto. Un método dibujaLaberinto() dibuja el
laberinto.

Un segundo ADT Fantasma representa los fantasmas que se mueven por el laberinto. Un
fantasma se describe por su posición actual (x,y) y la dirección en la que se mueve
(norte, sur, este, oeste). Para este ejercicio, el fantasma se mueve en la dirección actual
hasta encontrar un muro. En ese momento, elige una nueva dirección al azar entre
aquellas donde hay camino. El Fantasma implementa un método mover() que mueve el
fantasma en la dirección actual o cambia de dirección si encuentra un muro. Un método
dibujar() dibuja el fantasma en pantalla.

Finalmente, un ADT Simulacion contiene una instancia de Laberinto y un Bag con n
instancias de Fantasma. También contiene el main del programa, donde se crean las
instancias de todos los ADTs y tiene un método run que hace el movimiento de los
fantasmas hasta que el usuario presione una tecla para salir del programa.

Ejemplos de laberintos:

Python
data = [
 "1111111111111111111111111111111",
 "1010100010001000100010001000101",
 "1010101110111011101110111011101",
 "1000001000100000100000000000101",
 "1011111011111011101010101011101",
 "1000000000000000001010101010001",
 "1011101010101011111111111110101",
 "1000101010101000000000001000101",
 "1011101011111010101010111011111",
 "1010001000100010101010000000001",
 "1110111011101011111110111110111",
 "1000100010001000001000000010001",
 "1111111111111111111111111111111"
 ]

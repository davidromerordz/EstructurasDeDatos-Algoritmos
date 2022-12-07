### Ejercicios a desarrollar
1. Se requiere poder clasificar las películas por el año de publicación. Para tal
efecto se desea crear una tabla de símbolos utilizando como llave el año de
publicación y como valor un Bag/List de Película:
ST<Integer, Bag<Pelicula>> clasificarPorAño(Pelicula[] peliculas)
  
2. Asumiendo que la colección tiene N películas, estimar el orden de
crecimiento del método clasificarPorAño.
  
3. Se necesita determinar las top-M películas de cada año en función de su
avg_vote. Utilizando una cola de prioridad de forma que este proceso se
pueda realizar de forma eficiente implementar un método que cree una
nueva tabla de símbolos con la cola de prioridad de las top-M películas para
cada año:
ST<Integer, MinPQ<Pelicula>> topMxAño(
ST<Integer, Bag<Pelicula>> pelXaño,
int m)
  
4. En función del número de películas N y el número M de películas top,
estimar el orden de crecimiento del método topMxAño.
  
5. Implementar el método main en la clase Taller4 que obtenga las 10
películas top de cada año e imprima el listado en pantalla.

### Ejercicios a desarrollar

Para los efectos de este ejercicio se desea trabajar sobre los datos de la colección
de películas de IMDb que se encuentra en los archivos anexos. Cada reglón
corresponde a una película y los distintos atributos se encuentran separados por
commas (Comma Separated Values – CSV).

1. Definir un ADT Película que contenga los atributos de una película.
Considerar todos los atributos disponibles en la colección. Utilizar tipos de
datos acorde con el respectivo atributo. Incluir una versión sobre-escrita del
método toString.

2. Implementar la interface Comparable en el ADT Película. Se deben
comparar películas con base en su avg_vote.

3. Definir una función de biblioteca (método estático) leerCSV que lea los
datos de la colección y los retorne como un arreglo de objetos Película.

4. Se desea obtener el listado en orden descendiente por avg_vote. Definir el
método listarPorRating para realizar esta tarea. Incluir en el código la
medición del tiempo necesario para ordenar los datos (sin incluir I/O).

5. Si se desea utilizar campos distintos para efectos de la ordenación, la
solución más apropiada es implementar la interface Comparator como una
clase aparte (puede ser clase interna o clase anónima). Implementar dos
Comparators para el ADT Película: Uno por título (original_title) y otro por
fecha de publicación (date_published).

6. Implementar un método listarPorComparador que acepte como
parámetros el arreglo de películas y el comparador a utilizar. Se debe
imprimir el listado ordenado según el comparador indicado.

7. Se desea comparar la eficiencia de distintos métodos de ordenación. Para
tal efecto se requiere un conjunto de métodos medirTiempoALG que acepte
un comparador, ordene los datos y retorne el tiempo requerido (No realizar
operaciondes de I/O durante la medición de los tiempos). Implementar 3
casos para realizar la medición: Un algoritmo cuadrático, uno linearitmético,
y uno propio de las bibliotecas del lenguaje.

8. Realizar mediciones de tiempo para tres métodos seleccionados utilizando
el comparador por título. Realizar K=20 mediciones por caso para obtener
promedios más confiables. Tabular los resultados obtenidos en cada caso y
comparar. Nota: Hacer un StdRandom.shuffle antes de cada medición para
evitar que los datos lleguen en orden.

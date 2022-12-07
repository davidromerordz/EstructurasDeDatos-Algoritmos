import pelicula
from pelicula import Pelicula 

if __name__ == '__main__':

   peliculas = pelicula.read_csv(r"C:\Users\david\Downloads\IMDb movies.csv")

   # Punto 4: la ejecucion de listarPorRating tarda aprox. 1 minuto, ya que se usa Merge Sort
   """
   Pelicula.listarPorRating(peliculas)
   for i in range(10):
      print(peliculas[i])

   """

   # Punto 5: listamos las peliculas por titulo y fecha
   """
   Pelicula.comparator(peliculas)
   for i in range(10):
      print(peliculas[i])
   
   """

   # Punto 6: podemos listar por "promedio":avg_vote, "titulo":title, "fecha":date_published
   """
   Pelicula.listarPorComparador(peliculas, "promedio")
   for i in range(10):
      print(peliculas[i])

   """

   # Punto 7-8: el algoritmo cuadrático tarda más de una hora :(
   """
   for i in range(20):
      Pelicula.medirTiempoALGpython(peliculas)

   for i in range(20):
      Pelicula.medirTiempoALGlinAr(peliculas)

   for i in range(20):
      Pelicula.medirTiempoALGcuadratico(peliculas)
   
   """




   




   

    

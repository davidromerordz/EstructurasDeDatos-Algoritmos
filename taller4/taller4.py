import pelicula
from pelicula import Pelicula 
from symtable import SymbolTable
from algs4.min_pq import MinPQ
from algs4.bst import BST
from algs4.bag import Bag



if __name__ == '__main__':

   peliculas = pelicula.read_csv(r"C:\Users\david\Downloads\IMDb movies.csv")



   # PUNTO 1: 
   def clasificarPorAño(pelis):

      st={} 

      for n in pelis:
         if n.year not in st.keys():
            st[n.year] = [n]
         else:
            st[n.year].append(n)

      return st

      
   # Punto 3:
   def topMxAño(st, m):

      st2={}

      for i in st:
         cola=MinPQ()
         conteo=0
         for j in st.get(i):
            if conteo < m:
               cola.insert(j)
            elif j > cola.min():
               cola.del_min()
               cola.insert(j)
            conteo+=1
         st2[i] = cola

      return st2



   # Punto 5:
   def imprimirPelis(top):

      final = {}  
      
      for n in top:
         lista = []
         
         while (top.get(n).size()>0):
            lista.append(top.get(n).del_min())
         lista.reverse()
         
         final[n] = lista
      
      print(final)



   st = clasificarPorAño(peliculas)
   top = topMxAño(st,10)
   imprimirPelis(top)
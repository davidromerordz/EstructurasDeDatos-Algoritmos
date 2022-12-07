
from Laberinto import Laberinto
import stddraw
import random


class Fantasma:

    
    
    
    #Constructor
    def __init__(self):
     
     self.posicion = Laberinto()

     self.xLaberinto = 9
     self.yLaberinto = 9

     self.xFantasma = 9
     self.yFantasma = 9

     self.direccion = random.choice(["Norte", "Sur", "Este", "Oeste"])

        

    #metodo mover
    def mover(self):

      if self.direccion == "Norte" and self.posicion.getPosicion(self.xFantasma-1, self.yFantasma):
            self.xFantasma -= 1
            self.yLaberinto -= 1
      elif self.direccion == "Norte" and self.posicion.getPosicion(self.xFantasma-1, self.yFantasma) == False: 
            self.direccion = random.choice(["Norte", "Sur", "Este", "Oeste"])

      
      if self.direccion == "Sur" and self.posicion.getPosicion(self.xFantasma+1, self.yFantasma):
            self.xFantasma += 1
            self.yLaberinto += 1
      elif self.direccion == "Sur" and self.posicion.getPosicion(self.xFantasma+1, self.yFantasma) == False:
            self.direccion = random.choice(["Norte", "Sur", "Este", "Oeste"])

                                       
      if self.direccion == "Este" and self.posicion.getPosicion(self.xFantasma, self.yFantasma+1):
            self.yFantasma +=1
            self.xLaberinto += 1
      elif  self.direccion == "Este" and self.posicion.getPosicion(self.xFantasma, self.yFantasma+1) == False: 
            self.direccion = random.choice(["Norte", "Sur", "Este", "Oeste"])


      if self.direccion == "Oeste" and self.posicion.getPosicion(self.xFantasma, self.yFantasma-1):
            self.yFantasma -=1
            self.xLaberinto -= 1
      elif self.direccion == "Oeste" and self.posicion.getPosicion(self.xFantasma, self.yFantasma-1) == False:
            self.direccion = random.choice(["Norte", "Sur", "Este", "Oeste"])

      return self.yFantasma, self.xFantasma


    #metodo dibujar
    def dibujar(self, color):              
        stddraw.setPenRadius(1)
        stddraw.setXscale(0,31)
        stddraw.setYscale(1,14)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(self.xLaberinto, 13-self.yLaberinto, 1, 1)


# Pruebas unitarias
if __name__ == "__main__":
      prueba = Fantasma()
      assert prueba.xFantasma == 9 and prueba.yFantasma == 9
      print("Dirección y coordenadas: {0}".format(prueba.mover()))
      prueba.mover()
      assert prueba.xFantasma != 9 or prueba.yFantasma != 9
      print("Dirección y coordenadas: {0}".format(prueba.mover()))


      




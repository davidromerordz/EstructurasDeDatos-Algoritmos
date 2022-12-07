from Laberinto import Laberinto
from Fantasma import Fantasma
from algs4.bag import Bag
import stddraw



class Simulacion:

    def __init__(self):
        self.laberinto = Laberinto()
        self.cola = Bag()
        fantasma1 = Fantasma()
        fantasma2 = Fantasma()
        fantasma3 = Fantasma()
        fantasma4 = Fantasma()

        self.cola.add(fantasma1)
        self.cola.add(fantasma2)
        self.cola.add(fantasma3)
        self.cola.add(fantasma4)



    def run(self):


        self.laberinto.dibujaLaberinto()


        


        while not stddraw.hasNextKeyTyped():
            for i in self.cola:
                i.dibujar(stddraw.WHITE)
                i.mover()
                i.dibujar(stddraw.RED)
            stddraw.show(200)

              


if __name__ == '__main__':

    simulacion = Simulacion()
    simulacion.run()



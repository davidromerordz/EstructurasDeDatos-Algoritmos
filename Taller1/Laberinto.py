import stddraw 


class Laberinto:

    #Constructor
    def __init__(self):

        #matriz de 0,1
        self._data = [
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
            "1111111111111111111111111111111" ]

    #método obtener la posición
    def getPosicion(self, x,y):
        self._data= [list(map(int, i)) for i in self._data]  #convierto la matriz en numeros
        if self._data[x][y] == 0:
            return True
        else:
            return False


    #método dibujar laberinto  
    def dibujaLaberinto(self):

        self._data= [list(map(int, i)) for i in self._data]  #convierto la matriz en numeros

        for i in range(len(self._data)):
            for j in range(len(self._data[0])):            
                if self._data[i][j] == 1:
                    stddraw.setPenRadius(1)
                    stddraw.setXscale(0,31)
                    stddraw.setYscale(1,14)
                    stddraw.setPenColor(stddraw.BLACK)
                    stddraw.filledRectangle(j, len(self._data) - i, 1,1)
                else: 
                    stddraw.setPenRadius(1)
                    stddraw.setXscale(0,31)
                    stddraw.setYscale(1,14)
                    stddraw.setPenColor(stddraw.WHITE)
                    stddraw.filledRectangle(j, len(self._data) - i, 1,1)
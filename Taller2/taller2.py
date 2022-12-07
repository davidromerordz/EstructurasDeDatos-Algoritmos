from Matriz import Matriz
import time

if __name__ == '__main__':

    #Matriz 12x12
    matriz1 = Matriz([[2,3,4,5,7,8,3,7,4,1,4,5],[5,6,7,5,3,4,6,2,3,1,2,9],[8,9,10,5,1,4,8,0,8,2,9,1],
    [2,3,4,6,9,2,1,5,4,0,3,5],[2,3,4,6,9,1,4,0,3,5,5,2],[2,3,4,6,9,0,5,4,4,6,6,5],[5,6,7,5,3,4,6,2,8,9,7,6], 
    [5,6,7,5,3,4,6,1,7,5,5,6],[5,6,7,5,3,4,6,2,3,5,6,3], [5,6,7,5,3,4,6,2,3,4,6,2],[2,3,4,6,9,0,5,4,4,6,6,4], 
    [2,3,4,6,9,0,5,4,4,6,6,6]])
    
    comienzo = time.time()
    matriz1.potencia(1000)
    final = time.time()
    print(f'El algoritmo Potencia de una matriz tarda: {final - comienzo} segundos.')


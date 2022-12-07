import numpy as np

class Matriz:

    def __init__(self, matriz = []):

        self.matriz = matriz
        self.filas = len(self.matriz)
        self.columnas = len(self.matriz[0])     

        
    def __iter__(self):
        return iter(self.matriz)


    def __str__(self):
        return str(self.matriz)
    
    

    def __eq__(self, otraMatriz):
         return self.matriz == otraMatriz.matriz
        
   

    def hashIDs(self, id1, id2):
        """
        Devuelve el hashCode del String resultante
        de concatenar los ID de los miembros del equipo módulo 5. 
        """
        self.id1 = id1
        self.id2 = id2

        self.cadena = str(self.id1) + str(self.id2)
        self.codHash = hash(int(self.cadena)) % 5

        return self.codHash



    def suma(self, otraMatriz):
        if self.filas == otraMatriz.filas and self.columnas == otraMatriz.columnas:

            resultado = []

            for i in range(self.filas):
                resultado.append([])
                for j in range(self.columnas):
                    resultado[i].append(self.matriz[i][j] + otraMatriz.matriz[i][j])
            return Matriz(resultado)
        else:
            return None


    def producto(self, otraMatriz):
        if self.filas == otraMatriz.columnas:
        
            resultado = []

            for i in range(self.filas):
                resultado.append([0]*otraMatriz.columnas)

            for i in range(self.filas):
                for j in range(otraMatriz.columnas):
                    resultado[i][j] = 0
                    for k in range(self.columnas):
                        resultado[i][j] += self.matriz[i][k] * otraMatriz.matriz[k][j]
            return Matriz(resultado)
        else: 
            return None

    
    def potencia(self, exp):   

        if exp == 1:
            return self.matriz
        elif exp == 2:
            return self.producto(self)
        else:
            resultado = self.producto(self)
            for i in range(exp-2):
                resultado = resultado.producto(self)
            return resultado



# Pruebas Unitarias:
if __name__ == '__main__':
    
    
    matriz1 = Matriz([[2,3,4],[5,6,7],[8,9,10]])
    matriz2 = Matriz([[2,3,4],[5,6,7],[8,9,10]])
    matriz3 = Matriz([[2,9,1],[1,7,3],[8,1,5]])

    #Prueba de equals
    assert matriz1 == matriz2
    #Prueba de suma()
    assert (np.array(matriz1.matriz)+np.array(matriz3.matriz) == matriz1.suma(matriz3).matriz).all()  
    #Prueba de producto()
    assert (np.matmul(np.array(matriz1.matriz), np.array(matriz3.matriz)) == matriz1.producto(matriz3).matriz).all()
    #Prueba de potencia()
    assert (np.linalg.matrix_power(np.array(matriz1.matriz), 5) == matriz1.potencia(5).matriz).all()

    
    


    

    

    

    

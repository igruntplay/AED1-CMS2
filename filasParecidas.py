from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

# ESTA INCOMPLETO!!

def filasParecidas(matriz: List[List[int]]) -> bool :
  for n in matriz:
    if filasParecidasAanterior(matriz,n):
      return True
  return False

def filasParecidasAanterior(matriz:List[List[int]], n:int)-> bool :
  for i in range(1,len(matriz)):
    if not filaAnteriorMasN(matriz,i,n):
      return False
  return True

def filaAnteriorMasN(matriz: List[List[int]], i:int, n:int) -> bool : 
  for j in range(len(matriz[0])):
    if matriz[i][j] != matriz[i-j][j]+n:
      return False
  return True




if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))
from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
    longitud_maxima = 0
    for i in range(len(l)): # Itero sobre los indices de la lista desde cero
        for j in range(i, len(l)): # Recorre de j hasta i
            if todosIguales(l, i, j):
                longitud_meseta = j - i + 1 # si se cumple actualiza
                if longitud_meseta > longitud_maxima:
                    longitud_maxima = longitud_meseta
    return longitud_maxima
# Verifica que exista la meseta de la longitud en la lista
def hayMesetaDeLong(l: List[int],n:int)-> bool :
  for i in range(len(l)):
    for j in range(i, len(l)):
      if j-i + 1 == n and todosIguales(l,i,j):
        return True
  return False

## Verifica que todos los elementos de l entre i, j sean iguales
def todosIguales(l: List[int],i:int,j:int)-> bool :
  for k in range(i,j+1):
    if l[k] != l[i]:
      return False
  return True

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))
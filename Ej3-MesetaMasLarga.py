from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
    longitudMaxima:int = 0
    for i in range(len(l)): # Itero sobre los indices de la lista desde cero
        for j in range(i, len(l)): # Recorre de j hasta i
            # longitudMeseta es la longitud de la sub-lista actual que se verifica.
            longitudMeseta:int = j - i + 1
            if hayMesetaDeLong(l, longitudMeseta) and not hayMesetaDeLong(l, longitudMeseta + 1):
              # Actualizamos la longitud de la meseta si se cumple la condición    
                longitudMeseta:int = j - i + 1 # si se cumple actualiza
                if longitudMeseta > longitudMaxima:
                    longitudMaxima = longitudMeseta
    return longitudMaxima
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
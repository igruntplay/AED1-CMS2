from typing import Dict, List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
    # Crea un diccionario donde las claves son los lugares de origen y los valores son los destinos.
    mapa_vuelos: Dict[str, str] = {vuelo[0]: vuelo[1] for vuelo in vuelos}

    ciudad_actual: str = origen  # Inicia en la ciudad origen.
    num_vuelos: int = 0  # Inicializa el contador de vuelos tomados.
    
    while True:  # Continúa hasta que se encuentre con un return.
        if ciudad_actual not in mapa_vuelos:  # Si la ciudad actual no está en el mapa de vuelos,
            return -1  # no se puede llegar al destino desde la ciudad actual, así que retorna -1.
        ciudad_actual = mapa_vuelos[ciudad_actual]  # Actualiza la ciudad actual al destino del vuelo actual.
        num_vuelos += 1  # Incrementa el contador de vuelos tomados.
        if ciudad_actual == destino:  # Si la ciudad actual es el destino,
            return num_vuelos  # retorna el número de vuelos que se deben tomar para llegar al destino.


if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))
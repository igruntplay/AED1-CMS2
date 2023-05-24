import sys

def quienGana(j1: str, j2: str) -> str : 
      if j1 == "Piedra" and j2 == "Tijera":
        return "gana j1"
      elif j1 == "Tijera" and j2 == "Papel":
        return "gana j1"
      elif j1 == "Papel" and j2 == "Piedra":
        return "gana j1"
      elif j2 == "Piedra" and j1 == "Tijera":
        return "gana j2"
      elif j2 == "Tijera" and j1 == "Papel":
        return "gana j2"
      elif j2 == "Papel" and j1 == "Piedra":
        return "gana j2"
      else:
        return "Empate"


if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))
def quienGana(j1:str, j2:str) -> str:
    if gana(j1, j2):
        return "Jugador1"
    elif gana(j2, j1):
        return "Jugador2"
    else:
        return "Empate"

def gana(j1:str, j2:str) -> bool:
    return piedraGanaAtijera(j1, j2) or tijeraGanaAPapel(j1, j2) or papelGanaAPiedra(j1, j2)

def piedraGanaAtijera(j1:str, j2:str) -> bool:
    return j1 == "Piedra" and j2 == "Tijera"

def tijeraGanaAPapel(j1:str, j2:str) -> bool:
    return j1 == "Tijera" and j2 == "Papel"

def papelGanaAPiedra(j1:str, j2:str) -> bool:
    return j1 == "Papel" and j2 == "Piedra"

print(quienGana("Piedra", "Tijera"))  # Debería imprimir "Jugador1"
print(quienGana("Tijera", "Piedra"))  # Debería imprimir "Jugador2"
print(quienGana("Papel", "Papel"))  # Debería imprimir "Empate"
print(quienGana("Piedra", "Papel"))  # Debería imprimir "Jugador2"

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

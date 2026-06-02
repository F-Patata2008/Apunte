import random

# PROBLEMA 1: Sistema de Votaciones

print("--- SISTEMA DE VOTACIONES ---")
c1 = 0
c2 = 0
c3 = 0

while True:
    voto = int(input("Ingrese numero: "))

    if voto == 0:
        break
    elif voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    else:
        print("Numero inválido, ignorado")

total = c1 + c2 + c3

print("\n--- RESULTADOS ---")
if total > 0:
    print(f"Candidato 1: {c1} votos {int((c1/total)*100)}%")
    print(f"Candidato 2: {c2} votos {int((c2/total)*100)}%")
    print(f"Candidato 3: {c3} votos {int((c3/total)*100)}%")
else:
    print("No se registraron votos.")


# PROBLEMA 2: Cachipún

print("\n\n--- JUEGO DE CACHIPÚN (Al mejor de 3) ---")
print("Opciones: 1 (Papel), 2 (Tijeras), 3 (Piedra)")

c = 0  # Victorias del computador
u = 0  # Victorias del usuario

while u < 3 and c < 3:
    usuario = int(input("\nIngrese su jugada (1, 2 o 3): "))

    if usuario not in [1, 2, 3]:
        print("Jugada inválida, intenta de nuevo.")
        continue

    computador = random.randint(1, 3)
    print(f"El computador jugó: {computador}")

    # LÓGICA DE ARITMÉTICA MODULAR O(1), Mas rapida de implementar, y de facil lectura
    # Si (usuario - computador) % 3 == 1 -> Gana el usuario
    # Si (usuario - computador) % 3 == 2 -> Gana el computador
    # Si (usuario - computador) % 3 == 0 -> Empate

    resultado = (usuario - computador) % 3

    if resultado == 0:
        print("empate")
    elif resultado == 1:
        print("gana usuario")
        u += 1
    elif resultado == 2:
        print("gana computador")
        c += 1

print("\n--- JUEGO TERMINADO ---")
if u == 3:
    print(f"¡Felicidades! Ganaste la serie {u} a {c}.")
else:
    print(f"Perdiste. El computador ganó la serie {c} a {u}.")

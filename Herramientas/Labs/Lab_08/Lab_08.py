def clasifica_numeros(x):
    if x > 0:
        return "Positivo"
    elif x < 0:
        return "Negativo"
    else:
        return "Cero";


def bisiesto(a):
    if a % 4 == 0:
        if a % 400 == 0:
            return "bisiesto"
        elif a % 100 == 0:
            return "No bisiesto"
        else:
            return "bisiesto"
    else:
            return "No bisiesto"


def clasifica_trianagulos (a, b, c):
    if (a + b > c) or (b + c > a) or (c + a > b):
        if a==b and a== c:
            return "Equilatero"
        if (a == b and a !=c) or (a == c and a != b) or (b == c and a != b):
            return "Isóceles"
        else:
            return "Escaleno"
    else:
        return "No es Triangulo"



print(clasifica_numeros(float(input("Ingresa un numero:\n"))))
print(bisiesto(int(input("Ingresa un año\n"))))
print("Ingresa 3 numeros separados por un salto de linea:")
print(clasifica_trianagulos(int(input()),int(input()),int(input())))


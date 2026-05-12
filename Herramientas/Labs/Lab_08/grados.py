def notas(nota):
    if nota < 4.0:
        return "Reprobado"
    elif nota < 5.0:
        return "Aprobado"
    elif nota < 6.0:
        return "Aprobado con Distinción"
    else:
        return "Aporbado con Distinción Máxima"


nota = float(input("Ingrese su nota de Defensa de Tesis:\n"))
print(notas(nota))

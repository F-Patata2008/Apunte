alt =[70, 63, 72, 62, 66, 70, 74, 65, 62, 67, 65, 68]
pes =[155, 150, 180, 135, 156, 168, 178, 160, 132, 145, 139, 152]

x =[]
for a in alt:
    x.append(a * 0.0254)

y =[]
for a in pes:
    y.append(a * 0.45)

a = 0
aa = 0
b = 0
ab = 0
n = len(x)

for i in range(n):
    a += x[i]
    aa += x[i] * x[i]
    b += y[i]
    ab += x[i] * y[i]

d = (n * aa) - (a * a)
m = ((n * ab) - (a * b)) / d
c = ((b * aa) - (a * ab)) / d

y2 =[]
for i in range(n):
    y2.append(x[i] * m + c)

print("X | Y | Y2")
for i in range(n):
    print(x[i], "|", y[i], "|", y2[i])

print("\n")

# --- Prob 3: Notas ---
notas =[]
print("Ingrese las 15 notas:")
for i in range(15):
    val = float(input("Nota " + str(i+1) + ": "))
    notas.append(val)

notas2 = []
for a in notas:
    if a * 1.25 >= 7.0:
        notas2.append(7.0)
    else:
        notas2.append(a * 1.25)

p = 0
p2 = 0
print("Notas Originales | Notas Mejoradas")
for i in range(15):
    print(notas[i], "|", notas2[i])
    p += notas[i]
    p2 += notas2[i]

print("")
print("Promedio Notas Originales:")
print(p / 15)
print("\nPromedio Notas Mejoradas:")
print(p2 / 15)

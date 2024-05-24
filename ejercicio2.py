#2.	Lea dos matrices N * M y a continuación:
#a)	Genere una tercera con la suma de ambas
#b)	Genere una cuarta con la multiplicación de ambas, si es posible. Muestre las matrices resultantes

n = []
a = int(input("Digite número de filasN: "))
b = int(input("Digite número de columnasN: "))

for i in range(a):
    n.append([])
    for j in range(b):
        n[i].append(None)

for j in range(0, a):    
    for i in range(0, b):
        n[j][i] = int(input("Digite número: "))        
        
m = []
c = int(input("Digite número de filasM: "))
d = int(input("Digite número de columnasM: "))

for i in range(c):
    m.append([])
    for j in range(d):
        m[i].append(None)
        
for j in range(0, c):    
    for i in range(0, d):
        m[j][i] = int(input("Digite número: "))
        
suma = []
for i in range(a):
    suma.append([])
    for j in range(b):
        suma[i].append(None)
        suma[i][j] = n[i][j] + m[i][j]

multiplicacion = []
for i in range(a):
    multiplicacion.append([])
    for j in range(d):
        multiplicacion[i].append(0)
    for j in range(d):
        for k in range(b):
            multiplicacion[i][j] += n[i][k] * m[k][j]

print(suma) 
print(multiplicacion)


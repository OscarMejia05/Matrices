#1.	Leer una matriz B de orden M*A y un número K. Multiplicar todos los elementos de la matriz por el número K. Mostrar la matriz resultante.

b = []
m = int(input("Digite número de filas: "))  
a = int(input("Digite número de columnas: "))   
k = int(input("Digite número k: "))

for i in range(m):
    b.append([])
    for j in range(a):
        b[i].append(None)
    
for j in range(0, m):
    for i in range(0, a):
        b[j][i] = int(input("Digite número: "))
        
print(b)        

for j in range(0, m):
    for i in range(0, a):
        b[j][i] *= k

print(b)
#Hacer un algoritmo que llene una matriz de 5 * 5 y que almacene la diagonal principal en un vector. Imprimir el vector resultante.

matriz = []
filas = int(input("Digite número de filas: "))
columnas = int(input("Digite número de columnas: "))    

if filas == 5 and columnas == 5:
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(None)
    
    for j in range(0, filas):
        for i in range(0, columnas):
            matriz[j][i] = int(input("Digite número: "))
            
    if filas == columnas:
        for i in range(filas):
         diagonal = []
         for i in range(filas):
             diagonal.append(None)
             diagonal[i] = matriz[i][i]
        
    print("los valores de la diagonas principal son: ",diagonal)

else:
    print("La matriz no es de 5 * 5")
    
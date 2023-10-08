n : int
n = int(input("Ingrese un número natural mayor o igual a 2: "))
print("La lista de números pares anteriores a " +str(n)+ " es:")
while n > 2:
    if n % 2 == 0:
        n -= 2
    else:
        n = n +1
        n -= 2
    print(n)
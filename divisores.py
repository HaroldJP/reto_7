a : int
a = int(input("Ingrese un número de 2 a 50:"))
b : int = a
c : int = a
print("Los divisores de " +str(c)+ " son:")
while b >= 1:
    if a % b == 0:
        print(b)
    b -= 1


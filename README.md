# reto_7

Todos los puntos de este taller se encuentran en un cuaderno de Google Colab en el siguiente enlace: https://colab.research.google.com/drive/1tO5AWjg1vv9E60scXiJL5gydZBrHEpQs

### Punto 1

Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
i : int = 0
while i < 100:
    i += 1
    print(i, i**2)
```

### Punto 2

Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
i : int = 0
j : int = -1
while i < 1000 and j < 999:
    i += 2
    j += 2
    print(j, i)
```

### Punto 3

Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
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
```

### Punto 4

En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

```python
A : float = 25
B : float = 18.9
C : float = 2022
while A > B:
    crecA = 1 + 0.02
    crecB = 1 + 0.03
    A *= crecA
    B *= crecB
    C += 1
print("En el año " +str(C)+ " la población del país B será mayor que la población del país A")
```

### Punto 5

Imprimir el factorial de un número natural n dado.

```python
m = 1
n = int(input("Introduzca un número natural: "))
i = 1
while (i <= n):
    m *= i
    i += 1
print (str(n) + " factorial es igual a " +str(m))
```

### Punto 6

Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.

```python
import random
def adivinar():
    print("Piense en un número de 1 a 100")
    min = 1
    max = 100
    while True: 
        n = random.randint(min, max) 
        print("¿Su número es " + str(n)+ "?")
        print("(Responda 'igual' si es correcto, 'menor' si es menor o 'mayor' si es mayor): ")
        respuesta = input()
        if respuesta == 'igual':
            print("Adiviné")
            break
        elif respuesta == 'menor':
            max = n - 1
        elif respuesta == 'mayor':
            min = n + 1
        else:
            print("Yo no le di esa opción, ahora por irse de avión le tocó iniciar otra vez")
            break
adivinar()
```

### Punto 7

Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

```python
a : int
a = int(input("Ingrese un número de 2 a 50:"))
b : int = a
c : int = a
print("Los divisores de " +str(c)+ " son:")
while b >= 1:
    if a % b == 0:
        print(b)
    b -= 1
```

### Punto 8

Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

```python
def es_primo(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
for a in range(1, 101):
    if es_primo(a):
        print(a)
```










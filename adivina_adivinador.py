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

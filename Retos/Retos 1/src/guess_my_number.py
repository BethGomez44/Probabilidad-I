'''
Clásico juego "Guess My Number"

@author: Gómez de la Torre Heidi Lizbeth
'''
import random
from random import randrange, choice

print("\t¡Hola! ¿Cuál es tu nombre?")
nombre = input()
print("\nBueno,", nombre,
      ", estoy pensando en un número entre el 1 y el 100. Tienes 20 intentos para adivinarlo.")

x = random.randint(1, 100)
guess = int(input("Adivina el número:"))
salida = 1
intentos = 1

while guess != x and salida != 20:

    if guess > x:
        print("Muy alto...\n")
    else:
        print("Muy bajo...\n")

    guess = int(input("Adivina el número:"))
    intentos += 1
    salida += 1

if salida % 20 == 0:
        print("¿Enserio? Creí que lo lograrías. Mejor suerte para la próxima.")

input("\n\tPresiona Enter para salir del programa")

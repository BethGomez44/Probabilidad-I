'''
Clásico juego "Guess My Number"

@author: Gómez de la Torre Heidi Lizbeth
'''
import random
from random import randrange, choice

print("\t¡Hola! ¿Cuál es tu nombre?")
nombre = input()
print("\nBueno,", nombre, ", estoy pensando en un número entre el 1 y el 100.")

x = random.randint(1, 100)
guess = int(input("Adivina el número:"))
intentos = 1

while guess != x:

    if intentos % 10 == 0:
        print(choice(["Vamos, no es tan díficil.\n",
                      "¿Enserio? Tú eres mejor que eso.\n", "No es tan fácil, ¿verdad?.\n", "Te estoy esperando.\n",
                      "Es tan solo un número, nada difícil.\n", "Hasta mi abuelita lo haría mejor.\n"]))

    if guess > x:
        print("Muy alto...\n")
    else:
        print("Muy bajo...\n")

    guess = int(input("Adivina el número:"))
    intentos += 1

print("\n¡Adivinaste!, el número es", guess)
print("Y te tomó", intentos, "intentos")
input("\n\tPresiona Enter para salir del programa")

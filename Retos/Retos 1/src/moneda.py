'''
Este programa simula el lanzamiento de una moneda 100 veces.

@author: Gómez de la Torre Heidi Lizbeth
'''
import random

i = 0
cruz = 0
cara = 0

while i<100:
    x = random.randint(1, 2)
    if x == 1:
        cruz += 1
    elif x == 2:
        cara += 1
    i += 1

print(f'¡Hola! Una moneda se lanzó {i} veces.')
print(f'De las cuales, {cruz} veces fueron cruz y {cara} veces fueron cara.')
print('¡Hasta la proxima! :)')
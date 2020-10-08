'''
Este programa simula una galleta de la fortuna.

@author: Gómez de la Torre Heidi Lizbeth
'''
import random

x = random.randint(1, 5)

print('¡Hola! Tu fortuna predice lo siguiente:')
print(' ')

if x == 1:
	print('"El cielo sera tu limite, pues grandes acontecimientos te sucederán."')
elif x == 2:
	print('"Eso no era de pollo."')
elif x == 3:
	print('"Tu crush te escribirá dentro de las próximas 24 horas."')
elif x == 4:
	print('"¡Ayuda! Estoy siendo prisionero de una pastelería china".')
elif x == 5:
	print('"Si comes algo y nadie te ve comerlo, no tiene calorías".')
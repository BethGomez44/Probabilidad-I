from collections import defaultdict

print(f'Simulación para el ejercicio 2 de la tarea 2.')
print('Sea omega nuestro espacio muestral que simulará el lanzamiento de un dado justo dos veces.')

import random
def dadoJusto():
    return random.randint(1,6)

'Declaramos nuestras variables X, Y, Z y W como están definidas en nuestro problema'

print('En el caso de la variable x, tenemos lo siguiente')
X={(i,j):max(i,j) for i,j in Omega}
Y={(i,j):min(i,j) for i,j in Omega}
Z={(i,j):i+j for i,j in Omega}
W={(i,j):|i-j| for i,j in Omega}
W

iZ = defaultdict(list)
for i,j in Z.items():
    iZ[j].append(i)
    
iW = defaultdict(list)
for i,j in W.items():
    iW[j].append(i)

leyZ={i:len(j)/36 for i,j in iZ.items()}
leyZ
    
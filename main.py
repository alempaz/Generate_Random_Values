import random


for n in range(5):
    print(random.random())                          #.random // para obtener un numero aleatorio entre 0 y 1   ejemplo: 0.42238095994946134

for n in range(5):
    print(random.randint(0,20))                     #.randint // para obtener numeros aleatorios de entre dos numeros que nosotros definimos


miembros = ['Martin', 'Bryan', 'Zavala', 'Gabin', 'Ana', 'Mariam', 'Lily', 'Darwin']
lider = random.choice(miembros)                     #.choice // para obtener un dato aleatorio de una lista

print(f'El lider del grupo es {lider}! Felicidades!')

# EJERCICIO // Hacer un programa que cuando este es ejecutado, lanze dos dados.
    # 1) Crear una clases que se llame Dado. En este crear un metodos que se llame rodar. Que los datos que retorne sean un tuple


class Dado:
    def rodar(self):
        a = random.randint(1,6)
        b = random.randint(1, 6)
        return a, b                               # Cuando retornamos una lista con solo , Python automaticamente la hace un tuple.


dado = Dado()
print(f'Los dados son: {dado.rodar()}')

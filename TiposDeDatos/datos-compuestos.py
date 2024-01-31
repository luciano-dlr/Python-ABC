# si modificable
lista = ['Luciano','de la Rubia',True,1.75]

lista[2] = False

# no modificable
tupla = ('Luciano','de la Rubia',True,1.75)

# print(lista)
# print(tupla[0])

# conjunto (set),redifinable y sin orden, no puede tener datos duplicados
conjunto = {'Luciano','Luciano','de la Rubia',True,1.75}

# print(conjunto)

# diccionario (dict), json at js
diccionario = {
    'nombre': 'Luciano',
    'apellido':'de la Rubia',
    'feliz': True,
    'altura': 1.75
}

print(diccionario['altura'])
print(diccionario)



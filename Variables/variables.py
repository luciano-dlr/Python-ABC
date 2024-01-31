nombre = 'Luciano'
nombre = 'Leonidas'
nombre = 'Leonardo'
nombre += ''

datoRaro = 'error'
del datoRaro

apellido = 'de la Rubia'

# F strings
bienveido = f' {nombre,apellido}'

print(bienveido)

# Key sensitive
print('Rubia' in bienveido)
print('Rubia' not in bienveido)



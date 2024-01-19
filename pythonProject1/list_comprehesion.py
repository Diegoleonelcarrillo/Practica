lista_pares = []
numeros = range(10)

for numero in numeros:

    if numero % 2 == 0:
        lista_pares.append(numero)

print(f'Lista de numeros pares: {lista_pares}')

#Ahora hacemos lo mismo con list comprehesion
#[Expresion for vat in colecion if condicion]

lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]

print(f'Lista de numeros pares con  list comprehesion: {lista_pares}')

#Se puede usar dos condiciones
lista_pares = []
lista_impares = []

[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in range(10)]
print(f'Lista de pares:{lista_pares}')
print(f'Lista de impares: {lista_impares}')

#Listas de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9,10]]
print(f'Lista de listas sin ordenar: {lista_listas}')

#Convertivos la lista de listas en una lista simple
lista_simple = [valor for sublista in lista_listas for valor in sublista]

print(f'Lista simple ordenada: {lista_simple}')


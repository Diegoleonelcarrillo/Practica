# Matrices en Python

matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz orifinal: {matriz}')

matriz[2][1] = 75
print(f'Numero 70 cambiado por el 75: {matriz}')

#Ordenar lista
lista_DeLista = [[10, 20], [60, 43, 64, 35, 50], [43, 34, 55]]

lista_DeLista.sort(key=len)
print(f'Lista De listas Ordenadas: {lista_DeLista}')

#Extraer algunas partes de mi lista
mi_lista = [1,2,3,4,5,6]
print(f'Lista Original: {mi_lista}')
a, *b, c, d = mi_lista
print(f'Mi lista: {a,b,c,d}')

#Unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [*lista1, *lista2]

print(f'Union de listas: {lista3}')

#Unir Diccionarios
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5, 'E':6}
dic3 = {**dic1, **dic2}

print(f'Dic1: {dic1}')
print(f'Dic2: {dic2}')

print(f'Unios de dicionarios: {dic3}')
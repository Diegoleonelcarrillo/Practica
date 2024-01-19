#Generadores
#Es un tioo de funcion especial, retorna una secuencia de valores
#Suspende la ejecuacion de la funcion yield (Producir)

# def generador():
#     yield 1
#     yield 2
#     yield 3
#
# #Consumimos generadores a demanda
# gen = generador()
#
# #Con cada llamada consumimos un valor
# print(next(gen))

#Generador de numeros (1 al 5)
# def generador_numeros():
#     for numero in range(1,6):
#         yield numero
#
# generador = generador_numeros()
# print(f'Objeto generador {generador}')
# print(type(generador))
#
# #Consumimos el valor del generador:
# for valor in generador:
#     print(f'Numero producido {valor}')

# #Expresion generadora (es un generador anonimo)
# multiplicacion = (valor*valor for valor in range(4))
# print(next(multiplicacion))
# print(next(multiplicacion))
# print(next(multiplicacion))
# print(next(multiplicacion))
#
# #Tambien se puede pasar un expresion generadora a un a funcion (sin usar parentesis)
# import math
# suma = sum(valor*valor for valor in range(4))
# print(f'Resultado de la suma: {suma}')





















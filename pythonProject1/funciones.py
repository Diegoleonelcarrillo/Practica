
#Funciones anidadas:
def calculadora(a ,b , opcion = 'sumar'):

    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    if opcion == 'sumar':
        print(f'La suma de los valores es: {sumar(a, b)}')
    elif opcion == 'restar':
        print(f'La resta de las variables es: {restar(a, b)}')

#Alcance de Variables (Scope):

# var_global = 'Variable global'
#
# def imprimir():
#     #Acceder a una variable global
#     print(f'Variable global desde la funcion{var_global}')
#     #Definicion de varibale local
#     var_local = 'Varibale local'
#     print(var_local)
#     var_local = 'Nuevo Valor'
#
#     def funcion_anidada():
#         print(f'Varibale local dentro de una funcion anidada: {var_local}')
#
#     funcion_anidada()
#
# imprimir()

# contador = 0
#
# def mostrar_contador():
#     print(contador)
#
# def modificar_contaodr(c):
#     global contador
#     contador = c
#
# modificar_contaodr(5)
# mostrar_contador()

#Funciones Lamba
#Son funciones anonimas y solo tienen una sola linea
#No se necesita agregar parentesis para los parametros
#No se necesita un return, pero si una regresar una expresion

# mi_funcion_lamba = lambda a, b: a + b
#
# resultado = mi_funcion_lamba(1, 2)
# print(f'Resultado de mi funcion Lamba: {resultado}')
#
# #Funcion lamba que no recibe argumentos pero(debemos regresar una expresion valida)
# mi_funcion_lamba = lambda: 'Sin argumentos'
# resultado1 = mi_funcion_lamba
# print(f'Funcion lambda: {mi_funcion_lamba()}')
#
# #Funcion lambda con parametros por default
# mi_funcion_lamba = lambda a=2, b=2:a+b
# print(f'Resultado de funcion con valores default:{mi_funcion_lamba()}')
#
# #Funcion lamba con parametros *args y **kwargs:
# mi_funcion_lamba = lambda *args, **kwargs: len(args) + len(kwargs)
# print(f'Resuktado de valores variables: {mi_funcion_lamba(1,2,3, a=4,b=5)}')


#Una funcion closure es una funcion que define a otra y ademas la regresa la funcion anidada puede acceder a las variables locales definida en la funcion principal o externa

#Funcion prencipal
# def operacion(a, b):
#     #Dfinimos una funcion interna o anidada
#     def sumar():
#         return a + b
#     #Retornar la funcion
#     return sumar

#Defino la funcion:
# def operacion(a, b):
#     #1.Definimos la funcion lambda interna o anidada y la retornamos:
#     return lambda: a + b
#
# mi_funcion_closure = operacion(1, 2)
# print(f'Mi funcion: {mi_funcion_closure()}')
#
# #Llamar a mi funcion al vuelo
# print(f'Mi funcion al vuelo: {operacion(3,3)()}')
#












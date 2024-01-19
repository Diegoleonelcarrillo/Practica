

diccionario = {'nombre':'Ivan', 'edad':35, 'sueldo':8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 8000.00}
mensaje = f'Nombre {diccionario["nombre"]} Edad {diccionario["edad"]} Sueldo {diccionario["sueldo"]:.2f}'
print(mensaje)

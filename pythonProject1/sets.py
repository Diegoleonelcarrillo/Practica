#Los sets no se repiten los elementos

#Unioniones con sets
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_caje = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}

#Union (conmutativa)
print(ojos_caje.union(pelo_rubio))

#Interseccion (Conmutativa)
print(ojos_caje.intersection(pelo_rubio))

#Differencia (No es conmutativa)
print(pelo_negro.difference(ojos_caje))

#Diferencia Simetrica (Conmutativa)
print(pelo_negro.symmetric_difference(ojos_caje))

#Un Set esta contenido dentro de otro Set(subset)
print(menores_30.issubset(pelo_negro))

#Preguntar si un set contiene a otro(superSet)
print(menores_30.issuperset(pelo_negro))



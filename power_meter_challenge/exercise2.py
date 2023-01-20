import json

repetidos = [1,2,3,"1","2","3",3,4,5]

r = [1,"5",2,"3"]

d_str = '{"valor":125.3,"codigo":123}'

# CONSIDERACIÓN: Sea x un entero, asumo que x y "x" deben ser considerados el mismo valor.
# en su defecto, las transformaciones no serían necesarias para resolver el ejercicio. 

#1- Se crea una lista por comprensión aplicando como transformación int(x) para que todos los elementos sean enteros
#2- Se genera un conjunto a partir de esa lista para eliminar los duplicados (por definición un conjunto no posee elementos repetidos)
#3- Se genera una lista a partir del conjunto.
no_repetidos = list(set([int(x) for x in repetidos]))

#1- Se transforman los elementos de ambas listas, esta vez usando map y una función anonima (solo para variar, es lo mismo)
#2- Se aplica la intesección de conjuntos (operador &) que por definición retorna un conjunto con los elementos compartidos.
#3- Se genera una lista a partir del nuevo conjunto.
interseccion = list(set(map(lambda x : int(x), repetidos)) & set(map(lambda x : int(x), r)))

#json.loads parsea un JSON en forma de string armarmando un diccionario con las claves y valores del JSON.
diccionario = json.loads(d_str)

print("Respuestas:")
print("1) ", no_repetidos)
print("2) ", interseccion)
print("3) ", diccionario)
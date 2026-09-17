"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
mensaje = "¡Hola, mundo!"
print(mensaje)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
mensaje = "Hello, world!"
print(mensaje)
# El valor anterior se sobrescribe y ahora la variable contiene el nuevo texto.

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
my_string = "Potato"
my_int = 28
my_float = 8.88
my_bool = True
my_list = [2,3,4,5]
my_tuple = (6,7,8)
my_dicctionary = {"nombre": "Sara", "edad": 28}
my_set = {1,2,3,4}

print(my_string, type(my_string))
print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_bool, type(my_bool))
print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(my_dicctionary, type(my_dicctionary))
print(my_set, type(my_set))

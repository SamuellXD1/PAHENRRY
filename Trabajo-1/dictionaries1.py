#################DICCIONARIOS####################
###########################################

# Creación e impresión de diccionarios básicos
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}  # Crea un diccionario con lecturas de sensores
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}                   # Crea un diccionario con la cantidad de cámaras
print(sensors)                                                             # Muestra el diccionario de sensores
print(num_cameras)                                                         # Muestra el diccionario de cámaras

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}  # Crea un diccionario de traducciones
print(translations)                                                        # Muestra el diccionario de traducciones


# Verificación de errores y tipos de datos en claves
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}                      # Las listas son mutables y no pueden usarse como claves (TypeError)
# print(powers)                                                            # Código comentado por error de sintaxis/tipo

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}  # Diccionario con listas como valores
print(children)                                                            # Muestra el diccionario de listas

my_empty_dictionary = {}                                                   # Crea un diccionario vacío
print(my_empty_dictionary)                                                 # Muestra el diccionario vacío

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # Crea un diccionario con precios de menú
print("Before: ", menu)                                                    # Muestra el menú antes de modificarlo
menu["cheesecake"] = 8                                                     # Agrega una nueva clave y valor al diccionario
print("After", menu)                                                       # Muestra el menú actualizado

animals_in_zoo = {"dinosaurs": 0}                                          # Crea un diccionario con un elemento
animals_in_zoo = {"dinosaurs": 0}                                          # Sobrescribe la variable con el mismo diccionario
animals_in_zoo = {"horses": 2}                                             # Reasigna la variable con una nueva clave y valor
print(animals_in_zoo)                                                      # Muestra el diccionario final


# Agregar múltiples claves con update()
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}                # Define el diccionario inicial
print("Before", sensors)                                                   # Muestra el estado inicial

# Si quisiéramos agregar 3 habitaciones nuevas, podemos usar update():
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})               # Agrega múltiples pares clave-valor al diccionario
print("After", sensors)                                                    # Muestra el diccionario con los nuevos elementos

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}                 # Crea un diccionario de usuarios e IDs
print(user_ids)                                                            # Muestra el diccionario original
user_ids.update({"theLooper": 138475, "stringQueen": 85739})               # Extiende el diccionario agregando nuevos usuarios
print(user_ids)                                                            # Muestra el diccionario actualizado


# Sobrescribir valores en un diccionario
# Sabemos que podemos agregar una clave usando la siguiente sintaxis:
# menu["banana"] = 3
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # Define el diccionario inicial
print("Before: ", menu)                                                    # Muestra el menú inicial
menu["oatmeal"] = 5                                                        # Modifica el valor de una clave existente
print("After", menu)                                                       # Muestra el menú con el valor actualizado

# Note que el valor de "oatmeal" ahora ha cambiado a 5.
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}  # Crea un diccionario de ganadores del Oscar
print("Before", oscar_winners)                                             # Muestra los ganadores iniciales
print()                                                                    # Deja un espacio en blanco

oscar_winners.update({"Supporting Actress": "Viola Davis"})                # Agrega una nueva categoría y ganadora
print("After1", oscar_winners)                                             # Muestra el diccionario tras la adición
print()                                                                    # Deja otro espacio en blanco

oscar_winners["Best Picture"] = "Moonlight"                                # Corrige y sobrescribe el valor de la clave "Best Picture"
print("After2", oscar_winners)                                             # Muestra el diccionario con el valor corregido


# Comprensión de diccionarios (Dict Comprehensions)
# Supongamos que tenemos dos listas que queremos combinar en un
# diccionario, como una lista de estudiantes y una lista de sus alturas,
# en pulgadas:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']                                # Crea una lista de nombres
heights = [61, 70, 67, 64]                                                 # Crea una lista de alturas

# Python te permite crear un diccionario usando
# una comprensión de diccionario, con esta sintaxis:

zipStudents = zip(names, heights)                                          # Combina ambas listas en un objeto zip
print("zipStudents: ", zipStudents)                                        # Muestra la referencia del objeto zip en memoria

students = {key:value for key, value in zip(names, heights)}              # Genera un diccionario emparejando las dos listas
# students es ahora {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print(students)                                                            # Muestra el diccionario generado

# zip() combina dos listas en un iterador de tuplas con los elementos emparejados. Esta comprensión:

drinks = ["espresso", "chai", "decaf", "drip"]                            # Crea una lista de bebidas
caffeine = [64, 40, 0, 120]                                                # Crea una lista de niveles de cafeína

zipped_drinks = zip(drinks, caffeine)                                      # Combina las dos listas con zip
print(zipped_drinks)                                                       # Muestra la referencia del objeto zip

drinks_to_caffeine = {key:value for key, value in zipped_drinks}          # Crea el diccionario a partir de la lista combinada
print(drinks_to_caffeine)                                                  # Muestra el diccionario de bebidas y cafeína

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]  # Lista de canciones
playcounts = [78, 29, 44, 21, 89, 5]                                       # Lista de reproducciones

plays = {key:value for key, value in zip(songs, playcounts)}               # Crea un diccionario asociando canciones y reproducciones
print(plays)                                                               # Muestra el diccionario de reproducciones

plays.update({"Purple Haze": 1})                                           # Agrega una nueva canción con su número de reproducciones
plays.update({"Respect": 94})                                              # Actualiza las reproducciones de una canción existente
print("After: ", plays)                                                    # Muestra el diccionario de reproducciones actualizado

library = {"The Best Songs": plays, "Sunday Feelings": {}}                 # Crea un diccionario anidado que contiene a otro diccionario
print(library)                                                             # Muestra la estructura del diccionario anidado

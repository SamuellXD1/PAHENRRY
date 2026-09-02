#################DICCIONARIOS####################
###########################################

# Obteniendo un valor a traves de su clave
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # Crea un diccionario con alturas de edificios
print(building_heights["Burj Khalifa"])   # Muestra el valor de la clave especificada
print(building_heights["Ping An"])         # Muestra el valor de otra clave en el diccionario

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}  # Crea un diccionario con listas de elementos del zodiaco
print(zodiac_elements["earth"])           # Muestra la lista asociada a la clave earth
print(zodiac_elements["fire"])            # Muestra la lista asociada a la clave fire


# Acceso a clave inexistente y comprobacion de existencia
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # Define el diccionario de alturas
#print(building_heights["Landmark 81"])    # Intentar acceder a una clave inexistente genera un error KeyError

key_to_check = "Landmark 81"              # Guarda la clave a comprobar en una variable

if key_to_check in building_heights:       # Comprueba si la clave existe en el diccionario
    print(building_heights["Landmark 81"]) # Muestra el valor si la clave existe

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}  # Define el diccionario

zodiac_elements["energy"] = "Not a Zodiac element"  # Agrega una nueva clave y valor al diccionario

if "energy" in zodiac_elements:           # Comprueba si la nueva clave existe en el diccionario
    print(zodiac_elements["energy"])      # Muestra el contenido de la clave agregada


# Obtener un valor de forma segura usando get()
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # Reasigna el diccionario

print(building_heights.get("Shanghai Tower"))  # Devuelve el valor de la clave existente
print(building_heights.get("My House"))        # Devuelve None al no encontrar la clave especificada

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}  # Crea un diccionario de usuarios e IDs
user_ids.get("teraCoder")                 # Obtiene el valor de la clave pero no lo muestra

if user_ids.get("teraCoder") == None:     # Verifica si la clave no existe devolviendo None
    tc_id = 1000                          # Asigna un valor por defecto si es None
else: 
    tc_id = user_ids.get("teraCoder")     # Obtiene y asigna el valor guardado

print(tc_id)                              # Muestra el resultado final de la variable

if user_ids.get("superStackSmash") == None:  # Verifica una clave inexistente
    stack_id = 100000                     # Asigna un valor por defecto

print(stack_id)                           # Muestra el valor asignado


# Eliminar un elemento usando pop()
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}  # Crea un diccionario con premios de rifa
print(raffle.pop(320291, "No Prize"))     # Elimina la clave y muestra el valor eliminado
print(raffle)                             # Muestra el diccionario actualizado
print(raffle.pop(100000, "No Prize"))     # Intenta eliminar una clave inexistente y muestra el valor por defecto
print(raffle)                             # Muestra el diccionario sin cambios
print(raffle.pop(872921, "No Prize"))     # Elimina otra clave y muestra su valor
print(raffle)                             # Muestra el diccionario actualizado

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}  # Crea un diccionario de items
health_points = 20                        # Inicializa una variable numerica

health_points += available_items.pop("stamina grains", 0)  # Suma el valor eliminado a la variable
health_points += available_items.pop("power stew", 0)       # Suma otro valor eliminado a la variable
health_points += available_items.pop("mystic bread", 0)     # Intenta extraer clave inexistente sumando 0

print(available_items)                    # Muestra el diccionario modificado
print(health_points)                      # Muestra la suma total guardada en la variable


# Obtener todas las claves del diccionario
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}  # Crea un diccionario con calificaciones
print(list(test_scores))                  # Convierte y muestra las claves como una lista

for student in test_scores.keys():        # Recorre todas las claves del diccionario
    print(student)                        # Muestra cada clave en una nueva linea

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}  # Define diccionario de IDs
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}  # Define diccionario de ejercicios

users = user_ids.keys()                   # Guarda la vista de las claves del diccionario
lessons = num_exercises.keys()            # Guarda la vista de las claves del segundo diccionario

print(users)                              # Muestra la vista con las claves de usuarios
print(lessons)                            # Muestra la vista con las claves de lecciones


# Obtener todos los valores del diccionario
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}  # Reasigna diccionario de notas

for score_list in test_scores.values():   # Recorre directamente los valores del diccionario
    print(score_list)                     # Muestra cada lista de valores

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}  # Reasigna diccionario de ejercicios

total_exercises = 0                       # Inicializa un contador en 0

for exercises in num_exercises.values():  # Recorre los valores del diccionario
    total_exercises += exercises          # Acumula cada valor en la variable acumuladora
print(total_exercises)                    # Muestra el resultado total de la suma


# Obtener todos los pares clave-valor (items)
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}  # Crea un diccionario con marcas y sus valores

for company, value in biggest_brands.items():  # Recorre simultaneamente las claves y valores
    print(company + " has a value of " + str(value) + " billion dollars. ")  # Muestra el texto formateado con los datos

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}  # Crea un diccionario con porcentajes

for occupation, percentage in pct_women_in_occupation.items():  # Recorre los pares clave-valor
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")  # Muestra el mensaje con la informacion de cada elemento

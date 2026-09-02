#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']  # Crea una lista con 6 colores 
#input()
print(my_lista)                           # Muestra la lista 
print(type(my_lista))                     # Muestra el tipo de dato, que es una lista 
print(my_lista[2])                        # Muestra el elemento en el índice 2


print("my_lista size: ", len(my_lista))   # Muestra la cantidad de elementos que tiene la lista 
print(my_lista[0:2])                      # Muestra una parte de la lista
print(my_lista[:2])                       # Muestra los elementos desde el inicio hasta el índice 1 


my_lista.append('Blanco')                 # Agrega elemento al final de la lista osea Blanco
print(my_lista)                           # Muestra la lista actualizada con el color blanco

my_lista.insert(3, 'Negro')               # Inserta Negro en la posición con índice 3
print(my_lista)                           # Muestra la lista actualizada con el color Negro en el 3 indice 


my_lista.extend(['Marron', 'Gris'])       # Agrega múltiples elementos al final de la lista desde otra lista
print(my_lista)                           # Muestra la lista ampliada con los elementos de la otra lista como Marron y Gris

print(my_lista.index('Azul'))             # Muestra el número de índice donde se encuentra Azul 


#my_lista.remove('Magenta')               # Elimina la aparición de Mangeta en la lista
my_lista.remove('Marron')                 # Elimina la aparición de Marron en la lista
print(my_lista)                           # Muestra la lista después de eliminar Marron

my_lista.insert(8, 'Marron')              # Agrega Marron en la posición 8
print(my_lista)                           # Muestra la lista actualizada

print(my_lista.pop())                     # Elimina y muestra el último elemento de la lista
size = len(my_lista)                      # Guarda el tamaño de la lista en una variable
print("size = ", size)                    # Muestra el tamaño de la lista
#print(my_lista.pop(size))                # Elimina un elemento usando su posición

my_lista_3 = my_lista*3                    # Repite la lista 3 veces
print("my_lista_3: ", my_lista_3)          # Muestra la lista repetida

print("Sort:")                            # Muestra un mensaje
print()                                   # Deja un espacio

my_listaSort = my_lista.sort()            # Ordena la lista
print(my_listaSort)                       # Muestra el resultado de sort

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]  # Crea una lista de números
print("Ordering my_NumList: ")             # Muestra un mensaje
my_NumList.sort()                          # Ordena los números de menor a mayor
print(my_NumList)                          # Muestra la lista ordenada

#OrderedLList = my_NumList.sort()         # Ordena la lista
#print(my_listaSort)                      # Muestra la lista ordenada

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)            # Ordena la lista de mayor a menor
print("De menor a mayor: ", my_NumList)    # Muestra la lista ordenada



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")       # Muestra una línea
print("###########################")       # Muestra una línea
print("###########################")       # Muestra una línea
print("############TUPLAS#########")       # Muestra el título de la sección

my_tupla = tuple(my_lista)                  # Convierte la lista en una tupla
print()                                     # Deja un espacio
print()                                     # Deja otro espacio
print("my_tuple: ", my_tupla)               # Muestra la tupla

print(my_tupla[0])                          # Muestra el primer elemento
print(my_tupla[2])                          # Muestra el elemento en la posición 2


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)                   # Comprueba si Rojo está en la tupla
print(my_tupla.count('Rojo'))               # Cuenta cuántas veces aparece Rojo

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')              # Crea una variable con Blanco
print(my_tupla_unitaria)                    # Muestra el contenido

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999             # Crea una tupla sin usar paréntesis
print(my_tupla)                             # Muestra la tupla

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla            # Guarda cada valor en una variable
print(nombre)                               # Muestra el nombre
print(dia)                                  # Muestra el día
print(mes)                                  # Muestra el mes
print(año)                                  # Muestra el año

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)  # Muestra todos los datos

#Convertir una tupla en una lista
my_lista2=list(my_tupla)                    # Convierte la tupla en una lista
print(my_lista2)                            # Muestra la nueva lista

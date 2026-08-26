#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']  # Crea una lista con 6 colores 
#input()
print(my_lista)                           # Muestra la lista 
print(type(my_lista))                     # Muestra el tipo de dato, que es una lista 
print(my_lista[2])                        # Muestra el elemento en el índice 2


print("my_lista size: ", len(my_lista))   # Muestra la cantidad de elementos que tiene la lista 
print(my_lista[0:2])                      # Muestra una sublista desde el índice 0 hasta el 1 
print(my_lista[:2])                       # Muestra los elementos desde el inicio hasta el índice 1 


my_lista.append('Blanco')                 #Agrega elemento al final de la lista osea Blanco
print(my_lista)                           # Muestra la lista actualizada con el color blanco

my_lista.insert(3, 'Negro')               # Inserta Negro en la posición con índice 3
print(my_lista)                           # Muestra la lista actualizada con el color Negro en el 3 indice 


my_lista.extend(['Marron', 'Gris'])       # Agrega múltiples elementos al final de la lista desde otra lista
print(my_lista)                           # Muestra la lista ampliada con los elementos de la otra lista como Marron y Gris

print(my_lista.index('Azul'))             # Muestra el número de índice donde se encuentra Azul 


my_lista.remove('Magenta')                # Elimina la aparición de Mangeta en la lista 
my_lista.remove('Marron')                 # Elimina la aparición de Marron en la lista
print(my_lista)

my_lista.insert(8, 'Marron')
print(my_lista)

print(my_lista.pop())
size = len(my_lista)
print("size = ", size)
#print(my_lista.pop(size))

my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()
my_listaSort = my_lista.sort()
print(my_listaSort)

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
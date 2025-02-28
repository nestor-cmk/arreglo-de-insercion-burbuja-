def selection_sort(people): 
   #Implementar el algoritmo de clasificación por selección
    N = len(people)  #Obtener el tamaño de la lista
    i = 0
    #Bucle principal para recorrer la lista
    while i < N - 1:
        min_index = i
        j = i + 1
        #Encontrar el elemento menor en el resto de la lista
        while j < N:
            # Primero ordenamos por "name", si son iguales, ordenamos por "code"
            if (people[j]["name"] < people[min_index]["name"]) or \
               (people[j]["name"] == people[min_index]["name"] and people[j]["code"] < people[min_index]["code"]):
                min_index = j
            j += 1
            #Intercambiar los valores si min_indexcambiaron
        if min_index != i:
            temp = people[i]
            people[i] = people[min_index]
            people[min_index] = temp
        i += 1 #Avanzar a la siguiente posición
#Ejecutar el Código con una Lista de Personas
# Lista de personas
people = [
    {"name": "Camila", "code": 1},
    {"name": "Daniel", "code": 2},
    {"name": "Sofía", "code": 3},
    {"name": "Juan", "code": 4},
    {"name": "Valentina", "code": 5},
    {"name": "Carlos", "code": 6},
    {"name": "Isabella", "code": 7},
    {"name": "Andrés", "code": 8},
    {"name": "Mariana", "code": 9},
    {"name": "Felipe", "code": 10}
]

# Aplicamos el algoritmo de selección
selection_sort(people)

# Mostramos el resultado ordenado
for person in people:
    print(person)

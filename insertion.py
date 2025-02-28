def insertion_sort(arr):  #define la funcion
    n = len(arr) # calcula el tamaño el tamaño de la ista y lo  guarda en n
    for i in range(1, n): # desdedonde comienza hasta donde recorre
        current = arr[i] # guarda el elemento en la variable
        j = i - 1 #  aqui se compara el el elemento actual con el anterior 
        while j >= 0 and (arr[j]["code"] > current["code"] or 
                          (arr[j]["code"] == current["code"] and arr[j]["name"] > current["name"])): # Se ejecuta mientras j ≥ 0, moviendo elementos si arr[j]["code"] es mayor que current["code"] o, si son iguales, comparando "name" alfabéticamente.
            arr[j + 1] = arr[j] # mueve el elemento hasta la derecha para insertar el elemento correcto
            j -= 1 # se compara con el elemento anterio hasta encontra la posiscio correcta
        arr[j + 1] = current # Mueve elementos mientras sean mayores y los ajusta en la posicion correcta

# Lista de objetos
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

# Ordenar la lista
insertion_sort(people)

# Imprimir resultado
for person in people:
    print(person)

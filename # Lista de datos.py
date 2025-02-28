# Lista de datos
data = [
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

# definimos la función
def bubble_sort(arr):
    N = len(arr) #se obtine la longitud del arreglo
    i = 0 # i seria el numero que indica la posicion
    while i < N - 1: # bucle para iterar en la lista
        j = 0 # j es el numero para la controlar el numero de itearciones en cada pasada
        while j < N - i - 1: # comparamos cada elemento hasa que los mas grandes esten al final
            if arr[j]["code"] > arr[j + 1]["code"]:
                # Intercambiar elementos si arr[j] es mayor que arr[j + 1]
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp # almacenaos la variable temporalmente antes de hacer el intercambio
            j += 1
        i += 1

# Llamar la función de ordenamiento
bubble_sort(data)

# Imprimir la lista ordenada
for item in data:
    print(item)
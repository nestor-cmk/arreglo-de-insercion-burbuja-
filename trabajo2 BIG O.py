import heapq

def heap_sort(arr, key):
    heap = [(item[key], item) for item in arr]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(len(heap))]

def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][key]
    left = [x for x in arr if x[key] < pivot]
    middle = [x for x in arr if x[key] == pivot]
    right = [x for x in arr if x[key] > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)

def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def binary_search(arr, key, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][key] == target:
            return arr[mid]
        elif arr[mid][key] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "No encontrado"

empleados = [
    {"nombre": "Carlos", "edad": 29, "salario": 3000},
    {"nombre": "Ana", "edad": 25, "salario": 3500},
    {"nombre": "Luis", "edad": 32, "salario": 4000},
    {"nombre": "Marta", "edad": 28, "salario": 3200},
    {"nombre": "Pedro", "edad": 35, "salario": 4200},
    {"nombre": "Elena", "edad": 27, "salario": 2800},
    {"nombre": "Sofía", "edad": 30, "salario": 3100},
    {"nombre": "Javier", "edad": 26, "salario": 3300},
]

def main():
    while True:
        print("\nHola, bienvenido a mi aplicación Empresarial. ¿Qué quieres hacer?")
        print("1. Ordenar por edad (Heap Sort)")
        print("2. Ordenar por nombre (Quick Sort)")
        print("3. Ordenar por salario (Merge Sort)")
        print("4. Buscar por edad (Búsqueda binaria)")
        print("5. Buscar por salario (Búsqueda binaria)")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print(heap_sort(empleados, "edad"))
        elif opcion == "2":
            print(quick_sort(empleados, "nombre"))
        elif opcion == "3":
            print(merge_sort(empleados, "salario"))
        elif opcion == "4":
            edad = int(input("Introduce la edad a buscar: "))
            print(binary_search(heap_sort(empleados, "edad"), "edad", edad))
        elif opcion == "5":
            salario = int(input("Introduce el salario a buscar: "))
            print(binary_search(merge_sort(empleados, "salario"), "salario", salario))
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if _name_ == "_main_":
    main()
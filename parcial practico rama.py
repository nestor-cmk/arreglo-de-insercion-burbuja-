# 👨‍💻 Autor: JOHANBALCAZAR - 408651
# 🌿 Rama: JOHANBALCAZAR-408651
# ✔️ Selección automática de ubicaciones según el último dígito del código del estudiante

def seleccionar_ubicaciones(ubicaciones, codigo):
    """Selecciona ubicaciones en índices pares o impares según el último dígito del código."""
    ultimo_digito = int(str(codigo)[-1])  # Obtener el último dígito del código
    es_par = (ultimo_digito % 2 == 0)     # Verificar si es par

    # Filtrar ubicaciones según la condición
    ubicaciones_filtradas = [ubicaciones[i] for i in range(len(ubicaciones)) if (i % 2 == 0) == es_par]
    
    return ubicaciones_filtradas

def mostrar_ruta(ruta):
    """Muestra la ruta seleccionada."""
    print("\n📍 Ruta con ubicaciones seleccionadas:")
    if not ruta:
        print("⚠ No hay ubicaciones en la ruta.")
        return

    print("🛤 Ruta definida:")
    for lugar in ruta:
        print("➡", lugar)

    print("\n🗺 Recorriendo ruta:")
    print("🚗 Iniciando recorrido...")
    for lugar in ruta:
        print("🔴 Llegaste a:", lugar)
    print("\n🏁 Fin del recorrido.")

# Lista de ubicaciones de ejemplo
ubicaciones = ["Avenida Central", "Plaza Mayor", "Estación Norte", "Museo Nacional", "Universidad Central", "Parque Sur"]

# Código del estudiante
codigo = 408651

# Obtener la ruta filtrada
ruta_seleccionada = seleccionar_ubicaciones(ubicaciones, codigo)

# Mostrar la ruta
mostrar_ruta(ruta_seleccionada)
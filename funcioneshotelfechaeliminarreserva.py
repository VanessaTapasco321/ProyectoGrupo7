#funciones para hotel , fecha, y eliminar reserva
def eliminar_reserva(clientes, nombre_cliente, destino):
    cliente = buscar_cliente(clientes, nombre_cliente)
    if cliente:
        reservas = cliente["reservas"]
        for reserva in reservas:
            if reserva["destino"] == destino:
                reservas.remove(reserva)
                print(f"Reserva a {destino} eliminada para {cliente['nombre']}.")
                return
        print(f"No se encontró una reserva a {destino} para {cliente['nombre']}.")
    else:
        print(f"Cliente {nombre_cliente} no encontrado.")

# Mostrar lista de hoteles como menú
def seleccionar_hotel():
    print("\n--- Opciones de Hospedaje ---")
    for i, hotel in enumerate(hoteles, 1):
        print(f"{i}. {hotel}")
    opcion = input("Elige una opción de hotel: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= len(hoteles)):
        print("Opción inválida, intenta de nuevo.")
        opcion = input("Elige una opción de hotel: ")
    return hoteles[int(opcion) - 1]

# Validar formato de fecha
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
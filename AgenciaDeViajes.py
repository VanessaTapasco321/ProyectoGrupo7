import re
from datetime import datetime

paquetes = {
    "Aventura en la Selva": {
        "nombre": "Aventura en la Selva",
        "descripcion": "Un paquete turístico que incluye senderismo y campamentos en la selva.",
        "precio": "500"
    },
    "Escapada a la Playa": {
        "nombre": "Escapada a la Playa",
        "descripcion": "Vacaciones relajantes en una playa paradisiaca con actividades acuáticas.",
        "precio": "800"
    },
    "Tour Histórico por Europa": {
        "nombre": "Tour Histórico por Europa",
        "descripcion": "Un recorrido por las ciudades históricas más importantes de Europa.",
        "precio": "1500"
    }
}

clientes = {
    "Juan Perez": {
        "nombre": "Juan Perez",
        "correo": "juanperez@example.com",
        "reservas": [
            {
                "tipo": "vuelo",
                "destino": "Cancun",
                "fecha": "2024-09-20"
            }
        ]
    },
    "Maria Gonzales": {
        "nombre": "Maria Gonzales",
        "correo": "mariagonalez@example.com",
        "reservas": [
            {
                "tipo": "hotel",
                "destino": "Paris",
                "fecha": "2024-10-05"
            },
            {
                "tipo": "vuelo",
                "destino": "Nueva York",
                "fecha": "2024-12-12"
            }
        ]
    },
    "Carlos Lopez": {
        "nombre": "Carlos Lopez",
        "correo": "carloslopez@example.com",
        "reservas": []
    }
}
#  hoteles predefinidos
hoteles = ["Hotel Paris", "Resort Playa Azul", "Hostal Montaña", "Hotel Central City", "Hotel Luxor"]

# Funciones para gestionar los paquetes turísticos
def crear_paquete(paquetes, nombre, descripcion, precio):
    paquete = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio
    }
    if nombre in paquetes:
        print(f"El paquete '{nombre}' ya existe.")
    else:
        paquetes[nombre] = paquete
        print(f"Paquete '{nombre}' creado exitosamente.")

def buscar_paquete(paquetes, nombre):
    return paquetes.get(nombre, None)

def actualizar_paquete(paquetes, nombre, descripcion=None, precio=None):
    if nombre in paquetes:
        if descripcion:
            paquetes[nombre]["descripcion"] = descripcion
        if precio:
            paquetes[nombre]["precio"] = precio
        print(f"Paquete '{nombre}' actualizado.")
    else:
        print(f"El paquete '{nombre}' no existe.")

def eliminar_paquete(paquetes, nombre):
    if nombre in paquetes:
        del paquetes[nombre]
        print(f"Paquete '{nombre}' eliminado.")
    else:
        print(f"El paquete '{nombre}' no existe.")

def mostrar_paquetes(paquetes):
    print("\n--- Paquetes Turísticos Disponibles ---")
    for paquete in paquetes.values():
        print(f"Nombre: {paquete['nombre']}, Descripción: {paquete['descripcion']}, Precio: {paquete['precio']}")

# Funciones para gestionar los clientes
def registrar_cliente(clientes, nombre, correo):
    cliente = {
        "nombre": nombre,
        "correo": correo,
        "reservas": []
    }
    if nombre in clientes:
        print(f"El cliente '{nombre}' ya está registrado.")
    else:
        clientes[nombre] = cliente
        print(f"Cliente '{nombre}' registrado.")

def buscar_cliente(clientes, nombre):
    nombre_normalizado = nombre.strip().lower()
    for nombre_cliente, datos_cliente in clientes.items():
        if nombre_cliente.strip().lower() == nombre_normalizado:
            return datos_cliente
    return None

def actualizar_cliente(clientes, nombre, correo=None):
    if nombre in clientes:
        if correo:
            clientes[nombre]["correo"] = correo
        print(f"Cliente '{nombre}' actualizado.")
    else:
        print(f"El cliente '{nombre}' no existe.")

def eliminar_cliente(clientes, nombre):
    nombre_normalizado = nombre.strip().lower()  # Normalización del nombre
    cliente_encontrado = None
    for nombre_cliente, datos_cliente in list(clientes.items()):
        if nombre_cliente.strip().lower() == nombre_normalizado:
            cliente_encontrado = nombre_cliente
            break
    
    if cliente_encontrado:
        del clientes[cliente_encontrado]
        print(f"Cliente '{cliente_encontrado}' eliminado.")
    else:
        print(f"El cliente '{nombre}' no fue encontrado.")

# Funciones para gestionar las reservas
def hacer_reserva(clientes, tipo, destino, fecha, nombre_cliente):
    cliente = buscar_cliente(clientes, nombre_cliente)
    if cliente:
        reserva = {
            "tipo": tipo,
            "destino": destino,
            "fecha": fecha,
        }
        cliente["reservas"].append(reserva)
        print(f"Reserva de {tipo} a {destino} creada para {cliente['nombre']}.")
    else:
        print(f"Cliente {nombre_cliente} no encontrado.")

def mostrar_todas_reservas(clientes):
    print("\n--- Todas las reservas ---")
    for nombre_cliente, cliente in clientes.items():
        if cliente["reservas"]:
            print(f"Reservas de {cliente['nombre']}:")
            for reserva in cliente["reservas"]:
                print(f"- {reserva['tipo']} a {reserva['destino']} el {reserva['fecha']}")
        else:
            print(f"{cliente['nombre']} no tiene reservas.")

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
    
# Menú interactivo
def mostrar_menu():
    print("\n--- Agencia de Viajes ---")
    print("1. Crear paquete turístico")
    print("2. Registrar cliente")
    print("3. Hacer reserva")
    print("4. Buscar cliente y mostrar reservas")
    print("5. Buscar paquete turístico")
    print("6. Mostrar todas las reservas")
    print("7. Eliminar reserva")
    print("8. Actualizar paquete turístico")
    print("9. Mostrar paquetes turísticos")
    print("10. Eliminar paquete turístico")
    print("11. Actualizar cliente")
    print("12. Eliminar cliente")
    print("13. Salir")

# Bucle del menú #Hola
while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del paquete: ").strip().lower()
        descripcion = input("Descripción del paquete: ").strip()
        precio = input("Precio del paquete: ").strip()
        while not precio.replace('.', '', 1).isdigit():
            print("Por favor, ingrese un precio válido.")
            precio = input("Precio del paquete: ").strip()
        crear_paquete(paquetes, nombre, descripcion, precio)

    elif opcion == "2":
        while True:
            nombre = input("Nombre del cliente: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre) and len(nombre) > 0:
                break
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        
        while True:
            correo = input("Correo del cliente: ").strip()
            if "@" in correo:
                break
            print("Error: El correo debe contener '@'.")
        
        registrar_cliente(clientes, nombre, correo)

    elif opcion == "3":
        nombre_cliente = input("Nombre del cliente para la reserva: ").strip()
        tipo_reserva = input("Tipo de reserva (vuelo/hotel): ").strip().lower()
        if tipo_reserva not in ["vuelo", "hotel"]:
            print("Error: El tipo de reserva debe ser 'vuelo' o 'hotel'.")
            break
        destino = seleccionar_hotel() if tipo_reserva == "hotel" else input("Destino: ").strip()
        fecha = input("Fecha (YYYY-MM-DD): ").strip()
        while not validar_fecha(fecha):
            print("Error: El formato de la fecha es incorrecto. Intente de nuevo (formato YYYY-MM-DD).")
            break
        fecha = input("Fecha (YYYY-MM-DD): ").strip()
        hacer_reserva(clientes, tipo_reserva, destino, fecha, nombre_cliente)


    elif opcion == "4":
        nombre_cliente = input("Nombre del cliente: ").strip()
        cliente = buscar_cliente(clientes, nombre_cliente)
        if cliente:
            print(f"Cliente: {cliente['nombre']}, Correo: {cliente['correo']}")
            for reserva in cliente["reservas"]:
                print(f"Reserva {reserva['tipo']} a {reserva['destino']} en {reserva['fecha']}")
        else:
            print(f"Cliente {nombre_cliente} no encontrado.")

    elif opcion == "5":
        nombre_paquete = input("Nombre del paquete: ").strip().lower()
        paquete = buscar_paquete(paquetes, nombre_paquete)
        if paquete:
            print(f"Nombre: {paquete['nombre']}, Descripción: {paquete['descripcion']}, Precio: {paquete['precio']}")
        else:
            print(f"Paquete {nombre_paquete} no encontrado.")

    elif opcion == "6":
        mostrar_todas_reservas(clientes)

    elif opcion == "7":
        nombre_cliente = input("Nombre del cliente para eliminar la reserva: ").strip().lower()
        destino = input("Destino de la reserva a eliminar: ").strip()
        eliminar_reserva(clientes, nombre_cliente, destino)

    elif opcion == "8":
        nombre_paquete = input("Nombre del paquete a actualizar: ").strip().lower()
        descripcion = input("Nueva descripción (dejar vacío si no se actualiza): ").strip()
        precio = input("Nuevo precio (dejar vacío si no se actualiza): ").strip()
        actualizar_paquete(paquetes, nombre_paquete, descripcion, precio)

    elif opcion == "9":
        mostrar_paquetes(paquetes)

    elif opcion == "10":
        nombre_paquete = input("Nombre del paquete a eliminar: ").strip()
        eliminar_paquete(paquetes, nombre_paquete)

    elif opcion == "11":
        nombre_cliente = input("Nombre del cliente a actualizar: ").strip()
        nuevo_correo = input("Nuevo correo del cliente: ").strip()
        actualizar_cliente(clientes, nombre_cliente, nuevo_correo)

    elif opcion == "12":
        nombre_cliente = input("Nombre del cliente a eliminar: ").strip().lower()
        eliminar_cliente(clientes, nombre_cliente)

    elif opcion == "13":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Por favor, elige una opción correcta.")

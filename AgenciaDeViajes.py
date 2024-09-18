# Diccionarios con datos iniciales de paquetes y clientes

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
        "correo": "mariagonzalez@example.com",
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
    # Normaliza el nombre para hacer la búsqueda insensible a mayúsculas/minúsculas y espacios extras
    nombre_normalizado = nombre.strip().lower()
    for nombre_cliente, datos_cliente in clientes.items():
        # Normaliza los nombres de los clientes existentes para compararlos
        if nombre_cliente.strip().lower() == nombre_normalizado:
            return datos_cliente
    return None

# Funciones para gestionar las reservas
def hacer_reserva(clientes, tipo, destino, fecha, nombre_cliente):
    cliente = buscar_cliente(clientes, nombre_cliente)
    if cliente:
        reserva = {
            "tipo": tipo,  # 'vuelo' o 'hotel'
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
    print("8. Salir")

# Bucle del menú
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
                if nombre.isalpha():
                 break
                print("Dato no valido")
            
        while True:
            correo = input("Escribe el correo")
            if "@" in correo:
                break
            else:
                print("El dato no es valido")

    elif opcion == "3":
        # Validar el nombre del cliente
        while True:
            nombre_cliente = input("Nombre del cliente para la reserva: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre_cliente) and len(nombre_cliente) > 0:
                break
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")

        # Validar el tipo de reserva
        while True:
            tipo_reserva = input("Tipo de reserva (vuelo/hotel): ").strip().lower()
            if tipo_reserva in ["vuelo", "hotel"]:
                break
            print("Error: El tipo de reserva debe ser 'vuelo' o 'hotel'.")

        # Validar que el destino solo contenga letras
        while True:
            destino = input("Destino: ").strip()
            if all(c.isalpha() or c.isspace() for c in destino) and len(destino) > 0:
                break
            print("Error: El destino debe contener solo letras y no puede estar vacío.")

        # Validar el formato de la fecha como YYYY-MM-DD y que no sea en el pasado
        while True:
            fecha = input("Fecha (YYYY-MM-DD): ").strip()
            try:
                fecha_reserva = datetime.strptime(fecha, '%Y-%m-%d')
                if fecha_reserva >= datetime.now():
                    break
                else:
                    print("Error: La fecha no puede ser en el pasado.")
            except ValueError:
                print("Error: La fecha debe tener el formato YYYY-MM-DD.")

        # Hacer la reserva si todas las validaciones son correctas
        hacer_reserva(clientes, tipo_reserva, destino, fecha, nombre_cliente)

    elif opcion == "4":
        nombre_cliente = input("Nombre del cliente: ").strip().lower()
        cliente = buscar_cliente(clientes, nombre_cliente)
        if cliente:
            print(f"Cliente: {cliente['nombre']}, Correo: {cliente['correo']}")
            for reserva in cliente["reservas"]:
                print(f"Reserva {reserva['tipo']} a {reserva['destino']} el {reserva['fecha']}")
        else:
            print("Cliente no encontrado.")

    elif opcion == "5":
        nombre_paquete = input("Nombre del paquete turístico: ").strip().lower()
        paquete = buscar_paquete(paquetes, nombre_paquete)
        if paquete:
            print(f"Paquete: {paquete['nombre']}, Descripción: {paquete['descripcion']}, Precio: {paquete['precio']}")
        else:
            print("Paquete no encontrado.")

    elif opcion == "6":
        mostrar_todas_reservas(clientes)

    elif opcion == "7":
        nombre_cliente = input("Nombre del cliente para eliminar reserva: ").strip()
        destino = input("Destino de la reserva a eliminar: ").strip()

        while not all(c.isalpha() or c.isspace() for c in destino):
            print("Error: El destino debe contener solo letras.")
            destino = input("Destino de la reserva a eliminar: ").strip()

        eliminar_reserva(clientes, nombre_cliente, destino)

        

    elif opcion == "8":
        print("Gracias por utilizar la Agencia de Viajes.")
        break

    else:
        print("Opción no válida, intenta nuevamente.")
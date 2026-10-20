codigos = []
dnis_remitentes = []
nombres_remitentes = []
dnis_destinatarios = []
nombres_destinatarios = []
destinos = []

def registrar_paquete():
    """Función para registrar un nuevo paquete con validación de DNI"""
    print("\n--- REGISTRO DE NUEVO PAQUETE ---")

    dni_rem = input("Ingrese DNI del remitente (8 dígitos): ")
    while len(dni_rem) != 8 or not dni_rem.isdigit():
        print("ERROR: El DNI debe tener exactamente 8 números.")
        dni_rem = input("Ingrese DNI del remitente (8 dígitos): ")

    nombre_rem = input("Ingrese nombre completo del remitente: ")

    dni_dest = input("Ingrese DNI del destinatario (8 dígitos): ")
    while len(dni_dest) != 8 or not dni_dest.isdigit():
        print("ERROR: El DNI debe tener exactamente 8 números.")
        dni_dest = input("Ingrese DNI del destinatario (8 dígitos): ")

    nombre_dest = input("Ingrese nombre completo del destinatario: ")

    destino = input("Ingrese ciudad de destino: ")

    codigo_nuevo = "GUI-" + str(1001 + len(codigos))

    codigos.append(codigo_nuevo)
    dnis_remitentes.append(dni_rem)
    nombres_remitentes.append(nombre_rem)
    dnis_destinatarios.append(dni_dest)
    nombres_destinatarios.append(nombre_dest)
    destinos.append(destino)

    print("\n¡REGISTRO EXITOSO!")
    print("El código de guía asignado es:", codigo_nuevo)

def buscar_paquete():
    """Función para buscar un paquete utilizando su código de guía"""
    print("\n--- BÚSQUEDA DE PAQUETE ---")
    codigo_buscar = input("Ingrese el código de guía a buscar: ")

    if codigo_buscar in codigos:
        posicion = codigos.index(codigo_buscar)
        print("\n--- PAQUETE ENCONTRADO ---")
        print("Código Guía     :", codigos[posicion])
        print("DNI Remitente   :", dnis_remitentes[posicion])
        print("Nombre Remitente:", nombres_remitentes[posicion])
        print("DNI Destinatario:", dnis_destinatarios[posicion])
        print("Destino         :", destinos[posicion])
    else:
        print("\nERROR: El código de guía ingresado no existe.")

def menu_principal():
    opcion = 0
    while opcion != 4:
        print("\n========================================")
        print("   MESA DE PARTES - HUASCAR CARGO")
        print("========================================")
        print("1. Registrar nuevo paquete")
        print("2. Buscar paquete por código")
        print("3. Ver todos los paquetes")
        print("4. Salir")
        print("========================================")

        try:
            opcion = int(input("Seleccione una opción (1-4): "))
        except ValueError:
            print("\nERROR: Debe ingresar un número válido.")
            continue

        if opcion == 1:
            registrar_paquete()
        elif opcion == 2:
            buscar_paquete()
        elif opcion == 3:
            print("Ingrese los datos del paquete a ver: ")
        elif opcion == 4:
            print("\nSaliendo del sistema...")
        else:
            print("\nOpción no válida. Por favor ingrese un número del 1 al 4.")

if __name__ == "__main__":
    menu_principal()

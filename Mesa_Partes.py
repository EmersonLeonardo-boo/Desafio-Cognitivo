codigos = []
dnis_remitentes = []
nombres_remitentes = []
dnis_destinatarios = []
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
        
    destino = input("Ingrese ciudad de destino: ")
    
    codigo_nuevo = "GUI-" + str(1001 + len(codigos))
    
    codigos.append(codigo_nuevo)
    dnis_remitentes.append(dni_rem)
    nombres_remitentes.append(nombre_rem)
    dnis_destinatarios.append(dni_dest)
    destinos.append(destino)
    
    print("\n¡REGISTRO EXITOSO!")
    print("El código de guía asignado es:", codigo_nuevo)

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
            print("\nDebe ingresar un número válido.")
            continue

        if opcion == 1:
            registrar_paquete()
        elif opcion == 2:
            print("Ingrese los datos del paquete a buscar: ")
        elif opcion == 3:
            print("Ingrese los datos del paquete a ver: ")
        elif opcion == 4:
            print("\nSaliendo del sistema...")
        else:
            print("\nOpción no válida. Por favor ingrese un número del 1 al 4.")
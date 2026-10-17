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
            print("Ingrese los datos del paquete a registrar: ")
        elif opcion == 2:
            print("Ingrese los datos del paquete a buscar: ")
        elif opcion == 3:
            print("Ingrese los datos del paquete a ver: ")
        elif opcion == 4:
            print("\nSaliendo del sistema...")
        else:
            print("\nOpción no válida. Por favor ingrese un número del 1 al 4.")
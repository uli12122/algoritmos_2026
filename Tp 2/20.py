opuestos = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}

pila_movimientos = []

def registrar_movimiento():
    try:
        pasos = int(input("Ingrese la cantidad de pasos: "))
        direccion = input("Ingrese la dirección: ").lower()

        if direccion in opuestos:
            pila_movimientos.append((pasos, direccion))
            print("Movimiento registrado correctamente.\n")
        else:
            print("Dirección inválida.\n")
    except ValueError:
        print("Error: los pasos deben ser un número.\n")


def mostrar_movimientos():
    if not pila_movimientos:
        print("No hay movimientos registrados.\n")
    else:
        print("Movimientos registrados:")
        for pasos, direccion in pila_movimientos:
            print(f"{pasos} pasos hacia {direccion}")
        print()


def volver_al_origen():
    if not pila_movimientos:
        print("No hay movimientos para deshacer.\n")
        return

    print("Secuencia para volver al origen:")

    while pila_movimientos:
        pasos, direccion = pila_movimientos.pop()
        direccion_opuesta = opuestos[direccion]
        print(f"{pasos} pasos hacia {direccion_opuesta}")

    print("El robot volvió al punto de partida.\n")


def menu():
    opcion = 0

    while opcion != 4:
        print("===== MENÚ =====")
        print("1. Registrar movimiento")
        print("2. Mostrar movimientos")
        print("3. Volver al origen")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            print()

            if opcion == 1:
                registrar_movimiento()
            elif opcion == 2:
                mostrar_movimientos()
            elif opcion == 3:
                volver_al_origen()
            elif opcion == 4:
                print("Saliendo del programa...")
            else:
                print("Opción inválida.\n")

        except ValueError:
            print("Ingrese un número válido.\n")

menu()
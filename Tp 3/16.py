from heapq import heappush, heappop

def agregar_documento(cola, nombre, prioridad):
    """
    Agrega un documento a la cola de impresión.
    """
    global contador

    heappush(cola, (-prioridad, contador, nombre))
    contador += 1


def imprimir_documento(cola):
    if not cola:
        print("No hay documentos para imprimir")
        return

    prioridad, orden, nombre = heappop(cola)
    print(f"Imprimiendo documento: {nombre}")


def mostrar_cola(cola):
    if not cola:
        print("La cola está vacía")
        return

    print("\nDocumentos en cola:")

    for prioridad, orden, nombre in sorted(cola):
        print(nombre)


cola_impresion = []
contador = 0

agregar_documento(cola_impresion, "Empleado_1", 1)
agregar_documento(cola_impresion, "Empleado_2", 1)
agregar_documento(cola_impresion, "Empleado_3", 1)

print("\na) Se cargaron 3 documentos de empleados")

print("\nb) Imprimiendo primer documento")
imprimir_documento(cola_impresion)

agregar_documento(cola_impresion, "TI_1", 2)
agregar_documento(cola_impresion, "TI_2", 2)

print("\nc) Se cargaron 2 documentos de TI")

agregar_documento(cola_impresion, "Gerente_1", 3)

print("\nd) Se cargó 1 documento de gerente")

print("\ne) Imprimiendo dos documentos")
imprimir_documento(cola_impresion)
imprimir_documento(cola_impresion)

agregar_documento(cola_impresion, "Empleado_4", 1)
agregar_documento(cola_impresion, "Empleado_5", 1)
agregar_documento(cola_impresion, "Gerente_2", 3)

print("\nf) Se cargaron 2 empleados y 1 gerente")

while True:

    print("\n========== MENÚ ==========")
    print("1. Agregar documento de Empleado")
    print("2. Agregar documento de TI")
    print("3. Agregar documento de Gerente")
    print("4. Imprimir siguiente documento")
    print("5. Mostrar cola")
    print("6. Imprimir TODOS los documentos")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del documento: ")
        agregar_documento(cola_impresion, nombre, 1)

    elif opcion == "2":
        nombre = input("Nombre del documento: ")
        agregar_documento(cola_impresion, nombre, 2)

    elif opcion == "3":
        nombre = input("Nombre del documento: ")
        agregar_documento(cola_impresion, nombre, 3)

    elif opcion == "4":
        imprimir_documento(cola_impresion)

    elif opcion == "5":
        mostrar_cola(cola_impresion)

    elif opcion == "6":

        if not cola_impresion:
            print("No hay documentos para imprimir")
        else:
            print("\nImprimiendo todos los documentos:\n")

            while cola_impresion:
                imprimir_documento(cola_impresion)

    elif opcion == "7":
        print("Fin del programa")
        break

    else:
        print("Opción inválida")
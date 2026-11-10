from queue import PriorityQueue


EMPLEADO = 1
TI = 2
GERENTE = 3


def cargar_documento(cola, nombre, prioridad):
    cola.put((-prioridad, nombre))


def imprimir_siguiente(cola):
    if cola.empty():
        print("La cola de impresión está vacía.")
        return

    nombre = cola.get()
    print(nombre)


def imprimir_todos(cola):
    while not cola.empty():
        imprimir_siguiente(cola)


cola_impresion = PriorityQueue()

cargar_documento(cola_impresion, "Empleado 1", EMPLEADO)
cargar_documento(cola_impresion, "Empleado 2", EMPLEADO)
cargar_documento(cola_impresion, "Empleado 3", EMPLEADO)

print("Primer documento:")
imprimir_siguiente(cola_impresion)

cargar_documento(cola_impresion, "TI 1", TI)
cargar_documento(cola_impresion, "TI 2", TI)

cargar_documento(cola_impresion, "Gerente 1", GERENTE)

print("\nDos primeros documentos:")
imprimir_siguiente(cola_impresion)
imprimir_siguiente(cola_impresion)

cargar_documento(cola_impresion, "Empleado 4", EMPLEADO)
cargar_documento(cola_impresion, "Empleado 5", EMPLEADO)
cargar_documento(cola_impresion, "Gerente 2", GERENTE)

print("\nDocumentos restantes:")
imprimir_todos(cola_impresion)

from collections import deque

def eliminar_facebook(cola):
    cola_aux = deque()

    while cola:
        notificacion = cola.popleft()

        if notificacion["app"] != "Facebook":
            cola_aux.append(notificacion)

    while cola_aux:
        cola.append(cola_aux.popleft())


def mostrar_twitter_python(cola):
    cola_aux = deque()

    print("\nNotificaciones de Twitter que contienen 'Python':")

    encontrado = False

    while cola:
        notificacion = cola.popleft()

        if (notificacion["app"] == "Twitter"
                and "Python" in notificacion["mensaje"]):
            print(notificacion)
            encontrado = True

        cola_aux.append(notificacion)

    while cola_aux:
        cola.append(cola_aux.popleft())

    if not encontrado:
        print("No se encontraron notificaciones.")


def guardar_en_pila(cola):
    pila = []
    cola_aux = deque()

    hora_inicio = "11:43"
    hora_fin = "15:57"

    while cola:
        notificacion = cola.popleft()

        if hora_inicio <= notificacion["hora"] <= hora_fin:
            pila.append(notificacion)

        cola_aux.append(notificacion)

    while cola_aux:
        cola.append(cola_aux.popleft())

    return pila


def mostrar_cola(cola):
    if not cola:
        print("La cola está vacía.")
    else:
        for notificacion in cola:
            print(notificacion)


cola_notificaciones = deque()

cola_notificaciones.append({
    "hora": "10:15",
    "app": "Facebook",
    "mensaje": "Nuevo comentario"
})

cola_notificaciones.append({
    "hora": "12:30",
    "app": "Twitter",
    "mensaje": "Estoy aprendiendo Python"
})

cola_notificaciones.append({
    "hora": "13:45",
    "app": "Instagram",
    "mensaje": "Nueva historia"
})

cola_notificaciones.append({
    "hora": "14:20",
    "app": "Twitter",
    "mensaje": "Curso de Python disponible"
})

cola_notificaciones.append({
    "hora": "16:10",
    "app": "Facebook",
    "mensaje": "Nueva solicitud de amistad"
})


while True:

    print("\n===== MENÚ =====")
    print("1. Mostrar cola")
    print("2. Eliminar notificaciones de Facebook")
    print("3. Mostrar tweets que contienen 'Python'")
    print("4. Guardar en pila las notificaciones entre 11:43 y 15:57")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nContenido de la cola:")
        mostrar_cola(cola_notificaciones)

    elif opcion == "2":
        eliminar_facebook(cola_notificaciones)
        print("\nNotificaciones de Facebook eliminadas")

    elif opcion == "3":
        mostrar_twitter_python(cola_notificaciones)

    elif opcion == "4":
        pila = guardar_en_pila(cola_notificaciones)

        print("\nCantidad de notificaciones encontradas:",
              len(pila))

        print("\nContenido de la pila:")

        while pila:
            print(pila.pop())

    elif opcion == "5":
        print("Fin del programa")
        break

    else:
        print("Opción inválida")
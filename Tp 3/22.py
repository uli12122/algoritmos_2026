from collections import deque

def mostrar_cola(cola):
    if not cola:
        print("La cola está vacía")
        return

    for personaje in cola:
        print(personaje)


def buscar_capitana_marvel(cola):
    cola_aux = deque()
    encontrado = False

    while cola:
        personaje = cola.popleft()

        if personaje["superheroe"] == "Capitana Marvel":
            print(
                f"El personaje de Capitana Marvel es: {personaje['nombre']}")
            encontrado = True

        cola_aux.append(personaje)

    while cola_aux:
        cola.append(cola_aux.popleft())

    if not encontrado:
        print("Capitana Marvel no se encuentra en la cola")


def superheroes_femeninos(cola):
    cola_aux = deque()

    print("\nSuperhéroes femeninos:")

    while cola:
        personaje = cola.popleft()

        if personaje["genero"] == "F":
            print(personaje["superheroe"])

        cola_aux.append(personaje)

    while cola_aux:
        cola.append(cola_aux.popleft())


def personajes_masculinos(cola):
    cola_aux = deque()

    print("\nPersonajes masculinos:")

    while cola:
        personaje = cola.popleft()

        if personaje["genero"] == "M":
            print(personaje["nombre"])

        cola_aux.append(personaje)

    while cola_aux:
        cola.append(cola_aux.popleft())


def buscar_scott_lang(cola):
    cola_aux = deque()
    encontrado = False

    while cola:
        personaje = cola.popleft()

        if personaje["nombre"] == "Scott Lang":
            print(
                f"El superhéroe de Scott Lang es: {personaje['superheroe']}")
            encontrado = True

        cola_aux.append(personaje)

    while cola_aux:
        cola.append(cola_aux.popleft())

    if not encontrado:
        print("Scott Lang no se encuentra en la cola")


def nombres_con_s(cola):
    cola_aux = deque()

    print("\nPersonajes o superhéroes que comienzan con S:")

    while cola:
        personaje = cola.popleft()

        if (personaje["nombre"].startswith("S") or
                personaje["superheroe"].startswith("S")):
            print(personaje)

        cola_aux.append(personaje)

    while cola_aux:
        cola.append(cola_aux.popleft())


def buscar_carol_danvers(cola):
    cola_aux = deque()
    encontrado = False

    while cola:
        personaje = cola.popleft()

        if personaje["nombre"] == "Carol Danvers":
            print("Carol Danvers se encuentra en la cola.")
            print("Superhéroe:", personaje["superheroe"])
            encontrado = True

        cola_aux.append(personaje)

    while cola_aux:
        cola.append(cola_aux.popleft())

    if not encontrado:
        print("Carol Danvers NO se encuentra en la cola")


cola_mcu = deque()

cola_mcu.append({
    "nombre": "Tony Stark",
    "superheroe": "Iron Man",
    "genero": "M"
})

cola_mcu.append({
    "nombre": "Steve Rogers",
    "superheroe": "Capitán América",
    "genero": "M"
})

cola_mcu.append({
    "nombre": "Natasha Romanoff",
    "superheroe": "Black Widow",
    "genero": "F"
})

cola_mcu.append({
    "nombre": "Carol Danvers",
    "superheroe": "Capitana Marvel",
    "genero": "F"
})

cola_mcu.append({
    "nombre": "Scott Lang",
    "superheroe": "Ant-Man",
    "genero": "M"
})

cola_mcu.append({
    "nombre": "Stephen Strange",
    "superheroe": "Doctor Strange",
    "genero": "M"
})


while True:

    print("\n========== MENÚ ==========")
    print("1. Mostrar cola completa")
    print("2. Buscar personaje de Capitana Marvel")
    print("3. Mostrar superhéroes femeninos")
    print("4. Mostrar personajes masculinos")
    print("5. Buscar superhéroe de Scott Lang")
    print("6. Mostrar nombres que comienzan con S")
    print("7. Buscar Carol Danvers")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_cola(cola_mcu)

    elif opcion == "2":
        buscar_capitana_marvel(cola_mcu)

    elif opcion == "3":
        superheroes_femeninos(cola_mcu)

    elif opcion == "4":
        personajes_masculinos(cola_mcu)

    elif opcion == "5":
        buscar_scott_lang(cola_mcu)

    elif opcion == "6":
        nombres_con_s(cola_mcu)

    elif opcion == "7":
        buscar_carol_danvers(cola_mcu)

    elif opcion == "8":
        print("Fin del programa")
        break

    else:
        print("Opción inválida")
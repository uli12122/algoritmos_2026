pila = []


def cargar_personajes():
    global pila
    pila = []
    pila.append(("Iron Man", 10))
    pila.append(("Captain America", 9))
    pila.append(("Groot", 5))
    pila.append(("Rocket Raccoon", 6))
    pila.append(("Black Widow", 8))
    pila.append(("Doctor Strange", 6))
    pila.append(("Captain Marvel", 3))
    pila.append(("Gamora", 5))
    print("Personajes cargados.\n")


def posicion_personajes():
    aux = []
    posicion = 1

    while pila:
        nombre, pelis = pila.pop()

        if nombre == "Rocket Raccoon" or nombre == "Groot":
            print(f"{nombre} está en la posición {posicion}")

        aux.append((nombre, pelis))
        posicion += 1

    while aux:
        pila.append(aux.pop())

    print()


def mas_de_5_peliculas():
    aux = []
    print("Personajes con más de 5 películas:")

    while pila:
        nombre, pelis = pila.pop()

        if pelis > 5:
            print(f"{nombre} - {pelis} películas")

        aux.append((nombre, pelis))

    while aux:
        pila.append(aux.pop())

    print()


def peliculas_black_widow():
    aux = []
    encontrado = False

    while pila:
        nombre, pelis = pila.pop()

        if nombre == "Black Widow":
            print(f"Black Widow participó en {pelis} películas")
            encontrado = True

        aux.append((nombre, pelis))

    while aux:
        pila.append(aux.pop())

    if not encontrado:
        print("Black Widow no está en la pila.\n")
    else:
        print()


def personajes_por_letra():
    aux = []
    print("Personajes que empiezan con C, D o G:")

    while pila:
        nombre, pelis = pila.pop()

        if nombre[0].upper() in ["C", "D", "G"]:
            print(nombre)

        aux.append((nombre, pelis))

    while aux:
        pila.append(aux.pop())

    print()


def mostrar_pila():
    if not pila:
        print("La pila está vacía.\n")
    else:
        print("Pila actual (cima = último elemento):")
        for elem in reversed(pila):
            print(elem)
        print()


def menu():
    opcion = 0

    while opcion != 7:
        print("===== MENÚ MCU =====")
        print("1. Cargar personajes")
        print("2. Mostrar pila")
        print("3. Posición de Rocket y Groot")
        print("4. Personajes con más de 5 películas")
        print("5. Películas de Black Widow")
        print("6. Personajes que empiezan con C, D o G")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            print()

            if opcion == 1:
                cargar_personajes()
            elif opcion == 2:
                mostrar_pila()
            elif opcion == 3:
                posicion_personajes()
            elif opcion == 4:
                mas_de_5_peliculas()
            elif opcion == 5:
                peliculas_black_widow()
            elif opcion == 6:
                personajes_por_letra()
            elif opcion == 7:
                print("Saliendo del programa...")
            else:
                print("Opción inválida.\n")

        except ValueError:
            print("Ingrese un número válido.\n")


menu()
from super_heroes_data import superheroes
from queue import Queue


def listar_por_nombre():
    ordenados = sorted(superheroes, key=lambda x: x["name"])
    for personaje in ordenados:
        print(personaje["name"])


def buscar_posiciones():
    for i, personaje in enumerate(superheroes):
        if personaje["name"] == "The Thing":
            print("The Thing está en posición:", i)

        if personaje["name"] == "Rocket Raccoon":
            print("Rocket Raccoon está en posición:", i)


def listar_villanos():
    for personaje in superheroes:
        if personaje["is_villain"]:
            print(personaje["name"])


def villanos_antes_1980():
    cola = Queue()

    for personaje in superheroes:
        if personaje["is_villain"]:
            cola.put(personaje)

    print("Villanos aparecidos antes de 1980:")
    while not cola.empty():
        villano = cola.get()
        if villano["first_appearance"] < 1980:
            print(villano["name"], "-", villano["first_appearance"])


def filtrar_iniciales():
    for personaje in superheroes:
        nombre = personaje["name"]
        if nombre.startswith(("Bl", "G", "My", "W")):
            print(nombre)


def listar_por_nombre_real():
    ordenados = sorted(superheroes, key=lambda x: str(x["real_name"]))
    for personaje in ordenados:
        print(personaje["real_name"], "-", personaje["name"])


def listar_por_fecha():
    ordenados = sorted(superheroes, key=lambda x: x["first_appearance"])
    for personaje in ordenados:
        print(personaje["name"], "-", personaje["first_appearance"])


def modificar_antman():
    for personaje in superheroes:
        if personaje["name"] == "Ant Man":
            personaje["real_name"] = "Scott Lang"
            print("Modificado:", personaje)


def buscar_biografia():
    for personaje in superheroes:
        bio = personaje["short_bio"].lower()
        if "time-traveling" in bio or "suit" in bio:
            print(personaje["name"])


def eliminar_personajes():
    nombres = ["Electro", "Baron Zemo"]

    for nombre in nombres:
        for personaje in superheroes:
            if personaje["name"] == nombre:
                print("Eliminado:", personaje)
                superheroes.remove(personaje)
                break


opcion = -1
while opcion != 0:
    print("1: Listar por nombre")
    print("2: Buscar posiciones de The Thing y Rocket Raccoon")
    print("3: Listar villanos")
    print("4: Villanos antes de 1980")
    print("5: Filtrar por iniciales")
    print("6: Listar por nombre real")
    print("7: Listar por fecha")
    print("8: Modificar nombre real de Ant Man")
    print("9: Buscar que en biografía incluyan 'time-traveling' o 'suit'")
    print("10: Eliminar a Electro y Baron Zemo")
    print("0: Salir")

    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        listar_por_nombre()

    elif opcion == 2:
        buscar_posiciones()

    elif opcion == 3:
        listar_villanos()

    elif opcion == 4:
        villanos_antes_1980()

    elif opcion == 5:
        filtrar_iniciales()

    elif opcion == 6:
        listar_por_nombre_real()

    elif opcion == 7:
        listar_por_fecha()

    elif opcion == 8:
        modificar_antman()

    elif opcion == 9:
        buscar_biografia()

    elif opcion == 10:
        eliminar_personajes()

    elif opcion == 0:
        print("Programa finalizado")

    else:
        print("Opción inválida")
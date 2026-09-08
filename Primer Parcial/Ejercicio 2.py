from super_heroes_data import superheroes
from queue import Queue


def listar_por_nombre(lista):
    ordenados = sorted(lista, key=lambda x: x["name"])
    for personaje in ordenados:
        print(personaje["name"])


def buscar_posiciones(lista):
    pos_thing = -1
    pos_rocket = -1

    for i, personaje in enumerate(lista):
        if personaje["name"] == "The Thing":
            pos_thing = i
        if personaje["name"] == "Rocket Raccoon":
            pos_rocket = i

    if pos_thing != -1:
        print("The Thing está en posición:", pos_thing)
    else:
        print("The Thing no está en la lista")

    if pos_rocket != -1:
        print("Rocket Raccoon está en posición:", pos_rocket)
    else:
        print("Rocket Raccoon no está en la lista")


def listar_villanos(lista):
    for personaje in lista:
        if personaje["is_villain"]:
            print(personaje["name"])


def villanos_antes_1980(lista):
    cola_villanos = Queue()

    for personaje in lista:
        if personaje["is_villain"]:
            cola_villanos.put(personaje)

    while not cola_villanos.empty():
        villano = cola_villanos.get()
        if villano["first_appearance"] < 1980:
            print(villano["name"], "-", villano["first_appearance"])


def filtrar_iniciales(lista):
    for personaje in lista:
        nombre = personaje["name"]
        if nombre.startswith(("Bl", "G", "My", "W")):
            print(nombre)


def listar_por_nombre_real(lista):
    ordenados = sorted(lista, key=lambda x: str(x["real_name"]))
    for personaje in ordenados:
        print(personaje["real_name"], "-", personaje["name"])


def listar_por_fecha(lista):
    ordenados = sorted(lista, key=lambda x: x["first_appearance"])
    for personaje in ordenados:
        print(personaje["name"], "-", personaje["first_appearance"])


def modificar_antman(lista):
    for personaje in lista:
        if personaje["name"] == "Ant Man":
            personaje["real_name"] = "Scott Lang"
            print("Modificado:", personaje)
            return
    print("Ant Man no está en la lista")


def buscar_biografia(lista):
    for personaje in lista:
        bio = personaje["short_bio"].lower()
        if "time-traveling" in bio or "suit" in bio:
            print(personaje["name"])


def eliminar_personajes(lista):
    nombres_a_eliminar = ["Electro", "Baron Zemo"]
    for nombre in nombres_a_eliminar:
        encontrado = False
        for i, personaje in enumerate(lista):
            if personaje["name"] == nombre:
                print("Eliminado:", personaje)
                lista.pop(i)
                encontrado = True
        if not encontrado:
            print(nombre, "no estaba en la lista")


print("Ordenados por nombre:")
listar_por_nombre(superheroes)

print("\nPosiciones:")
buscar_posiciones(superheroes)

print("\nVillanos:")
listar_villanos(superheroes)

print("\nVillanos antes de 1980:")
villanos_antes_1980(superheroes)

print("\nNombres que empiezan con Bl, G, My, W:")
filtrar_iniciales(superheroes)

print("\nOrdenados por nombre real:")
listar_por_nombre_real(superheroes)

print("\nOrdenados por fecha de aparición:")
listar_por_fecha(superheroes)

print("\nModificar Ant Man:")
modificar_antman(superheroes)

print("\nBiografía contiene 'time-traveling' o 'suit':")
buscar_biografia(superheroes)

print("\nEliminar Electro y Baron Zemo:")
eliminar_personajes(superheroes)
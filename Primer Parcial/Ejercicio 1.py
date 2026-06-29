from super_heroes_data import superheroes
lista_heroes = superheroes[:15]


def listar_superheroes(lista, indice=0):
    if indice == len(lista):
        return

    print(f"{indice + 1}. {lista[indice]['name']}")
    listar_superheroes(lista, indice + 1)


def buscar_capitan_america(lista, indice=0):
    if indice == len(lista):
        return False

    if lista[indice]["name"] == "Captain America":
        return True

    return buscar_capitan_america(lista, indice + 1)


opcion = 0
while opcion != 3:
    print("1: Listar superhéroes")
    print("2: Buscar a Captain America")
    print("3: Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("\nLista de superhéroes:")
        listar_superheroes(lista_heroes)

    elif opcion == 2:
        if buscar_capitan_america(lista_heroes):
            print("\nCaptain America está en la lista")
        else:
            print("\nCaptain America NO está en la lista")

    elif opcion == 3:
        print("\nPrograma finalizado")

    else:
        print("\nOpción inválida")
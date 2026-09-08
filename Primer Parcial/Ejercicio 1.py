lista_heroes = ["Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Spider-Man", "Doctor Strange", "Black Panther", "Wanda",
    "Vision", "Falcon", "Winter Soldier", "Ant-Man",
    "Wasp", "Captain America"]


def listar_superheroes(lista, indice=0):
    if indice == len(lista):
        return
    print(f"{indice + 1}. {lista[indice]}")
    listar_superheroes(lista, indice + 1)


def buscar_captain_america(lista, indice=0):
    if indice == len(lista):
        return False
    if lista[indice] == "Captain America":
        return True
    return buscar_captain_america(lista, indice + 1)


listar_superheroes(lista_heroes)
print("¿Está Captain America?:", buscar_captain_america(lista_heroes))
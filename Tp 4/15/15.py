from lista_pokemons import lista_entrenadores


def buscar_entrenador(lista, nombre):
    for entrenador in lista:
        if entrenador["nombre"].lower() == nombre.lower():
            return entrenador

    return None


def buscar_pokemon(lista_pokemons, nombre):
    for pokemon in lista_pokemons:
        if pokemon["nombre"].lower() == nombre.lower():
            return pokemon

    return None


def mostrar_datos_pokemon(pokemon):
    for clave, valor in pokemon.items():
        print(f"{clave}: {valor}")



def cantidad_pokemons_de_entrenador(lista, nombre_entrenador):
    entrenador = buscar_entrenador(lista, nombre_entrenador)

    if entrenador is not None:
        cantidad = len(entrenador["pokemons"])

        print(
            f"{entrenador['nombre']} tiene "
            f"{cantidad} Pokémon."
        )
    else:
        print(f"No se encontró al entrenador {nombre_entrenador}.")



def entrenadores_mas_de_tres_torneos(lista):
    print("Entrenadores que ganaron más de tres torneos:")

    for entrenador in lista:
        if entrenador["torneos_ganados"] > 3:
            print(
                f"- {entrenador['nombre']} "
                f"({entrenador['torneos_ganados']} torneos)"
            )



def pokemon_mayor_nivel_entrenador_mas_torneos(lista):
    if len(lista) == 0:
        print("La lista de entrenadores está vacía.")
        return

    entrenador_mas_torneos = lista[0]

    for entrenador in lista:
        if (
            entrenador["torneos_ganados"]
            > entrenador_mas_torneos["torneos_ganados"]
        ):
            entrenador_mas_torneos = entrenador

    pokemon_mayor_nivel = entrenador_mas_torneos["pokemons"][0]

    for pokemon in entrenador_mas_torneos["pokemons"]:
        if pokemon["nivel"] > pokemon_mayor_nivel["nivel"]:
            pokemon_mayor_nivel = pokemon

    print(
        f"Entrenador con más torneos: "
        f"{entrenador_mas_torneos['nombre']}"
    )
    print(
        f"Torneos ganados: "
        f"{entrenador_mas_torneos['torneos_ganados']}"
    )
    print(
        f"Pokémon de mayor nivel: "
        f"{pokemon_mayor_nivel['nombre']}"
    )
    print(f"Nivel: {pokemon_mayor_nivel['nivel']}")



def mostrar_datos_entrenador(lista, nombre_entrenador):
    entrenador = buscar_entrenador(lista, nombre_entrenador)

    if entrenador is None:
        print(f"No se encontró al entrenador {nombre_entrenador}.")
        return

    print(f"\nDatos del entrenador: {entrenador['nombre']}")
    print(f"Torneos ganados: {entrenador['torneos_ganados']}")
    print(f"Batallas perdidas: {entrenador['batallas_perdidas']}")
    print(f"Batallas ganadas: {entrenador['batallas_ganadas']}")

    print("\nPokémons:")

    for pokemon in entrenador["pokemons"]:
        print(f"\nNombre: {pokemon['nombre']}")
        print(f"Nivel: {pokemon['nivel']}")
        print(f"Tipo: {pokemon['tipo']}")
        print(f"Subtipo: {pokemon['subtipo']}")



def entrenadores_con_mas_de_79_por_ciento(lista):
    print("Entrenadores con más del 79% de batallas ganadas:")

    for entrenador in lista:
        ganadas = entrenador["batallas_ganadas"]
        perdidas = entrenador["batallas_perdidas"]
        total_batallas = ganadas + perdidas

        if total_batallas > 0:
            porcentaje = ganadas * 100 / total_batallas

            if porcentaje > 79:
                print(
                    f"- {entrenador['nombre']}: "
                    f"{porcentaje:.2f}%"
                )



def entrenadores_por_tipo(lista):
    print(
        "Entrenadores con Pokémon de tipo Fuego y Planta "
        "o Agua/Volador:"
    )

    for entrenador in lista:
        tiene_fuego = False
        tiene_planta = False
        tiene_agua_volador = False

        for pokemon in entrenador["pokemons"]:
            if pokemon["tipo"].lower() == "fuego":
                tiene_fuego = True

            if pokemon["tipo"].lower() == "planta":
                tiene_planta = True

            if (
                pokemon["tipo"].lower() == "agua"
                and pokemon["subtipo"] is not None
                and pokemon["subtipo"].lower() == "volador"
            ):
                tiene_agua_volador = True

        if (tiene_fuego and tiene_planta) or tiene_agua_volador:
            print(f"- {entrenador['nombre']}")



def promedio_nivel(lista, nombre_entrenador):
    entrenador = buscar_entrenador(lista, nombre_entrenador)

    if entrenador is None:
        print(f"No se encontró al entrenador {nombre_entrenador}.")
        return

    pokemons = entrenador["pokemons"]

    if len(pokemons) == 0:
        print("El entrenador no tiene Pokémon.")
        return

    suma_niveles = 0

    for pokemon in pokemons:
        suma_niveles += pokemon["nivel"]

    promedio = suma_niveles / len(pokemons)

    print(
        f"El promedio de nivel de los Pokémon de "
        f"{entrenador['nombre']} es {promedio:.2f}."
    )



def cantidad_entrenadores_con_pokemon(lista, nombre_pokemon):
    cantidad = 0
    entrenadores = []

    for entrenador in lista:
        pokemon = buscar_pokemon(
            entrenador["pokemons"],
            nombre_pokemon
        )

        if pokemon is not None:
            cantidad += 1
            entrenadores.append(entrenador["nombre"])

    print(
        f"{cantidad} entrenador(es) tienen al Pokémon "
        f"{nombre_pokemon}."
    )

    if cantidad > 0:
        print("Entrenadores:")

        for nombre in entrenadores:
            print(f"- {nombre}")



def mostrar_pokemons_repetidos(lista):
    print("Entrenadores que tienen Pokémon repetidos:")

    hay_repetidos = False

    for entrenador in lista:
        nombres_pokemons = []
        repetidos = []

        for pokemon in entrenador["pokemons"]:
            nombre = pokemon["nombre"].lower()

            if nombre in nombres_pokemons:
                if nombre not in repetidos:
                    repetidos.append(nombre)
            else:
                nombres_pokemons.append(nombre)

        if len(repetidos) > 0:
            hay_repetidos = True
            print(
                f"- {entrenador['nombre']}: "
                f"{', '.join(repetidos)}"
            )

    if not hay_repetidos:
        print("No hay entrenadores con Pokémon repetidos.")



def entrenadores_con_pokemons_especificos(lista):
    pokemons_buscados = (
        "tyrantrum",
        "terrakion",
        "wingull"
    )

    print(
        "Entrenadores que tienen Tyrantrum, Terrakion "
        "o Wingull:"
    )

    for entrenador in lista:
        encontrados = []

        for pokemon in entrenador["pokemons"]:
            if pokemon["nombre"].lower() in pokemons_buscados:
                encontrados.append(pokemon["nombre"])

        if len(encontrados) > 0:
            print(
                f"- {entrenador['nombre']}: "
                f"{', '.join(encontrados)}"
            )



def verificar_pokemon_de_entrenador(
    lista,
    nombre_entrenador,
    nombre_pokemon
):
    entrenador = buscar_entrenador(lista, nombre_entrenador)

    if entrenador is None:
        print(f"No se encontró al entrenador {nombre_entrenador}.")
        return

    pokemon = buscar_pokemon(
        entrenador["pokemons"],
        nombre_pokemon
    )

    if pokemon is None:
        print(
            f"{entrenador['nombre']} no tiene al Pokémon "
            f"{nombre_pokemon}."
        )
        return

    print(
        f"{entrenador['nombre']} sí tiene al Pokémon "
        f"{pokemon['nombre']}."
    )

    print("\nDatos del entrenador:")
    print(f"Nombre: {entrenador['nombre']}")
    print(f"Torneos ganados: {entrenador['torneos_ganados']}")
    print(f"Batallas perdidas: {entrenador['batallas_perdidas']}")
    print(f"Batallas ganadas: {entrenador['batallas_ganadas']}")

    print("\nDatos del Pokémon:")
    mostrar_datos_pokemon(pokemon)



print("A.")
cantidad_pokemons_de_entrenador(
    lista_entrenadores,
    "Ash Ketchum"
)


print("\nB.")
entrenadores_mas_de_tres_torneos(
    lista_entrenadores
)


print("\nC.")
pokemon_mayor_nivel_entrenador_mas_torneos(
    lista_entrenadores
)


print("\nD.")
mostrar_datos_entrenador(
    lista_entrenadores,
    "Ash Ketchum"
)


print("\nE.")
entrenadores_con_mas_de_79_por_ciento(
    lista_entrenadores
)


print("\nF.")
entrenadores_por_tipo(
    lista_entrenadores
)


print("\nG.")
promedio_nivel(
    lista_entrenadores,
    "Ash Ketchum"
)


print("\nH.")
cantidad_entrenadores_con_pokemon(
    lista_entrenadores,
    "Wingull"
)


print("\nI.")
mostrar_pokemons_repetidos(
    lista_entrenadores
)


print("\nJ.")
entrenadores_con_pokemons_especificos(
    lista_entrenadores
)


print("\nK.")
nombre_entrenador = input("Ingrese el nombre del entrenador: ")
nombre_pokemon = input("Ingrese el nombre del Pokémon: ")

verificar_pokemon_de_entrenador(
    lista_entrenadores,
    nombre_entrenador,
    nombre_pokemon
)
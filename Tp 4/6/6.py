from lista_superheroes import lista_superheroes


def buscar_superheroe(lista, nombre):
    for superheroe in lista:
        if superheroe["nombre"].lower() == nombre.lower():
            return superheroe

    return None


def eliminar_superheroe(lista, nombre):
    for posicion in range(len(lista)):
        if lista[posicion]["nombre"].lower() == nombre.lower():
            eliminado = lista.pop(posicion)
            print(f"Se eliminó a {eliminado['nombre']}.")
            return

    print(f"No se encontró a {nombre}.")


def mostrar_anio_aparicion(lista, nombre):
    superheroe = buscar_superheroe(lista, nombre)

    if superheroe is not None:
        print(
            f"{superheroe['nombre']} apareció por primera vez "
            f"en el año {superheroe['anio_aparicion']}."
        )
    else:
        print(f"No se encontró a {nombre}.")


def cambiar_casa(lista, nombre, nueva_casa):
    superheroe = buscar_superheroe(lista, nombre)

    if superheroe is not None:
        superheroe["casa"] = nueva_casa
        print(
            f"La casa de {superheroe['nombre']} ahora es {nueva_casa}."
        )
    else:
        print(f"No se encontró a {nombre}.")


def mostrar_por_biografia(lista):
    print("Superhéroes que mencionan 'traje' o 'armadura':")

    for superheroe in lista:
        biografia = superheroe["biografia"].lower()

        if "traje" in biografia or "armadura" in biografia:
            print(f"- {superheroe['nombre']}")


def mostrar_anteriores_a_1963(lista):
    print("Superhéroes anteriores a 1963:")

    for superheroe in lista:
        if superheroe["anio_aparicion"] < 1963:
            print(
                f"- Nombre: {superheroe['nombre']} | "
                f"Año de aparición: {superheroe['anio_aparicion']} | "
                f"Casa: {superheroe['casa']}"
            )


def mostrar_casa(lista, nombres):
    for nombre in nombres:
        superheroe = buscar_superheroe(lista, nombre)

        if superheroe is not None:
            print(
                f"{superheroe['nombre']} pertenece a "
                f"{superheroe['casa']}."
            )
        else:
            print(f"No se encontró a {nombre}.")


def mostrar_informacion(lista, nombres):
    for nombre in nombres:
        superheroe = buscar_superheroe(lista, nombre)

        print(f"\nInformación de {nombre}:")

        if superheroe is not None:
            for clave, valor in superheroe.items():
                print(f"{clave}: {valor}")
        else:
            print("Superhéroe no encontrado.")


def listar_por_inicial(lista):
    iniciales = ("b", "m", "s")

    print("Superhéroes que comienzan con B, M o S:")

    for superheroe in lista:
        nombre = superheroe["nombre"].lower()

        if nombre.startswith(iniciales):
            print(f"- {superheroe['nombre']}")


def contar_por_casa(lista):
    cantidades = {}

    for superheroe in lista:
        casa = superheroe["casa"]

        if casa not in cantidades:
            cantidades[casa] = 0

        cantidades[casa] += 1

    print("Cantidad de superhéroes por casa:")

    for casa, cantidad in cantidades.items():
        print(f"- {casa}: {cantidad}")


print("A. Eliminar Linterna Verde")
eliminar_superheroe(lista_superheroes, "Linterna Verde")

print("\nB. Año de aparición de Wolverine")
mostrar_anio_aparicion(lista_superheroes, "Wolverine")

print("\nC. Cambiar la casa de Dr. Strange")
cambiar_casa(lista_superheroes, "Dr. Strange", "Marvel")

print("\nD. Superhéroes con traje o armadura")
mostrar_por_biografia(lista_superheroes)

print("\nE. Superhéroes anteriores a 1963")
mostrar_anteriores_a_1963(lista_superheroes)

print("\nF. Casa de Capitana Marvel y Mujer Maravilla")
mostrar_casa(
    lista_superheroes,
    ["Capitana Marvel", "Mujer Maravilla"]
)

print("\nG. Información de Flash y Star-Lord")
mostrar_informacion(
    lista_superheroes,
    ["Flash", "Star-Lord"]
)

print("\nH. Superhéroes que comienzan con B, M o S")
listar_por_inicial(lista_superheroes)

print("\nI. Cantidad de superhéroes por casa")
contar_por_casa(lista_superheroes)
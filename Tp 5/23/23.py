from lista_23 import lista_23
from arbol_23 import ArbolBinario


arbol = ArbolBinario()

for criatura in lista_23:
    arbol.insertar(
        criatura["nombre"],
        criatura["derrotado_por"]
    )



def listado_inorden():
    print("Criaturas ordenadas alfabéticamente:")

    for nodo in arbol.inorden():
        derrotado_por = nodo.derrotado_por

        if derrotado_por is None:
            derrotado_por = "Nadie"

        print(
            f"- {nodo.nombre} | "
            f"Derrotado por: {derrotado_por}"
        )



def cargar_descripcion():
    nombre = input(
        "Ingrese el nombre de la criatura: "
    )

    nodo = arbol.buscar(nombre)

    if nodo is not None:
        descripcion = input(
            "Ingrese una breve descripción: "
        )

        nodo.descripcion = descripcion

        print("Descripción cargada correctamente.")
    else:
        print("No se encontró la criatura.")



def mostrar_talos():
    nodo = arbol.buscar("Talos")

    if nodo is not None:
        print("Información de Talos:")
        print(f"Nombre: {nodo.nombre}")
        print(f"Derrotado por: {nodo.derrotado_por}")
        print(f"Descripción: {nodo.descripcion}")
        print(f"Capturada por: {nodo.capturada}")
    else:
        print("No se encontró a Talos.")



def tres_heroes_mas_derrotas():
    cantidades = {}

    for nodo in arbol.inorden():
        if nodo.derrotado_por is not None:
            heroe = nodo.derrotado_por

            if heroe not in cantidades:
                cantidades[heroe] = 0

            cantidades[heroe] += 1

    ranking = []

    for heroe, cantidad in cantidades.items():
        ranking.append((heroe, cantidad))

    ranking.sort(
        key=lambda elemento: (
            -elemento[1],
            elemento[0]
        )
    )

    print("Héroes o dioses con más criaturas derrotadas:")

    for heroe, cantidad in ranking[:3]:
        print(f"- {heroe}: {cantidad} criaturas")



def criaturas_derrotadas_por_heracles():
    print("Criaturas derrotadas por Heracles:")

    for nodo in arbol.inorden():
        if (
            nodo.derrotado_por is not None
            and nodo.derrotado_por.lower() == "heracles"
        ):
            print(f"- {nodo.nombre}")



def criaturas_no_derrotadas():
    print("Criaturas que no han sido derrotadas:")

    for nodo in arbol.inorden():
        if nodo.derrotado_por is None:
            print(f"- {nodo.nombre}")



def mostrar_campo_capturada():
    print("Criaturas y héroe o dios que las capturó:")

    for nodo in arbol.inorden():
        capturada = nodo.capturada

        if capturada is None:
            capturada = "Nadie"

        print(
            f"- {nodo.nombre} | "
            f"Capturada por: {capturada}"
        )



def modificar_capturas_heracles():
    nombres = [
        "Cerbero",
        "Toro de Creta",
        "Cierva de Cerinea",
        "Jabalí de Erimanto"
    ]

    for nombre in nombres:
        nodo = arbol.buscar(nombre)

        if nodo is not None:
            nodo.capturada = "Heracles"

    print(
        "Heracles capturó las criaturas correspondientes."
    )



def buscar_por_coincidencia():
    texto = input(
        "Ingrese el texto que desea buscar: "
    )

    coincidencias = arbol.buscar_por_coincidencia(texto)

    if len(coincidencias) == 0:
        print("No se encontraron coincidencias.")
        return

    print("Coincidencias encontradas:")

    for nodo in coincidencias:
        print(f"- {nodo.nombre}")



def eliminar_basilisco_y_sirenas():
    arbol.eliminar("Basilisco")
    arbol.eliminar("Sirenas")

    print("Se eliminaron Basilisco y Sirenas.")



def modificar_aves_estinfalo():
    nodo = arbol.buscar("Aves del Estínfalo")

    if nodo is not None:
        nodo.derrotado_por = "Heracles"
        nodo.descripcion = (
            "Heracles derrotó a varias Aves del Estínfalo."
        )

        print(
            "Se modificaron los datos de las Aves del Estínfalo."
        )
    else:
        print(
            "No se encontraron las Aves del Estínfalo."
        )



def cambiar_nombre_ladon():
    nodo = arbol.buscar("Ladón")

    if nodo is None:
        print("No se encontró a Ladón.")
        return

    derrotado_por = nodo.derrotado_por
    descripcion = nodo.descripcion
    capturada = nodo.capturada

    arbol.eliminar("Ladón")

    arbol.insertar(
        "Dragón Ladón",
        derrotado_por,
        descripcion
    )

    nuevo_nodo = arbol.buscar("Dragón Ladón")

    if nuevo_nodo is not None:
        nuevo_nodo.capturada = capturada

    print("Ladón fue cambiado por Dragón Ladón.")



def listado_por_nivel():
    print("Listado por nivel:")

    for nodo in arbol.por_nivel():
        print(f"- {nodo.nombre}")



def criaturas_capturadas_por_heracles():
    print("Criaturas capturadas por Heracles:")

    for nodo in arbol.inorden():
        if (
            nodo.capturada is not None
            and nodo.capturada.lower() == "heracles"
        ):
            print(f"- {nodo.nombre}")



print("A.")
listado_inorden()


print("\nB.")
cargar_descripcion()


print("\nC.")
mostrar_talos()


print("\nD.")
tres_heroes_mas_derrotas()


print("\nE.")
criaturas_derrotadas_por_heracles()


print("\nF.")
criaturas_no_derrotadas()


print("\nG.")
mostrar_campo_capturada()


print("\nH.")
modificar_capturas_heracles()


print("\nI.")
buscar_por_coincidencia()


print("\nJ.")
eliminar_basilisco_y_sirenas()


print("\nK.")
modificar_aves_estinfalo()


print("\nL.")
cambiar_nombre_ladon()


print("\nM.")
listado_por_nivel()


print("\nN.")
criaturas_capturadas_por_heracles()
from lista_5 import lista_5
from avl import AVL


arbol_mcu = AVL()

for personaje in lista_5:
    arbol_mcu.insertar(
        personaje["nombre"],
        personaje["es_heroe"]
    )



def mostrar_datos_arbol():
    print("Datos almacenados en el árbol:")

    for nodo in arbol_mcu.inorden(arbol_mcu.raiz):
        if nodo.es_heroe:
            tipo = "Héroe"
        else:
            tipo = "Villano"

        print(f"{nodo.nombre} - {tipo}")



def listar_villanos():
    print("Villanos ordenados alfabéticamente:")

    for nodo in arbol_mcu.inorden(arbol_mcu.raiz):
        if nodo.es_heroe is False:
            print(f"- {nodo.nombre}")



def heroes_que_empiezan_con_c():
    print("Superhéroes que empiezan con C:")

    for nodo in arbol_mcu.inorden(arbol_mcu.raiz):
        if nodo.es_heroe and nodo.nombre.lower().startswith("c"):
            print(f"- {nodo.nombre}")



def contar_superheroes():
    cantidad = 0

    for nodo in arbol_mcu.inorden(arbol_mcu.raiz):
        if nodo.es_heroe:
            cantidad += 1

    print(f"Cantidad de superhéroes: {cantidad}")



def buscar_por_proximidad(consulta):
    nodo_mas_cercano = None
    mejor_puntaje = 0

    for nodo in arbol_mcu.inorden(arbol_mcu.raiz):
        texto_consulta = consulta.lower()
        texto_nodo = nodo.nombre.lower()

        caracteres_iguales = 0

        for caracter in texto_consulta:
            if caracter in texto_nodo:
                caracteres_iguales += 1

        puntaje = caracteres_iguales / len(texto_consulta)

        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            nodo_mas_cercano = nodo

    return nodo_mas_cercano


def corregir_doctor_strange():
    nodo_encontrado = buscar_por_proximidad("Dr Strange")

    if nodo_encontrado is not None:
        print(
            f"Nombre encontrado por proximidad: "
            f"{nodo_encontrado.nombre}"
        )

        nodo_encontrado.nombre = "Doctor Strange"

        print(
            "El nombre fue corregido a: "
            f"{nodo_encontrado.nombre}"
        )
    else:
        print("No se encontró el personaje.")



def listar_heroes_descendente():
    print("Superhéroes ordenados de forma descendente:")

    for nodo in arbol_mcu.inorden_descendente(arbol_mcu.raiz):
        if nodo.es_heroe:
            print(f"- {nodo.nombre}")


def generar_bosque():
    arbol_heroes = AVL()
    arbol_villanos = AVL()

    for nodo in arbol_mcu.inorden(arbol_mcu.raiz):
        if nodo.es_heroe:
            arbol_heroes.insertar(
                nodo.nombre,
                nodo.es_heroe
            )
        else:
            arbol_villanos.insertar(
                nodo.nombre,
                nodo.es_heroe
            )

    return arbol_heroes, arbol_villanos


def mostrar_bosque():
    arbol_heroes, arbol_villanos = generar_bosque()

    print("Árbol de superhéroes:")
    print(
        "Cantidad de nodos:",
        arbol_heroes.contar_nodos(arbol_heroes.raiz)
    )

    print("Barrido ordenado:")
    for nodo in arbol_heroes.inorden(arbol_heroes.raiz):
        print(f"- {nodo.nombre}")

    print("\nÁrbol de villanos:")
    print(
        "Cantidad de nodos:",
        arbol_villanos.contar_nodos(arbol_villanos.raiz)
    )

    print("Barrido ordenado:")
    for nodo in arbol_villanos.inorden(arbol_villanos.raiz):
        print(f"- {nodo.nombre}")



print("A.")
mostrar_datos_arbol()


print("\nB.")
listar_villanos()


print("\nC.")
heroes_que_empiezan_con_c()


print("\nD.")
contar_superheroes()


print("\nE.")
corregir_doctor_strange()


print("\nF.")
listar_heroes_descendente()


print("\nG.")
mostrar_bosque()
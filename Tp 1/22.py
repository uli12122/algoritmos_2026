def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        print("La mochila está vacía. No se encontró el sable.")
        return False, 0

    print(f"Obi-Wan Kenobi sacó: {mochila[indice]}")

    if mochila[indice] == "sable de luz":
        print("¡El Jedi encontró su sable de luz!")
        return True, 1

    encontrado, cantidad = usar_la_fuerza(mochila, indice + 1)

    return encontrado, cantidad + 1

mochila = ["comida", "mapa", "capa", "sable de luz", "herramientas"]

encontrado, objetos = usar_la_fuerza(mochila)

print("Objetos sacados:", objetos)
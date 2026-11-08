from dataclasses import dataclass
import heapq


@dataclass(frozen=True)
class Arista:
    origen: str
    destino: str
    metros: int


class GrafoCasa:
    def __init__(self):
        self.ambientes = set()
        self.adyacencias = {}

    def agregar_ambiente(self, ambiente):
        self.ambientes.add(ambiente)
        self.adyacencias.setdefault(ambiente, {})

    def agregar_arista(self, origen, destino, metros):
        if metros <= 0:
            raise ValueError("La distancia debe ser mayor que cero.")
        self.agregar_ambiente(origen)
        self.agregar_ambiente(destino)
        self.adyacencias[origen][destino] = metros
        self.adyacencias[destino][origen] = metros

    def obtener_aristas(self):
        aristas = []
        visitadas = set()
        for origen, vecinos in self.adyacencias.items():
            for destino, metros in vecinos.items():
                identificador = frozenset((origen, destino))
                if identificador not in visitadas:
                    aristas.append(Arista(origen, destino, metros))
                    visitadas.add(identificador)
        return aristas

    def grados(self):
        return {
            ambiente: len(vecinos)
            for ambiente, vecinos in self.adyacencias.items()
        }

    def arbol_expansion_minima(self):
        aristas = sorted(
            self.obtener_aristas(),
            key=lambda arista: arista.metros,
        )
        padre = {ambiente: ambiente for ambiente in self.ambientes}

        def encontrar(ambiente):
            while padre[ambiente] != ambiente:
                padre[ambiente] = padre[padre[ambiente]]
                ambiente = padre[ambiente]
            return ambiente

        def unir(origen, destino):
            raiz_origen = encontrar(origen)
            raiz_destino = encontrar(destino)
            if raiz_origen == raiz_destino:
                return False
            padre[raiz_destino] = raiz_origen
            return True

        arbol = []
        metros_totales = 0
        for arista in aristas:
            if unir(arista.origen, arista.destino):
                arbol.append(arista)
                metros_totales += arista.metros

        if len(arbol) != len(self.ambientes) - 1:
            raise ValueError("El grafo no es conexo.")
        return arbol, metros_totales

    def camino_mas_corto(self, origen, destino):
        distancias = {
            ambiente: float("inf")
            for ambiente in self.ambientes
        }
        anteriores = {
            ambiente: None
            for ambiente in self.ambientes
        }
        distancias[origen] = 0
        pendientes = [(0, origen)]

        while pendientes:
            distancia_actual, actual = heapq.heappop(pendientes)
            if distancia_actual != distancias[actual]:
                continue
            if actual == destino:
                break

            for vecino, metros in self.adyacencias[actual].items():
                nueva_distancia = distancia_actual + metros
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = actual
                    heapq.heappush(
                        pendientes,
                        (nueva_distancia, vecino),
                    )

        if distancias[destino] == float("inf"):
            return [], float("inf")

        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]
        camino.reverse()
        return camino, distancias[destino]


def crear_casa():
    grafo = GrafoCasa()

    ambientes = (
        "cocina",
        "comedor",
        "cochera",
        "quincho",
        "baño 1",
        "baño 2",
        "habitación 1",
        "habitación 2",
        "sala de estar",
        "terraza",
        "patio",
    )
    for ambiente in ambientes:
        grafo.agregar_ambiente(ambiente)

    # Cocina y sala de estar tienen cinco conexiones.
    conexiones = [
        ("cocina", "comedor", 6),
        ("cocina", "baño 1", 8),
        ("cocina", "quincho", 10),
        ("cocina", "patio", 12),
        ("cocina", "sala de estar", 14),
        ("sala de estar", "comedor", 5),
        ("sala de estar", "habitación 1", 7),
        ("sala de estar", "habitación 2", 9),
        ("sala de estar", "terraza", 11),
        ("sala de estar", "patio", 13),
        ("comedor", "cochera", 15),
        ("comedor", "baño 2", 9),
        ("comedor", "habitación 1", 8),
        ("cochera", "patio", 7),
        ("cochera", "terraza", 16),
        ("quincho", "patio", 6),
        ("quincho", "terraza", 8),
        ("baño 1", "habitación 1", 5),
        ("baño 1", "baño 2", 4),
        ("baño 2", "habitación 2", 6),
        ("habitación 1", "habitación 2", 4),
        ("habitación 2", "terraza", 7),
        ("terraza", "patio", 10),
    ]
    for origen, destino, metros in conexiones:
        grafo.agregar_arista(origen, destino, metros)
    return grafo


def mostrar_arbol_minimo(grafo):
    arbol, metros = grafo.arbol_expansion_minima()
    print("\nÁrbol de expansión mínima:")
    for arista in arbol:
        print(
            f"{arista.origen} -- {arista.destino}: "
            f"{arista.metros} m"
        )
    print(f"Metros de cable necesarios: {metros} m")


def main():
    grafo = crear_casa()

    print("\nCantidad de conexiones por ambiente:")
    for ambiente, cantidad in sorted(grafo.grados().items()):
        print(f"- {ambiente}: {cantidad}")

    mostrar_arbol_minimo(grafo)

    camino, metros = grafo.camino_mas_corto(
        "habitación 1",
        "sala de estar",
    )
    print("\nCamino más corto desde habitación 1 hasta sala de estar:")
    print(" -> ".join(camino))
    print(f"Metros de cable de red necesarios: {metros} m")


if __name__ == "__main__":
    main()

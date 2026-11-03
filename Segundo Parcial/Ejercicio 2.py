from dataclasses import dataclass
import heapq


EPISODIOS = set(range(1, 10))


APARICIONES = {
    "Luke Skywalker": {4, 5, 6, 7, 8, 9},
    "Darth Vader": {3, 4, 5, 6},
    "Yoda": {1, 2, 3, 5, 6, 8},
    "Boba Fett": {2, 3, 4, 5, 6, 9},
    "C-3PO": EPISODIOS.copy(),
    "Leia": {3, 4, 5, 6, 7, 8, 9},
    "Rey": {7, 8, 9},
    "Kylo Ren": {7, 8, 9},
    "Chewbacca": {3, 4, 5, 6, 7, 8, 9},
    "Han Solo": {4, 5, 6, 7, 9},
    "R2-D2": EPISODIOS.copy(),
    "BB-8": {7, 8, 9},
}


@dataclass(frozen=True)
class Arista:
    origen: str
    destino: str
    peso: int


class Grafo:
    def __init__(self):
        self.adyacencias = {nombre: {} for nombre in APARICIONES}
        self.aristas = []

    def agregar_arista(self, origen, destino, peso):
        self.adyacencias[origen][destino] = peso
        self.adyacencias[destino][origen] = peso
        self.aristas.append(Arista(origen, destino, peso))

    def construir_desde_apariciones(self):
        nombres = list(APARICIONES)
        for posicion, origen in enumerate(nombres):
            for destino in nombres[posicion + 1:]:
                episodios_compartidos = (
                    APARICIONES[origen] & APARICIONES[destino]
                )
                if episodios_compartidos:
                    self.agregar_arista(
                        origen,
                        destino,
                        len(episodios_compartidos),
                    )

    def prim(self, inicio):
        visitados = {inicio}
        candidatos = [
            (peso, inicio, destino)
            for destino, peso in self.adyacencias[inicio].items()
        ]
        heapq.heapify(candidatos)
        resultado = []
        costo_total = 0

        while candidatos and len(visitados) < len(self.adyacencias):
            peso, origen, destino = heapq.heappop(candidatos)
            if destino in visitados:
                continue
            visitados.add(destino)
            resultado.append(Arista(origen, destino, peso))
            costo_total += peso

            for vecino, peso_vecino in self.adyacencias[destino].items():
                if vecino not in visitados:
                    heapq.heappush(
                        candidatos,
                        (peso_vecino, destino, vecino),
                    )

        if len(visitados) != len(self.adyacencias):
            raise ValueError("El grafo no es conexo.")
        return resultado, costo_total

    def dijkstra(self, inicio, fin):
        distancias = {nombre: float("inf") for nombre in self.adyacencias}
        anteriores = {nombre: None for nombre in self.adyacencias}
        distancias[inicio] = 0
        pendientes = [(0, inicio)]

        while pendientes:
            distancia_actual, actual = heapq.heappop(pendientes)
            if distancia_actual != distancias[actual]:
                continue
            if actual == fin:
                break

            for vecino, peso in self.adyacencias[actual].items():
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = actual
                    heapq.heappush(
                        pendientes,
                        (nueva_distancia, vecino),
                    )

        if distancias[fin] == float("inf"):
            return [], float("inf")

        camino = []
        actual = fin
        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]
        camino.reverse()
        return camino, distancias[fin]

    def maximo_compartido(self):
        maximo = max(arista.peso for arista in self.aristas)
        pares = [
            (arista.origen, arista.destino)
            for arista in self.aristas
            if arista.peso == maximo
        ]
        return maximo, pares

    def personajes_en_nueve_episodios(self):
        return [
            nombre for nombre, episodios in APARICIONES.items()
            if episodios == EPISODIOS
        ]


def mostrar_arbol(aristas, costo):
    for arista in aristas:
        print(
            f"{arista.origen} -- {arista.destino} "
            f"(episodios compartidos: {arista.peso})"
        )
    print(f"Costo total: {costo}")


def mostrar_camino(grafo, origen, destino):
    camino, costo = grafo.dijkstra(origen, destino)
    print(" -> ".join(camino))
    print(f"Costo total: {costo}")

def main():
    grafo = Grafo()
    grafo.construir_desde_apariciones()

    print("\nÁrbol de expansión mínimo desde C-3PO:")
    arbol, costo = grafo.prim("C-3PO")
    mostrar_arbol(arbol, costo)

    print("\nÁrbol de expansión mínimo desde Yoda:")
    arbol, costo = grafo.prim("Yoda")
    mostrar_arbol(arbol, costo)

    print("\nÁrbol de expansión mínimo desde Leia:")
    arbol, costo = grafo.prim("Leia")
    mostrar_arbol(arbol, costo)

    maximo, pares = grafo.maximo_compartido()
    print("\nMáximo número de episodios compartidos:")
    print(f"Cantidad máxima: {maximo}")
    for origen, destino in pares:
        print(f"{origen} -- {destino}")

    print("\nCamino más corto de C-3PO a R2-D2:")
    mostrar_camino(grafo, "C-3PO", "R2-D2")

    print("\nCamino más corto de Yoda a Darth Vader:")
    mostrar_camino(grafo, "Yoda", "Darth Vader")

    print("\nPersonajes que aparecen en los nueve episodios:")
    print(", ".join(grafo.personajes_en_nueve_episodios()))

if __name__ == "__main__":
    main()

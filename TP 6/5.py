from dataclasses import dataclass
import heapq


NUEVO_PESO_IMPRESORA = 22


@dataclass(frozen=True)
class Nodo:
    nombre: str
    tipo: str


@dataclass(frozen=True)
class Arista:
    origen: str
    destino: str
    peso: int


class GrafoRed:
    def __init__(self):
        self.nodos = {}
        self.adyacencias = {}

    def agregar_nodo(self, nombre, tipo):
        self.nodos[nombre] = Nodo(nombre, tipo)
        self.adyacencias.setdefault(nombre, {})

    def agregar_arista(self, origen, destino, peso):
        self.adyacencias[origen][destino] = peso
        self.adyacencias[destino][origen] = peso

    def aristas(self):
        resultado = []
        visitadas = set()
        for origen, vecinos in self.adyacencias.items():
            for destino, peso in vecinos.items():
                identificador = frozenset((origen, destino))
                if identificador not in visitadas:
                    resultado.append(Arista(origen, destino, peso))
                    visitadas.add(identificador)
        return resultado

    def recorrido_profundidad(self, inicio):
        visitados = set()
        resultado = []

        def dfs(actual):
            visitados.add(actual)
            resultado.append(actual)
            for vecino in sorted(self.adyacencias[actual]):
                if vecino not in visitados:
                    dfs(vecino)

        dfs(inicio)
        return resultado

    def recorrido_amplitud(self, inicio):
        visitados = {inicio}
        resultado = []
        cola = [inicio]

        while cola:
            actual = cola.pop(0)
            resultado.append(actual)
            for vecino in sorted(self.adyacencias[actual]):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return resultado

    def dijkstra(self, inicio, fin):
        distancias = {
            nombre: float("inf") for nombre in self.nodos
        }
        anteriores = {nombre: None for nombre in self.nodos}
        distancias[inicio] = 0
        pendientes = [(0, inicio)]

        while pendientes:
            distancia, actual = heapq.heappop(pendientes)
            if distancia != distancias[actual]:
                continue
            if actual == fin:
                break

            for vecino, peso in self.adyacencias[actual].items():
                nueva_distancia = distancia + peso
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

    def arbol_expansion_minima(self):
        aristas = sorted(self.aristas(), key=lambda arista: arista.peso)
        padre = {nombre: nombre for nombre in self.nodos}

        def encontrar(nombre):
            while padre[nombre] != nombre:
                padre[nombre] = padre[padre[nombre]]
                nombre = padre[nombre]
            return nombre

        def unir(origen, destino):
            raiz_origen = encontrar(origen)
            raiz_destino = encontrar(destino)
            if raiz_origen == raiz_destino:
                return False
            padre[raiz_destino] = raiz_origen
            return True

        resultado = []
        costo = 0
        for arista in aristas:
            if unir(arista.origen, arista.destino):
                resultado.append(arista)
                costo += arista.peso

        if len(resultado) != len(self.nodos) - 1:
            raise ValueError("La red no es conexa.")
        return resultado, costo

    def equipos_conectados(self, nombre):
        return [
            vecino for vecino in self.adyacencias[nombre]
            if self.nodos[vecino].tipo in {"pc", "notebook"}
        ]

    def cambiar_impresora_a_router02(self):
        self.adyacencias["Switch 1"].pop("Impresora", None)
        self.adyacencias["Impresora"].pop("Switch 1", None)
        self.agregar_arista(
            "Router 2",
            "Impresora",
            NUEVO_PESO_IMPRESORA,
        )


def crear_red():
    grafo = GrafoRed()

    nodos = {
        "Manjaro": "pc",
        "Ubuntu": "pc",
        "Mint": "pc",
        "Fedora": "pc",
        "Parrot": "pc",
        "Red Hat": "notebook",
        "Debian": "notebook",
        "Arch": "notebook",
        "Guarani": "servidor",
        "MongoDB": "servidor",
        "Router 1": "router",
        "Router 2": "router",
        "Router 3": "router",
        "Switch 1": "switch",
        "Switch 2": "switch",
        "Impresora": "impresora",
    }

    for nombre, tipo in nodos.items():
        grafo.agregar_nodo(nombre, tipo)

    conexiones = [
        ("Red Hat", "Router 2", 25),
        ("Guarani", "Router 2", 9),
        ("Router 2", "Router 3", 50),
        ("Router 2", "Router 1", 37),
        ("Debian", "Switch 1", 17),
        ("Ubuntu", "Switch 1", 18),
        ("Switch 1", "Router 1", 29),
        ("Switch 1", "Impresora", 22),
        ("Switch 1", "Mint", 80),
        ("Router 1", "Router 3", 43),
        ("Router 3", "Switch 2", 61),
        ("Manjaro", "Switch 2", 40),
        ("Parrot", "Switch 2", 12),
        ("MongoDB", "Switch 2", 5),
        ("Fedora", "Switch 2", 3),
        ("Arch", "Switch 2", 56),
    ]

    for origen, destino, peso in conexiones:
        grafo.agregar_arista(origen, destino, peso)
    return grafo


def mostrar_recorridos(grafo, titulo):
    print(f"\n{titulo}")
    for inicio in ("Red Hat", "Debian", "Arch"):
        dfs = grafo.recorrido_profundidad(inicio)
        bfs = grafo.recorrido_amplitud(inicio)
        print(f"\nDesde {inicio}:")
        print("  Profundidad:", " -> ".join(dfs))
        print("  Amplitud:   ", " -> ".join(bfs))


def mostrar_camino(grafo, origen, destino):
    camino, costo = grafo.dijkstra(origen, destino)
    print(
        f"{origen} -> {destino}: "
        f"{' -> '.join(camino)} | costo: {costo}"
    )


def mostrar_arbol_minimo(grafo):
    aristas, costo = grafo.arbol_expansion_minima()
    for arista in aristas:
        print(
            f"{arista.origen} -- {arista.destino} "
            f"(peso {arista.peso})"
        )
    print(f"Costo total: {costo}")


def resolver_punto_f(grafo):
    pcs = [
        nombre for nombre, nodo in grafo.nodos.items()
        if nodo.tipo == "pc"
    ]
    caminos_guarani = [
        (grafo.dijkstra(pc, "Guarani"), pc)
        for pc in pcs
    ]
    camino_guarani, pc_guarani = min(
        caminos_guarani,
        key=lambda elemento: elemento[0][1],
    )

    equipos_switch_1 = grafo.equipos_conectados("Switch 1")
    caminos_mongodb = [
        (grafo.dijkstra(equipo, "MongoDB"), equipo)
        for equipo in equipos_switch_1
    ]
    camino_mongodb, equipo_mongodb = min(
        caminos_mongodb,
        key=lambda elemento: elemento[0][1],
    )

    print("\nDesde qué PC se llega más rápido a Guarani:")
    print(f"PC elegida: {pc_guarani}")
    print(
        f"Camino: {' -> '.join(camino_guarani[0])} | "
        f"costo: {camino_guarani[1]}"
    )

    print("\nDesde qué computadora del Switch 1 se llega más rápido a MongoDB:")
    print(f"Computadora elegida: {equipo_mongodb}")
    print(
        f"Camino: {' -> '.join(camino_mongodb[0])} | "
        f"costo: {camino_mongodb[1]}"
    )


def main():
    grafo = crear_red()

    print("\nTipos de nodos:")
    for nodo in grafo.nodos.values():
        print(f"- {nodo.nombre}: {nodo.tipo}")

    mostrar_recorridos(grafo, "Barridos originales")

    print("\nCaminos más cortos hasta la impresora:")
    for origen in ("Manjaro", "Red Hat", "Fedora"):
        mostrar_camino(grafo, origen, "Impresora")

    print("\nÁrbol de expansión mínima:")
    mostrar_arbol_minimo(grafo)

    resolver_punto_f(grafo)

    grafo.cambiar_impresora_a_router02()
    mostrar_recorridos(grafo, "Barridos después de conectar la impresora al Router 2")


if __name__ == "__main__":
    main()

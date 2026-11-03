from collections import Counter, deque
from dataclasses import dataclass
import unicodedata

from pokemon_100 import POKEMONS


def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")

@dataclass
class Pokemon:
    numero: int
    nombre: str
    tipos: tuple
    debilidades: tuple
    mega: bool
    gigamax: bool


class Nodo:
    def __init__(self, clave, pokemon):
        self.clave = clave
        self.pokemons = [pokemon]
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, pokemon):
        if self.raiz is None:
            self.raiz = Nodo(clave, pokemon)
            return

        actual = self.raiz
        while True:
            if clave == actual.clave:
                actual.pokemons.append(pokemon)
                return
            if clave < actual.clave:
                if actual.izquierda is None:
                    actual.izquierda = Nodo(clave, pokemon)
                    return
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = Nodo(clave, pokemon)
                    return
                actual = actual.derecha

    def buscar(self, clave):
        actual = self.raiz
        while actual is not None:
            if clave == actual.clave:
                return actual.pokemons
            actual = actual.izquierda if clave < actual.clave else actual.derecha
        return []

    def inorden(self):
        resultado = []
        pila = []
        actual = self.raiz
        while pila or actual is not None:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierda
            actual = pila.pop()
            resultado.extend(actual.pokemons)
            actual = actual.derecha
        return resultado

    def por_niveles(self):
        if self.raiz is None:
            return []
        resultado = []
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            resultado.extend(actual.pokemons)
            if actual.izquierda is not None:
                cola.append(actual.izquierda)
            if actual.derecha is not None:
                cola.append(actual.derecha)
        return resultado


def crear_pokemon(registro):
    return Pokemon(
        numero=registro["numero"],
        nombre=registro["nombre"],
        tipos=tuple(registro["tipos"]),
        debilidades=tuple(registro["debilidades"]),
        mega=registro["mega"],
        gigamax=registro["gigamax"],
    )


pokemons = [crear_pokemon(registro) for registro in POKEMONS]
arbol_nombre = Arbol()
arbol_numero = Arbol()
arbol_tipo = Arbol()

for pokemon in pokemons:
    arbol_nombre.insertar(normalizar(pokemon.nombre), pokemon)
    arbol_numero.insertar(pokemon.numero, pokemon)
    for tipo in pokemon.tipos:
        arbol_tipo.insertar(normalizar(tipo), pokemon)


def mostrar(pokemons_encontrados):
    for pokemon in pokemons_encontrados:
        print(
            f"#{pokemon.numero:03d} {pokemon.nombre} | "
            f"tipos: {', '.join(pokemon.tipos)} | "
            f"debilidades: {', '.join(pokemon.debilidades)} | "
            f"mega={pokemon.mega} | gigamax={pokemon.gigamax}"
        )


print("\nDatos por número:")
mostrar(arbol_numero.buscar(25))

print("\nDatos por nombre con búsqueda por proximidad ('bul'):")
mostrar([
    pokemon for pokemon in arbol_nombre.inorden()
    if normalizar("bul") in normalizar(pokemon.nombre)
])

print("\nNombres por tipo:")
for tipo in ("ghost", "fire", "steel", "electric"):
    nombres = sorted(
        {pokemon.nombre for pokemon in arbol_tipo.buscar(tipo)},
        key=normalizar,
    )
    print(f"{tipo}: {', '.join(nombres)}")

print("\nListado ascendente por número:")
print(", ".join(pokemon.nombre for pokemon in arbol_numero.inorden()))

print("\nListado ascendente por nombre:")
print(", ".join(pokemon.nombre for pokemon in arbol_nombre.inorden()))

print("\nListado por niveles del árbol de nombres:")
print(", ".join(pokemon.nombre for pokemon in arbol_nombre.por_niveles()))

print("\nPokémon débiles frente a Jolteon, Lycanroc y Tyrantrum:")
for nombre_rival in ("Jolteon", "Lycanroc", "Tyrantrum"):
    rivales = [
        pokemon for pokemon in pokemons
        if normalizar(nombre_rival) in normalizar(pokemon.nombre)
    ]
    tipos_rival = {
        tipo for rival in rivales for tipo in rival.tipos
    }
    debiles = [
        pokemon for pokemon in arbol_numero.inorden()
        if tipos_rival.intersection(pokemon.debilidades)
    ]
    print(f"{nombre_rival}: {', '.join(pokemon.nombre for pokemon in debiles)}")

print("\nTipos y cantidad de Pokémon:")
cantidades = Counter(
    tipo for pokemon in pokemons for tipo in pokemon.tipos
)
for tipo, cantidad in sorted(cantidades.items()):
    print(f"{tipo}: {cantidad}")

print(f"\nPokémon con megaevolución: {sum(pokemon.mega for pokemon in pokemons)}")
print(f"Pokémon con forma gigamax: {sum(pokemon.gigamax for pokemon in pokemons)}")

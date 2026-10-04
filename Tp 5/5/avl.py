class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class AVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if nodo is None:
            return 0

        return nodo.altura

    def obtener_balance(self, nodo):
        if nodo is None:
            return 0

        return (
            self.obtener_altura(nodo.izquierda)
            - self.obtener_altura(nodo.derecha)
        )

    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierda),
            self.obtener_altura(nodo.derecha)
        )

    def rotacion_derecha(self, nodo):
        nueva_raiz = nodo.izquierda
        subarbol = nueva_raiz.derecha

        nueva_raiz.derecha = nodo
        nodo.izquierda = subarbol

        self.actualizar_altura(nodo)
        self.actualizar_altura(nueva_raiz)

        return nueva_raiz

    def rotacion_izquierda(self, nodo):
        nueva_raiz = nodo.derecha
        subarbol = nueva_raiz.izquierda

        nueva_raiz.izquierda = nodo
        nodo.derecha = subarbol

        self.actualizar_altura(nodo)
        self.actualizar_altura(nueva_raiz)

        return nueva_raiz

    def insertar_nodo(self, nodo, nombre, es_heroe):
        if nodo is None:
            return Nodo(nombre, es_heroe)

        if nombre.lower() < nodo.nombre.lower():
            nodo.izquierda = self.insertar_nodo(
                nodo.izquierda,
                nombre,
                es_heroe
            )
        elif nombre.lower() > nodo.nombre.lower():
            nodo.derecha = self.insertar_nodo(
                nodo.derecha,
                nombre,
                es_heroe
            )
        else:
            return nodo

        self.actualizar_altura(nodo)

        balance = self.obtener_balance(nodo)

        # Caso izquierda-izquierda
        if balance > 1 and nombre.lower() < nodo.izquierda.nombre.lower():
            return self.rotacion_derecha(nodo)

        # Caso derecha-derecha
        if balance < -1 and nombre.lower() > nodo.derecha.nombre.lower():
            return self.rotacion_izquierda(nodo)

        # Caso izquierda-derecha
        if balance > 1 and nombre.lower() > nodo.izquierda.nombre.lower():
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        # Caso derecha-izquierda
        if balance < -1 and nombre.lower() < nodo.derecha.nombre.lower():
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    def insertar(self, nombre, es_heroe):
        self.raiz = self.insertar_nodo(
            self.raiz,
            nombre,
            es_heroe
        )

    def inorden(self, nodo):
        if nodo is not None:
            yield from self.inorden(nodo.izquierda)
            yield nodo
            yield from self.inorden(nodo.derecha)

    def inorden_descendente(self, nodo):
        if nodo is not None:
            yield from self.inorden_descendente(nodo.derecha)
            yield nodo
            yield from self.inorden_descendente(nodo.izquierda)

    def contar_nodos(self, nodo):
        if nodo is None:
            return 0

        return (
            1
            + self.contar_nodos(nodo.izquierda)
            + self.contar_nodos(nodo.derecha)
        )
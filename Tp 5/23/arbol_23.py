class Nodo:
    def __init__(
        self,
        nombre,
        derrotado_por=None,
        descripcion=""
    ):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = descripcion
        self.capturada = None

        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(
        self,
        nombre,
        derrotado_por=None,
        descripcion=""
    ):
        nuevo = Nodo(
            nombre,
            derrotado_por,
            descripcion
        )

        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar(self.raiz, nuevo)

    def _insertar(self, actual, nuevo):
        if nuevo.nombre.lower() < actual.nombre.lower():
            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self._insertar(actual.izquierda, nuevo)

        elif nuevo.nombre.lower() > actual.nombre.lower():
            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self._insertar(actual.derecha, nuevo)

    def buscar(self, nombre):
        return self._buscar(self.raiz, nombre)

    def _buscar(self, actual, nombre):
        if actual is None:
            return None

        if actual.nombre.lower() == nombre.lower():
            return actual

        if nombre.lower() < actual.nombre.lower():
            return self._buscar(actual.izquierda, nombre)

        return self._buscar(actual.derecha, nombre)

    def buscar_por_coincidencia(self, texto):
        coincidencias = []
        self._buscar_coincidencias(
            self.raiz,
            texto.lower(),
            coincidencias
        )
        return coincidencias

    def _buscar_coincidencias(
        self,
        actual,
        texto,
        coincidencias
    ):
        if actual is not None:
            self._buscar_coincidencias(
                actual.izquierda,
                texto,
                coincidencias
            )

            if texto in actual.nombre.lower():
                coincidencias.append(actual)

            self._buscar_coincidencias(
                actual.derecha,
                texto,
                coincidencias
            )

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, actual, resultado):
        if actual is not None:
            self._inorden(actual.izquierda, resultado)
            resultado.append(actual)
            self._inorden(actual.derecha, resultado)

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, actual, resultado):
        if actual is not None:
            resultado.append(actual)
            self._preorden(actual.izquierda, resultado)
            self._preorden(actual.derecha, resultado)

    def por_nivel(self):
        if self.raiz is None:
            return []

        resultado = []
        cola = [self.raiz]

        while len(cola) > 0:
            nodo_actual = cola.pop(0)
            resultado.append(nodo_actual)

            if nodo_actual.izquierda is not None:
                cola.append(nodo_actual.izquierda)

            if nodo_actual.derecha is not None:
                cola.append(nodo_actual.derecha)

        return resultado

    def eliminar(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre)

    def _eliminar(self, actual, nombre):
        if actual is None:
            return None

        if nombre.lower() < actual.nombre.lower():
            actual.izquierda = self._eliminar(
                actual.izquierda,
                nombre
            )

        elif nombre.lower() > actual.nombre.lower():
            actual.derecha = self._eliminar(
                actual.derecha,
                nombre
            )

        else:
            if actual.izquierda is None:
                return actual.derecha

            if actual.derecha is None:
                return actual.izquierda

            sucesor = self._minimo(actual.derecha)

            actual.nombre = sucesor.nombre
            actual.derrotado_por = sucesor.derrotado_por
            actual.descripcion = sucesor.descripcion
            actual.capturada = sucesor.capturada

            actual.derecha = self._eliminar(
                actual.derecha,
                sucesor.nombre
            )

        return actual

    def _minimo(self, nodo):
        actual = nodo

        while actual.izquierda is not None:
            actual = actual.izquierda

        return actual

    def cantidad(self):
        return self._cantidad(self.raiz)

    def _cantidad(self, actual):
        if actual is None:
            return 0

        return (
            1
            + self._cantidad(actual.izquierda)
            + self._cantidad(actual.derecha)
        )
from nodo_avl import NodoAVL

class AgendaTelefonicaAVL:
    def obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        return self.obtener_altura(nodo.izq) - self.obtener_altura(nodo.der) if nodo else 0

    def rotacion_derecha(self, z):
        y = z.izq
        temp = y.der
        y.der = z
        z.izq = temp

        # Actualizar alturas
        z.altura = 1 + max(self.obtener_altura(z.izq), self.obtener_altura(z.der))
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))

        print(f"Rotación Derecha en {z.nombre}")
        return y

    def rotacion_izquierda(self, z):
        y = z.der
        temp = y.izq
        y.izq = z
        z.der = temp

        z.altura = 1 + max(self.obtener_altura(z.izq), self.obtener_altura(z.der))
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))

        print(f"Rotación Izquierda en {z.nombre}")
        return y

    def insertar(self, nodo, nombre, telefono, correo):
        if not nodo:
            print(f"Insertando {nombre}")
            return NodoAVL(nombre, telefono, correo)

        if nombre < nodo.nombre:
            nodo.izq = self.insertar(nodo.izq, nombre, telefono, correo)
        elif nombre > nodo.nombre:
            nodo.der = self.insertar(nodo.der, nombre, telefono, correo)
        else:
            return nodo

        nodo.altura = 1 + max(self.obtener_altura(nodo.izq), self.obtener_altura(nodo.der))
        balance = self.balance(nodo)

        # para la rotaciones
        if balance > 1 and nombre < nodo.izq.nombre:
            return self.rotacion_derecha(nodo)
        if balance < -1 and nombre > nodo.der.nombre:
            return self.rotacion_izquierda(nodo)
        if balance > 1 and nombre > nodo.izq.nombre:
            nodo.izq = self.rotacion_izquierda(nodo.izq)
            return self.rotacion_derecha(nodo)
        if balance < -1 and nombre < nodo.der.nombre:
            nodo.der = self.rotacion_derecha(nodo.der)
            return self.rotacion_izquierda(nodo)

        return nodo

    def buscar(self, nodo, nombre):
        if nodo is None:
            return None
        if nombre == nodo.nombre:
            return nodo
        elif nombre < nodo.nombre:
            return self.buscar(nodo.izq, nombre)
        else:
            return self.buscar(nodo.der, nombre)

    def mostrar_inorden(self, nodo):
        if nodo:
            self.mostrar_inorden(nodo.izq)
            print(f"Nombre: {nodo.nombre}, Teléfono: {nodo.telefono}, Correo: {nodo.correo}")
            self.mostrar_inorden(nodo.der)

class NodoAVL:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.izq = None
        self.der = None
        self.altura = 1

class Estudiante:
    def _init_(self, seccion):
        self.seccion = seccion

    def get_seccion(self):
        return self.seccion

    def set_seccion(self, seccion):
        self.seccion = seccion

# Ejemplo de uso
# Crear un objeto Estudiante
estudiante = Estudiante("A")

# Obtener el valor de seccion
print(estudiante.get_seccion())

# Establecer un nuevo valor de seccion
estudiante.set_seccion("B")

# Obtener el nuevo valor de seccion
print(estudiante.get_seccion())
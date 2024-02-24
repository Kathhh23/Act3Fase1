class Cliente:
    def __init__(self, nombre, nit):
        self.nombre = nombre
        self.nit = nit

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nit(self):
        return self.nit

    def set_nit(self, nit):
        self.nit = nit

# Ejemplo de uso
cliente1 = Cliente("Juan Perez", "1234-5678-901-2")
print("Nombre del cliente:", cliente1.get_nombre())
print("NIT del cliente:", cliente1.get_nit())

# Modificamos los datos del cliente
cliente1.set_nombre("Maria Lopez")
cliente1.set_nit("9876-5432-109-8")
print("\nDespués de la modificación:")
print("Nombre del cliente:", cliente1.get_nombre())
print("NIT del cliente:", cliente1.get_nit())



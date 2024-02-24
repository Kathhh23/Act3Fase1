class Persona():
    def _init_(self):
        self.nombre = None
        self.apellido = None
        self.direccion = None
        self.telefono = None
        self.fecha_nacimiento = None

    def crear_persona(self, nombre, apellido, direccion, telefono, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento

    def leer_persona(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Direccion: ", self.direccion)
        print("Telefono: ", self.telefono)
        print("Fecha de Nacimiento: ", self.fecha_nacimiento)

    def actualizar_persona(self, nombre, apellido, direccion, telefono, fecha_nacimiento):

        if nombre != "":
            self.nombre = nombre
        if apellido != "":
            self.apellido = apellido
        if direccion != "":
            self.direccion = direccion
        if telefono != "":
            self.telefono = telefono
        if fecha_nacimiento != "":
            self.fecha_nacimiento = fecha_nacimiento

    def borra_persona(self):
        self.nombre = None
        self.apellido = None
        self.direccion = None
        self.telefono = None
        self.fecha_nacimiento = None
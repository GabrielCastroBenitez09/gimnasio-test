class Persona:
    def __init__(self, nombre, id, email):
        self.nombre = nombre
        self.id = id
        self.email = email
    def __str__(self):
        return f"{self.nombre} (ID {self.id})"
    
class Socio(Persona):
    def __init__(self, nombre, id, email, membresia):
        super().__init__(nombre, id, email)
        self.memebresia = membresia
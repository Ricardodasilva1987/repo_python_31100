class Persona:
    def __init__(self, nombre, apellido,dni): 
        self.nombre =nombre
        self.apellido =apellido
        self.dni=dni
    def hablar(self):
        print(f"Hola soy {self.nombre}")
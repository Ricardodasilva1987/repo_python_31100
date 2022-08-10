class Persona:
    def __init__(self, nombre, apellido): 
        self.nombre =nombre
        self.apellido =apellido
    def hablar(self):
        print(f"Hola soy {self.nombre}")
class Student:
    def __init__(self, nombre, edad , carnet):
        self.nombre = nombre
        self.edad = edad
        self.carnet = carnet

    def __str__(self):
        return f"ESTUDIANTE:{self.nombre} | EDAD:{self.edad} | CARNET: {self.carnet}."

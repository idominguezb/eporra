from src.modelo.declarative_base import engine, Base, session

class Carrera():
    def __init__(self):
        Base.metadata.create_all(engine)

    def crear_carrera(self, nombre, competidores):
        if len(nombre) == 0 and len(competidores) == 0:
            return False

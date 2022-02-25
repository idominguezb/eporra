from src.modelo.declarative_base import engine, Base, session

class Carrera():
    def __init__(self):
        Base.metadata.create_all(engine)

    def crear_carrera(self, nombre, competidores):
        nombre = nombre.strip()
        if len(nombre) == 0 or len(competidores) == 0:
            return False

from src.modelo.declarative_base import engine, Base, session

class Carrera():
    def __init__(self):
        Base.metadata.create_all(engine)

    def crear_carrera(self, nombre, competidores):
        return None



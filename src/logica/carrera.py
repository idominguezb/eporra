from src.modelo.declarative_base import engine, Base, session

class Carrera():
    def __init__(self):
        Base.metadata.create_all(engine)

    def crear_carrera(self, nombre, competidores):
        nombre = nombre.strip()
        if len(nombre) == 0 or len(competidores) == 0:
            return False
        isvalid = True
        for competidor in competidores:
            if len(competidor['nombre']) == 0 or 'probabilidad' in competidor:
                isvalid = False

        return isvalid

    def crear_competidor(self, nombre, probabilidad):
        nombre = nombre.strip()
        if len(nombre) or probabilidad == 0:
            return False
        return True

from .carrera import Carrera
from .apostador import Apostador
from .competidor import Competidor
from .apuesta import Apuesta
from .declarative_base import Session, engine, Base

def setupBD():
    # Borra y crea la BD
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from .apostador import Apostador
from .declarative_base import Base

class Apuesta(Base):
    __tablename__ = 'apuestas'

    id            = Column(Integer, primary_key=True)
    Valor         = Column(Float)
    Carrera_id    = Column(Integer, ForeignKey('carreras.id'))
    Apostador_id  = Column(Integer, ForeignKey('apostadores.id'))
    Competidor_id = Column(Integer, ForeignKey('competidores.id'))
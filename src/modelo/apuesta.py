from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Apuesta(Base):
    __tablename__ = 'apuestas'

    id            = Column(Integer, primary_key=True)
    valor         = Column(Float)
    carrera_id    = Column(Integer, ForeignKey('carreras.id'))
    apostador_id  = Column(Integer, ForeignKey('apostadores.id'))
    competidor_id = Column(Integer, ForeignKey('competidores.id'))
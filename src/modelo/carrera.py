import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Estado(enum.Enum):
    ABIERTA  = 1
    CERRADA  = 2
    INICIADA = 3

class Carrera(Base):
    __tablename__ = 'carreras'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    estado = Column(Enum(Estado))
    competidores = relationship('Competidor', cascade='all, delete, delete-orphan')
    apuestas = relationship('Apuesta', cascade='all, delete, delete-orphan')

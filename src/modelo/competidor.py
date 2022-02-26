from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Competidor(Base):
    __tablename__ = 'competidores'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Probabilidad = Column(Float)
    Carrera_id = Column(Integer, ForeignKey('carreras.id'))

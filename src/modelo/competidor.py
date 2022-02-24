from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Competidor(Base):
    __tablename__ = 'competidores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    probabilidad = Column(Float)
   
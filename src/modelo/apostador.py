from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Apostador(Base):
    __tablename__ = 'apostadores'

    id       = Column(Integer, primary_key=True)
    Nombre   = Column(String)
    Apuestas = relationship('Apuesta', cascade='all, delete, delete-orphan')

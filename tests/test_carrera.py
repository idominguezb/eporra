import unittest
import random
from src.modelo.carrera import Carrera
from src.modelo.declarative_base import Session
from src.logica.carrera import Carrera


class CarreraTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = Carrera()

    def test_crear_carrera_sin_nombre_sin_competidores(self):
        nueva_carrera = self.logica.crear_carrera('', [])
        self.assertEqual(nueva_carrera, False)




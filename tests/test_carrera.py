import unittest
import random
from src.modelo.carrera import Carrera
from src.modelo.declarative_base import Session
from src.logica.Logica_mock import Logica_mock


class CarreraTestCase(unittest.TestCase):
    def test_prueba(self):
        self.assertEquals(0, 0)

    def setUp(self) -> None:
        self.logica = Logica_mock()

    def test_crearCarrera(self):
        self.logica.crear_carrera('Carrera Formula 1')
        print(len(self.logica.carreras))

    def test_listarCarreras(self):
        res = self.logica.dar_carreras()
        self.assertEquals(len(res), 2)

    def tearDown(self) -> None:
        self.session = Session()


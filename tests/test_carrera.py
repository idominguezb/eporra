import unittest
import random
from src.modelo.declarative_base import Base, engine
from src.logica.Logica import Logica

class CarreraTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = Logica()
        Base.metadata.create_all(engine)

    def test_crear_carrera_con_nombre_en_blanco(self):
        nueva_carrera = self.logica.crear_carrera('')
        self.assertEqual(nueva_carrera, False)

    def test_crear_carrera(self):
        nueva_carrera = self.logica.crear_carrera('Carrera 1')
        self.assertEqual(nueva_carrera, True)

    def test_crear_carrera_con_nombre_existente(self):
        nueva_carrera = self.logica.crear_carrera('Carrera 1')
        self.assertEqual(nueva_carrera, False)

    def tearDown(self):
        Base.metadata.drop_all(engine)

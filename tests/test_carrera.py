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

    def test_crear_carrera_con_espacios_en_blanco_en_el_nombre_y_sin_competidores(self):
        nueva_carrera = self.logica.crear_carrera('           ', [])
        self.assertEqual(nueva_carrera, False)

    def test_crear_carrera_con_nombre_sin_competidores(self):
        nueva_carrera = self.logica.crear_carrera('Carrera Indianapolis', [])
        self.assertEqual(nueva_carrera, False)

    def test_crear_carrera_con_nombre_y_con_un_competidor_con_nombre_vacio_y_sin_probabilidad(self):
        competidores = [{ "nombre": "" }]
        nueva_carrera = self.logica.crear_carrera('Carrera Indianapolis', competidores)
        self.assertEqual(nueva_carrera, False)

    def test_crear_competidor_sin_nombre_con_probabilidad_cero(self):
        nuevo_competidor = self.logica.crear_competidor('', '')
        self.assertEqual(nuevo_competidor, False)



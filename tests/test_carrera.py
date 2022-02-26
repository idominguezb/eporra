import unittest
import random
from src.modelo.declarative_base import Base, engine
from src.logica.Logica import Logica

class CarreraTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
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

    def test_validar_suma_probabilidades_igual_uno(self):
        competidoresFail = [{
            "Nombre": "Michael Shummy",
            "Probilidad": "1"
        },
        {
            "Nombre": "Ronny Stand",
            "Probilidad": "0.8"
        }
        ]

        competidoresSuccess = [{
            "Nombre": "Michael Shummy",
            "Probilidad": "0.5"
        },
        {
            "Nombre": "Ronny Stand",
            "Probilidad": "0.5"
        }
        ]

        competidoresNoValidos = self.logica.validar_competidores(competidoresFail)
        competidoresValidos = self.logica.validar_competidores(competidoresSuccess)
        self.assertEqual(competidoresNoValidos, False)
        self.assertEqual(competidoresValidos, True)


    @classmethod
    def tearDownClass(self):
        Base.metadata.drop_all(engine)

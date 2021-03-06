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
            "Probabilidad": "1"
        },
        {
            "Nombre": "Ronny Stand",
            "Probabilidad": "0.8"
        }
        ]

        competidoresSuccess = [{
            "Nombre": "Michael Shummy",
            "Probabilidad": "0.5"
        },
        {
            "Nombre": "Ronny Stand",
            "Probabilidad": "0.5"
        }
        ]

        competidoresNoValidos = self.logica.validar_competidores(competidoresFail)
        competidoresValidos = self.logica.validar_competidores(competidoresSuccess)
        self.assertEqual(competidoresNoValidos, False)
        self.assertEqual(competidoresValidos, True)

    def test_validar_que_el_nombre_del_competidor_no_esta_vacio(self):
        competidoresFail    = self.logica.aniadir_competidor("   ", "1")
        competidoresSuccess = self.logica.aniadir_competidor("Michael Shummy", "0.5")

        self.assertEqual(competidoresFail, False)
        self.assertEqual(competidoresSuccess, True)

    def test_validar_probabilidad_entre_cero_y_uno(self):
        competidoresFail        = self.logica.aniadir_competidor("Juan Pablo", 2)
        competidoresSuccess     = self.logica.aniadir_competidor("Michael Shummy", 0.5)
        competidoresFailLessOne = self.logica.aniadir_competidor("Michael Shummy", -0.7)

        self.assertEqual(competidoresFail, False)
        self.assertEqual(competidoresSuccess, True)
        self.assertEqual(competidoresFailLessOne, False)

    def test_asociar_competidores_a_carrera(self):
        self.logica.crear_carrera('Carrera 3')
        self.logica.aniadir_competidor("Michael Shummy", 1)

        self.assertEqual(self.logica.asociar_competidores_carrera('Carrera 3'), True)
        self.assertEqual(self.logica.asociar_competidores_carrera('Carrera 2'), False)

    @classmethod
    def tearDownClass(self):
        Base.metadata.drop_all(engine)

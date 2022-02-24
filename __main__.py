import sys
from PyQt5.QtWidgets import QApplication
from src.vista.InterfazEPorra import App_EPorra
from src.logica.Logica_mock import Logica_mock
from src.modelo.declarative_base import Session, engine, Base
from src.modelo.carrera import Carrera
from src.modelo.apostador import Apostador
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta

if __name__ == '__main__':
    # Punto inicial de la aplicación
    #Crea la BD
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()

    logica = Logica_mock()

    app = App_EPorra(sys.argv, logica)
    sys.exit(app.exec_())
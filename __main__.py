import sys
from PyQt5.QtWidgets import QApplication
from src.vista.InterfazEPorra import App_EPorra
from src.logica.Logica import Logica
from src.modelo.declarative_base import Session, engine, Base
from src.modelo.setup import setupBD

if __name__ == '__main__':
    setupBD()

    # Punto inicial de la aplicación
    logica = Logica()

    app = App_EPorra(sys.argv, logica)
    sys.exit(app.exec_())
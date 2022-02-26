from src.modelo.declarative_base import engine, Base, session
from src.modelo.declarative_base import Session
from src.modelo.carrera import Carrera, Estado
from src.modelo.competidor import Competidor

class Logica():

    def __init__(self):
        Base.metadata.create_all(engine)
        self.competidores = []
        # #Este constructor contiene los datos falsos para probar la interfaz
        self.carreras    = []
        self.apostadores = []
        self.apuestas    = []
        self.ganancias   = []

    def dar_carreras(self):
        carreras = [elem.__dict__ for elem in session.query(Carrera).all()]
        newCarreras = []

        for carrera in carreras:
            newCarreras.append({
                "Nombre": carrera["Nombre"],
                "Competidores": [],
                "Abierta": True
            })

        return newCarreras
        # return self.carreras.copy()

    def dar_carrera(self, id_carrera):
        carreras = [elem.__dict__ for elem in session.query(Carrera).all()]

        return carreras[id_carrera].copy()

    def crear_carrera(self, nombre):
        busqueda = [elem.__dict__ for elem in session.query(Carrera).filter(Carrera.Nombre == nombre).all()]

        if len(busqueda) == 0:
            print("creando carrera")
            carrera = Carrera(Nombre=nombre, Estado=Estado.ABIERTA)
            session.add(carrera)
            session.commit()
            session.close()
            return True
        else:
            return False

    def asociar_competidores_carrera(self, nombre):
        carrera = session.query(Carrera).filter(Carrera.Nombre == nombre).first()
        competidores = self.competidores
        competidoresCarrera = []

        print("asociar_competidores_carrera", carrera,competidores)

        if carrera:
            for item in competidores:
                competidor = Competidor(
                    Nombre=item["nombre"],
                    Probabilidad=item["probabilidad"]
                )

                session.add(competidor)
                competidoresCarrera.append(competidor)

            carrera.Competidores = competidoresCarrera
            session.commit()
            session.close()

            self.competidores = []
            return True
        else:
            return False

    def editar_carrera(self, id, nombre):
        self.carreras[id]['Nombre'] = nombre

    def terminar_carrera(self, id, ganador):
        self.carreras[id]['Ganador'] = ganador

    def eliminar_carrera(self, id):
        del self.carreras[id]

    def dar_apostadores(self):
        return self.apostadores.copy()

    def aniadir_apostador(self, nombre):
        self.apostadores.append({'Nombre': nombre})

    def editar_apostador(self, id, nombre):
        self.apostadores[id]['Nombre'] = nombre

    def eliminar_apostador(self, id):
        del self.apostadores[id]

    def dar_competidores_carrera(self, id):
        carreras = [elem.__dict__ for elem in session.query(Carrera).all()]
        carrera_id = carreras[id]["id"]
        competidores = [elem.__dict__ for elem in session.query(Competidor)
            .filter(Competidor.Carrera_id == carrera_id).all()]

        return competidores

    def dar_competidor(self, id_carrera, id_competidor):
        return self.carreras[id_carrera]['Competidores'][id_competidor].copy()

    def aniadir_competidor(self, nombre, probabilidad):
        nombre = nombre.strip()

        if isinstance(probabilidad, str):
            return False

        if len(nombre) == 0 or (probabilidad < 0 and probabilidad > 1):
            return False

        self.competidores.append({"nombre": nombre, "probabilidad": probabilidad})
        print("aniadir_competidor", self.competidores)
        return True
        # self.carreras[id]['Competidores'].append({'Nombre':nombre, 'Probabilidad':probabilidad})

    def editar_competidor(self, id_carrera, id_competidor, nombre, probabilidad):
        self.carreras[id_carrera]['Competidores'][id_competidor]['Nombre']=nombre
        self.carreras[id_carrera]['Competidores'][id_competidor]['Probabilidad']=probabilidad

    def eliminar_competidor(self, id_carrera, id_competidor):
        del self.carreras[id_carrera]['Competidores'][id_competidor]

    def dar_apuestas_carrera(self, id_carrera):
        nombre_carrera =self.carreras[id_carrera]['Nombre']
        return list(filter(lambda x: x['Carrera']==nombre_carrera, self.apuestas))

    def dar_apuesta(self, id_carrera, id_apuesta):
        return self.dar_apuestas_carrera(id_carrera)[id_apuesta].copy()

    def crear_apuesta(self, apostador, id_carrera, valor, competidor):
        n_apuesta = {}
        n_apuesta['Apostador'] = apostador
        n_apuesta['Carrera'] = self.carreras[id_carrera]['Nombre']
        n_apuesta['Valor'] = valor
        n_apuesta['Competidor'] = competidor
        self.apuestas.append(n_apuesta)

    def editar_apuesta(self, id_apuesta, apostador, carrera, valor, competidor):
        self.apuestas[id_apuesta]['Apostador'] = apostador
        self.apuestas[id_apuesta]['Carrera'] = carrera
        self.apuestas[id_apuesta]['Valor'] = valor
        self.apuestas[id_apuesta]['Competidor'] = competidor

    def eliminar_apuesta(self, id_carrera, id_apuesta):
        nombre_carrera =self.carreras[id_carrera]['Nombre']
        i = 0
        id = 0
        while i < len(self.apuestas):
            if self.apuestas[i]['Carrera'] == nombre_carrera:
                if id == id_apuesta:
                    self.apuestas.pop(i)
                    return True
                else:
                    id+=1
            i+=1

        return False


        del self.apuesta[id_apuesta]

    def dar_reporte_ganancias(self, id_carrera, id_competidor):
        self.carreras[id_carrera]['Abierta']=False
        n_carrera = self.carreras[id_carrera]['Nombre']

        for ganancias in self.ganancias:
            if ganancias['Carrera'] == n_carrera:
                return ganancias['Ganancias'], ganancias['Ganancias de la casa']

    
    def validar_competidores(self, competidores):
        totalProbabilidad = 0
    
        for item in competidores:
            totalProbabilidad += float(item["Probabilidad"])
        
        if not totalProbabilidad == 1:
            return False

        return True

        





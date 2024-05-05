from materia.domain.entities.materia import Materia
from pymongo import MongoClient

class MongoDBMateriaRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['materias']

    def save(self, materia):
        materia_data = {
            'nombre': materia.nombre,
            'cuatrimestre': materia.cuatrimestre
        }
        result = self.collection.insert_one(materia_data)

    def find_by_name(self, nombre):
        query = {"nombre": nombre}
        materia_data = self.collection.find_one(query)
        if materia_data:
            return Materia(nombre=materia_data['nombre'], cuatrimestre=materia_data['cuatrimestre'])
        else:
            return None
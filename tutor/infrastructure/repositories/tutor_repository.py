from pymongo import MongoClient
from tutor.domain.entities.tutor import Tutor

class MongoDBTutorRepository:
    def __init__(self, connection_string, database_name, alumno_repository):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['tutores']
        self.alumno_repository = alumno_repository

    def save(self, tutor: Tutor):
        tutor_data = {
            'nombres': tutor.nombres,
            'primer_apellido': tutor.primer_apellido,
            'segundo_apellido': tutor.segundo_apellido,
            'identificador': tutor.generar_identificador()
        }
        self.collection.insert_one(tutor_data)

    def find_by_names_and_lastname(self, nombres, primer_apellido):
        query = {"nombres": nombres, "primer_apellido": primer_apellido}
        tutor_data = self.collection.find_one(query)
        if tutor_data:
            return Tutor(nombres=tutor_data['nombres'], primer_apellido=tutor_data['primer_apellido'], segundo_apellido=tutor_data.get('segundo_apellido'))
        else:
            return None
        
    def find_all(self):
        tutors_data = self.collection.find({})
        tutors = [Tutor(nombres=tutor['nombres'], primer_apellido=tutor['primer_apellido'], segundo_apellido=tutor.get('segundo_apellido')) for tutor in tutors_data]
        return tutors
    
    def find_by_id(self, identificador):
        query = {"identificador": identificador}
        tutor_data = self.collection.find_one(query)
        if tutor_data:
            return Tutor(nombres=tutor_data['nombres'], primer_apellido=tutor_data['primer_apellido'], segundo_apellido=tutor_data.get('segundo_apellido'))
        else:
            return None

    def assign_alumnos(self, identificador, matriculas_alumnos):
    # Obtener el tutor correspondiente al identificador
        tutor = self.find_by_id(identificador)
        if not tutor:
            raise ValueError("El tutor especificado no existe")

        # Obtener los objetos de alumnos correspondientes a las matrículas proporcionadas
        alumnos_asignados = []
        for matricula in matriculas_alumnos:
            alumno = self.alumno_repository.find_by_enrollment(matricula)
            if not alumno:
                raise ValueError(f"El alumno con matrícula {matricula} no existe")
            alumnos_asignados.append(alumno)

        # Asignar los alumnos al tutor
        self.collection.update_one(
            {"identificador": identificador},
            {"$addToSet": {"alumnos": {"$each": alumnos_asignados}}}
        )
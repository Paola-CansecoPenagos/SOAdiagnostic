from pymongo import MongoClient
from alumno.domain.entities.alumno import Alumno

class MongoDBAlumnoRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['alumnos']

    def get_last_enrollment_number(self, year, status_code):
        query = {
            "enrollment": {"$regex": f"^{year}{status_code}"},
        }
        projection = {"enrollment": 1, "_id": 0}
        result = self.collection.find(query, projection).sort("enrollment", -1).limit(1)
        last_enrollment = result[0]['enrollment'] if self.collection.count_documents(query) > 0 else f"{year}{status_code}000"
        return last_enrollment

    def save(self, student: Alumno):
        student_data = {
            'nombre': student.nombre,
            'carrera': student.carrera,
            'matricula': student.matricula,
            'status_inicial': student.status_inicial,
            'materias': []  
        }
        self.collection.insert_one(student_data)

    def find_all(self):
        alumnos_data = self.collection.find({})
        alumnos = [Alumno(
            nombre=alumno['nombre'],
            carrera=alumno['carrera'],
            matricula=alumno['matricula'],
            status_inicial=alumno['status_inicial']
        ) for alumno in alumnos_data]
        return alumnos

    def find_by_name(self, nombre):
        query = {"nombre": nombre}
        student_data = self.collection.find_one(query)
        if student_data:
            return Alumno(nombre=student_data['nombre'], carrera=student_data['carrera'], matricula=student_data['matricula'], status_inicial=student_data['status_inicial'])
        else:
            return None
    
    def find_by_enrollment(self, matricula):
        query = {"matricula": matricula}
        student_data = self.collection.find_one(query)
        if student_data:
            return Alumno(nombre=student_data['nombre'], carrera=student_data['carrera'], matricula=student_data['matricula'], status_inicial=student_data['status_inicial'])
        else:
            return None
        
    def assign_materias(self, matricula, materias):
        student_data = self.collection.find_one({"matricula": matricula})
        if not student_data:
            raise ValueError("El alumno no está registrado")

        for materia in materias:
            if not self.db['materias'].find_one({"nombre": materia}):
                raise ValueError(f"La materia '{materia}' no existe")

        # Guardar solo los nombres de las materias en la lista
        self.collection.update_one(
            {"matricula": matricula},
            {"$addToSet": {"materias": {"$each": materias}}}
        )

    
    def get_materias(self, matricula):
        query = {"matricula": matricula}
        projection = {"_id": 0, "materias": 1}
        result = self.collection.find_one(query, projection)
        return result.get("materias", []) if result else []

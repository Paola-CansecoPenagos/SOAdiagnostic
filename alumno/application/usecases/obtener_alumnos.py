from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository
from alumno.domain.entities.alumno import Alumno

class GetAllAlumnos:
    def __init__(self, alumno_repository: MongoDBAlumnoRepository):
        self.alumno_repository = alumno_repository

    def execute(self):
        return self.alumno_repository.find_all()

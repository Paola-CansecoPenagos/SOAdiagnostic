from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository
from alumno.domain.entities.alumno import Alumno
from datetime import datetime

class RegisterAlumno:
    def __init__(self, alumno_repository: MongoDBAlumnoRepository):
        self.alumno_repository = alumno_repository

    def execute(self, nombre, carrera, matricula, status_inicial):
        if not nombre or not carrera or not matricula or not status_inicial:
            raise ValueError("Todos los datos del alumno son necesarios")

        if not matricula.startswith(datetime.now().strftime("%y")):
            raise ValueError("El principio de la matrícula debe ser los últimos dos dígitos del año")

        year = matricula[:2]
        status_code = matricula[2]

        if status_code not in ("1", "3"):
            raise ValueError("El código de estado de la matrícula debe ser '1' para preuniversitario o '3' para universitario")

        if status_inicial not in ("preu", "uni"):
            raise ValueError("El estado inicial solo puede ser 'preu' para preuniversitario o 'uni' para universitario")

        existing_student = self.alumno_repository.find_by_name(nombre)
        if existing_student:
            raise ValueError("Ya existe un alumno con ese nombre")

        existing_student = self.alumno_repository.find_by_enrollment(matricula)
        if existing_student:
            raise ValueError("Ya existe un alumno con esa matrícula")

        alumno = Alumno(nombre, carrera, matricula, status_inicial)
        self.alumno_repository.save(alumno)

    def get_all_students(self):
        return self.alumno_repository.find_all()
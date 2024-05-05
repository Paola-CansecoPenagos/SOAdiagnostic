from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository
from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository

class AssignAlumnosTutor:
    def __init__(self, tutor_repository: MongoDBTutorRepository, alumno_repository: MongoDBAlumnoRepository):
        self.tutor_repository = tutor_repository
        self.alumno_repository = alumno_repository

    def execute(self, identificador, matriculas_alumnos):
        tutor = self.tutor_repository.find_by_id(identificador)
        if not tutor:
            raise ValueError("El tutor especificado no existe")

        alumnos_asignados = []
        for matricula in matriculas_alumnos:
            alumno = self.alumno_repository.find_by_enrollment(matricula)
            if not alumno:
                raise ValueError(f"El alumno con matrícula {matricula} no existe")
            alumnos_asignados.append(alumno.matricula)

        self.tutor_repository.assign_alumnos(identificador, alumnos_asignados)

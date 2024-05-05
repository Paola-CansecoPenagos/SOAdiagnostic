class GetMateriasAlumno:
    def __init__(self, alumno_repository):
        self.alumno_repository = alumno_repository

    def execute(self, matricula):
        alumno = self.alumno_repository.find_by_enrollment(matricula)
        if not alumno:
            raise ValueError("La matrícula no corresponde a ningún alumno")
        
        return self.alumno_repository.get_materias(matricula)

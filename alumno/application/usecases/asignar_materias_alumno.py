class AssignMateriasAlumno:
    def __init__(self, alumno_repository, materia_repository):
        self.alumno_repository = alumno_repository
        self.materia_repository = materia_repository

    def execute(self, matricula, materias):
        alumno = self.alumno_repository.find_by_enrollment(matricula)
        if not alumno:
            raise ValueError("La matrícula no corresponde a ningún alumno")

        for materia_nombre in materias:
            materia = self.materia_repository.find_by_name(materia_nombre)
            if not materia:
                raise ValueError(f"La materia '{materia_nombre}' no existe")
        
        self.alumno_repository.assign_materias(matricula, materias)

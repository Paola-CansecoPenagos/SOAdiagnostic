from materia.domain.entities.materia import Materia
from materia.infrastructure.repositories.materia_repository import MongoDBMateriaRepository

class RegisterMateria:
    def __init__(self, materia_repository: MongoDBMateriaRepository):
        self.materia_repository = materia_repository

    def execute(self, nombre, cuatrimestre):
        if not isinstance(cuatrimestre, int):
            raise ValueError("El cuatrimestre debe de ser un número")
        
        existing_materia = self.materia_repository.find_by_name(nombre)
        if existing_materia:
            raise ValueError("Ya existe una materia con ese nombre")
        
        materia = Materia(nombre, cuatrimestre)
        self.materia_repository.save(materia)
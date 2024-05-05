from tutor.domain.entities.tutor import Tutor

class RegisterTutor:
    def __init__(self, tutor_repository):
        self.tutor_repository = tutor_repository

    def execute(self, nombres, primer_apellido, segundo_apellido=None):
        existing_tutor = self.tutor_repository.find_by_names_and_lastname(nombres, primer_apellido)
        if existing_tutor:
            raise ValueError("Ya existe un tutor con estos nombres y primer apellido")

        tutor = Tutor(nombres, primer_apellido, segundo_apellido)
        self.tutor_repository.save(tutor)

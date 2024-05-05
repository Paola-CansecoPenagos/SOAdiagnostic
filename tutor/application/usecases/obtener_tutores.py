class GetAllTutores:
    def __init__(self, tutor_repository):
        self.tutor_repository = tutor_repository

    def execute(self):
        return self.tutor_repository.find_all()

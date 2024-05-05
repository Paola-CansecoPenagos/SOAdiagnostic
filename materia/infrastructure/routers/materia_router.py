from flask import Blueprint
from materia.infrastructure.controllers.crear_materia_controller import create_materia_blueprint, initialize_endpoints as create_materia_endpoints
from materia.infrastructure.repositories.materia_repository import MongoDBMateriaRepository

materia_router = Blueprint('materia_router', __name__)

def initialize_endpoints(repository):
    create_materia_endpoints(repository)

initialize_endpoints(MongoDBMateriaRepository(connection_string='mongodb://localhost:27017/', database_name='diagnostico'))

materia_router.register_blueprint(create_materia_blueprint, url_prefix='/api/materias')

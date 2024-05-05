from flask import Blueprint
from tutor.infrastructure.controllers.crear_tutor_controller import create_tutor_blueprint, initialize_endpoints as crear_tutor_endpoints
from tutor.infrastructure.controllers.obtener_tutores_controller import get_all_tutors_blueprint, initialize_endpoints as get_all_tutors_endpoints
from tutor.infrastructure.controllers.asignar_alumnos_tutor_controller import assign_alumnos_tutor_blueprint, initialize_endpoints as assign_alumnos_tutor_endpoints
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository
from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository

tutor_router = Blueprint('tutor_router', __name__)

def initialize_endpoints(tutor_repository, alumno_repository):
    crear_tutor_endpoints(tutor_repository)
    get_all_tutors_endpoints(tutor_repository)
    assign_alumnos_tutor_endpoints(tutor_repository, alumno_repository)
    
alumno_repo = MongoDBAlumnoRepository(connection_string='mongodb://localhost:27017/', database_name='diagnostico')
tutor_repo = MongoDBTutorRepository(connection_string='mongodb://localhost:27017/', database_name='diagnostico', alumno_repository=alumno_repo)

initialize_endpoints(
    tutor_repository=tutor_repo,
    alumno_repository=alumno_repo
)

tutor_router.register_blueprint(create_tutor_blueprint, url_prefix='/api/tutores')
tutor_router.register_blueprint(get_all_tutors_blueprint, url_prefix='/api/tutores')
tutor_router.register_blueprint(assign_alumnos_tutor_blueprint, url_prefix='/api/tutores')

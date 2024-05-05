from flask import Blueprint
from alumno.infrastructure.controllers.crear_alumno_controller import create_student_blueprint, initialize_endpoints as crear_alumno_endpoints
from alumno.infrastructure.controllers.obtener_alumnos_controller import get_all_students_blueprint, initialize_endpoints as obtener_alumnos_endpoints
from alumno.infrastructure.controllers.asignar_materias_alumno_controller import assign_materias_blueprint, initialize_endpoints as assign_materias_endpoints
from alumno.infrastructure.controllers.obtener_materias_alumnos_controller import get_materias_blueprint, initialize_endpoints as get_materias_endpoints
from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository
from materia.infrastructure.repositories.materia_repository import MongoDBMateriaRepository

alumno_router = Blueprint('alumno_router', __name__)

def initialize_endpoints(alumno_repository, materia_repository):
    crear_alumno_endpoints(alumno_repository)
    obtener_alumnos_endpoints(alumno_repository)
    assign_materias_endpoints(alumno_repository, materia_repository)
    get_materias_endpoints(alumno_repository)

initialize_endpoints(
    MongoDBAlumnoRepository(connection_string='mongodb://localhost:27017/', database_name='diagnostico'),
    MongoDBMateriaRepository(connection_string='mongodb://localhost:27017/', database_name='diagnostico')
)

alumno_router.register_blueprint(create_student_blueprint, url_prefix='/api/alumnos')
alumno_router.register_blueprint(get_all_students_blueprint, url_prefix='/api/alumnos')
alumno_router.register_blueprint(assign_materias_blueprint, url_prefix='/api/alumnos')
alumno_router.register_blueprint(get_materias_blueprint, url_prefix='/api/alumnos')
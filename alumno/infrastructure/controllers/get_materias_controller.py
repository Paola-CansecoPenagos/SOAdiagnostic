from flask import Blueprint, jsonify
from alumno.application.usecases.get_materias_alumno import GetMateriasAlumno
from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository

get_materias_blueprint = Blueprint('get_materias', __name__)

def initialize_endpoints(alumno_repository):
    get_materias_usecase = GetMateriasAlumno(alumno_repository=alumno_repository)
    
    @get_materias_blueprint.route('/<matricula>/materias', methods=['GET'])
    def get_materias(matricula):
        try:
            materias = get_materias_usecase.execute(matricula)
            return jsonify({"materias": materias}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

from flask import Blueprint, request, jsonify
from tutor.application.usecases.asignar_alumnos_tutor import AssignAlumnosTutor
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository
from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository

assign_alumnos_tutor_blueprint = Blueprint('assign_alumnos_tutor', __name__)

def initialize_endpoints(tutor_repository, alumno_repository):
    assign_alumnos_tutor_usecase = AssignAlumnosTutor(tutor_repository=tutor_repository, alumno_repository=alumno_repository)
    
    @assign_alumnos_tutor_blueprint.route('/<identificador>/alumnos', methods=['POST'])
    def assign_alumnos_to_tutor(identificador):
        data = request.get_json()

        if not data or not 'alumnos' in data:
            return jsonify({"error": "Se requiere la lista de matrículas de alumnos"}), 400

        matriculas_alumnos = data['alumnos']

        try:
            assign_alumnos_tutor_usecase.execute(identificador, matriculas_alumnos)
            return jsonify({"message": "Alumnos asignados correctamente al tutor"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

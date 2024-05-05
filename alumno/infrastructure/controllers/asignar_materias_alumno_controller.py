from flask import Blueprint, request, jsonify
from alumno.application.usecases.asignar_materias_alumno import AssignMateriasAlumno
from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository
from materia.infrastructure.repositories.materia_repository import MongoDBMateriaRepository

assign_materias_blueprint = Blueprint('assign_materias', __name__)

def initialize_endpoints(alumno_repository, materia_repository):
    assign_materias_usecase = AssignMateriasAlumno(alumno_repository=alumno_repository, materia_repository=materia_repository)
    
    @assign_materias_blueprint.route('/<matricula>/materias', methods=['POST'])
    def assign_materias(matricula):
        data = request.get_json()

        if not data or not 'materias' in data:
            return jsonify({"error": "Se requiere la lista de materias"}), 400

        materias = data['materias']

        try:
            assign_materias_usecase.execute(matricula, materias)
            return jsonify({"message": "Materias asignadas correctamente"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

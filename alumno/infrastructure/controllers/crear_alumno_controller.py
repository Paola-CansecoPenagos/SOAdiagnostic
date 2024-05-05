from flask import Blueprint, request, jsonify
from alumno.application.usecases.crear_alumno import RegisterAlumno
from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository

create_student_blueprint = Blueprint('create_student', __name__)

def initialize_endpoints(repository):
    register_student_usecase = RegisterAlumno(alumno_repository=repository)
    
    @create_student_blueprint.route('', methods=['POST'])
    def register_student():
        data = request.get_json()

        if not data or not all(key in data for key in ['nombre', 'carrera', 'matricula', 'status_inicial']):
            return jsonify({"error": "Todos los datos del alumno son necesarios"}), 400

        nombre = data.get('nombre')
        carrera = data.get('carrera')
        matricula = data.get('matricula')
        status_inicial = data.get('status_inicial')

        try:
            register_student_usecase.execute(nombre, carrera, matricula, status_inicial)
            return jsonify({"message": "Alumno registrado exitosamente"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

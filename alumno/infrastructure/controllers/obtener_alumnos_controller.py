from flask import Blueprint, jsonify
from alumno.application.usecases.obtener_alumnos import GetAllAlumnos
from alumno.infrastructure.repositories.alumno_repository import MongoDBAlumnoRepository

get_all_students_blueprint = Blueprint('get_all_students', __name__)

def initialize_endpoints(repository):
    get_all_students_usecase = GetAllAlumnos(alumno_repository=repository)
    
    @get_all_students_blueprint.route('', methods=['GET'])
    def get_all_students():
        try:
            students = get_all_students_usecase.execute()
            student_list = [{"nombre": student.nombre, "carrera": student.carrera, "matricula": student.matricula, "status_inicial": student.status_inicial} for student in students]
            return jsonify({"students": student_list}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

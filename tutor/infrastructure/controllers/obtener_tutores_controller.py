from flask import Blueprint, jsonify
from tutor.application.usecases.obtener_tutores import GetAllTutores
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository

get_all_tutors_blueprint = Blueprint('get_all_tutors', __name__)

def initialize_endpoints(tutor_repository):
    get_all_tutors_usecase = GetAllTutores(tutor_repository=tutor_repository)
    
    @get_all_tutors_blueprint.route('', methods=['GET'])
    def get_all_tutors():
        try:
            tutors = get_all_tutors_usecase.execute()
            tutors_data = [{"nombres": tutor.nombres, "primer_apellido": tutor.primer_apellido, "segundo_apellido": tutor.segundo_apellido} for tutor in tutors]
            return jsonify({"tutores": tutors_data}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

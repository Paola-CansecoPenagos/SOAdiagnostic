from flask import Blueprint, request, jsonify
from tutor.application.usecases.crear_tutor import RegisterTutor
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository

create_tutor_blueprint = Blueprint('create_tutor', __name__)

def initialize_endpoints(tutor_repository):
    register_tutor_usecase = RegisterTutor(tutor_repository=tutor_repository)
    
    @create_tutor_blueprint.route('', methods=['POST'])
    def register_tutor():
        data = request.get_json()

        if not data or not all(key in data for key in ['nombres', 'primer_apellido']):
            return jsonify({"error": "Se requieren nombres y primer apellido del tutor"}), 400

        nombres = data.get('nombres')
        primer_apellido = data.get('primer_apellido')
        segundo_apellido = data.get('segundo_apellido')

        try:
            register_tutor_usecase.execute(nombres, primer_apellido, segundo_apellido)
            return jsonify({"message": "Tutor creado exitosamente"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

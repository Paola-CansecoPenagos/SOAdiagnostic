from flask import Blueprint, request, jsonify
from materia.application.usecases.crear_materia import RegisterMateria
from materia.infrastructure.repositories.materia_repository import MongoDBMateriaRepository

create_materia_blueprint = Blueprint('create_materia', __name__)

def initialize_endpoints(repository):
    register_materia_usecase = RegisterMateria(materia_repository=repository)
    
    @create_materia_blueprint.route('', methods=['POST'])
    def register_materia():
        data = request.get_json()

        if not data or not all(key in data for key in ['nombre', 'cuatrimestre']):
            return jsonify({"error": "Name and quarter are required"}), 400

        nombre = data.get('nombre')
        cuatrimestre = data.get('cuatrimestre')

        try:
            register_materia_usecase.execute(nombre, cuatrimestre)
            return jsonify({"message": "Materia registered successfully"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

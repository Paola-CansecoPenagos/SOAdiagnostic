from flask import Flask, jsonify
from flask_cors import CORS
#from tutor.infrastructure.routers.tutor_router import tutor_router
from materia.infrastructure.routers.materia_router import materia_router
from alumno.infrastructure.routers.alumno_router import alumno_router

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
#app.register_blueprint(tutor_router)
app.register_blueprint(materia_router)
app.register_blueprint(alumno_router)

@app.route('/')
def index():
    return jsonify("INICIO")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

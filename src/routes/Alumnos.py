from flask import Blueprint, jsonify, request
from models.AlumnosModel import AlumnoModel
from models.entities.Alumnos import Alumno

main = Blueprint('alumnos_blueprint', __name__)

@main.route('/alumnos', methods=['GET'])
def get_alumno():
    try:
        alumnos = AlumnoModel.get_alumnos()
        return jsonify(alumnos)
    except Exception as ex:
        return jsonify({"message":str(ex)}),500

@main.route('/alumno/<int:id>', methods=['GET'])
def get_OneAlumno(id):
    try:
        alumno = AlumnoModel.get_OneAlumno(id)
        return jsonify(alumno)
    except Exception as ex:
        return jsonify({"message":str(ex)}),500
    

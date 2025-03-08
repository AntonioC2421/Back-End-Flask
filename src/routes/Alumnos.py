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

@main.route("/alumnos/add", methods=["POST"])
def add_alumnos():
    try:
        id =  request.json["id"]
        name =  request.json["name"]
        last_name = request.json["last_name"]
        email = request.json["email"]

        alumno =  Alumno(id,name,last_name,email)

        affect_rows=AlumnoModel.add_alumno(alumno)

        if affect_rows == 1:
            return jsonify({
                "message": "Registro de alumno, exitoso!!"
                })
        else:
            return jsonify({
                "message":"Ocurrio un problema con el registro de alumno"
            }),500

    except Exception as ex:
        raise Exception(ex)
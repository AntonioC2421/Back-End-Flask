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

@main.route('/alumnos/<int:id>', methods=['GET'])
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
                "message": "Registro exitoso",
                "id": id,
                "name": name,
                "last_name": last_name,
                "email": email
            }), 200
        else:
            return jsonify({
                "message":"Ocurrio un problema con el registro de alumno"
            }),500

    except Exception as ex:
        raise Exception(ex)
    
@main.route("/alumnos/update/<int:id>", methods=["PUT"])
def update_alumno(id):
    try:
        name = request.json["name"]
        last_name = request.json["last_name"]
        email = request.json["email"]

        alumno = Alumno(id, name, last_name, email)

        affected_rows = AlumnoModel.update_alumno(alumno)

        if affected_rows == 1:
            #Devolver el alumno actualizado
            return jsonify({
                "id": id,
                "name": name,
                "last_name": last_name,
                "email": email
            }), 200
        else:
            return jsonify({"message": "Error al editar alumno"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

    
@main.route("/alumnos/delete/<int:id>", methods=["DELETE"])
def delete_alumno(id):
    try:
        alumno = Alumno(id)

        affected_rows = AlumnoModel.delete_alumno(alumno)
        
        if affected_rows == 1:
            return jsonify({"message":"Alumno Eliminado"})
        else:
            return jsonify({"message":"Error al eliminar alumno"}),500
        
    except Exception as ex:
        return jsonify({"message":str(ex)}),500

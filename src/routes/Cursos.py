from flask import Blueprint, jsonify, request
from models.CursosModel import CursosModel
from models.entities.Cursos import Curso

main = Blueprint("cursos_blueprint", __name__)

@main.route("/cursos" , methods=["GET"])
def get_cursos():
    try:
        cursos = CursosModel.get_cursos()
        return jsonify(cursos)
    
    except Exception as ex:
        return jsonify({"message":str(ex)}),500
    
@main.route("/cursos/<int:id>", methods=["GET"])
def get_curso(id):
    try:
        curso = CursosModel.get_curso(id)
        return jsonify(curso)
    
    except:
        return jsonify({"message": "No se encuentra registro de curso solicitado"})
    
@main.route("/cursos/add", methods=["POST"])
def add_curso():
    try:
        id = request.json["id"]
        name = request.json["name"]
        id_profesor = request.json["id_profesor"]

        curso = Curso(id,name,id_profesor)

        affected_row = CursosModel.add_curso(curso)

        if affected_row == 1:
            return jsonify({
                "message": "Registro exitoso",
                "id": id,
                "name": name,
                "id_profesor": id_profesor
            }), 200
        else:
            return jsonify({"message":"Error en crear el curso"}),500
        
    except Exception as ex:
       return jsonify({"message": str(ex)}),500  
    
@main.route("/cursos/update/<int:id>", methods=["PUT"])
def update_curso(id):
    try:
        name = request.json["name"]
        id_profesor = request.json["id_profesor"]

        alumno = Curso(id, name, id_profesor)

        affected_rows = CursosModel.update_curso(alumno)

        if affected_rows == 1:
            return jsonify({
                "message": "Registro exitoso",
                "id": id,
                "name": name,
                "id_profesor": id_profesor
            }), 200
        else:
            return jsonify({"message":"Error al actualizar curso"}),500
        
    except Exception as ex:
        return jsonify({"message":str(ex)}),500
    
@main.route("/cursos/delete/<int:id>",methods=["DELETE"])
def delete_curso(id):
    try:
        curso = Curso(id)

        affected_rows = CursosModel.delete_curso(curso)

        if affected_rows == 1:
            return jsonify({"message":"Eliminacion de curso, exitoso!!"})
        else:
            return jsonify({"message":"Error en eliminacion de curso"})
        
    except Exception as ex:
        return jsonify({"message":str(ex)})
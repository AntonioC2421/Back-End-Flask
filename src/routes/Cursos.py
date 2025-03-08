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
    except Exception as ex:
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
            return jsonify({"message":"Curso agreado correctamente"})
        else:
            return jsonify({"message":"Error en crear el curso"}),500
        
    except Exception as ex:
       return jsonify({"message": str(ex)}),500  
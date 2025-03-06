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
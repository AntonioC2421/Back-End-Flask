from flask import Blueprint, jsonify, request
from models.MatriculasModel import MatriculaModel
from models.entities.Matriculas import Matricula

main = Blueprint('matricula_blueprint', __name__)

@main.route('/matriculas', methods = ['GET'])
def get_matriculas():
    try:
        matriculas = MatriculaModel.get_matriculas()
        return jsonify(matriculas)
    except Exception as ex:
        return jsonify({"message":str(ex)}),500

@main.route("/matriculas/<int:id>", methods=["GET"])
def get_matricula(id):
    try:
        matricula = MatriculaModel.get_matricula(id)
        return jsonify(matricula)
    except Exception as ex:
        return jsonify({"message": str(ex)}),500
    
@main.route("/matriculas/add", methods=["POST"])
def add_matricula():
    try:
        id = request.json["id"]
        curso_id = request.json["curso_id"]
        alumno_id =  request.json["alumno_id"]

        matricula = Matricula(id,curso_id,alumno_id)

        affected_row = MatriculaModel.add_matricula(matricula)

        if affected_row == 1:
            return jsonify({"message":"Matricula registrada correctamente"})
        else:
            return jsonify({"message":"Error en registro de matricula"})
    except Exception as ex:
        return jsonify({"message": str(ex)}),500
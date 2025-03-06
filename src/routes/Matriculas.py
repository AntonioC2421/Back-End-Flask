from flask import Blueprint, jsonify, request
from models.MatriculasModel import MatriculaModel
from models.entities.Matriculas import Matricula

main = Blueprint('matricula_blueprint', __name__)

@main.route('/matriculas', methods = ['GET'])
def get_matriculas():
    try:
        matriculas = MatriculaModel.get_matricula()
        return jsonify(matriculas)
    except Exception as ex:
        return jsonify({"message":str(ex)}),500

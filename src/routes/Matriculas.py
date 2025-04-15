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
        alumno_id = request.json["alumno_id"]

        matricula = Matricula(id,alumno_id, curso_id)
        affected_row = MatriculaModel.add_matricula(matricula)

        if affected_row == 1:
            return jsonify({
                "message": "Registro exitoso",
                "id": id,
                "alumno_id": alumno_id,
                "curso_id": curso_id
            }), 200
        else:
            return jsonify({"message": "Error en registro de matrícula"}), 400

    except ValueError as ve:
        # Errores de validación de datos (como IDs que no existen)
        return jsonify({"message": str(ve)}), 404

    except Exception as ex:
        # Errores internos
        return jsonify({"message": str(ex)}), 500

    
@main.route("/matriculas/update/<int:id>", methods=["PUT"])
def update_matricula(id):
    try:
        alumno_id = request.json["alumno_id"]
        curso_id = request.json["curso_id"]
        
        matricula = Matricula(id,alumno_id,curso_id)

        affected_rows = MatriculaModel.update_matricula(matricula)

        if affected_rows == 1:
            return jsonify({
                "message": "Registro exitoso",
                "id": id,
                "alumno_id": alumno_id,
                "curso_id": curso_id
            }), 200
        else:
            return jsonify({"message":"Error en actualizacion de matricula"}),500
        
    except Exception as ex:
        return jsonify({"message": str(ex)}),500

@main.route("/matriculas/delete/<int:id>", methods=["DELETE"])
def delete_matricula(id):
    try:
        matricula = Matricula(id)

        affected_rows = MatriculaModel.delete_matricula(matricula)

        if affected_rows == 1:
            return jsonify({"message":"Matricula eliminada correctamente"})
        else:
            return jsonify({"message":"Error al eliminar matricula"}),500
        
    except Exception as ex:
        return jsonify({"message":str(ex)}),500
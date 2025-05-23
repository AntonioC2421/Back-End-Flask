from flask import Blueprint, jsonify, request
from models.ProfesoresModel import ProfesoresModel
from models.entities.Profesores import Profesor

main = Blueprint('profesor_blueprint', __name__)

@main.route('/profesores' , methods=['GET'])
def get_profesor():
    try:
        model = ProfesoresModel()  # Se instancia la clase
        profesores = model.get_profesores()
        return jsonify(profesores)
    except Exception as ex:
        return jsonify({"message": str(ex)}),500

@main.route('/profesores/<int:id>', methods=['GET'])
def get_profe(id):
    try:
        profesores = ProfesoresModel.get_profe(id)

        if profesores != None:
            return jsonify(profesores)
        else:
            return jsonify({}),404
  
    except Exception as ex:
        return jsonify({"message": str(ex)}),500
    
@main.route('/profesores/add', methods=['POST'])
def add_profe():
    try:
        id=request.json['id']
        name=request.json['name']
        last_name=request.json['last_name']
        email=request.json['email']

        profe = Profesor(id,name,last_name,email)

        affected_rows=ProfesoresModel.add_profes(profe)

        if affected_rows == 1:
            return jsonify({
                "message": "Registro exitoso",
                "id": id,
                "name": name,
                "last_name": last_name,
                "email": email
            }), 200
        else:
            return jsonify({'message':'Error en agregar profesor'}),500
        
    except Exception as ex:
        return jsonify({"message": str(ex)}),500

@main.route('/profesores/update/<int:id>', methods=['PUT'])
def update_profe(id):
    try:
        name=request.json['name']
        last_name=request.json['last_name']
        email=request.json['email']

        profe = Profesor(id,name,last_name,email)

        affected_rows=ProfesoresModel.update_profes(profe)

        if affected_rows == 1:
            #Devolver el alumno actualizado
            return jsonify({
                "id": id,
                "name": name,
                "last_name": last_name,
                "email": email
            }), 200
        else:
            return jsonify({'message':'Error en actualizar profesor'}),500
        
    except Exception as ex:
        return jsonify({"message": str(ex)}),500

@main.route('/profesores/delete/<int:id>', methods=['DELETE'])
def delete_profe(id):
    try:
        profe = Profesor(id)

        affected_rows = ProfesoresModel.delete_profes(profe)

        if affected_rows == 1:
            return jsonify({"message":"Profesor Eliminado"})
        else:
            return jsonify({'message':'Error al eliminar Profesor'}),500
        
    except Exception as ex:
        return jsonify({"message": str(ex)}),500
from flask import Flask
from config import config
from flask_cors import CORS
from routes.Profesores import main as profesor_routes
from routes.Cursos import main as cursos_blueprint
from routes.Alumnos import main as alumnos_blueprint
from routes.Matriculas import main as matriculas_blueprint

app = Flask(__name__)

#Aqui puedo cambiar el puerto dependiendo en cual voy a usarla
CORS(app, resources={r"/*/": {"origins": "http://localhost:3000"}})

#Error 404
def page_not_found(error):
    return '<h1>Error 404</h1>', 404 

if __name__ == "__main__":
    app.config.from_object(config['development'])
    # Registrar los blueprints
    app.register_blueprint(profesor_routes, url_prefix='/api/escuela')
    app.register_blueprint(cursos_blueprint, url_prefix='/api/escuela')
    app.register_blueprint(alumnos_blueprint, url_prefix='/api/escuela')
    app.register_blueprint(matriculas_blueprint, url_prefix='/api/escuela')

    #ERROR 404
    app.register_error_handler(404, page_not_found)
    app.run()

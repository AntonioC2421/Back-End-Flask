from database.db import get_connection
from .entities.Matriculas import Matricula

class MatriculaModel():
    @classmethod
    def get_matricula(self):
        try:
            connection = get_connection()
            listaMatricula = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, alumno_id, curso_id FROM matriculas')
                resultset = cursor.fetchall()

                for OneMatricula in resultset:
                    matricula = Matricula(OneMatricula[0], OneMatricula[1], OneMatricula[2])
                    listaMatricula.append(matricula.to_JSON())

            connection.close()
            return listaMatricula
        
        except Exception as ex:
            raise Exception(ex)
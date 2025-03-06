from database.db import get_connection
from .entities.Cursos import Curso

class CursosModel():
    @classmethod
    def get_cursos(self):

        try:

            connection = get_connection()
            listaCursos = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, id_profesor FROM cursos')
                resultset = cursor.fetchall()

                for OneCurso in resultset:
                    curso = Curso(OneCurso[0],OneCurso[1],OneCurso[2])
                    listaCursos.append(curso.to_JSON())

            connection.close()
            return listaCursos
        
        except Exception as ex:
            raise Exception(ex)
        
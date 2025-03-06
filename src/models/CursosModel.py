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
    
    @classmethod
    def get_curso(self, id):
        
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, id_profesor FROM cursos WHERE id = %s', (id,))
                resultset = cursor.fetchone()

                if resultset:
                    curso = Curso(resultset[0], resultset[1], resultset[2])
                    return curso.to_JSON()
                else:
                    return {"message":"No se encuentra registro del curso"}
        except Exception as ex:
            raise Exception(ex)
        
        finally:
            connection.close()

from database.db import get_connection
from .entities.Cursos import Curso

class CursosModel():
    @classmethod
    def get_cursos(self):
        try:
            connection = get_connection()
            listaCursos = []
            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, id_profesor FROM cursos ORDER BY id asc')
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

    @classmethod
    def add_curso(self,newCurso):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT EXISTS(SELECT 1 FROM cursos WHERE id = %s)", (newCurso.id,))
                id_exists = cursor.fetchone()[0]

                cursor.execute("SELECT EXISTS(SELECT 1 FROM profesores WHERE id = %s)", (newCurso.id_profesor,))
                profesor_exists = cursor.fetchone()[0]

                if id_exists:
                    raise ValueError(f"No se puede repetir Id principal: \n- Id no valido: {newCurso.id} ")

                if not profesor_exists:
                    raise ValueError(f"Profesor con ID {newCurso.id_profesor} no existe.")
                
                cursor.execute("INSERT INTO cursos(id, name, id_profesor) VALUES (%s,%s,%s)", (newCurso.id, newCurso.name,newCurso.id_profesor))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(f"Error al registrar la curso: {str(ex)}")

    @classmethod
    def update_curso(self, updatecurso):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE cursos SET id_profesor=%s, name=%s WHERE id=%s",(updatecurso.id_profesor,updatecurso.name,updatecurso.id))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_curso(self,deletecurso):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM cursos WHERE id=%s",(deletecurso.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)        

from database.db import get_connection
from .entities.Matriculas import Matricula

class MatriculaModel():
    @classmethod
    def get_matriculas(self):
        try:
            connection = get_connection()
            listaMatricula = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, alumno_id, curso_id FROM matriculas ORDER BY id ASC')
                resultset = cursor.fetchall()

                for OneMatricula in resultset:
                    matricula = Matricula(OneMatricula[0], OneMatricula[1], OneMatricula[2])
                    listaMatricula.append(matricula.to_JSON())

            connection.close()
            return listaMatricula
        
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_matricula(self,id):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, alumno_id, curso_id FROM matriculas WHERE id = %s", (id,))
                resultset = cursor.fetchone()

                if resultset:
                    matricula = Matricula(resultset[0], resultset[1], resultset[2])
                    return matricula.to_JSON()
                else:
                    return {"message": "No se encuentra registro de Matricula"}
                
        except Exception as ex:
            raise Exception(ex)
        
        finally:
            connection.close()    
    
    @classmethod
    def add_matricula(self, newmatricula):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                # Verificar si el ID existe
                cursor.execute("SELECT EXISTS(SELECT 1 FROM matriculas WHERE id = %s)", (newmatricula.id,))
                id_exists = cursor.fetchone()[0]

                # Verificar si el curso existe
                cursor.execute("SELECT EXISTS(SELECT 1 FROM cursos WHERE id = %s)", (newmatricula.curso_id,))
                curso_exists = cursor.fetchone()[0]

                # Verificar si el alumno existe
                cursor.execute("SELECT EXISTS(SELECT 1 FROM alumnos WHERE id = %s)", (newmatricula.alumno_id,))
                alumno_exists = cursor.fetchone()[0]

                # Validaciones antes del insert
                if id_exists:
                    raise ValueError(f"No se puede repetir Id principal: \n- Id no valido: {newmatricula.id} ")
                
                if not alumno_exists and not curso_exists:
                    raise ValueError(f"No existen registros con los IDs proporcionados:\n- Curso ID: {newmatricula.curso_id}\n- Alumno ID: {newmatricula.alumno_id}")

                if not curso_exists:
                    raise ValueError(f"Curso con ID {newmatricula.curso_id} no existe.")

                if not alumno_exists:
                    raise ValueError(f"Alumno con ID {newmatricula.alumno_id} no existe.")

                # Si ambos existen, insertar matrícula
                cursor.execute(
                    "INSERT INTO matriculas (id, curso_id, alumno_id) VALUES (%s, %s, %s)",
                    (newmatricula.id, newmatricula.curso_id, newmatricula.alumno_id)
                )

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except ValueError as ve:
            raise ve # Enviar el error para que el route lo maneje y pueda devolver un 404

        except Exception as ex:
            raise Exception(f"Error al registrar la matrícula: {str(ex)}")

        
    @classmethod
    def update_matricula(self,updatematricula):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE matriculas SET alumno_id=%s, curso_id=%s WHERE id=%s",(updatematricula.alumno_id, updatematricula.curso_id, updatematricula.id))

                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_matricula(self,deletematricula):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM matriculas WHERE id = %s", (deletematricula.id,))

                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)

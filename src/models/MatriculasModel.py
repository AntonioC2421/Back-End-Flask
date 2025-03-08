from database.db import get_connection
from .entities.Matriculas import Matricula

class MatriculaModel():
    @classmethod
    def get_matriculas(self):
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
    def add_matricula(self,newmatricula):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO matriculas (id, curso_id, alumno_id) VALUES (%s,%s,%s)", (newmatricula.id, newmatricula.curso_id, newmatricula.alumno_id))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)

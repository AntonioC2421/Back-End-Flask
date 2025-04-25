from database.db import get_connection
from .entities.Alumnos import Alumno

class AlumnoModel():
    @classmethod
    def get_alumnos(self):
        try:
            connection = get_connection()
            listaAlumnos = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, last_name, email FROM alumnos ORDER BY id asc')
                resultset = cursor.fetchall()

                if resultset:
                    for OneAlumno in resultset:
                        alumnos = Alumno(OneAlumno[0],OneAlumno[1],OneAlumno[2],OneAlumno[3])
                        listaAlumnos.append(alumnos.to_JSON())
                else:
                    return {"message":"No se encontraron registros de Alumnos"}
                
            connection.close()
            return listaAlumnos
        
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_OneAlumno(self, id):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, last_name, email FROM alumnos WHERE id = %s" , (id,))
                resultset = cursor.fetchone()

                if resultset:
                    alumno = Alumno(resultset[0], resultset[1], resultset[2], resultset[3])
                    return alumno.to_JSON()
                else:
                    return {"message":"No se encuentra registro de el alumno"}
                
        except Exception as ex:
            raise Exception(ex)
        
        finally:
            connection.close()

    @classmethod
    def add_alumno(self, newalumno):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO alumnos (id, name, last_name, email) VALUES(%s,%s,%s,%s)", (newalumno.id, newalumno.name, newalumno.last_name, newalumno.email))

                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_alumno(self, updatealumno):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE alumnos SET name=%s, last_name=%s, email=%s WHERE id = %s",(updatealumno.name, updatealumno.last_name, updatealumno.email, updatealumno.id))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_alumno(self, deletealumno):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM alumnos WHERE id=%s",(deletealumno.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)
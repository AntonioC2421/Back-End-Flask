from database.db import get_connection
from .entities.Alumnos import Alumno

class AlumnoModel():
    @classmethod
    def get_alumnos(self):
        try:
            connection = get_connection()
            listaAlumnos = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, last_name, email FROM alumnos')
                resultset = cursor.fetchall()

                for OneAlumno in resultset:
                    alumnos = Alumno(OneAlumno[0],OneAlumno[1],OneAlumno[2],OneAlumno[3])
                    listaAlumnos.append(alumnos.to_JSON())
            connection.close()
            return listaAlumnos
        
        except Exception as ex:
            raise Exception(ex)

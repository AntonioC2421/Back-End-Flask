from database.db import get_connection
from .entities.Profesores import Profesor

class ProfesoresModel():
    @classmethod
    def get_profesores(self):
        try:
            connection = get_connection()
            listProfe = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, last_name, email FROM profesores')
                resultset = cursor.fetchall()

                for row in resultset:
                    profe = Profesor(row[0],row[1],row[2],row[3])
                    listProfe.append(profe.to_JSON())

            connection.close()
            return listProfe

        except Exception as ex: 
            raise Exception(ex)
        
    @classmethod
    def get_profe(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, last_name, email FROM profesores WHERE id = %s", (id,))

                row = cursor.fetchone() #fetchone() -> para un solo resultado

                if row is not None:
                    profe = Profesor(row[0], row[1], row[2], row[3])
                    profe = profe.to_JSON()
                else:
                    profe = None 

            connection.close()
            return profe
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_profes(self, newprofe):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO profesores (id,name,last_name,email) VALUES(%s,%s,%s,%s)""",(newprofe.id,newprofe.name,newprofe.last_name, newprofe.email))
                
                #Ver cuantas filas fueron afectadas
                affected_rows=cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_profes(self, deleteprofe):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM profesores WHERE id = %s", (deleteprofe.id,))
                
                #Ver cuantas filas fueron afectadas
                affected_rows=cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_profes(self, updateprofe):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE profesores SET name=%s, last_name=%s, email=%s WHERE id = %s", (updateprofe.name,updateprofe.last_name,updateprofe.email,updateprofe.id))
                
                #Ver cuantas filas fueron afectadas
                affected_rows=cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)
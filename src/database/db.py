import psycopg2 #Sirver para la conexion a la db
from psycopg2 import DatabaseError #control de errores
from decouple import config

def get_connection():
    try:
        return psycopg2.connect( 
            #Valores traidos desde <.env>
            host = config('PGSQL_HOST'),
            user = config('PGSQL_USER'),
            password = config('PGSQL_PASSWORD'),
            database = config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex
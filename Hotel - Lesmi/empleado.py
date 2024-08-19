import mysql.connector
from db_config import configure_database

class Empleado:
    @staticmethod
    def crear_empleado(nombre, apellidos, email, password):
        try:
            conn = configure_database()
            cursor = conn.cursor()
            query = "INSERT INTO empleado (nombre, apellidos, email, password) VALUES (%s, %s, %s, %s)"
            values = (nombre, apellidos, email, password)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    @staticmethod
    def iniciar_sesion(email, password):
        try:
            conn = configure_database()
            cursor = conn.cursor()
            query = "SELECT id, nombre, apellidos FROM empleado WHERE email = %s AND password = %s"
            values = (email, password)
            cursor.execute(query, values)
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

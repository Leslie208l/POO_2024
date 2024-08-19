import mysql.connector
from db_config import configure_database

class Reserva:
    @staticmethod
    def registrar_cliente(nombre, apellidos, email, telefono):
        try:
            conn = configure_database()
            cursor = conn.cursor()
            query = "INSERT INTO cliente (nombre, apellidos, email, telefono) VALUES (%s, %s, %s, %s)"
            values = (nombre, apellidos, email, telefono)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    @staticmethod
    def crear_reserva(cliente_id, fecha_llegada, fecha_salida, habitacion, empleado_id):
        try:
            conn = configure_database()
            cursor = conn.cursor()
            query = "INSERT INTO reserva (cliente_id, fecha_llegada, fecha_salida, habitacion, empleado_id) VALUES (%s, %s, %s, %s, %s)"
            values = (cliente_id, fecha_llegada, fecha_salida, habitacion, empleado_id)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

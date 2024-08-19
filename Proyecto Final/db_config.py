import mysql.connector

def configure_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Cambia esto si tienes una contraseña
        database="hotel"
    )

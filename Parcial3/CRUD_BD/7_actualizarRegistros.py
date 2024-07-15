try:
    #Conectarse con la BD MySql
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
    )

except Exception as e:
    print(f"Error: (e)")
    print(f"Tipo de error: {type(e)._name_}")
    print(f"Ocuerrio un problema con el servidor por favor intentalo mas tarde")
else:
    print(f"Se creo la concexion con la BD exitosamente")
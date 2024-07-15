import mysql.connector

try:
    #Crear concexion con la BD
 conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
 )

 #Verificar la conexion
 if conexion.is_connected():
    print("Se crear la conexicon con exito")
 else:
    print("No fue posible conectarse")

 #Crear otro objeto par aejecutar la instrucciones
 micursor=conexion.cursor()

 #Crear la BD desde Python
 sql="create database bd_python"
 micursor.execute(sql)

 #verificar que se creo la BD
 if micursor:
    print("Se creo la BD exitosamente")

 #Mostrar la BD que existen en mi servidor de MYSQL
 micursor.execute("show databases")

 for x in micursor:
    print(x)

except:
   print(f"Ocuerrio un problema con el servidor por favor intentalo mas tarde")



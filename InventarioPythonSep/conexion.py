# Este archivo usa el connector de Python de MySQL.
# Para instalarlo, escribe en la consola "pip install mysql-connector-python".
import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',password='Flopypeluchito20046.',
            host='127.0.0.1',database='proto_inventario_db',port='3306')
            print("Conexión completada con exito")
            
            return conexion

        except mysql.connector.Error as error:
            print("Error de conexión con la base de datos {}".format(error))

            # return conexion
    ConexionBaseDeDatos()
from conexion import *

class CProductos:

    def mostrarProductos():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from `inventario principal`;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error al mostrar los datos: Error {}".format(error))



    def añadirEntradas(Id,Nombre,Cantidad,Fecha,Comentarios):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into `entradas` values(null,%s,%s,%s,%s,%s);"
            valores = (Id,Nombre,Cantidad,Fecha,Comentarios)
            cursor.execute(sql,valores)

            cone.commit()
            sql = "update `inventario principal` set `Entradas` = `Entradas` + %s, `Fecha de modificación` = %s WHERE (`ID producto` = %s);"
            valores = (Cantidad,Fecha,Id)
            cursor.execute(sql,valores)

            cone.commit()
            print(cursor.rowcount,"Entrada ingresada correctamente")
            cone.close()

        except ValueError as error:
            print("Error de comunicación: Error {}".format(error))
    


    def añadirSalidas(Id,Nombre,Cantidad,Fecha,Comentarios):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into `salidas` values(null,%s,%s,%s,%s,%s);"
            valores = (Id,Nombre,Cantidad,Fecha,Comentarios)
            cursor.execute(sql,valores)

            cone.commit()
            sql = "update `inventario principal` set `Salidas` = `Salidas` + %s,`Fecha de modificación` = %s WHERE (`ID producto` = %s);"
            valores = (Cantidad,Fecha,Id)
            cursor.execute(sql,valores)

            cone.commit()
            print(cursor.rowcount,"Salida ingresada correctamente")
            cone.close()

        except ValueError as error:
            print("Error de comunicación: Error {}".format(error))

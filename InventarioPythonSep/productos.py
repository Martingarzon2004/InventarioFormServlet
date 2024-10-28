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


    def ingresarProductos(Categorias,Ubicación,Nombre,ValorCompra,Iva,Cantidad,CantidadMinima,Fecha,Comentarios):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into `inventario principal` values(null,%s,%s,%s,%s,%s,%s,0,default,%s,default,%s,null,%s);"
            valores = (Categorias,Ubicación,Nombre,ValorCompra,Iva,Cantidad,CantidadMinima,Fecha,Comentarios)
            cursor.execute(sql,valores)

            cone.commit()
            print(cursor.rowcount,"Registro ingresado correctamente")
            cone.close()

        except ValueError as error:
            print("Error de comunicación: Error {}".format(error))
    

    def modificarProductos(Id,Categorias,Ubicación,Nombre,ValorCompra,Iva,CantidadMinima,Fecha,Comentarios):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "update `inventario principal` set `Categoria` = %s,`Ubicación` = %s,`Producto` = %s,`Valor compra` = %s,`Iva`= %s,`Cantidad minima` =%s,`Fecha de modificación`= %s,`Comentarios` = %s WHERE (`ID producto` = %s);"
            valores = (Categorias,Ubicación,Nombre,ValorCompra,Iva,CantidadMinima,Fecha,Comentarios,Id)
            cursor.execute(sql,valores)

            cone.commit()
            print(cursor.rowcount,"Registro modificado correctamente")
            cone.close()

        except ValueError as error:
            print("Error de comunicación: Error {}".format(error))
    

    def eliminarProductos(Id):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "delete from `inventario principal` WHERE (`ID producto` = %s);"
            valores = (Id,)
            cursor.execute(sql,valores)

            cone.commit()
            print(cursor.rowcount,"Registro eliminado correctamente")
            cone.close()

        except ValueError as error:
            print("Error de comunicación: Error {}".format(error))
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


    def ingresarProductos(Categorias,Ubicación,Nombre,ValorCompra,Iva,CantidadMinima,Fecha,Comentarios):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into `inventario principal` values(null,%s,%s,%s,%s,%s,0,0,default,%s,default,%s,null,%s,default);"
            valores = (Categorias,Ubicación,Nombre,ValorCompra,Iva,CantidadMinima,Fecha,Comentarios)
            print(Categorias)
            print(Ubicación)
            print(Nombre)
            print(ValorCompra)
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
            sql = "insert into `papelera de reciclaje` (`ID producto`,`Categoria`,`Ubicación`,`Producto`,`Valor compra`,`Iva`,`Entradas`,`Salidas`,`Cantidad minima`,`Fecha de inclución`,`Fecha de modificación`,`Comentarios`) select `ID producto`,`Categoria`,`Ubicación`,`Producto`,`Valor compra`,`Iva`,`Entradas`,`Salidas`,`Cantidad minima`,`Fecha de inclución`,`Fecha de modificación`,`Comentarios` from `inventario principal` where (`ID producto` = %s);"
            valores = (Id,)
            cursor.execute(sql,valores)

            cone.commit()
            sql = "delete from `inventario principal` WHERE (`ID producto` = %s);"
            cursor.execute(sql,valores)

            cone.commit()
            print(cursor.rowcount,"Registro eliminado correctamente")
            cone.close()

        except ValueError as error:
            print("Error de comunicación: Error {}".format(error))


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


    def mostrarPapelera():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from `papelera de reciclaje`;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error al mostrar los datos: Error {}".format(error))
    
    def sacarPapelera(Id):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into `inventario principal` (`ID producto`,`Categoria`,`Ubicación`,`Producto`,`Valor compra`,`Iva`,`Entradas`,`Salidas`,`Cantidad minima`,`Fecha de inclución`,`Fecha de modificación`,`Comentarios`) select `ID producto`,`Categoria`,`Ubicación`,`Producto`,`Valor compra`,`Iva`,`Entradas`,`Salidas`,`Cantidad minima`,`Fecha de inclución`,`Fecha de modificación`,`Comentarios` from `papelera de reciclaje` where (`ID producto` = %s);"
            valores = (Id,)
            cursor.execute(sql,valores)

            cone.commit()
            sql = "delete from `papelera de reciclaje` WHERE (`ID producto` = %s);"
            cursor.execute(sql,valores)

            cone.commit()
            print(cursor.rowcount,"Registro eliminado correctamente")
            cone.close()

        except ValueError as error:
            print("Error de comunicación: Error {}".format(error))

    
    def mostrarHistorialEntradas():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from `entradas`;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error al mostrar los datos: Error {}".format(error))

    def mostrarHistorialSalidas():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from `salidas`;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error al mostrar los datos: Error {}".format(error))
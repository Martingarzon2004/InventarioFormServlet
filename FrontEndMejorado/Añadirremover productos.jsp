<%-- 
    Document   : Añadirremover productos
    Created on : 25/08/2023, 12:26:35 p. m.
    Author     : Compac CQ40
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="es-CO">
    <head>
        <title>A&ntilde;adir y Remover productos</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="styles 3A_1.css">
    </head>
    <body>
        <header>
            <section id="title">
                <h2>Añadir/remover productos</h2>
            </section> 
        </header>
        <main>
            <ul>
                <li>
                    <h3><a href="Menú principal_1.html" id="salida">Salir del módulo</a></h3>
                </li>
                <li>
                    <h3><button type="submit" id="anadir">Añadir nuevos productos</button></h3>
                </li>
                <li>
                    <h3><button type="button" id="borrar">Borrar productos</button></h3>
                </li>
                <li>
                    <h3><button type="submit" id="guardar">Guardar datos de la pre-factura</button></h3>
                </li>
            </ul>
            <section id="ingreso">
                <%=new String("Ingreso de productos").toUpperCase()%>
                <form accion="AddRemove" method="POST">
                    <h4>
                        <label for="nombre">Nombre del producto...</label><input type="text" name="nombre" id="nombre">
                        <br><br>
                        <label for="cantidad">Cantidad...</label><input type="number" name="cantidad" id="cantidad">
                        <br><br>
                        <label for="precio">Precio...</label><input type="number" name="precio" id="precio">
                        <br><br>
                        <label for="iva">IVA...</label><input type="number" name="iva" id="iva">
                        <br><br>
                        <label for="categoria">Categoria...</label><input type="text" name="categoria" id="categoria">
                        <br><br>
                        <label for="lugar">Lugar...</label><input type="text" name="lugar" id="lugar">
                        <br><br>
                        <input type="submit" value="enviar" id="enviar">
                    </h4>
                </form>
            </section>
            <section id="seleccion">
                <%=new String("Selección de productos").toUpperCase()%>
                <table>
                    <tr>
                        <th><h4>ID</h4></th>
                        <th><h4>Nombre</h4></th>
                        <th><h4>Categoria</h4></th>
                        <th><h4>Lugar</h4></th>
                        <th><h4>Cantidad</h4></th>
                        <th><h4>Precio</h4></th>
                        <th><h4>IVA</h4></th>
                    </tr>
                    <tr>
                        <td><p>10101010</p></td>
                        <td><p>Aromáticas</p></td>
                        <td><p>Cafeteria</p></td>
                        <td><p>Caja 1.1</p></td>
                        <td><p>12</p></td>
                        <td><p>3000</p></td>
                        <td><p>N/A</p></td>
                    </tr>
                </table>
            </section>
            <section id="pre-factura">
                <%=new String("Pre-factura").toUpperCase()%>
                <table>
                    <tr>
                        <th><h4>ID</h4></th>
                        <th><h4>Nombre</h4></th>
                        <th><h4>Categoria</h4></th>
                        <th><h4>Lugar</h4></th>
                        <th><h4>Cantidad</h4></th>
                        <th><h4>Precio</h4></th>
                        <th><h4>IVA</h4></th>
                    </tr>
                    <tr>
                        <td><p>10101010</p></td>
                        <td><p>Aromáticas</p></td>
                        <td><p>Cafeteria</p></td>
                        <td><p>Caja 1.1</p></td>
                        <td><p>12</p></td>
                        <td><p>3000</p></td>
                        <td><p>N/A</p></td>
                    </tr>
                </table>
            </section>
        </main>
        <footer>
        </footer>
    </body>
</html>


/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package conexionjdbc;

/**
 *
 * @author Compac CQ40
 */
import java.sql.*;
import java.util.logging.Level;
import java.util.logging.Logger;
public class ConexionJDBC {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        String usuario = "root";
        String password = "Flopypeluchito20046.";
        String url = "jdbc:mysql://localhost:3306/Inventario";
        Connection conexion;
        Statement statement;
        ResultSet rs;
        
        try {
            // TODO code application logic here
            Class.forName("com.mysql.cj.jdbc.Driver");
            
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(ConexionJDBC.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        try {
            conexion = DriverManager.getConnection(url,usuario,password);
            statement = conexion.createStatement();
            statement.executeUpdate("INSERT INTO LISTADEPRODUCTOS(NOMBRE,CANTIDAD,TIPODEPRODUCTO,LOCALIZACION,PRECIODEVENTA) VALUES('PAPELES','10','PAPELERIA','1.1','20000')");
            rs = statement.executeQuery("SELECT * FROM LISTADEPRODUCTOS");
            rs.next();
            do{
                System.out.println(rs.getInt("ID")+" : "+rs.getString("NOMBRE"));
            }while(rs.next());
            
        } catch (SQLException ex) {
            Logger.getLogger(ConexionJDBC.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
}

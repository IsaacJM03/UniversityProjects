package JDBCWork;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class JDBCWork {

  private static Connection connection;

  /**
   * The main method that starts the server and handles client connections.
   *
   * @param  args    the command-line arguments passed to the program
   * @throws ClassNotFoundException if the JDBC driver class is not found
   */
  public static void main(String[] args) throws ClassNotFoundException {
      String dbHost = "localhost";
      String dbPort = "3306";
      String dbName = "test";
      String dbUser = "root";
      String dbPass = "root";

      try {
          Class.forName("com.mysql.cj.jdbc.Driver");
          connection = DriverManager.getConnection("jdbc:mysql://"+dbHost+":"+dbPort+"/"+dbName, dbUser, dbPass);
          register("john", "w0YnR@example.com");
      } catch (SQLException e) {
          e.printStackTrace();
      }
  }

  private static void register(String username, String email) {

        try {
            String query = "INSERT INTO users (username,email) VALUES (?, ?)";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, username);
            statement.setString(2, email);

            statement.executeUpdate();
            
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

}

package ExceptionsPractice;

import java.io.*;

class InvalidAgeException extends Exception {
  public InvalidAgeException(String message){
    super(message);
  }
}
public class Example {
  public static void checkAge(int age) throws InvalidAgeException {
    if (age < 18 ){
      throw new InvalidAgeException("Too young");
    } else {
      System.out.println("Access granted");
    }
  }

  public static void main(String[] args) {
    try (BufferedReader reader = new BufferedReader(new FileReader("example.txt"))){
      String line = reader.readLine();
      System.out.println(line);
      checkAge(16);
    } catch (InvalidAgeException | IOException e) {
      e.printStackTrace();
    }
    // finally { // no need for this if using try-with-resources, they are automatically closed
    //   System.out.println("This is our system");
    // }
  }
}

// scanner vlass used to capture input at runtime

// nextDouble() - captures double values
// nextFloat() - captures float values
// nextLine() - captures the whole line of text up to when ...

import java.util.*;

public class Book2 {

  public String Title;
  public double Price;
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);

    Book2 bk2 = new Book2();

    System.out.println("Enter Book Title: ");
    bk2.Title = s.nextLine();

    System.out.println("Enter Book Price: ");
    bk2.Price = s.nextDouble();
    System.out.println("Title is: "+bk2.Title+" and Price is: "+bk2.Price+" shs.");

    s.close();
  }

}

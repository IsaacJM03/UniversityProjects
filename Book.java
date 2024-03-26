public class Book {
  public String Title;
  public double Price;
  final double cons = 35.7;

  Book() {
    //TODO Auto-generated constructor stub
    System.out.println("the book has been registered");
  }

  Book(String t,double P)
  {
    this.Title = t;
    this.Price = P;
    System.out.println("Book title is: "+t+" and the price is: "+P);
  }

  public static void main(String args[])
  {
      Book lesson = new Book("One", 300);
      Book lesson2 = new Book(); //no-arg constructor
      // lesson2.Price = 300;
      // System.out.println(lesson2.Price);
      // System.out.println(lesson.Price);
      // System.out.println(lesson.Title);
      // System.out.print("Wagwan"); // doesnt move to next line
      // System.out.println("yep");
      
  }
}

/**
 * InnerBook
 */
class InnerBook extends Book {

  public static void main(String[] args) {
    System.out.println(cons);
  }
}
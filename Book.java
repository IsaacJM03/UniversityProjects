public class Book {
  public String Title;
  public double Price;

  Book(String t,double P)
  {
    this.Title = t;
    this.Price = P;
  }

  Book() {
    //TODO Auto-generated constructor stub
  }

  public static void main(String args[])
  {
      Book lesson = new Book("One", 300);
      Book lesson2 = new Book(); //no-arg constructor
      lesson2.Price = 300;
      System.out.println(lesson2.Price);
      System.out.println(lesson.Price);
      System.out.println(lesson.Title);
      System.out.print("Wagwan"); // doesnt move to next line
      System.out.println("yep");
      
  }
}
public class lesson5_2 extends lesson5_1 {

  // method overriding
  void eat()
  {
    System.out.println("I am eating bread...");
  }

  public static void main(String[] args) {
    System.out.println("Hello World!");
    lesson5_2 myInstance = new lesson5_2();
    myInstance.eat();
  }
}

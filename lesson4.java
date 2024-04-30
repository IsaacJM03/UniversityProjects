public class lesson4 {

  private String method1() {
    return "method 1";
  }
  public static String method2() {
    return "method 2";
  }

  protected String method3() {
    return "method 3";
  }
  public static void main(String[] args) {
    System.out.println("Hello World!");
  }
}

class Innerlesson4 {
  public static void main(String[] args) {
    System.out.println("Hello World!");
    // Creating an instance of the lesson4 class
    lesson4 myLesson = new lesson4();

    // Accessing public method (method2) directly
    String result2 = myLesson.method2();
    System.out.println(result2);

    // Accessing protected method (method3) directly
    String result3 = myLesson.method3();
    System.out.println(result3);

    // Private method (method1) is not accessible from this class
    // You will get a compilation error if you uncomment the line below
    // String result1 = myLesson.method1();
  } 
  
}

public class lesson4_1 extends lesson4 {
  public static void main(String[] args) {
    System.out.println("Hello World!");
    lesson4_1 myInstance = new lesson4_1();

    // Accessing public method (method2) directly
    String result2 = myInstance.method2();
    System.out.println(result2);

    // Accessing protected method (method3) from the inherited class
    String result3 = myInstance.method3();
    System.out.println(result3);

    // private method is not accessible from this class
    // String result1 = myInstance.method1(); 
  }
  
}

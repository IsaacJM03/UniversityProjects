// Define the interface
interface MyInterface {
  // Static method
  static void staticMethod() {
      System.out.println("This is a static method in the interface.");
  }

  // Abstract method
  void abstractMethod();
}

// Class implementing the interface
class MyClass1 implements MyInterface {
  // Implement the abstract method
  public void abstractMethod() {
      System.out.println("Implementation of abstractMethod() in MyClass1");
  }

  // Main method
  public static void main(String[] args) {
      // Call static method of the interface
      MyInterface.staticMethod();
      
      // Create an object of MyClass1
      MyClass1 obj = new MyClass1();
      // Call abstract method of the interface
      obj.abstractMethod();
  }
}

// Another class implementing the interface
public class MyClass2 implements MyInterface {
  // Implement the abstract method
  public void abstractMethod() {
      System.out.println("Implementation of abstractMethod() in MyClass2");
  }

  // Main method
  public static void main(String[] args) {
      // Call static method of the interface
      MyInterface.staticMethod();
      
      // Create an object of MyClass2
      MyClass2 obj = new MyClass2();
      // Call abstract method of the interface
      obj.abstractMethod();
  }
}

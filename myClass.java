// public class myClass {
//   static int staticVar; // Static variable
//   int instanceVar; // Instance variable

//   static void staticMethod() {
//       staticVar = 10; // OK: Accessing static variable
//       // instanceVar = 20; // Error: Cannot access instance variable directly
//       // instanceMethod(); // Error: Cannot access instance method directly
//   }

//   void instanceMethod() {
//       staticVar = 30; // OK: Static variables can be accessed from instance methods
//       instanceVar = 40; // OK: Accessing instance variable
//   }

// }
interface MyInterface {
  // Private method in interface
  private void privateMethod() {
      System.out.println("Private method in interface");
  }

  // Static method in interface
  static void staticMethod() {
      // privateMethod(); // Error: Cannot access private method
      System.out.println("Static method in interface");
  }
}

public class myClass implements MyInterface {
  // Implementing the interface but cannot access privateMethod()

  // In Java, static methods in interfaces are not inherited by implementing classes. Therefore, when you define a static method with the same name in the implementing class, it doesn't override the static method from the interface; rather, it is considered a separate static method in the class.

  public static void staticMethod() {
      System.out.println("Private method in class");
  }
  public static void main(String[] args) {
      // MyInterface[] b = new MyInterface[3];
      // b[1] = 2;
      // Can call static method directly
      myClass test = new myClass();
      test.staticMethod();
      // MyInterface.privateMethod();
  }
}

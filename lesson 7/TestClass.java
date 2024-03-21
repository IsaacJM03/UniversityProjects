interface interfaceTest1 {
  // public, static and final
  final int a = 10;
  int age = 90;
  
  // public and abstract
  void display();
}


interface interfaceTest2 {

  int age = 45;
  void enter();

  // void display(String word);
  // This will fail because - The type TestClass must implement the inherited abstract method interfaceTest2.display(String)
}

// A class that implements the interface.
public class TestClass extends CalcPayment implements interfaceTest1, interfaceTest2 {
   
  // Implementing the capabilities of
  // interface.
  public void display(){ 
    System.out.println("Geek"); 
  }

  public void enter(){
    System.out.println("Enter");
  }

  // Driver Code
  public static void main(String[] args)
  {
      TestClass t = new TestClass();
      t.display();
      t.enter();
      System.out.println(a);
      // System.out.println(age); //The field age is ambiguous

  }
}
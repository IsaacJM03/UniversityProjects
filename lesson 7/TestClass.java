interface interfaceTest1 {
  // public, static and final
  final int a = 10;
  
  // public and abstract
  void display();
}


interface interfaceTest2 {

  void enter();
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
  }
}
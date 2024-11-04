package InnerClasses;

// method local inner class
public class OuterClass {
  public void displayMessage() {
    class InnerClass {
      public void print() {
        System.out.println("hi from print");
      }
    }

    InnerClass inner = new InnerClass();
    inner.print();
  }
  
  public static void main(String[] args) {
    OuterClass outer = new OuterClass();
    // InnerClass inner = new InnerClass(); //unaccessible here
    outer.displayMessage();
  }
}
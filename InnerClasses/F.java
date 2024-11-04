package InnerClasses;

class E {
  void show() {
    System.out.println("I am in E");
  }
}

public class F {

  static E e = new E() {
    void show()
    {
      super.show();
      System.out.println("I am in F");
    }
  };

  public static void main(String[] args) {
    e.show();
    // int a = 20;
    // int b = 10;
    
    // if ((a/b)==10){
    //   System.out.println("This is okay");
    // } else {
    //   throw new ArithmeticException();
    // }
  }
}
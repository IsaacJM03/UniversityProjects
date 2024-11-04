package InnerClasses;

class A { // cannot make outer class static, only public, abstract and final allowed
  int age;

  public void show()
  {
    System.out.println("in show");
  }

  static class B {
    public void config()
    {
      System.out.println("in config");
    }
  }
}

public class Demo {
  public static void main(String[] args) {
    A obj = new A();
    obj.show();

    // A.B obj1 = obj.new B(); // since it is non-static at the moment, we need object of A(outer class) to create an object of B(inner class)
    A.B obj1 = new A.B(); //since class B is static
    obj1.config();
  }
}
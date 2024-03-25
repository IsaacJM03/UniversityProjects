public class A {
  A()
  {
    System.out.println("A Exists");
  }

  A(String name)
  {
    System.out.println(name + " Exists");
  }

  public static void main(String[] args) {
    A a = new A();
    A a2 = new A("Hello");
  }
}

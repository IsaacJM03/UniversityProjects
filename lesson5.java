public class lesson5 {

  public String name;
  public int age;

  lesson5(String name, int age)
  {
    this.name = name;
    this.age = age;
  }
  static int add(int a, int b)
  {
    return a+b;
  }

  // method overloading
  static int add(int a, int b, int c)
  {
    return a+b+c;
  }
  
  public static void main(String[] args) {
    System.out.println("Hello World!");
    System.out.println(add(1,2));
    System.out.println(add(1,2,3));
  }
}
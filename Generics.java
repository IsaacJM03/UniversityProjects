class Printer<T> {
  T printed;
  public Printer(T printed) {
    this.printed = printed;
  }
  public void print() {
    // T.method2();
    System.out.println(printed);
  }
  
}

// int, long, double and other primitives do not work with generics.
public class Generics {

  private static <T,V> void shout(T thingToShout,V otherThing) {
    System.out.println(thingToShout + "!!!!");
    System.out.println(otherThing + "!!!!");
  }
  public static void main(String[] args) {
    shout(3.14535344235355646464766474735353535345345345345353f,"Yooo");
    shout("Test",1);

    // Printer<String> stringPrinter = new Printer<>("Test");
    // stringPrinter.print();
    // Printer<Float> floatPrinter = new Printer<>(3.14535344235355646464766474735353535345345345345353f); // rounds off since it is a float
    // floatPrinter.print();

  }
}
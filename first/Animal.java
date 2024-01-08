package first;

public class Animal {
  String name;
  String colour;
  int legs;
  static int numberOfEars = 2;

  public static void main(String[] args) {
    Animal dog = new Animal();
    dog.printAtrributes("Scooby", "Black", 4);
    Animal cat = new Animal();
    cat.printAtrributes("Tom", "Brown", 4);
    Animal person = new Animal();
    person.printAtrributes("Malcolm", "Light-skinned",2);
  }

  public void printAtrributes(String name, String colour, int legs) {
    this.name = name;
    this.colour = colour;
    this.legs = legs;
    // this.numberOfEars = numberOfEars;
    System.out.println("Name is "+ this.name + "\nColour is: "+ this.colour + "\nLegs are: "+ this.legs + "\nNumber of ears are: "+ numberOfEars + "\n");
  }
}

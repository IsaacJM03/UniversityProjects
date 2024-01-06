package first;

public class Animal {
  String name;
  String colour;
  int legs;
  int numberOfEars;

  public static void main(String[] args) {
    Animal dog = new Animal();
    dog.printAtrributes("Scooby", "Black", 4, 2);
    Animal cat = new Animal();
    cat.printAtrributes("Tom", "Brown", 4, 2);
    Animal person = new Animal();
    person.printAtrributes("Malcolm", "Light-skinned",4, 2);
  }

  public void printAtrributes(String name, String colour, int legs, int numberOfEars) {
    this.name = name;
    this.colour = colour;
    this.legs = legs;
    this.numberOfEars = numberOfEars;
    System.out.println("Name is "+ this.name + "\nColour is: "+ this.colour + "\nLegs are: "+ this.legs + "\nNumber of ears are: "+ this.numberOfEars + "\n");
  }
}

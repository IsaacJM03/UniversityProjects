// class Animal {
//   void makeSound() {
//       System.out.println("Generic animal sound");
//   }
// }

// class Dog extends Animal {
//   void makeSound() {
//       System.out.println("Bark");
//   }
// }

// public class Test {
//   public static void main(String[] args) {
//       Animal genericAnimal = new Animal();
//       Dog dog = new Dog();

//       genericAnimal.makeSound();  // Output: Generic animal sound
//       dog.makeSound();           // Output: Bark
//   }
// }
interface A {
  void mA();
}
interface B {
  void mB();
  default void mC(){
    System.out.println("Wagwan");
  } 
}
interface D {} // tagging interface, use: Adds a data type to a class − This situation is where the term, tagging comes from. A class that implements a tagging interface does not need to define any methods (since the interface does not have any), but the class becomes an interface type through polymorphism.
interface C extends A,B,D{
  default void mA(){
    System.out.println("Hello");
  };
}
class E {

  void mE(){
    System.out.println("Hello E");
  }
  int x = 5;
}
public class Test extends E implements C{

  public void mA(){
    System.out.println("Hello World");
  }

  public void mB(){
    System.out.println("Hello B");
  }

  public static void main(String[] args) {
    B t = new Test();
    t.mC(); // interesting
    E e[] = new E[3]; // no errors because an abstract class can be used as a reference data type to create references
    E e1 = new E();
    boolean ans = t instanceof C; //true but why? Test inherits and extends all these
    System.out.println(++e1.x);
    System.out.println(ans);
  }
}
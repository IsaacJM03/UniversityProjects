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
}
interface D {} // tagging interface, use: Adds a data type to a class − This situation is where the term, tagging comes from. A class that implements a tagging interface does not need to define any methods (since the interface does not have any), but the class becomes an interface type through polymorphism.
interface C extends A,B,D{
  default void mA(){
    System.out.println("Hello");
  };
}
public class Test implements C{

  public void mA(){
    System.out.println("Hello World");
  }

  public void mB(){
    System.out.println("Hello B");
  }

  public static void main(String[] args) {
    Test t = new Test();
    t.mA();
  }
}
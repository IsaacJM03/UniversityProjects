class Animal {
  void makeSound() {
      System.out.println("Generic animal sound");
  }
}

class Dog extends Animal {
  void makeSound() {
      System.out.println("Bark");
  }
}

public class Test {
  public static void main(String[] args) {
      Animal genericAnimal = new Animal();
      Dog dog = new Dog();

      genericAnimal.makeSound();  // Output: Generic animal sound
      dog.makeSound();           // Output: Bark
  }
}

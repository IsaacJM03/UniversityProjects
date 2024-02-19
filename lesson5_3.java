// Java Program to implement
// Method Overriding

/*
 * Note: Static methods belong to the class rather than an instance of the class. They are associated with the class itself and not with the instances of the class.
 * Note: final methods cannot be overriden.
 */
import java.io.*;

// Base Class
class Animal {
	static void eat()
	{
		System.out.println("eat() method of base class");
		System.out.println("eating.");
	}
  final void talk()
  {
    System.out.println("talk() method of base class");
    System.out.println("talking.");
  }
}

// Inherited Class
class Dog extends Animal {
  // This is not considered an override; it's a separate static method(polymorphism).
	static void eat()
	{
		System.out.println("eat() method of derived class");
		System.out.println("Dog is eating.");
	}

  void talk()
  {
    System.out.println("talk() method of derived class");
    System.out.println("Dog is talking.");
  }
}

class MethodOverridingEx {
	// Main Function
	public static void main(String args[])
	{
		Dog d1 = new Dog();
		Animal a1 = new Animal();

		d1.eat();
		a1.eat();

    d1.talk();
    a1.talk();

		Animal animal = new Dog();
		// eat() method of animal class is overridden by
		// base class eat()
		animal.eat();
    animal.talk();
	}
}

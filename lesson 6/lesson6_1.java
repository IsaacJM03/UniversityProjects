
abstract class Animalia {
  public abstract void talk();// abstract methods DO NOT specify a body

  public void walk()
  {
    System.out.println("Walking");
  }

  public static void main(String[] args) {
    System.out.println("Hello World!");
  }
}

class Cat extends Animalia{
  public void talk()
  {
    System.out.println("Talking");
  }
}

abstract class Dog extends Animalia{
  public void talk()
  {
    System.out.println("Barking");
  }

  public abstract void walk();
  
}

class AnimaliaImplementation {
  public static void main(String[] args) {
    Cat c1 = new Cat();
    c1.talk();
    c1.walk();

    Dog d1 = new Dog();
    d1.talk();
  }
}
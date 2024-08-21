package Immutability;

// A strongly immutable object is one that cannot be modified after creation, and none of its fields can reference mutable objects.

public class StrongImmutableExample {
  public static void main(String[] args) {
    StrongImmutable person = new StrongImmutable("John", 30);
    System.out.println(person.getName());
    System.out.println(person.getAge());
  }
}
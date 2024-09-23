class Person{
  private String name;
  private int age;
  public String getName(){
    return name;
  }
  public int getAge(){
    return age;
  }
}
public class Student extends Person{
  public int x = 10;
  public static void main(String[] args) {
    // Student s = new Person(); //fails
    Student s = (Student)new Person(); //passes
    Person p = new Student(); // implicit casting
    System.out.println(s.x); //p.x fails
    System.out.println(p.getName());
    System.out.println(p.getAge());
  }
}

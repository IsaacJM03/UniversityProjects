import java.io.*;

class Employee implements Serializable {
  transient int a;
  static int b;
  String name;
  int age;

  public Employee(int a, int b, String name, int age) {
    this.a = a;
    this.b = b;
    this.name = name;
    this.age = age;
  }
}

public class SerialExample {

  public static void printdata(Employee emp1) {
    System.out.println(emp1.a + " " + emp1.b + " " + emp1.name + " " + emp1.age);
  }
  public static void main(String[] args) throws IOException, ClassNotFoundException {
    Employee emp1 = new Employee(10, 20, "John", 30);
    String filename = "emp.txt";

    // save object in file
    FileOutputStream fos = new FileOutputStream(filename);
    ObjectOutputStream oos = new ObjectOutputStream(fos);

    // serialization
    oos.writeObject(emp1);
    oos.close();
    fos.close();
    
    emp1.b = 2000; //changing value of static variable


    // deserialization
    FileInputStream fis = new FileInputStream(filename);
    ObjectInputStream ois = new ObjectInputStream(fis);
    Employee emp2 = (Employee) ois.readObject();
    ois.close();
    fis.close();
    printdata(emp2);
  }
}

import java.io.*;

class Demo implements Serializable
{
  String name;
  int age;
  Demo(String name, int age)
  {
    this.name = name;
    this.age = age;
  }
}

public class Test
{
  public static void main(String[] args) throws IOException, ClassNotFoundException
  {
    Demo d = new Demo("John", 30);
    FileOutputStream fos = new FileOutputStream("file.ser");
    ObjectOutputStream oos = new ObjectOutputStream(fos);
    oos.writeObject(d);
    oos.close();

    System.out.println("Object has been serialized");
    // deserialization
    Demo d1 = null;
    FileInputStream fis = new FileInputStream("file.ser");
    ObjectInputStream ois = new ObjectInputStream(fis);
    d1 = (Demo) ois.readObject();
    ois.close();

    System.out.println("Object has been deserialized");
    System.out.println(d1.name + " " + d1.age);
  }
}
import java.io.*;

class Person implements Externalizable {
    private String name;
    private int age;

    // No-argument constructor is required when using Externalizable
    public Person() {}

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Custom serialization: Write the data manually
    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeUTF(name); // Write the name
        out.writeInt(age);  // Write the age
    }

    // Custom deserialization: Read the data manually
    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
        name = in.readUTF(); // Read the name
        age = in.readInt();  // Read the age
    }

    @Override
    public String toString() {
        return "Person{name='" + name + "', age=" + age + "}";
    }
}

public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);

        // Serialize the object to a file
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("person.dat"))) {
            person.writeExternal(oos);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Deserialize the object from the file
        Person newPerson = new Person();
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("person.dat"))) {
            newPerson.readExternal(ois);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }

        // Display the deserialized object
        System.out.println(newPerson);
    }
}

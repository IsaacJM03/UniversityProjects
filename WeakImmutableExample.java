import java.util.Date;

public class WeakImmutableExample {
  public static void main(String[] args) {
    Date birthDate = new Date();
    WeakImmutable person = new WeakImmutable("John", birthDate);

    System.out.println("original: " +person.getBirthDate());

    // trying to modify it externally
    birthDate.setTime(0);
    System.out.println("modified: "+person.getBirthDate()); //still unchanged

    // trying to modify using the object
    Date retrievedDate = person.getBirthDate();
    retrievedDate.setTime(0);
    System.out.println("modified retrieved date: "+person.getBirthDate());
  }
}

public class School {
  public String name;
  public String address;
  public String year;

  // instance variables in constructor
  School(String name, String address, String year) {
    this.name = name;
    this.address = address;
    this.year = year;
  }
  public static void main(String[] args) {
    School s = new School("Kampala Parents'School", "Naguru", "1999");
    System.out.println("You are in a school");
    System.out.println("The school name is: "+s.name);
    System.out.println("The address is: "+s.address);
    System.out.println("Was founded in: "+s.year);
  }
}
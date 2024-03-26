package first;
// class Hello
// {
//   public static void main(String a[]) {
//     // making number easier to read
//     int num = 20_000_000; 
//     byte num1 = 3;
//     int result = num*num1; //type promotion
//     System.out.println(result); 
//   }
// }

public class Student {
	int age; // instance variables
	String name; 
	static int number_of_types;  //class variable     

	public static void main(String[] args) {
		Student s = new Student();
		s.age = 8_000_000;
		s.name = "Isaac";
		
		System.out.println("Name is: "+s.name +"\nAge is:"+s.age);
	}

}

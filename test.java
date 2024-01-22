public class test {

  public static void main(String[] args) {
    // int x = 7;
    // int y = 5;
    // int a = 5;
    // int b = 9;
    // if (x > y) {
    //   System.out.println(x);

    // }
    // else if(x < y) {
    //   System.out.println(y);
    // }
    // else {
    //   System.out.println(a);
    // }

    // String result = x%2==0 ? "Even" : "Odd";
    // System.out.println(result);

    String day = "F]s";
    String result = switch (day) {
      case "Monday" -> "Wake up";
      case "Tuesday"-> "Breakfast";
      case "Wednesday"-> "Lunch";
      case "Thursday","Friday"-> "Dinner";
      default -> "Invalid"; 
    };
    System.out.println(result);
  }
}
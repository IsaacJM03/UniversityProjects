import java.util.Scanner;

public class ArrayOfObjects {
  public int num;
  public String name;

  public static void main(String[] args) {
    ArrayOfObjects[] array = new ArrayOfObjects[3];
    Scanner s = new Scanner(System.in);
    for (int i = 0; i < array.length; i++) {
      System.out.println("Input number "+(i+1)+": ");
      array[i] = new ArrayOfObjects();
      array[i].num = s.nextInt();
      s.nextLine();
      System.out.println("Input name "+(i+1)+": ");
      array[i].name = s.nextLine();
    }
    // for (int i = 0; i < array.length; i++) {
    //   System.out.println(array[i].num + " ," + array[i].name);
    // }
    for (ArrayOfObjects i : array) {
      System.out.println(i.num + " ," + i.name);
    }
    s.close();
  }
  
}
import java.util.Scanner;

public class ArrayOfObjects {
  public int num;

  public static void main(String[] args) {
    ArrayOfObjects[] array = new ArrayOfObjects[3];
    Scanner s = new Scanner(System.in);
    for (int i = 0; i < array.length; i++) {
      System.out.println("Input number "+(i+1)+": ");
      array[i] = new ArrayOfObjects();
      array[i].num = s.nextInt();
    }
    for (int i = 0; i < array.length; i++) {
      System.out.println(array[i].num);
    }
    s.close();
  }
  
}
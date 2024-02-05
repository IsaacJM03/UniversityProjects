import java.util.Scanner;

public class BubbleSort {
  public static void main(String[] args) {
    System.out.println("Enter the number of elements: ");
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    int[] a = new int[n];
    System.out.println("Enter the elements: ");
    for (int i = 0; i < n; i++) {
      a[i] = s.nextInt();
    }
    for (int i = 0; i < n - 1; i++) {
      for (int j = 0; j < n - i - 1; j++) {
        if (a[j] > a[j + 1]) {
          int temp = a[j];
          a[j] = a[j + 1];
          a[j + 1] = temp;
        }
      }
    }
    System.out.println("Sorted array: ");
    for (int i = 0; i < n; i++) {
      System.out.print(a[i] + " ");
    }
    System.out.println("\n");
    s.close();
  }
}

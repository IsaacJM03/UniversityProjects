import java.util.Scanner;

public class MatrixInverse {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.println("Enter the elements of the 2x2 matrix:");
    System.out.println("Enter A00: ");
    double a00 = scanner.nextDouble();
    System.out.println("Enter A01: ");
    double a01 = scanner.nextDouble();
    System.out.println("Enter A10: ");
    double a10 = scanner.nextDouble();
    System.out.println("Enter A11: ");
    double a11 = scanner.nextDouble();

    double determinant = (a00 * a11) - (a10 * a01);
    
    if (determinant == 0) {
      System.out.println("Matrix is wnot invertible(determinant is zero)");
    } else {
      double[][] inverse = new double[2][2];
      double[][] adjoint = {
        {a11,-a01},
        {-a10,a00}
      };

      for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
          inverse[i][j] = adjoint[i][j] / determinant;
        }
      }

      System.out.println("\nInverse of the matrix is: ");
      for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
          System.out.print(inverse[i][j] + " ");
        }
        System.out.println();
      }
    }
    scanner.close();
  }
}

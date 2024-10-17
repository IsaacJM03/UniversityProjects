package Matrices;

public class Matrix {
  public static void main(String[] args) {

    int[][] A = {{1, 2, 3}, {4, 5, 6}};
    int[][] B = {{7, 8, 9}, {10, 11, 12}};
    int[][] C = new int[4][3];
    int[][] D = new int[2][6];
    C = merge(A, B);
    D = mergeHorizontally(A, B);

    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 3; j++) {
        System.out.print(C[i][j] + " ");
      }
      System.out.println();
    }
    System.out.println();
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 6; j++) {
        System.out.print(D[i][j] + " ");
      }
      System.out.println();
    } 
  }

  public static int[][] merge(int[][] A, int[][] B) {
    int[][] C = new int[4][3];
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 3; j++) {
        C[i][j] = A[i][j];
        C[i + 2][j] = B[i][j];
      }
    }
    return C;
  }

  public static int[][] mergeHorizontally(int[][] A, int[][] B) {
    int[][] C = new int[2][6];
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 3; j++) {
        C[i][j] = A[i][j];
        C[i][j + 3] = B[i][j];
      }
    }
    return C;
  }
}
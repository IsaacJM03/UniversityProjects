#include<stdio.h>

int main()
{
  int A[2][3] = { 
    {1, 2, 3}, 
    {4, 5, 6} 
    };
  int B[2][3] = { 
    {7, 8, 9}, 
    {10, 11, 12} 
    };

  // merging the two 2d arrays vertically
  int C[4][3]; //requires space complexity of O(n^2)
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
      C[i][j] = A[i][j];
      C[i + 2][j] = B[i][j];
    }
  }

  // merging horizontally
  int D[2][6];
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
      D[i][j] = A[i][j];
      D[i][j+3] = B[i][j];
    }
  }
  
  printf("Matrix C: \n");
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 3; j++) {
      printf("%d ", C[i][j]);
    }
    printf("\n");
  }
  printf("Matrix D: \n");
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 6; j++) {
      printf("%d ", D[i][j]);
    }
    printf("\n");
  }
}
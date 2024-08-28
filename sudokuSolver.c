#include <stdio.h>
#include <stdbool.h>

int main() {
  int sudoku_array[9][9] = {
    {0,0,0,0,0,0,2,0,0},
    {0,8,0,0,0,7,0,9,0},
    {6,0,2,0,0,0,5,0,0},
    {0,7,0,0,6,0,0,0,0},
    {0,0,0,9,0,1,0,0,0},
    {0,0,0,0,2,0,0,4,0},
    {0,0,5,0,0,0,6,0,3},
    {0,9,0,4,0,0,0,7,0},
    {0,0,6,0,0,0,0,0,0}
  };
  // determine if it is unique in the 3x3 sub grid
  for (int row = 0; row < 9; row+=3) {
    for (int col = 0; col < 9; col+=3) {
      bool seen[10] = {false}; // track numbers

      // iterate through the 3x3 sub grid
      for(int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
          int current = sudoku_array[row + i][col + j];

          if(current != 0){ //ignore empty cells
            if(seen[current]) {
              printf("Duplicate found in sub grid starting at (%d, %d)\n", row, col+1);
              return 1;
            }
            seen[current] = true; //number has been seen
          }
        }
        
      }
    }
  }
  printf("All subgrids are unique\n");
  return 0;
}
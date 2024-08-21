#include <stdio.h>

typedef unsigned char byte; // byte
typedef enum {
    false = 0,
    true = 1
} bool;

int main() {
  byte myByte = 100;
  short int shortX = 32000;
  long int longX = 3201001;
  char charA = 'A';
  bool boolA = true;

  printf("My char is %c\n",charA);
  printf("My byte is %d\n",myByte);
  printf("My short is %d\n",shortX);
  printf("My long is %ld\n",longX);
  if (boolA) {
    printf("BoolA\n");
  } else {
    printf("Not boolA\n");
  }

  return 0;

}
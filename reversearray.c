#include <stdio.h>

void inplace_swap(int *x,int *y)
{
  *y = *x ^ *y; 
  *x = *x ^ *y; // *x = (*x ^ *x )^ *y ---> *x = *y since  (*x ^ *x) = 0
  *y = *x ^ *y; // *y = (*y ^ *y )^ *x ---> *y = *x since  (*y ^ *y) = 0
}

void reverse_array(int a[],int cnt)
{
  int first,last;
  for(first=0,last=cnt-1;first<last;first++,last--)
  {
    inplace_swap(&a[first],&a[last]);
  }

}

int main() {
  int a = 10;
  int b = 20;

  printf("Before swap: a = %d, b = %d\n", a, b);
  inplace_swap(&a, &b);
  printf("After swap: a = %d, b = %d\n", a, b);

  return 0;
}
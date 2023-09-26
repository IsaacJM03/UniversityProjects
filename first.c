#include<stdio.h>

int main(void){
  int width;
  int length;
  int height;
  float area;
  

  printf("Enter width and height:");
  scanf("%d %d",&width,&height);

  area = height*width;

  printf("Area is %.2f",area);
  return 0;
}
#include <stdio.h>
#include <math.h>

int mean (int number);
int standardDeviation(void);

int main(void)
{
  int num;
  int count=0;
  int sum;
  float mean;

  printf("Enter an integer between 1 and 100:");
  scanf("%d",&num);

  if (num >100)
    num =100;

   while(count <= num)
    {
      sum += count;
      count++;

    }
    mean = sum/num;
    printf("The mean is %f \n",mean);
    printf("The sum is: %d \n",sum);
    return 0;
}

int mean (int number)
{
  
}
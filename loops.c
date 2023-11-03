#include <stdio.h>
#include <math.h>

int mean (int number);

int main(void)
{
  int num;
  int count=0;
  int sum;
  float mean_number;
  double standard_dev;

  printf("Enter an integer between 1 and 100:");
  scanf("%d",&num);
  
  mean_number = mean(num);

    for (count = 0; count <= num; count++)
    {
      int difference = count - mean_number;
      int square_difference = difference * difference;

      sum += square_difference;

    }

    float standard_dev = sqrt(sum/num);
    printf("The standard deviation is %lf",standard_dev);
    
    return 0;
}

int mean (int number)
{
  int count = 0, sum =0, mean_value=0;

  while (count<=number)
  {
    
    sum += count;
    count++;
  }

  mean_value = (sum/number);
  // printf("The sum is %d",sum);
  return mean_value;
  
}
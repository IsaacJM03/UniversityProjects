#include <stdio.h>
#include <stdbool.h>

int main()
{
  int score;
  bool validScore = false;

  while(!validScore){
    printf("Enter the student's score (0-100): ");
    if (scanf("%d", &score) == 1) {
        if (score >= 0 && score <= 100) {
            validScore = true;
        } else {
            printf("Invalid score. Please enter a score between 0 and 100.\n");
        }
    } else {
        printf("Invalid input. Please enter a whole number.\n");
        while (getchar() != '\n'); 
    }
  }

  char grade;
  if(score>=90){
    grade='A';
  } else if (score>=80){
    grade='B';
  } else if (score>=70){
    grade='C';
  } else if (score>=60){
    grade='D';
  } else {
    grade='F';
  }

  printf("Grade: %c\n", grade);
  return 0;
}
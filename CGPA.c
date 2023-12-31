#include <stdio.h>
#include <stdlib.h>


int main()
{
  int courseUnits;
  printf("Enter number of course units: ");
  scanf("%d",&courseUnits);
  // Using dynamic memory allocation (malloc) to request memory as needed, rather than pre-allocating a fixed amount of memory that might not be fully used.
  double *gradeScores = malloc(courseUnits * sizeof(double)); 
  int *creditUnits = malloc(courseUnits * sizeof(int));

  for (int i = 0; i< courseUnits; i++)
  {
    printf("Enter course unit score: (Course number)%d ",i+1);
    scanf("%lf",&gradeScores[i]);
    printf("Enter its credit units: ");
    scanf("%d",&creditUnits[i]);

    // Convert scores to grade points immediately
    if (gradeScores[i] >= 80) gradeScores[i] = 5.0;
    else if (gradeScores[i] >= 75) gradeScores[i] = 4.5;
    else if (gradeScores[i] >= 70) gradeScores[i] = 4.0;
    else if (gradeScores[i] >= 65) gradeScores[i] = 3.5;
    else if (gradeScores[i] >= 60) gradeScores[i] = 3.0;
    else if (gradeScores[i] >= 55) gradeScores[i] = 2.5;
    else if (gradeScores[i] >= 50) gradeScores[i] = 2.0;
    else gradeScores[i] = 0.0;
  }

  double sum = 0, totalCreditUnits = 0;
  for (int i = 0; i < courseUnits; i++)
  {
    double product = gradeScores[i] * creditUnits[i];
    sum += product;
    totalCreditUnits += creditUnits[i];
  }

  double cgpa = sum / totalCreditUnits;
  printf("Your CGPA is %.2lf",cgpa);

  // releasing the memory taken up by these two
  free(gradeScores);
  free(creditUnits);

  // // creating csv file and writing to it
  // FILE *csvFile = fopen("cgpa.csv","w");
  // fprintf(csvFile,"Course Title,Score,Grade Points,\n");

  // //  looping and writing data to csv file
  // for (int i = 0; i < courseUnits; i++)
  // {
  //   fprintf(csvFile,"%s,%lf,%lf,\n",courseTitles[i],gradeScores[i],creditUnits[i],gradePoints[i]);
  // }

  // fprintf(csvFile,"Total,,,%.2lf\n",cgpa);

  // printf("Report succesfully generated in cgpa.csv file");
  return 0;

}


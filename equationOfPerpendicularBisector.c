/*
 *Program in C to compute the equation of line of a perpendicular bisector given:
 * Two pairs of coordinates
*/
#include<stdio.h>

int main(void)
{
    float x1;
    float x2;
    float y1;
    float y2;
    float slope;
    float midpoint_x;
    float midpoint_y;
    float midpoint;
    float perpendicular_slope;
    float y_intercept;

    printf("Enter the first coordinate: " );
    scanf("%f",&x1);

    printf("Enter the second coordinate: " );
    scanf("%f",&y1);

    printf("Enter the third coordinate: " );
    scanf("%f",&x2);

    printf("Enter the fourth coordinate: " );
    scanf("%f",&y2);

    slope = (y2-y1)/(x2-x1);
    printf("Slope: %f",slope);

    midpoint_x = (x1+x2)/2;
    midpoint_y = (y1+y2)/2;

    printf("The midpoint of the line segment is: (%f, %f)", midpoint_x, midpoint_y);

    perpendicular_slope = -1*(1/slope);

    printf("The perpendicular slope is:%f", perpendicular_slope);

    y_intercept=(midpoint_y-(perpendicular_slope*midpoint_x));

    printf("the y intercept is: %f",y_intercept);

    printf("The original two points are: A(%.2f,%.2f) and B(%.2f,%.2f).\n The equation of the line is y=%.2fx+%.2f",x1,y1,x2,y2,perpendicular_slope,y_intercept);



}

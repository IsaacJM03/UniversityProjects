/* Simple program to compute the price of a plot of land given;
 * the size/area of the plot 
 * price per decimal
*/
#include <stdio.h>
/* Note that: 
 *  price_per_decimal * size_of_the_plot(area) = price_of_plot
 *  price_per_decimal = total_price / area 
 *  1 sqaure metre = 0.024 decimals
*/

int main(void) {
  float length,width,area_in_sq_metres,price_per_decimal,size_of_the_plot_in_decimals,price_of_the_plot;
  float one_square_metre_in_decimals = 0.0247;

  printf("Enter length: ");
  scanf("%f",&length);

  printf("Enter width: ");
  scanf("%f",&width);

  printf("Enter price per decimal: ");
  scanf("%f",&price_per_decimal);

  area_in_sq_metres = length * width;
  size_of_the_plot_in_decimals = area_in_sq_metres * one_square_metre_in_decimals;

  printf("Area is %.2f decimals \n",size_of_the_plot_in_decimals);

  price_of_the_plot = price_per_decimal * size_of_the_plot_in_decimals;

  printf("The price of the plot is UGX.%.2f \n",price_of_the_plot);

  return 0;
}

#include <stdio.h>
// formulas ; price_per_decimal * size_of_the_plot(area) = price_of_plot
//  price_per_decimal = total_price / area 
//  1 m^2 = 0.024 decimal

int main(void) {
  float length,width,area,price_per_decimal,size_of_the_plot_in_decimals,price_of_the_plot;
  float one_square_metre_in_decimals = 0.024;

  printf("Enter length: ");
  scanf("%f",&length);

  printf("Enter width: ");
  scanf("%f",&width);

  printf("Enter price per decimal: ");
  scanf("%f",&price_per_decimal);

  area = length * width;
  size_of_the_plot_in_decimals = area * one_square_metre_in_decimals;

  printf("Area is %.2f decimals \n",size_of_the_plot_in_decimals);

  price_of_the_plot = price_per_decimal * size_of_the_plot_in_decimals;

  printf("Price of the plot: UGX.%.2f \n",price_of_the_plot);

  return 0;
}
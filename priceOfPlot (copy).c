#include <stdio.h>
#include <string.h>

float getPositiveFloat(const char *prompt) {
    float value;
    do {
        printf("%s", prompt);
        if (scanf("%f", &value) != 1 || value <= 0) {
            printf("Invalid input. Please enter a positive number.\n");
            while (getchar() != '\n'); // Clear input buffer
        }
    } while (value <= 0);
    return value;
}

float convertToSquareMetres(float length, float width, const char *units) {
    if (strcmp(units, "metres") == 0) {
        return length * width;
    } else if (strcmp(units, "feet") == 0) {
        // Implement the conversion factor from square feet to square metres
        // For example, 1 square foot = 0.092903 square metres
        float conversionFactor = 0.092903;
        return length * width * conversionFactor;
    }
    return -1.0; // Invalid units
}

void displayPrice(float price, const char *currency) {
    printf("The price of the plot is %s%.2f\n", currency, price);
}

int main(void) {
    int calculateAnother;
    do {
        float length, width, area_in_sq_metres, price_per_decimal, size_of_the_plot_in_decimals, price_of_the_plot;
        float one_square_metre_in_decimals = 0.0247;

        length = getPositiveFloat("Enter length: ");
        width = getPositiveFloat("Enter width: ");
        price_per_decimal = getPositiveFloat("Enter price per decimal: ");

        char units[20];
        printf("Enter input units (e.g., metres or feet): ");
        scanf("%s", units);

        if (strcmp(units, "metres") != 0 && strcmp(units, "feet") != 0) {
            printf("Invalid units. Please enter 'metres' or 'feet'.\n");
            return 1; // Exit with an error code
        }

        area_in_sq_metres = convertToSquareMetres(length, width, units);

        if (area_in_sq_metres < 0) {
            printf("Invalid units for conversion.\n");
            return 1; // Exit with an error code
        }

        size_of_the_plot_in_decimals = area_in_sq_metres * one_square_metre_in_decimals;

        printf("Area is %.2f decimals \n", size_of_the_plot_in_decimals);

        price_of_the_plot = price_per_decimal * size_of_the_plot_in_decimals;

        char currency[10];
        printf("Enter currency (e.g., UGX, USD, EUR): ");
        scanf("%s", currency);

        // Calculate and display the price...
        displayPrice(price_of_the_plot, currency);

        printf("Calculate another plot? (1 for yes, 0 for no): ");
        scanf("%d", &calculateAnother);
    } while (calculateAnother == 1);

    return 0;
}

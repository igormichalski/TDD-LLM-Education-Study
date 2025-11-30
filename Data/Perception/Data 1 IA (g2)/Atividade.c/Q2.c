#include <stdio.h>

int graus_celsius_para_fahrenheit(int celsius) {
    return (celsius * 9 / 5) + 32;
}

int main() {
    int celsius;
    printf("Digite a temperatura em graus Celsius: ");
    scanf("%d", &celsius);
    printf("A temperatura em graus Fahrenheit eh %d\n", graus_celsius_para_fahrenheit(celsius));
    return 0;
}
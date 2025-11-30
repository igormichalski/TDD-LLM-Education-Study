#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, resto;
    int numero, soma = 0, digito;

    printf("digite um numero positivo:");
    scanf("%d", &a);

    if (a<=0){
        printf("o numero deve ser positivo!");
        return 1;
    }

    printf("digite um numero positivo:");
    scanf("%d", &b);

    if (b<=0){
        printf("o numero deve ser positivo!");
        return 1;
    }

    while (b != 0) {
        resto = a % b;
        a = b;
        b = resto;}

        printf("o mdc e: %d\n", a);

    printf("Digite um numero inteiro positivo: ");
    scanf("%d", &numero);

    if (numero <= 0) {
        printf("O numero deve ser positivo!\n");
        return 1;
    }


    while (numero > 0) {
        digito = numero % 10;
        soma += digito;
        numero /= 10;
    }

    printf("A soma dos digitos eh: %d\n", soma);

    return 0;
}

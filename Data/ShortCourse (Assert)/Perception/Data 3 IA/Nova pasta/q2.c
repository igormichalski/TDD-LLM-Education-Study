#include <stdio.h>
#include <stdlib.h>

int main(){
    int numero, soma = 0, digito;

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

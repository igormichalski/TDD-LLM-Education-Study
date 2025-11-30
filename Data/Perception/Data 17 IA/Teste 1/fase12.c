#include <stdio.h>
#include<assert.h>
int main() {
    int numero, somas = 0;

 
    printf("Mê de um numero positivo para que que possa comecar: ");
    scanf("%d", &numero);

    if (numero <= 0) {
        printf("Apenas numeros positivos!.\n");
        return 1;
    }
 
    while (numero > 0) {
        somas += numero % 10;  
        numero /= 10;         
    }

    printf("A soma dos dígitos é: %d\n", somas);



}
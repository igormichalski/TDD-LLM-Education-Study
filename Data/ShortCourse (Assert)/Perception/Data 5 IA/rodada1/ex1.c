#include <stdio.h>
#include <assert.h>

// Função para calcular o MDC usando o algoritmo de Euclides
int mdc(int a, int b) {
    while (b != 0) {
        int resto = a % b;
        a = b;
        b = resto;
    }
    return a;
}

void testarMdc(){
    assert(mdc(60,48) == 12);
    assert(mdc(100,25) == 25);
    assert(mdc(7,3) == 1);
    printf("Passou nos testes\n");
}

int main() {

    testarMdc();

    int x, y;

    printf("Digite dois numeros: ");
    scanf("%d %d", &x, &y);

    printf("O MDC de %d e %d eh: %d\n", x, y, mdc(x, y));

    return 0;
}

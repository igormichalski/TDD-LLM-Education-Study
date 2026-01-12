#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

/**
 * Função que soma os dígitos de um número inteiro.
 * Exemplo: 123 -> 1 + 2 + 3 = 6
 */
int soma_digitos(int numero) {
    if (numero < 0)
        numero = -numero; // trata números negativos

    int soma = 0;
    while (numero > 0) {
        soma += numero % 10;
        numero /= 10;
    }
    return soma;
}

/**
 * Função de testes (TDD)
 */
void testes() {
    // Testes básicos
    assert(soma_digitos(0) == 0);
    assert(soma_digitos(5) == 5);
    assert(soma_digitos(12) == 3);
    assert(soma_digitos(12345) == 15);

    // Teste com número negativo
    assert(soma_digitos(-456) == 15);

    // Teste com número grande
    assert(soma_digitos(9999) == 36);

        #include <assert.h>
    #include <stdio.h>

    #define EXPECT_ERR (-1)

    /* ========== PRINCIPAIS ========== */
    assert(soma_digitos(492)   == 15);
    assert(soma_digitos(12345) == 15);

    /* ========== BORDA (inclui inválidos) ========== */
    assert(soma_digitos(7)         == 7);    /* um dígito */
    assert(soma_digitos(100000)    == 1);    /* zeros */
    assert(soma_digitos(9999999999)== 90);   /* muitos dígitos */
    assert(soma_digitos(98765432109876543210) == 90); /* 64+ bits */
    assert(soma_digitos(0)    == EXPECT_ERR);  /* inválido: não positivo */
    assert(soma_digitos(-123) == EXPECT_ERR);  /* inválido */
    puts("P02 OK (inteiro: principais + borda)");

    printf("✅ Todos os testes passaram!\n");
}

int main() {
    // Primeiro executa os testes TDD
    testes();

    int numero;
    printf("Digite um número: ");
    scanf("%d", &numero);

    int resultado = soma_digitos(numero);
    printf("A soma dos dígitos de %d é: %d\n", numero, resultado);

    return 0;
}

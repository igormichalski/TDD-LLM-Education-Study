#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include <ctype.h>

int main() {
    float valor, resultado;
    char unidade;

    printf("=== Conversor Celsius ↔ Fahrenheit ===\n");
    printf("Digite o valor e a unidade (ex: 25 C ou 77 F): ");
    
    // Lê um número e um caractere
    if (scanf("%f %c", &valor, &unidade) != 2) {
        printf("❌ Entrada inválida! Use o formato: número espaço unidade (ex: 25 C)\n");
        return 1;
    }

    // Converte a unidade para maiúscula
    unidade = toupper(unidade);

    // Verifica qual é a unidade e faz

}


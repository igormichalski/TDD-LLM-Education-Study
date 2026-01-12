#include <stdio.h>
#include <ctype.h>
#include <assert.h>
#include <string.h>

// Função que conta o número de vogais em uma string
int contar_vogais(const char *texto) {
    int contador = 0;
    for (int i = 0; texto[i] != '\0'; i++) {
        char c = tolower(texto[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            contador++;
        }
    }
    return contador;
}

// Função de testes (TDD)
void testes_contar_vogais() {
    // Teste 1: string vazia
    assert(contar_vogais("") == 0);

    // Teste 2: sem vogais
    assert(contar_vogais("rhythms") == 0);

    // Teste 3: apenas vogais
    assert(contar_vogais("aeiou") == 5);

    // Teste 4: mistura de maiúsculas e minúsculas
    assert(contar_vogais("AeIoU") == 5);

    // Teste 5: frase com espaços e pontuação
    assert(contar_vogais("Ola, tudo bem?") == 5);

    // Teste 6: palavra longa
    assert(contar_vogais("computador") == 4);

    // Teste 7: frase com acentos (não devem contar)
    assert(contar_vogais("ação") == 2);  // 'a' e 'o' contam, 'ã' não
    
    printf("✅ Todos os testes passaram com sucesso!\n");
}

int main() {
    // Etapa de TDD: primeiro rodar os testes
    testes_contar_vogais();

    // Depois, executar a lógica principal com input do usuário
    char texto[100];
    printf("Digite uma frase: ");
    fgets(texto, sizeof(texto), stdin);
    texto[strcspn(texto, "\n")] = '\0'; // remove \n

    int resultado = contar_vogais(texto);
    printf("Quantidade de vogais: %d\n", resultado);

    return 0;
}



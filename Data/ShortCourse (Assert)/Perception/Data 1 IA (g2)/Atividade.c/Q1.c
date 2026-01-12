#include <stdio.h>
#include <string.h>

int conta_vogais(char *str) {
    int contagem = 0;
    char vogais[] = "aeiouAEIOU";
    while (*str) {
        if (strchr(vogais, *str)) {
            contagem++;
        }
        str++;
    }
    return contagem;
}

int main() {
    char texto[100];
    printf("Digite um texto: ");
    fgets(texto, sizeof(texto), stdin);
    printf("O numero de vogais no texto eh %d\n", conta_vogais(texto));
    return 0;
}
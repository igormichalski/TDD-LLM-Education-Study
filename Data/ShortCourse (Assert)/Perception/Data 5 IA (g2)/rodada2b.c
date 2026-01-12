#include <stdio.h>
#include <string.h>
#include <ctype.h> // para tolower()

int main() {
    char texto[200];
    int contador = 0;

    printf("=== Contador de Vogais ===\n");
    printf("Digite uma frase: ");
    
    // Lê a linha inteira (inclusive espaços)
    fgets(texto, sizeof(texto), stdin);

    // Percorre cada caractere da string
    for (int i = 0; texto[i] != '\0'; i++) {
        char c = tolower(texto[i]); // converte para minúscula
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            contador++;
        }
    }

    printf("Quantidade de vogais: %d\n", contador);

    return 0;
}

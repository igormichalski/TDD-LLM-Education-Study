#include <stdio.h>
#include <ctype.h>
#include <assert.h>
#include <math.h>

/*
 * convert_temperature:
 *   input  - valor de temperatura
 *   unit   - 'C' ou 'F' (aceita maiúsculas/minúsculas)
 *   result - ponteiro onde será escrito o valor convertido
 *
 * Retorna:
 *   0  - sucesso (result preenchido)
 *  -1  - unidade inválida
 *
 * Fórmulas:
 *   C -> F: F = C * 9/5 + 32
 *   F -> C: C = (F - 32) * 5/9
 */
int convert_temperature(double input, char unit, double *result) {
    if (!result) return -1;
    char u = toupper((unsigned char)unit);
    if (u == 'C') {
        *result = input * 9.0 / 5.0 + 32.0;
        return 0;
    } else if (u == 'F') {
        *result = (input - 32.0) * 5.0 / 9.0;
        return 0;
    } else {
        return -1;
    }
}

/* Função utilitária para comparar doubles com tolerância */
int quase_igual(double a, double b, double eps) {
    return fabs(a - b) <= eps;
}

/* Suíte de testes TDD usando assert */
void testes_convert_temperature() {
    double out;
    const double eps = 1e-6;

    /* Teste 1: 0°C -> 32°F */
    assert(convert_temperature(0.0, 'C', &out) == 0);
    assert(quase_igual(out, 32.0, eps));

    /* Teste 2: 100°C -> 212°F */
    assert(convert_temperature(100.0, 'C', &out) == 0);
    assert(quase_igual(out, 212.0, eps));

    /* Teste 3: 32°F -> 0°C */
    assert(convert_temperature(32.0, 'F', &out) == 0);
    assert(quase_igual(out, 0.0, eps));

    /* Teste 4: -40°C -> -40°F (ponto especial onde são iguais) */
    assert(convert_temperature(-40.0, 'C', &out) == 0);
    assert(quase_igual(out, -40.0, eps));

    /* Teste 5: -40°F -> -40°C (simetria) */
    assert(convert_temperature(-40.0, 'F', &out) == 0);
    assert(quase_igual(out, -40.0, eps));

    /* Teste 6: letra minúscula funciona */
    assert(convert_temperature(0.0, 'c', &out) == 0);
    assert(quase_igual(out, 32.0, eps));
    assert(convert_temperature(32.0, 'f', &out) == 0);
    assert(quase_igual(out, 0.0, eps));

    /* Teste 7: valores com casas decimais */
    assert(convert_temperature(36.6, 'C', &out) == 0);
    assert(quase_igual(out, 97.88, 1e-3)); /* 36.6*9/5 +32 = 97.88 */

    /* Teste 8: unidade inválida deve retornar -1 e não tocar result */
    double sentinel = 12345.6789;
    out = sentinel;
    assert(convert_temperature(25.0, 'K', &out) == -1);
    assert(quase_igual(out, sentinel, eps)); /* result não foi alterado */

    /* Teste 9: ponteiro result nulo -> erro */
    assert(convert_temperature(0.0, 'C', NULL) == -1);

    printf("✅ Todos os testes TDD passaram.\n");
}

int main(void) {
    /* Roda os testes TDD primeiro */
    testes_convert_temperature();

    /* Depois faz a interação com usuário */
    double valor;
    char unidade;
    double resultado;

    printf("\nConversor C <-> F\n");
    printf("Digite o valor seguido da unidade (C ou F), ex.: 36.6 C\n");
    printf("Entrada: ");

    if (scanf("%lf %c", &valor, &unidade) != 2) {
        fprintf(stderr, "Entrada inválida. Use formato: <numero> <unidade>\n");
        return 1;
    }

    if (convert_temperature(valor, unidade, &resultado) == 0) {
        char u = toupper((unsigned char)unidade);
        if (u == 'C') {
            printf("%.6g %c = %.6g F\n", valor, u, resultado);
        } else { /* 'F' */
            printf("%.6g %c = %.6g C\n", valor, u, resultado);
        }
    } else {
        fprintf(stderr, "Unidade inválida: %c. Use 'C' ou 'F'.\n", unidade);
        return 1;
    }

    return 0;
}

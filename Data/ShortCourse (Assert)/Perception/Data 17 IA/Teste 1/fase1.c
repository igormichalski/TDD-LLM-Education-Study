#include <assert.h>
#include <stdio.h>

int main() {

    int a , b;

    printf("Escreva os numeros para o MDC (sendo positivos):" );
    scanf("%d %d", &a , &b );
    if( a<= 0 , b <= 0) {
        printf("escreva numeros positivos!");
        return 1;
    }
while ( b != 0) {
 int temp = b;
        b = a % b;
        a = temp;
}
  printf("MDC = %d\n", a);

}
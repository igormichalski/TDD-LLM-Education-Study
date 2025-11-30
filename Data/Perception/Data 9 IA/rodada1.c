#include <stdio.h>
#include <assert.h>

int mdc(int x, int y){
    while (y != 0){
        int resto = x % y;
        x = y;
        y = resto;
    }
    return x;    
}

int main(){

    assert(mdc(12, 18) == 6);
    assert(mdc(100, 25) == 25);

    
    printf("deu certo chefe\n");
    
    int a, b;
    printf("digite dois numeros: ");
    scanf(" %d %d", &a, &b);
    printf("mdc de %d e %d eh: %d", a, b, mdc(a, b));
    


    return 0;

}
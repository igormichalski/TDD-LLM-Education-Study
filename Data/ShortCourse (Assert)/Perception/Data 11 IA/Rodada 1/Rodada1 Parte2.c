#include <stdio.h>
#include <assert.h>

int soma_dos_digitos (int n){
    int soma = 0;

    while (n>0){
        soma = soma + n % 10;
        n = n / 10;
    }
    
    return soma;

}

int main(){


    
    assert(soma_dos_digitos(492)==15);
    assert(soma_dos_digitos(12345)==15);

    return 0;
}
#include <stdio.h>
#include <assert.h>

int mdc(int a, int b) {
    int resto;
    while (b != 0) {
        resto = a % b;
        a = b;
        b = resto;
    }
    return a;
}

int main() {

    
    assert(mdc(12, 18)==6);
    assert(mdc(25, 30)==5);

    return 0;
}

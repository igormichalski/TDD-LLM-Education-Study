#include <assert.h>
#include <stdio.h>

#define EXPECT_ERR (-1)


/*==========MAIN==========*/
    assert(soma_digitos(492)   == 15);
    assert(soma_digitos(12345) == 15);

/*==========BORDER (includes invalids)==========*/
    assert(soma_digitos(7)         == 7);    
    assert(soma_digitos(100000)    == 1);  
    assert(soma_digitos(9999999999)== 90);   
    assert(soma_digitos(98765432109876543210) == 90); 
    assert(soma_digitos(0)    == EXPECT_ERR);  
    assert(soma_digitos(-123) == EXPECT_ERR);  

#include <assert.h>
#include <stdio.h>

#define EXPECT_ERR (-1)
    

/*==========MAIN==========*/
    assert(conta_vogais("ChatGPT") == 1);
    assert(conta_vogais("Inteligência Artificial") == 10);

/*==========BORDER (includes invalids)==========*/
    assert(conta_vogais("") == 0);                   
    assert(conta_vogais("rhythm") == 0);           
    assert(conta_vogais("aeiouAEIOU") == 10);        
    assert(conta_vogais("Olá, mundo!") == 4);         
    assert(conta_vogais("  a  A  \t \n  ") == 2);  
    assert(conta_vogais("àéîõü café CAÇÃO") == 8);    
    assert(conta_vogais(NULL) == EXPECT_ERR);        
#include <assert.h>
#include <stdio.h>

#define EXPECT_ERR (-1)


/*==========MAIN==========*/
   assert(mdc(12, 18) == 6);
   assert(mdc(25, 30) == 5);
   assert(mdc(7, 7)   == 7);
   assert(mdc(18, 12) == 6);   

/*==========BORDER (includes invalids)==========*/
   assert(mdc(8, 32)     == 8);    
   assert(mdc(35, 64)    == 1);    
   assert(mdc(1, 99991)  == 1);   
   assert(mdc(123456, 789012) == 12); 
   assert(mdc(0, 5)      == EXPECT_ERR);  
   assert(mdc(-4, 10)    == EXPECT_ERR);  

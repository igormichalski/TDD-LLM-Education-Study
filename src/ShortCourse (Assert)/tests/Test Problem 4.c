#include <assert.h>
#include <math.h>
#include <stdio.h>

#define EPS 1e-6
#define ASSERT_NEAR(a,b) assert(fabs((a)-(b)) <= EPS)


/*==========MAIN==========*/
    ASSERT_NEAR(convCtoF(0.0),    32.0);
    ASSERT_NEAR(convFtoC(32.0),    0.0);
    ASSERT_NEAR(convCtoF(100.0), 212.0);

/*==========BORDER (includes invalids)==========*/
    ASSERT_NEAR(convCtoF(-40.0), -40.0); 
    ASSERT_NEAR(convFtoC(98.6),   37.0); 
    ASSERT_NEAR(convCtoF(-10.0),  14.0); 
    ASSERT_NEAR(convCtoF(1e6), 1800032.0); 

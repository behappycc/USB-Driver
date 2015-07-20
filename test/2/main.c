#include <stdio.h>
#include "math.h"

int main(void) {
    int num = 0;
    int power = 0; 

    printf("input num："); 
    scanf("%d", &num); 

    printf("input pow："); 
    scanf("%d", &power); 

    printf("%d pow：%d\\n", num, myPow2(num));
    printf("%d  %d  %d\\n", num, power, myPow(num, power));
    
    return 0;
}
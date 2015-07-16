#include <stdio.h>

int main(void) {
    int var = 10; 
    int *ptr = &var ; 

    printf("變數 var 的位址：%X\\n", &var);
    printf("指標 ptr 指向的位址：%X\\n", ptr);

    return 0;

}
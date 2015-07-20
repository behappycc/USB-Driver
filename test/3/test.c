#include <stdio.h>

void strcpy1(char *s, char *t);

int main(){
    char str1[] = "hello";
    char str2[40];
    strcpy1(str2, str1);
    printf("%s\n", str2);
    return 0;
}

void strcpy1(char *s, char *t){
    while((*s = *t) != '\0'){
        s++;
        t++;
    }
}
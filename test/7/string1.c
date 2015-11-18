#include <stdlib.h>
#include "string1.h"

int strLen(char *str) {
    char *ptr = str;
    while ( *ptr != '\0' )
        ptr++;
    return ptr - str;
}

char *strCpy(char *dest, char *source) {
    char *ptr = dest;
    while ( (*ptr++=*source++) != '\0' );
    return dest;
}

char *strCat(char *dest, char *source) {
    char *ptr = dest;
    while ( *ptr++ != '\0' );    
    ptr--;
    while ( (*ptr++=*source++) != '\0' );
    return dest;
}

int strCmp(char *source, char *target) {
    for ( ; *source == *target; source++, target++)
         if ( *source == '\0')
             return 0;
    if ((*source-*target) < 0 )
       return -1; 
    else
       return 1;
}

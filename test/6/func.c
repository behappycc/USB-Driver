#include <stdio.h>
#include <stdlib.h>
#include "func.h"

static void maxvalue(void);
static void minvalue(void);
int var1, var2;
static int result;

static void maxvalue() {
   if ( var1 > var2 ) result = var1;
   else               result = var2;
}

static void minvalue() {
   if ( var1 < var2 ) result = var1;
   else               result = var2;
}

void cmpresult(int type) {
   printf("var1: %d\n", var1);
   printf("var2: %d\n", var2);
   if ( type == MAXCMP ) {
       maxvalue();
       printf("maxresult: %d\n", result);
   } else {
       minvalue();
       printf("minresult: %d\n", result);
   }
}
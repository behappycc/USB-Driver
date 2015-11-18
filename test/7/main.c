#include <stdio.h>
#include <stdlib.h>
#include "string1.h"

int main() {
   char str[80];
   char str1[80];
   char *ptr;
   int len;
   printf("input string: ");
   gets(str);
   printf("原始字串: \"%s\"\n", str);
   len = strLen(str);
   printf("字串\"%s\"的長度為: %d\n", str, len);
   printf("複製字串: \"%s\"\n", strCpy(str1, str));
   printf("請輸入欲連接的字串: ");
   gets(str1);
   printf("欲連接字串: \"%s\"\n", str1); 
   ptr = strCat(str, str1);       
   printf("連接結果的字串: \"%s\"\n", ptr);
   printf("請輸入欲比較的字串: ");
   gets(str1);
   printf("欲比較的字串: \"%s\"\n", str1);
   printf("字串比較結果: %d\n", strCmp(str, str1));
}
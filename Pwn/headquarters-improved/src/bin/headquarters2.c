/*
Compile options:
    gcc headquarters2.c -o headquarters2 -fno-stack-protector -no-pie -D_FORTIFY_SOURCE=0
*/

#include <stdio.h>
#include <stdlib.h>

void admin()
{   
    printf("Welcome admin.\n");
    puts("Here is your flag: ");
    system("cat flag");
}

int main()
{   
    char name[32];

    printf("Welcome to Sieberrsec's headquarters!\n");
    printf("Enter your name: ");
    gets(name);

    printf("\nHello %s, welcome to Sieberrsec headquarters.\n",name);

    return 0;
}
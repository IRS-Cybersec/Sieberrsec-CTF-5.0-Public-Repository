/*
Compile options:
    gcc headquarters.c -o headquarters -fno-stack-protector
*/

#include <stdio.h>
#include <stdlib.h>

void print_flag()
{
    system("cat flag");
}

int main()
{   
    int admin_key = 0;
    char name[8];

    printf("Welcome to Sieberrsec's headquarters!\n");
    printf("Enter your name: ");
    gets(name);

    if (admin_key==0xdeadbeef)
    {   
        printf("Welcome back, admin.\n");
        print_flag();
    }
    else {
        printf("Hi %s! Welcome to Sieberrsec headquarters!\n", name);
    }

    return 0;
}
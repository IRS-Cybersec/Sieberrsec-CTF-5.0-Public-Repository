/*
Compile options:
    gcc headquarters2.c -o headquarters2 -D_FORTIFY_SOURCE=0
*/

#include <stdio.h>
#include <stdlib.h>

void setup() {
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  setbuf(stderr, 0);
}

void admin()
{   
    printf("Welcome admin.\n");
    system("cat flag");
}

int get_credentials() 
{   
    setup();
    char name[8];
    char nric[16];
    char email[32];

    printf("Welcome to Sieberrsec's headquarters!\n");

    printf("Enter your name: ");
    read(0, name, 0x100);

    printf("\nHello %s, welcome to Sieberrsec headquarters.\n",name);

    printf("Due to additional security concerns, please provide us your NRIC: ");
    read(0, nric, 0x100);

    printf("\nNRIC:%s\n",nric);

    printf("Please also provide us with your email: ");
    read(0, email, 0x100);

    printf("Thank you for visiting Sieberrsec headquarters! Have a nice day.\n");
}

int main()
{      
    setup();
    get_credentials();

    return 0;
}
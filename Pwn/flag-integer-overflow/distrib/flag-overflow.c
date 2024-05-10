/*
Compile options:
    gcc flag-overflow.c -o flag-overflow
*/

#include <stdio.h>
#include <stdlib.h>

void print_flag()
{   
    puts("\nCongrats! You have obtained the flag.");
    system("cat flag");
}

int main()
{
    int balance = 1000;
    int input;
    int cost = 0;

    puts("Goal: Make your balance greater than $13371337");
    printf("Current balance: $%d\n",balance);
    puts("\nHow many flags would you like to buy? Cost of 1 flag is $100.");

    scanf("%d", &input);
    cost = 100*abs(input);

    if (cost <= balance) {
        balance -= cost;
        printf("You bought %d flags. Cost is $%d.\n",input,cost);
        printf("New balance: $%d\n",balance);
    }
    else {
        printf("Insufficient funds to pay the cost of $%d\n",cost);
    }

    if (balance >= 13371337) {
        print_flag();
    }
    
    return 0;
}
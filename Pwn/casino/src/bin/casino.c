/*
Compile options:
    gcc casino.c -o casino
*/

#include <stdio.h>
#include <stdlib.h> 

void print_flag()
{
    system("cat flag");
}

void print_options()
{
    puts("\n1. gamble");
    puts("2. buy flag (costs $13371337)");
    puts("3. leave\n");
}

int gamble(int balance)
{
    int input;

    puts("How much would you like to gamble: ");
    
    // if user provides invalid input
    if(scanf("%d", &input) == 0) {
        puts("Invalid input, please input an integer next time.");
        exit(0);
    }

    // check that the user has enough funds to gamble
    if (balance >= input) {
        int guess;

        puts("Guess an integer from 1-100:");

        // if user provides invalid input
        if (scanf("%d", &guess)==0) {
            puts("Invalid input, please input an integer next time.");
            exit(0);
        }
        
        // shh, the casino is actually rigged.
        printf("Oops, your guess of %d is wrong. $%d will be deducted from your balance.\n",guess,input);

        // i'm sure no one can exploit this ;)
        balance -= abs(input);
    }
    else {
        printf("Too little funds to gamble $%d\n",input);
    }
    return balance;
}

void buy_flag(int balance)
{
    if (balance > 13371337) {
        printf("You bought the flag! ");
        print_flag();
    }
    else {
        puts("You lack sufficient funds to buy the flag, which costs $13371337.\n");
    }
}

int main()
{
    int balance = 100;
    int menu;

    puts("Welcome to the casino.");

    while(1) {
        print_options();
        printf("Current balance: $%d\n",balance);
        printf("What would you like to do (input an integer from 1-3): ");
        scanf("%d", &menu);
        
        if (menu == 1) {
            balance = gamble(balance);
        }
        else if (menu == 2) {
            buy_flag(balance);
        }
        else if (menu == 3) {
            puts("Bye!");
            break;
        }
        else {
            puts("Invalid option");
            break;
        }
    }
    return 0;
}
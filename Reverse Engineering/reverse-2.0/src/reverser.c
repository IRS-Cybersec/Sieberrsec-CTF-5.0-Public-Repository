#include <stdio.h>
#include <string.h>

int interesting[12] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8};

void reverser(char* text, char* output) {
    int curr = 0;
    int index = 0;

    for (int i = 0; i < 12; i++) {
        int length = interesting[i];
        int j;

        for (j = length - 1; j >= 0; j--) {
            output[index++] = text[curr + j];
        }

        curr += length;
    }

    output[index] = '\0';
}

int main() {
    char reversed[53];
    char output[53];

    printf("Enter the reversed text: ");
    scanf("%52s", reversed);

    reverser(reversed, output);

    printf("%s", output);

    return 0;
}

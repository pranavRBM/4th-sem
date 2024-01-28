#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generateRandomNumbers(int n) {
    srand(time(NULL));
    printf("Random numbers: ");
    for (int i = 0; i < n; i++) printf("%d ", rand());
}

int main() {
    generateRandomNumbers(5); // Change this value to generate a different number of random numbers
    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    unsigned int prev = 0;
    while (1) {
        srand(time(NULL));
        unsigned int secret1 = rand();

        if (secret1 != prev) {
            prev = secret1;
            printf("1 : %u\n", secret1);
            secret1 *= 0x5EC12E7;
            printf("2 : %u\n", secret1);
        }
        
    }

    return 0;
}

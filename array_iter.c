#include <stdio.h>

void main() { 
    double input[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    double output[10] = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    
    for (int i = 0; i <= 9; i++) {
        printf("(%.2lf,%.2lf)\n", input[i], output[i]);
    }
}
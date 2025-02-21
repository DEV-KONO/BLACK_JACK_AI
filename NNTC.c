#include <stdio.h>
#include <time.h>
#define RAND_MAX 1000

float randomFloat()
{
   return (float)(rand()) / (float)(RAND_MAX);
}

int main() {
    
    float train_x[10] = {1,2,3,4,5,6,7,8,9,10};
    float train_y[10] = {2,4,6,8,10,12,14,16,18,20};

    srand(time(NULL));

    float w = randomFloat();
    float b = randomFloat()

}
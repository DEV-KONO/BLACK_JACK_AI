#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define len(x)  (sizeof(x) / sizeof((x)[0]))

float RandomFloat();

float MeanSquaredError(float* SD);

float Dmse_en_Dw(float* train_X, float* train_Y, float* predictions);

float Dmse_en_Db(float* train_X, float* train_Y, float* predictions);

float Predict(float w, float x, float b);

void main() {

    float SquaredDiff[10] = {0,0,0,0,0,0,0,0,0,0};
    float Predictions[10] = {0,0,0,0,0,0,0,0,0,0};
    
    float train_x[10] = {1,2,3,4,5,6,7,8,9,10};
    float train_y[10] = {2,4,6,8,10,12,14,16,18,20};

    srand(time(NULL));

    float w = RandomFloat();
    float b = RandomFloat();

    printf("Weight : %f, Bias : %f\n", w, b);

    float alpha = 0.001f;

    int epochs = 1000000;

    float prev_mse = 0;

    float start_time = (float)clock()/CLOCKS_PER_SEC;

    for (int epoch = 0 ; epoch < epochs ; epoch++) {
        
        for (int element = 0 ; element < len(train_x) ; element++) {
            Predictions[element] = Predict(w, train_x[element], b);
            SquaredDiff[element] = pow(train_y[element] - Predict(w, train_x[element], b), 2);
        }
        
        // for (int element = 0 ; element < 10 ; element++) {
        //     printf("%f : %f\n", Predictions[element], SquaredDiff[element]);
        // }

        float mse = MeanSquaredError(SquaredDiff);

        if (epoch%1 == 0) {
            printf("Epoch : %d\nMSE : %f\n", epoch, mse);
        }

        if (fabsf(prev_mse - mse) < 1E-8) {
            printf("Converged at Epoch %d\nMSE : %f, Weight : %f, Bias : %f, Alpha : %f\n", epoch, mse, w, b, alpha);
            break;
        }

        prev_mse = mse;

        w -= alpha*Dmse_en_Dw(train_x, train_y, Predictions);
        b -= alpha*Dmse_en_Db(train_x, train_y, Predictions);

        // memset(Predictions, 0.0f, sizeof(Predictions));
        // memset(SquaredDiff, 0.0f, sizeof(SquaredDiff));

        for (int i = 0 ; i < len(train_x) ; i++) {
            Predictions[i] = 0;
            SquaredDiff[i] = 0;
        }        

        // for (int element = 0 ; element < 10 ; element++) {
        //     printf("%f : %f\n", Predictions[element], SquaredDiff[element]);
        // }

    }

    // printf("Weight: %f\nBias: %f\n", w,b);

    float end_time = (float)clock()/CLOCKS_PER_SEC;

    printf("Tiempo de Entrenamiento : %f", end_time - start_time);

}

float RandomFloat() {
   return (float)(rand()) / (float)(RAND_MAX);
}

float MeanSquaredError(float* SD) {
    float SquaredErrorSum = 0;
    for (int i = 0 ; i < len(SD) ; i++ ) {
        SquaredErrorSum += SD[i];
    }
    return SquaredErrorSum/len(SD);
}

float Dmse_en_Dw(float* train_X, float* train_Y, float* predictions) {
    float X_Diff_Sum = 0;
    for (int i = 0 ; i < len(train_X) ; i++) {
        X_Diff_Sum += train_X[i] * (train_Y[i] - predictions[i]);
    }
    return (-2.0f/len(train_X)) * X_Diff_Sum;
}

float Dmse_en_Db(float* train_X, float* train_Y, float* predictions) {
    float X_Diff_Sum = 0;
    for (int i = 0 ; i < len(train_X) ; i++) {
        X_Diff_Sum += (train_Y[i] - predictions[i]);
    }
    return (-2.0f/len(train_X)) * X_Diff_Sum;
}

float Predict(float w, float x, float b) {
    return w*x+b;
}
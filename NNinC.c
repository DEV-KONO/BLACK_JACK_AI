#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>

double randf() {
    //random numbers from 0 to 1
    return (double)rand()/(double)RAND_MAX;
}

double randf_n() {
    //random numbers from -1 to 1
    return 2.0f * ((double)rand()/(double)RAND_MAX) - 1.0f;
}

double ReLU(double x) {
    if (x >= 0) {
        return x;
    } else {
        return 0;
    }
}

double predict(double x, double w, double b) {
    return ReLU(w * x + b);
}

// double De_Dw(double Yr, double Yp, double h) {
//     return -1*(Yr - Yp)*(h);
// }

// double De_Dw_w1(double Yr, double Yp, double h1) {
//     return -2*(Yr - Yp)*(h1);
// }

// double De_Dw_w2(double Yr, double Yp, double h1, double h2) {
//     return -2*(Yr - Yp)*(h1 + h2);
// }

double De_Dw(double Yr, double Yp, double h) {
    return -1*(Yr - Yp)*(h);
}

double De_Db(double Yr, double Yp) {
    return -2*(Yr - Yp);
}

void main() {
    srand(time(NULL));
    // double r = rand();
    // printf("Random Number : %f\n", r);
    // printf("Random double generated : %f\n", randf());
    // printf("Random double generated from -1 to 1: %f\n", randf_n());
    // printf("RAND_MAX : %d\n", RAND_MAX);

    double w1_1 = randf_n();
    double w1_2 = randf_n();
    double w2_1 = randf_n();
    double b_h1 = randf_n();
    double b_h2 = randf_n();
    double b_o = randf_n();

    double input = 3.0f;
    double y_real = 6.0f;
    double alpha  = 0.001f;
    int epochs = 10000000;

    double diff_ant = 0.0f;
    double diff_act = 0.0f;

    

    // printf("w1_1: %f, w1_2: %f, w2_1: %f\n", w1_1, w1_2, w2_1);
    // printf("b_h1: %f, b_h2: %f, b_o: %f\n", b_h1, b_h2, b_o);
    // printf("h1: %f, h2: %f\n", h1, h2);

    // printf("Error : %f\n", y_real-y_pred);

    // printf("De/Dw1 : %f\n", De_Dw_w1(y_real, y_pred, h1));
    // printf("De/Dw2 : %f\n", De_Dw_w2(y_real, y_pred, h1, h2));

    for (int epoch = 0; epoch < epochs; epoch++) {

        double h1 = predict(input, w1_1, b_h1);
        double h2 = predict(input, w1_2, b_h2);
        double y_pred = (w2_1*h1) + (w2_1*h2) + b_o;

        // Cálculo de los gradientes
        double dE_dW1_1 = De_Dw(y_real, y_pred, h1);
        double dE_dW1_2 = De_Dw(y_real, y_pred, h2);
        double dE_dW2_1 = De_Dw(y_real, y_pred, h1 + h2); // Consideramos el efecto de h1 y h2
        double dE_dB_h1 = De_Db(y_real, y_pred);
        double dE_dB_h2 = De_Db(y_real, y_pred);
        double dE_dB_o = De_Db(y_real, y_pred);

        // Actualización de los pesos y sesgos
        w1_1 -= alpha * dE_dW1_1;
        w1_2 -= alpha * dE_dW1_2;
        w2_1 -= alpha * dE_dW2_1;
        b_h1 -= alpha * dE_dB_h1;
        b_h2 -= alpha * dE_dB_h2;
        b_o -= alpha * dE_dB_o;

        if (epoch % 1000 == 0) {
            printf("Predicción : %f\n", y_pred);
            printf("Valor real : %f\n", y_real);
            printf("Diff : %f\n", y_real-y_pred);
        }

        if (y_real-y_pred < 1E-8 ){
            do
            {
                double test = 0.0f;
                printf("Ingrese Un Numero : ");
                scanf("%lf", &test);
                printf("El numero ingresado es %f\n La predicción es : %f\n", test, (w2_1*predict(test, w1_1, b_h1)) + (w2_1*predict(test, w1_2, b_h2)) + b_o);
            } while (1);
            
            break;
        }

    }

}
#include <stdio.h>

int main() {
    int edad = 20;
    float promedio = 9.5;
    char letra = 'A';

    if (edad >= 18) {
        return 1;
    } else {
        while (edad > 0) {
            edad = edad - 1;
        }

        return 0;
    }
}
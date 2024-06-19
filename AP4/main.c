#include <stdio.h>

extern float calc_volume_cone(float raio, float height);

int main() {
    float r, h;
    printf("Digite o raio do cone: ");
    scanf("%f", &r);
    printf("Digite a altura do cone: ");
    scanf("%f", &h);


    float ret = calc_volume_cone(r, h);

    printf("O volume de cone com raio %f e altura %f eh igual a: %f \n", r, h, ret);

    return 0;

}


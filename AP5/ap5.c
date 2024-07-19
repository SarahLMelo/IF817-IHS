#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

const int N = 3;
int NUM_THREADS;

void init(int a[][N], int b[][N]){
    NUM_THREADS = omp_get_num_procs();

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            a[i][j] = rand() % 10;
            b[i][j] = rand() % 10;
        }
    }
}

void serial(int a[][N], int b[][N], int result[][N], int *even){
    *even = 0;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            for(int k = 0; k < N; k++){
                result[i][j] += a[i][k] * b[k][j];

                if(result[i][j] % 2 == 0){
                    (*even)++;
                }
            }
        }
    }
}

void clear(int result[][N]){
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            result[i][j] = 0;
        }
    }
}

void parallel(int a[][N], int b[][N], int result[][N], int *even){
    *even = 0;
    #pragma omp parallel num_threads(NUM_THREADS)
    {
        int id = omp_get_thread_num();
        int i, j, k;

        for(i = id; i < N; i += NUM_THREADS){ //Esse é o for que será dividido entre as threads
            for(j = 0; j < N; j++){ //Esse for não será dividido entre as threads
                for(k = 0; k < N; k++){ //Nem esse
                    result[i][j] += a[i][k] * b[k][j];

                    if(result[i][j] % 2 == 0){
                        #pragma omp atomic //Acessa a variável atomicamente, ou seja, garante que apenas uma thread por vez acesse a variável
                        (*even)++;
                    }
                }
            }
        }
    }
}

int main() {
    int a[N][N], b[N][N], result[N][N], even;
    clear(result);
    double time;

    init(a, b);
    time = omp_get_wtime();

    serial(a, b, result, &even);
    time = omp_get_wtime() - time;
    printf("Serial:\nTempo da multiplicacao de matrizes em serial = %lf\nNumero de elementos pares = %d\n", time, even);

    clear(result);
    time = omp_get_wtime();

    parallel(a, b, result, &even);
    time = omp_get_wtime() - time;
    printf("\nParalelo:\nTempo da multiplicacao de matrizes em paralelo = %lf\nNumero de elementos pares = %d\n", time, even);

    return 0;
}
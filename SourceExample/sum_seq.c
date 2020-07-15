#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {
    int n;
    if(argc == 1) {
        printf("Insira o tamanho da matriz quadrada: ");
        scanf(" %d", &n);
    }
    else
        n = atoi(argv[1]);

    int **A, **B, **C;

    srand(time(NULL));

    A = (int**)malloc(n*sizeof(int*));
    B = (int**)malloc(n*sizeof(int*));
    C = (int**)malloc(n*sizeof(int*));
    for(int i=0; i<n; i++) {
        A[i] = (int*)malloc(n*sizeof(int));
        B[i] = (int*)malloc(n*sizeof(int));
        C[i] = (int*)malloc(n*sizeof(int));
        for(int j=0; j<n; j++) {
            A[i][j] = rand()%1000;
            B[i][j] = rand()%1000;
        }
    }

    clock_t t = clock(), t1;
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            C[i][j] = A[i][j] + B[i][j];
    t1 = clock();
    printf("SEQUENCIAL: %lf s\n", ((double) t1-t) / CLOCKS_PER_SEC);
    return 0;
}
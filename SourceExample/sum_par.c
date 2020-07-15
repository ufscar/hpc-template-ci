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
    // Initialize the MPI environment
    MPI_Init(NULL, NULL);

    // Get the number of processes
    int size;
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Get the rank of the process
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // Get the name of the processor
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;
    MPI_Get_processor_name(processor_name, &name_len);

    int r = rank, s = size;
    int N = n*n;
    int beg = (N/s) * r;
    int end = r == s-1 ? N : (N/s) * (r+1);
    if(end>N) end = N;
    for(int i=beg; i<end; i++)
        C[0][i] = A[0][i] + B[0][i];

    // Finalize the MPI environment.
    MPI_Finalize();
    t1 = clock();
    if(rank == 0)
        printf("PARALELO: %lf s\n", ((double) t1-t) / CLOCKS_PER_SEC);
    return 0;
}
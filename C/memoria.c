#include <stdlib.h>
 
int global = 99; // Estática (DATA)
 
int main() {
    int i; // variável i declarada uma única vez
    int a = 10; // Automática (STACK)
    printf("a = %d\n", a);
 
    // Automática em loop
    for(i = 0; i < 3; i++) {
        int b = i;
        printf("b = %d\n", b);
    }
 
    // Dinâmica (HEAP)
    int *vet = (int*) malloc(3 * sizeof(int));
    vet[0] = 1; vet[1] = 2; vet[2] = 3;
 
    for(i = 0; i < 3; i++) {
        printf("vet[%d] = %d\n", i, vet[i]);
    }
 
    free(vet); // liberar memória dinâmica
    return 0;
}
#include <stdio.h>
#include <string.h>
#include <locale.h>
int main(void) {
    setlocale(LC_ALL, "");
    char letra = 'A';
    char palavra[] = "Ola";
    printf("Valor de letra: %c\n", letra);
    printf("Tamanho de letra: %zu byte(s)\n", sizeof(letra));
    printf("Valor de palavra: %s\n", palavra);
    printf("Tamanho de palavra (strlen): %zu\n", strlen(palavra));
    printf("Tamanho de palavra (sizeof): %zu\n", sizeof(palavra));
    for (size_t i = 0; i < sizeof(palavra); i++)
        printf("palavra[%zu] = '%c' (ASCII: %d)\n", i, palavra[i], (unsigned char)palavra[i]);
    printf("\n" "===============================\n\n");
    char origem[] = "Ola, mundo!";
    char destino[50];
    strcpy(destino, origem);
    printf("String original: %s\n", origem);
    printf("String copiada: %s\n", destino);
    return 0;
}

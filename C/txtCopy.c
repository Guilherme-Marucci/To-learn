#include <stdio.h>
#include <string.h>
#include <locale.h>
int main(void) {
    setlocale(LC_ALL, "");
    char texto[] = "Programacao em C e poderosa e divertida!";
    char copia[100], temp[100];
    char *posicao;
    //strelen 
    printf("Tamanho do texto: %zu caracteres\n", strlen(texto));
    posicao = strchr(texto, 'C');
    if (posicao) printf("Primeira ocorrencia de 'C': %s\n", posicao);
    posicao = strstr(texto, "poderosa");
    if (posicao) printf("Substring encontrada: %s\n", posicao);
    strcpy(temp, texto);
    puts("Palavras separadas:");
    char *token = strtok(temp, " ");
    while (token) { printf("- %s\n", token); token = strtok(NULL, " "); }
    memcpy(copia, texto, strlen(texto) + 1);
    printf("Texto copiado com memcpy: %s\n", copia);
    memset(copia, '*', 10);
    printf("Texto apos memset: %s\n", copia);
    return 0;
}
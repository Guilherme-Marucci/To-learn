#include <stdio.h>
#include <string.h>
 
#define MAX 5
 
// Estrutura do contato
struct Contato {
    char nome[50];
    int idade;
    char telefone[20];
};
 
// Função de busca
int buscar(struct Contato lista[], int n, char nome[]) {
    int i;
 
    for (i = 0; i < n; i++) {
        if (strcmp(lista[i].nome, nome) == 0) {
            return i; // Retorna a posição encontrada
        }
    }
 
    return -1; // Contato não encontrado
}
 
// Função de inserção
int inserir(struct Contato lista[], int *n, struct Contato novo) {
    int i;
 
    // Verifica se ainda há espaço
    if (*n >= MAX) {
        return -1; // Lista cheia
    }
 
    // Verifica se já existe contato com o mesmo nome
    if (buscar(lista, *n, novo.nome) != -1) {
        return -1; // Já existe
    }
 
    // Insere no final da lista
    lista[*n] = novo;
    (*n)++; // Atualiza quantidade
 
    return 1; // Sucesso
}
 
int main() {
    struct Contato agenda[MAX] = {
        {"Ana", 25, "99999-1111"},
        {"Carlos", 30, "98888-2222"},
        {"Beatriz", 22, "97777-3333"},
        {"Daniel", 28, "96666-4444"}
    };
 
    int n = 3; // Número inicial de contatos
    int resultado;
    int i; // Declarado fora do for
 
    // Novo contato
    struct Contato novo = {"Daniel", 28, "96666-4444"};
 
    resultado = inserir(agenda, &n, novo);
 
    if (resultado == 1) {
        printf("Contato inserido com sucesso!\n");
    } else {
        printf("Erro: contato nao inserido (duplicado ou lista cheia).\n");
    }
 
    // Mostrando agenda atualizada
    printf("\nAgenda atualizada:\n");
 
    for (i = 0; i < n; i++) {
        printf("Nome: %s | Idade: %d | Telefone: %s\n",
               agenda[i].nome,
               agenda[i].idade,
               agenda[i].telefone);
    }
 printf("\n===============================\n\n", novo.nome);
    return 0;
}
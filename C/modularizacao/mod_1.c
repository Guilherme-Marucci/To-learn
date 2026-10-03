#include <stdio.h>
float calcTotal(float price1, float price2){
    return price1 * price2; // Retorna multiplicação das duas vars
//var global ^^^      ^^^
}
int main()//função especial que é o ponto de entrada do programa
{
    float item1 = 7;
    float item2 = 2.99;
    float total = calcTotal(item1, item2); 
    printf("Total da compra: %.2f \n", total);
    //Subrotina exemple
    wellcome();
return 0;
}
void wellcome(){
    printf("Vai toma no cu kkkkkkkkkk");
    // Procedimento sem atribuição ou retorno de valores é usados void
    printf("Uma função sempre retornarão um valor. como no int main\n");
    printf("Um procedimento não precisa retornar valores. pode somente fazer uma ação,\n como imprimir uma mensagem, fazer proceçoes etc.\n");
}
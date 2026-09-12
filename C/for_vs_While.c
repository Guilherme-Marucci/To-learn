#include <stdio.h>



 
int main ()

{

    int i;

    float soma, media, nota[3];

    soma = 0.0f;

    i = 0;

    while (i < 3)

    {

        printf("Digite a Nota %d \n", i+1);

        scanf("%f", &nota[i]);
        soma += nota[i];
        i++;



    }

    media = soma / 3;

    printf("A media das 3 notas e: %.1f \n", media);

    system("pause");

}
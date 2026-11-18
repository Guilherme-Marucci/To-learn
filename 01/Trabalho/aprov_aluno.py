print("=" * 50)
print("4ª: Sistema deaprovação de alunos") 
print("=" * 50)

nome = input("Digite o nome do aluno: ")
nota1 = float(input(" Primeira nota: "))
nota2 = float(input(" Segunda nota: "))
nota3 = float(input(" Terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"Aluno: {nome} - Média: {media:.1f}")

if media != 0:
    if media >= 7 and media < 11:
        print("Aprovado")
    elif media >= 5 and media <= 6.9:
        print("Recuperação")
    else:
        print("Reprovado!")
else:
    print("Média inválida! Tente novamente.")
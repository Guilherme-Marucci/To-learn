from funcionario import Funcionario

funcionario = Funcionario("Guilherme", "guilherme@example.com")

funcionario.cadastro_hora('janeiro', float(input("Digite as horas trabalhadas em janeiro: ")))
funcionario.cadastro_salario_hora('janeiro', 40)

print(funcionario)
print(funcionario.calcula_salario('janeiro'))
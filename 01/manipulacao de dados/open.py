def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == "sair":
            break
        frases.append(entrada)

    with open("open.txt", "a") as arquivo: # a = append (adiciona ao final do arquivo)
        arquivo.writelines(frase + "\n" for frase in frases)

    print("Arquivo original criado. Agora vamos manipular os dados.")
    dados_modificados = []
    with open("open.txt", "r") as arquivo: # r = read (lê o arquivo)
        for linha in arquivo:
            dados_modificados.append(
                linha.strip().upper()
            )  # Exemplo de manipulação: converter para maiúsculas

    with open("open.txt", "w") as arquivo: # w = write (sobrescreve o arquivo)
        for linha in dados_modificados:
            arquivo.write(linha + "\n")

    print("O arquivo foi sobrescrito com os dados modificados.")


if __name__ == "__main__":
    main()

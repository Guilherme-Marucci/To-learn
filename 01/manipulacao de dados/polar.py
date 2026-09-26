#ainda manipulando strings temos a função polar, que transforma uma string em um objeto do tipo polar, que é uma forma de representar coordenadas
#  polares.
#Para isso, é necessário importar a biblioteca polar do módulo manipulacao de dados.
from cmath import polar

def zenit_polar_replace(text):
    # Aplicar a codificação ZENIT POLAR utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text
 
def main():
    # Entrada da frase e aplicação da codificação
    #phrase = "The quick brown fox jumps over the lazy dick"
    phrase = "Polar Zenit "
    phrase = phrase.title()  # Primeira letra de cada palavra em maiúscula
 
    # Dividir a frase em palavras
    words = phrase.split()
 
    # Processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words]
 
    # Juntar todas as palavras codificadas em uma frase
    coded_phrase = " ".join(coded_words)
    print("Original:", phrase)
    print("Coded:", coded_phrase)
 
if __name__ == "__main__":
    main()

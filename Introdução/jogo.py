import random
from os import system, name

#Limpa Tela do prompt
def limpa_tela():

    #Windows
    if name == 'nt':
        _ = system('cls')

    #macOS/Linux
    else:
        _ = system ('clear')

#Função
def game ():

    limpa_tela()
    print("\nBem vindo(a) ao jogo da forca")
    print("Adivinhe a palavra abaixo:\n")

    #Lista de palavras
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'melao', 'pera']

    #Escolhe uma palavra aleatoriamente
    palavra = random.choice(palavras)

    #List Comprehension
    letras_descobertas = ['_' for letra in palavra]

    chances = 4

    letras_erradas = []

    while chances > 0:

        #Print
        print(" ".join(letras_descobertas))
        print("\nChances Restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #Tentativa
        tentativa = input ("\nDigite uma letra: ").lower()

        #Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #Condicional
        if "_" not in letras_descobertas:
            limpa_tela()
            print("\n Você venceu, a palavra era: ", palavra)
            break

    #Condicional
    if "_" in letras_descobertas:
        print("\n Você perdeu, a palavra era: ", palavra)

dict3 = {}
if __name__ == "__main__":
    game()
    print("\n Parabéns!\n")
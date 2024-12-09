#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"While Loop"

#Minha versão
key_word = "them"
key_word_score = 0
key_word_blank = ""
guess = ""
i = 0

while  i < len(key_word):
    key_word_blank += "_"
    i += 1


print("Seja bem-vindo ao jogo da adivinhação")
print("Uma palavra foi escolhida")
print("e você deverá descobri-la")


while key_word_score < len(key_word):
    print("-------------------------------------")
    print("A palavra é:")
    print(key_word_blank)
    guess = input("Informe uma letra:")
    if key_word.find(guess) != -1:
        key_word_blank = list(key_word_blank)
        key_word_blank[key_word.find(guess)] = guess
        key_word_blank = ''.join(key_word_blank)
        key_word_score += 1
        print("-------------------------------------")
        print("Você acertou!")
    else:
        print("-------------------------------------")
        print("Tente novamente!")

print("-------------------------------------")
print("Você ganhou!")
print("A palavra era: " + key_word)